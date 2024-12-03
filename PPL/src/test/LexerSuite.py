import unittest
from TestUtils import TestLexer

testcaseArray = [
    # Testcase 100 - 106 about DOUBLE PRECISE ESCAPE SEQUENCES
    ['"\\b"','\\b,<EOF>'],
    ['"\\f"','\\f,<EOF>'],
    ['"\\r"','\\r,<EOF>'],
    ['"\\n"','\\n,<EOF>'],
    ['"\\t"','\\t,<EOF>'],
    ['"\\\\\\\'"','\\\\\\\',<EOF>'],
    ['"\\\\\\\\"','\\\\\\\\,<EOF>'],
    # Testcase 107 - 113 about PRECISE ESCAPE SEQUENCES
    ['"a\b"','a\b,<EOF>'],       # 2nd " is removed
    ['"a\f"','a\f,<EOF>'],
    ['"a\r"','Unclosed String: a'],        # NEWLINE IN WINDOWS
    ['"a\n"','Unclosed String: a'],
    ['"a\t"','a\t,<EOF>'],        # ACCEPT IN STRING
    ['"\\\'"','\\\',<EOF>'],
    ['"\\\\"','\\\\,<EOF>'],
]

class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        testcaseNo = 100
        """test identifiers"""
        for testcase in testcaseArray:
            TestLexer.test(testcase[0], testcase[1], testcaseNo)
            testcaseNo+=1
