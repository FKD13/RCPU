from RCPU.assembler.expanders.baseexpander import BaseExpander
class ArithmeticExpander(BaseExpander):

    @BaseExpander.instruction
    def ADD(arg):
        return ['ATH {d},{s},0,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def ADDS(arg):
        return ['ATH {d},{s},0,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def SUB(arg):
        return ['ATH {d},{s},1,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def SUBS(arg):
        return ['ATH {d},{s},1,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def MUL(arg):
        return ['ATH {d},{s},2,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def MULS(arg):
        return ['ATH {d},{s},2,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def DIV(arg):
        return ['ATH {d},{s},3,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def DIVS(arg):
        return ['ATH {d},{s},3,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def LSH(arg):
        return ['ATH 0,{s},4,1,{b}'.format(s=arg[0], b=arg[1])]

    @BaseExpander.instruction
    def RSH(arg):
        return ['ATH 0,{s},5,1,{b}'.format(s=arg[0], b=arg[1])]

    @BaseExpander.instruction
    def AND(arg):
        return ['ATH {d},{s},6,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def ANDS(arg):
        return ['ATH {d},{s},6,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def OR(arg):
        return ['ATH {d},{s},7,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def ORS(arg):
        return ['ATH {d},{s},7,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def XOR(arg):
        return ['ATH {d},{s},8,0,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def XORS(arg):
        return ['ATH {d},{s},8,1,0'.format(d=arg[0], s=arg[1])]

    @BaseExpander.instruction
    def NOT(arg):
        return ['ATH 0,{s},9,1,0'.format(s=arg[0])]



