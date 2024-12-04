# Generated from BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("*\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\6\2\23\n\2\r\2\16\2\24\3\3\6\3\30\n\3\r\3")
        buf.write("\16\3\31\3\4\6\4\35\n\4\r\4\16\4\36\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\3\2\5\3\2\62;\3\2c|\5\2\13\f\17\17\"\"\2,\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\3\22\3\2\2\2\5\27\3\2\2\2")
        buf.write("\7\34\3\2\2\2\t\"\3\2\2\2\13$\3\2\2\2\r&\3\2\2\2\17(\3")
        buf.write("\2\2\2\21\23\t\2\2\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\4\3\2\2\2\26\30\t\3\2\2\27\26")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32")
        buf.write("\6\3\2\2\2\33\35\t\4\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36")
        buf.write("\34\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\b\4\2\2!\b\3\2")
        buf.write("\2\2\"#\13\2\2\2#\n\3\2\2\2$%\13\2\2\2%\f\3\2\2\2&\'\13")
        buf.write("\2\2\2\'\16\3\2\2\2()\13\2\2\2)\20\3\2\2\2\6\2\24\31\36")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ID = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6
    UNTERMINATED_COMMENT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


