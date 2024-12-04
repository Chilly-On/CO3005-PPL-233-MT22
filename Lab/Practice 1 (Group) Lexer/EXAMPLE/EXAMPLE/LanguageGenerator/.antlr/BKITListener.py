# Generated from e:/General_Subjects/Principle of Programming Languages/TA-PPL-IU/PPL-IS-2024/Lab/1. Lexer/Lexer_Example/LanguageGenerator/BKIT.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass



del BKITParser