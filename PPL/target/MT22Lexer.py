# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01c0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u0134\n\61\f\61\16\61\u0137\13\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\7\62\u0142\n\62\f\62\16\62")
        buf.write("\u0145\13\62\3\62\3\62\3\63\3\63\3\63\5\63\u014c\n\63")
        buf.write("\3\63\7\63\u014f\n\63\f\63\16\63\u0152\13\63\3\63\5\63")
        buf.write("\u0155\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u015f\n\64\3\64\6\64\u0162\n\64\r\64\16\64\u0163\7")
        buf.write("\64\u0166\n\64\f\64\16\64\u0169\13\64\3\64\3\64\5\64\u016d")
        buf.write("\n\64\3\64\3\64\5\64\u0171\n\64\3\65\3\65\7\65\u0175\n")
        buf.write("\65\f\65\16\65\u0178\13\65\3\66\3\66\5\66\u017c\n\66\3")
        buf.write("\66\6\66\u017f\n\66\r\66\16\66\u0180\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u0187\n\67\f\67\16\67\u018a\13\67\3\67\3\67\3")
        buf.write("\67\38\38\78\u0191\n8\f8\168\u0194\138\39\69\u0197\n9")
        buf.write("\r9\169\u0198\39\39\3:\3:\3:\3:\7:\u01a1\n:\f:\16:\u01a4")
        buf.write("\13:\3:\5:\u01a7\n:\3:\5:\u01aa\n:\3:\5:\u01ad\n:\3:\3")
        buf.write(":\3;\3;\3;\3;\7;\u01b5\n;\f;\16;\u01b8\13;\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3\u0135\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\2k\2m\66o\67q8s9u:w;\3\2\22\3\2\f\f\3\2\63;\3\2")
        buf.write("\62;\3\2\60\60\4\2GGgg\4\2--//\3\2$$\7\2\f\f\16\17$$)")
        buf.write(")^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\3\2\16\16\3\2\17\17\7\2\n\f\16\17$$))")
        buf.write("^^\3\2^^\2\u01d6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2")
        buf.write("\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5~\3\2")
        buf.write("\2\2\7\u0084\3\2\2\2\t\u008c\3\2\2\2\13\u008f\3\2\2\2")
        buf.write("\r\u0094\3\2\2\2\17\u009a\3\2\2\2\21\u00a0\3\2\2\2\23")
        buf.write("\u00a4\3\2\2\2\25\u00ad\3\2\2\2\27\u00b0\3\2\2\2\31\u00b8")
        buf.write("\3\2\2\2\33\u00bf\3\2\2\2\35\u00c6\3\2\2\2\37\u00cb\3")
        buf.write("\2\2\2!\u00d1\3\2\2\2#\u00d6\3\2\2\2%\u00da\3\2\2\2\'")
        buf.write("\u00e3\3\2\2\2)\u00e6\3\2\2\2+\u00ee\3\2\2\2-\u00f4\3")
        buf.write("\2\2\2/\u00f6\3\2\2\2\61\u00f8\3\2\2\2\63\u00fa\3\2\2")
        buf.write("\2\65\u00fc\3\2\2\2\67\u00fe\3\2\2\29\u0100\3\2\2\2;\u0103")
        buf.write("\3\2\2\2=\u0106\3\2\2\2?\u0109\3\2\2\2A\u010c\3\2\2\2")
        buf.write("C\u010e\3\2\2\2E\u0111\3\2\2\2G\u0113\3\2\2\2I\u0116\3")
        buf.write("\2\2\2K\u0119\3\2\2\2M\u011b\3\2\2\2O\u011d\3\2\2\2Q\u011f")
        buf.write("\3\2\2\2S\u0121\3\2\2\2U\u0123\3\2\2\2W\u0125\3\2\2\2")
        buf.write("Y\u0127\3\2\2\2[\u0129\3\2\2\2]\u012b\3\2\2\2_\u012d\3")
        buf.write("\2\2\2a\u012f\3\2\2\2c\u013d\3\2\2\2e\u0154\3\2\2\2g\u0170")
        buf.write("\3\2\2\2i\u0172\3\2\2\2k\u0179\3\2\2\2m\u0182\3\2\2\2")
        buf.write("o\u018e\3\2\2\2q\u0196\3\2\2\2s\u019c\3\2\2\2u\u01b0\3")
        buf.write("\2\2\2w\u01bd\3\2\2\2yz\7c\2\2z{\7w\2\2{|\7v\2\2|}\7q")
        buf.write("\2\2}\4\3\2\2\2~\177\7d\2\2\177\u0080\7t\2\2\u0080\u0081")
        buf.write("\7g\2\2\u0081\u0082\7c\2\2\u0082\u0083\7m\2\2\u0083\6")
        buf.write("\3\2\2\2\u0084\u0085\7d\2\2\u0085\u0086\7q\2\2\u0086\u0087")
        buf.write("\7q\2\2\u0087\u0088\7n\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7p\2\2\u008b\b\3\2\2\2\u008c\u008d")
        buf.write("\7f\2\2\u008d\u008e\7q\2\2\u008e\n\3\2\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\u0091\7n\2\2\u0091\u0092\7u\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\f\3\2\2\2\u0094\u0095\7h\2\2\u0095\u0096")
        buf.write("\7c\2\2\u0096\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\16\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c")
        buf.write("\7n\2\2\u009c\u009d\7q\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7t\2\2\u00a3\22\3\2\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7e\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7p\2\2\u00ac\24\3\2\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7h\2\2\u00af\26\3\2\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\30\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7p\2\2\u00be\32\3\2\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\34")
        buf.write("\3\2\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7w\2\2\u00c9\u00ca\7g\2\2\u00ca\36\3\2\2\2\u00cb\u00cc")
        buf.write("\7y\2\2\u00cc\u00cd\7j\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7g\2\2\u00d0 \3\2\2\2\u00d1\u00d2")
        buf.write("\7x\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7f\2\2\u00d5\"\3\2\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7w\2\2\u00d8\u00d9\7v\2\2\u00d9$\3\2\2\2\u00da\u00db")
        buf.write("\7e\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7w\2\2\u00e1\u00e2\7g\2\2\u00e2&\3\2\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7h\2\2\u00e5(\3\2\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7j\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed*\3\2\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7{\2\2\u00f3,\3\2\2\2\u00f4\u00f5\7-\2\2\u00f5.\3\2\2")
        buf.write("\2\u00f6\u00f7\7/\2\2\u00f7\60\3\2\2\2\u00f8\u00f9\7,")
        buf.write("\2\2\u00f9\62\3\2\2\2\u00fa\u00fb\7\61\2\2\u00fb\64\3")
        buf.write("\2\2\2\u00fc\u00fd\7\'\2\2\u00fd\66\3\2\2\2\u00fe\u00ff")
        buf.write("\7#\2\2\u00ff8\3\2\2\2\u0100\u0101\7(\2\2\u0101\u0102")
        buf.write("\7(\2\2\u0102:\3\2\2\2\u0103\u0104\7~\2\2\u0104\u0105")
        buf.write("\7~\2\2\u0105<\3\2\2\2\u0106\u0107\7?\2\2\u0107\u0108")
        buf.write("\7?\2\2\u0108>\3\2\2\2\u0109\u010a\7#\2\2\u010a\u010b")
        buf.write("\7?\2\2\u010b@\3\2\2\2\u010c\u010d\7>\2\2\u010dB\3\2\2")
        buf.write("\2\u010e\u010f\7>\2\2\u010f\u0110\7?\2\2\u0110D\3\2\2")
        buf.write("\2\u0111\u0112\7@\2\2\u0112F\3\2\2\2\u0113\u0114\7@\2")
        buf.write("\2\u0114\u0115\7?\2\2\u0115H\3\2\2\2\u0116\u0117\7<\2")
        buf.write("\2\u0117\u0118\7<\2\2\u0118J\3\2\2\2\u0119\u011a\7*\2")
        buf.write("\2\u011aL\3\2\2\2\u011b\u011c\7+\2\2\u011cN\3\2\2\2\u011d")
        buf.write("\u011e\7]\2\2\u011eP\3\2\2\2\u011f\u0120\7_\2\2\u0120")
        buf.write("R\3\2\2\2\u0121\u0122\7\60\2\2\u0122T\3\2\2\2\u0123\u0124")
        buf.write("\7.\2\2\u0124V\3\2\2\2\u0125\u0126\7=\2\2\u0126X\3\2\2")
        buf.write("\2\u0127\u0128\7<\2\2\u0128Z\3\2\2\2\u0129\u012a\7}\2")
        buf.write("\2\u012a\\\3\2\2\2\u012b\u012c\7\177\2\2\u012c^\3\2\2")
        buf.write("\2\u012d\u012e\7?\2\2\u012e`\3\2\2\2\u012f\u0130\7\61")
        buf.write("\2\2\u0130\u0131\7,\2\2\u0131\u0135\3\2\2\2\u0132\u0134")
        buf.write("\13\2\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0138\3\2\2\2")
        buf.write("\u0137\u0135\3\2\2\2\u0138\u0139\7,\2\2\u0139\u013a\7")
        buf.write("\61\2\2\u013a\u013b\3\2\2\2\u013b\u013c\b\61\2\2\u013c")
        buf.write("b\3\2\2\2\u013d\u013e\7\61\2\2\u013e\u013f\7\61\2\2\u013f")
        buf.write("\u0143\3\2\2\2\u0140\u0142\n\2\2\2\u0141\u0140\3\2\2\2")
        buf.write("\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3")
        buf.write("\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147")
        buf.write("\b\62\2\2\u0147d\3\2\2\2\u0148\u0155\7\62\2\2\u0149\u0150")
        buf.write("\t\3\2\2\u014a\u014c\7a\2\2\u014b\u014a\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\t\4\2\2")
        buf.write("\u014e\u014b\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0153\u0155\b\63\3\2\u0154\u0148\3\2\2\2\u0154")
        buf.write("\u0149\3\2\2\2\u0155f\3\2\2\2\u0156\u0157\5e\63\2\u0157")
        buf.write("\u0158\5k\66\2\u0158\u0171\3\2\2\2\u0159\u015a\5i\65\2")
        buf.write("\u015a\u015b\5k\66\2\u015b\u0171\3\2\2\2\u015c\u0167\t")
        buf.write("\4\2\2\u015d\u015f\7a\2\2\u015e\u015d\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u0162\t\4\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u015e\3")
        buf.write("\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u0167\3\2\2\2\u016a")
        buf.write("\u016c\5i\65\2\u016b\u016d\5k\66\2\u016c\u016b\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\b")
        buf.write("\64\4\2\u016f\u0171\3\2\2\2\u0170\u0156\3\2\2\2\u0170")
        buf.write("\u0159\3\2\2\2\u0170\u015c\3\2\2\2\u0171h\3\2\2\2\u0172")
        buf.write("\u0176\t\5\2\2\u0173\u0175\t\4\2\2\u0174\u0173\3\2\2\2")
        buf.write("\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177j\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017b")
        buf.write("\t\6\2\2\u017a\u017c\t\7\2\2\u017b\u017a\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017f\t\4\2\2")
        buf.write("\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181l\3\2\2\2\u0182\u0188")
        buf.write("\t\b\2\2\u0183\u0187\n\t\2\2\u0184\u0185\7^\2\2\u0185")
        buf.write("\u0187\t\n\2\2\u0186\u0183\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c")
        buf.write("\t\b\2\2\u018c\u018d\b\67\5\2\u018dn\3\2\2\2\u018e\u0192")
        buf.write("\t\13\2\2\u018f\u0191\t\f\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193p\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0197\t\r\2")
        buf.write("\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019b\b9\2\2\u019br\3\2\2\2\u019c\u01a2\7$\2\2\u019d")
        buf.write("\u01a1\n\t\2\2\u019e\u019f\7^\2\2\u019f\u01a1\t\n\2\2")
        buf.write("\u01a0\u019d\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a4\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7\t\16\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2")
        buf.write("\u01a8\u01aa\t\17\2\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01ad\t\2\2\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\b:\6\2\u01aft\3\2\2\2\u01b0\u01b6\t\b\2\2")
        buf.write("\u01b1\u01b5\n\20\2\2\u01b2\u01b3\t\21\2\2\u01b3\u01b5")
        buf.write("\t\n\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\t")
        buf.write("\21\2\2\u01ba\u01bb\n\n\2\2\u01bb\u01bc\b;\7\2\u01bcv")
        buf.write("\3\2\2\2\u01bd\u01be\13\2\2\2\u01be\u01bf\b<\b\2\u01bf")
        buf.write("x\3\2\2\2\33\2\u0135\u0143\u014b\u0150\u0154\u015e\u0163")
        buf.write("\u0167\u016c\u0170\u0176\u017b\u0180\u0186\u0188\u0192")
        buf.write("\u0198\u01a0\u01a2\u01a6\u01a9\u01ac\u01b4\u01b6\t\b\2")
        buf.write("\2\3\63\2\3\64\3\3\67\4\3:\5\3;\6\3<\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BRK = 2
    BOOL = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNC = 9
    IF = 10
    INT = 11
    RTN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONT = 18
    OF = 19
    INHERIT = 20
    ARR = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQ = 30
    IEQ = 31
    LESS = 32
    LEQ = 33
    GREATER = 34
    GEQ = 35
    CONCAT = 36
    LC = 37
    RC = 38
    LS = 39
    RS = 40
    DOT = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    LB = 45
    RB = 46
    ASSN = 47
    ACMT = 48
    CMT = 49
    INTNUM = 50
    FLOATNUM = 51
    STR = 52
    ID = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BRK", "BOOL", "DO", "ELSE", "FALSE", "FLOAT", "FOR", 
            "FUNC", "IF", "INT", "RTN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONT", "OF", "INHERIT", "ARR", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQ", "IEQ", "LESS", "LEQ", 
            "GREATER", "GEQ", "CONCAT", "LC", "RC", "LS", "RS", "DOT", "COMMA", 
            "SEMI", "COLON", "LB", "RB", "ASSN", "ACMT", "CMT", "INTNUM", 
            "FLOATNUM", "STR", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BRK", "BOOL", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNC", "IF", "INT", "RTN", "STRING", "TRUE", "WHILE", 
                  "VOID", "OUT", "CONT", "OF", "INHERIT", "ARR", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
                  "IEQ", "LESS", "LEQ", "GREATER", "GEQ", "CONCAT", "LC", 
                  "RC", "LS", "RS", "DOT", "COMMA", "SEMI", "COLON", "LB", 
                  "RB", "ASSN", "ACMT", "CMT", "INTNUM", "FLOATNUM", "DECI", 
                  "EXP", "STR", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INTNUM_action 
            actions[50] = self.FLOATNUM_action 
            actions[53] = self.STR_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTNUM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace('_', '') 
     

    def FLOATNUM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace('_', '')
     

    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	if self.text.find('\r\n') != -1:          # if not found newline
                    pos = self.text.find('\r\n')          # go to endline;
                    raise UncloseString(self.text[1:pos])  # not found: raise error to end
            	if self.text.find('\r') != -1:          # if not found newline
                    pos = self.text.find('\r')          # go to endline;
                    raise UncloseString(self.text[1:pos])   #  then raise Error
            	if self.text.find('\n') != -1:          # if not found newline
                    pos = self.text.find('\n')          # go to endline;
                    raise UncloseString(self.text[1:pos])   #  then raise Error
            	if self.text.find('\f') != -1:          # if not found newline
                    pos = self.text.find('\f')          # go to endline;
                    raise UncloseString(self.text[1:pos])   #  then raise Error
            	else:
                    raise UncloseString(self.text[1:])  # not found: raise error to end
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise IllegalEscape(self.text[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


