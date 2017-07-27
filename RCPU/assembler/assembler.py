from . import parser
from . import translator
from RCPU.assembler.expanders.expander import expand_instruction
from RCPU.architecture import MAX_VALUE

def create_resourcetable(data):
    resourcetable = {}
    for line in data:
        name, value = parser.parse_resource(line)
        resourcetable[name] = value
    return resourcetable

def expand(text):
    '''Expands pseudo-instructions into real instructions, supports symbolic arguments'''
    newtext = []
    for line in text:
        if parser.is_instruction(line):
            # Copy list of expanded instructions on the end of newtext
            newtext.extend(expand_instruction(line))
        else:
            # Just add label in
            newtext.append(line)
    return newtext

def expand_all(text):
    '''Expands pseudo-instructions until all pseudo-instructions are converted to real instructions'''
    while text != expand(text):
        text = expand(text)
    return text

def replace_labels(text):
    '''Replaces labels in text with their locations in text'''
    labels = {}
    first_pass = []
    second_pass = []
    current_location = 0
    # Put all labels in dictionary
    for line in text:
        if parser.is_label(line):
            labels[line] = current_location
        else:
            first_pass.append(line)
            current_location += 1
    # Translate all labels
    for line in first_pass:
        assert parser.is_instruction(line)
        instruction, arguments = parser.parse_instruction(line)
        newarguments = []
        for argument in arguments:
            if parser.is_label(argument):
                argument = str(labels[argument])
            newarguments.append(argument)
        translated = parser.unparse_instruction(instruction, newarguments)
        second_pass.append(translated)
    return second_pass

def generate_datasection(text, resourcetable, base_address=None):
    #TODO make sure that if label is used twice, it points to the same data
    if base_address is None:
        base_address = len(text)
    newtext = []
    datasection = []
    for line in text:
        # Should all be instructions by now
        instruction, arguments = parser.parse_instruction(line)
        newarguments = []
        for argument in arguments:
            if parser.is_reference(argument):
                value = resourcetable[argument]
                if type(value) == int:
                    assert 0 <= value and value <= MAX_VALUE
                    argument = str(value)
                elif type(value) == str:
                    argument = str(len(datasection) + base_address)
                    for char in value:
                        datasection.append(ord(char))
                    datasection.append(0)
                else:
                    raise Exception('Unknown type') #TODO: make a special class for assembler errors
            newarguments.append(argument)
        newtext.append(parser.unparse_instruction(instruction, newarguments))
    return newtext, datasection

def translate_all(text):
    binary = []
    t = translator.InstructionTranslator
    for line in text:
        instruction, arguments = parser.parse_instruction(line)
        binary.append(t.translate(instruction, arguments))
    return binary

def replace_entrypoint(text):
    # TODO: replace this with a long jump in case entrypoint is above 0x3FF
    entrypoint = parser.parse_global(text[0])
    text[0] = "JMP {label}".format(label=entrypoint)
    return text