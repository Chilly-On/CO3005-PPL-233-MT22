import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """FUNC: function void(){
    print("WARNING: THIS IS ULTIMATE TESTCASES FOR MT22 IN 233",
    "FINISH BASIC TESTCASES BEFORE TRYING THIS.");
    }"""
        expect = """Program([
	FuncDecl(FUNC, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(WARNING: THIS IS ULTIMATE TESTCASES FOR MT22 IN 233), StringLit(FINISH BASIC TESTCASES BEFORE TRYING THIS.))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """ // 201 unclose string
FUNC: function void(){
i : integer;
for (i = x + 2,i < 4, i + 1){
    if (i ==3){
        i = i + 10;     // Made by Chiily On
    }
    else {
        if (i==2){
            i = i + 1;
        }
    }
    print("Made by Chiily On 100%");
}}"""
        expect = """Program([
	FuncDecl(FUNC, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(x), IntegerLit(2))), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(3)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(10)))]), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])), CallStmt(print, StringLit(Made by Chiily On 100%))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """ // ID start with num ;
del: function void (out str: string , n: integer) inherit deef{                 // del let.
        for (n = n, n < (strlen(str) - 1), n + 1)
                str[n] = str[n + 1];                    // copy af. to bef.
                str[strlen(score) - 1] = "";                      // last is blank
        return;
}"""
        expect = """Program([
	FuncDecl(del, VoidType, [OutParam(str, StringType), Param(n, IntegerType)], deef, BlockStmt([ForStmt(AssignStmt(Id(n), Id(n)), BinExpr(<, Id(n), BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))), BinExpr(+, Id(n), IntegerLit(1)), AssignStmt(ArrayCell(str, [Id(n)]), ArrayCell(str, [BinExpr(+, Id(n), IntegerLit(1))]))), AssignStmt(ArrayCell(str, [BinExpr(-, FuncCall(strlen, [Id(score)]), IntegerLit(1))]), StringLit()), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """ // do while w/o blkstmt
    main: function integer() 
    {
            char : string = "     doAn VAN   *(()hau       ";
            // TODO
            i : integer;                                                                    // letter str
            sp1 : boolean = false;                                          // check 1st space
            // CUT SP HEAD, FIND 1ST LETTER.
            // CUT >2ND REPEAT SP
            for (i = 0, i < strlen(str), i + 1) {
                    if (str[i] == " ")
                            if (sp1 == true) {
                                    del(str, i);
                                    i = i - 1;                                              // auto-move => no plus i
                            }
                            else
                                    sp1 = true;
                    else
                            sp1 = false;
            }
            // CUT SP TAILS
            for (i = (strlen(str) - 1), ((str[i] == " ") && (i >= 0)), i - 1) {
                    str[i] = "";
            }
            // TRANSFER TO OUTSTR (this var is harder to code)
	        for (i = 0, (i < strlen(str)), i + 1) {
			    outstr[i] = str[i];
	        }
            for (n = n, (i < strlen(outstr)), i + 1) {              // set redundant char slots to blank
                    outstr[i] = "";
            }
            // REMOVE BELOW WHEN ENTER CODE, THIS IS RESULT DISP.
            print(outstr, ".");
            do {del(str, 0);}
            while (str[0] == " ");
            return 0; //REMOVE 0
    }
    """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(char, StringType, StringLit(     doAn VAN   *(()hau       )), VarDecl(i, IntegerType), VarDecl(sp1, BooleanType, BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(strlen, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(str, [Id(i)]), StringLit( )), IfStmt(BinExpr(==, Id(sp1), BooleanLit(True)), BlockStmt([CallStmt(del, Id(str), Id(i)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))]), AssignStmt(Id(sp1), BooleanLit(True))), AssignStmt(Id(sp1), BooleanLit(False)))])), ForStmt(AssignStmt(Id(i), BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))), BinExpr(&&, BinExpr(==, ArrayCell(str, [Id(i)]), StringLit( )), BinExpr(>=, Id(i), IntegerLit(0))), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(str, [Id(i)]), StringLit())])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(strlen, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(outstr, [Id(i)]), ArrayCell(str, [Id(i)]))])), ForStmt(AssignStmt(Id(n), Id(n)), BinExpr(<, Id(i), FuncCall(strlen, [Id(outstr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(outstr, [Id(i)]), StringLit())])), CallStmt(print, Id(outstr), StringLit(.)), DoWhileStmt(BinExpr(==, ArrayCell(str, [IntegerLit(0)]), StringLit( )), BlockStmt([CallStmt(del, Id(str), IntegerLit(0))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):     # WRONG
        input = """    // Illegal Escape In String
process : function void (str : string, outstr : string) {
	// TODO
	// REWORK use knowledge of pointer and c-str

	strcpy(outstr, str);
	outstr = outstr + strlen(str) - 1;
	
	for (i = 0, i :: strLen, i+1)		// bring ptr outstr to end; when str++, cut head, pointer is the 1st ltr
	{
		outstr = str;
		str = str + 1;
		outstr = outstr -1;
	}
	if (bool())
		strLen : integer  = strlen[3];
	return "\\n";
}"""
        expect = """Program([
	FuncDecl(process, VoidType, [Param(str, StringType), Param(outstr, StringType)], None, BlockStmt([CallStmt(strcpy, Id(outstr), Id(str)), AssignStmt(Id(outstr), BinExpr(-, BinExpr(+, Id(outstr), FuncCall(strlen, [Id(str)])), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(::, Id(i), Id(strLen)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(outstr), Id(str)), AssignStmt(Id(str), BinExpr(+, Id(str), IntegerLit(1))), AssignStmt(Id(outstr), BinExpr(-, Id(outstr), IntegerLit(1)))])), IfStmt(FuncCall(bool, []), VarDecl(strLen, IntegerType, ArrayCell(strlen, [IntegerLit(3)]))), ReturnStmt(StringLit(\\n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """    // declare in if expression
main : function integer() {
	str, outstr : string = "timing", strlen(str) + 1;
	process(str, outstr);
	print("df\\"");
	if (strstr(szString1, " ") != c && g)
	print("1");
	else print("/");
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(str, StringType, StringLit(timing)), VarDecl(outstr, StringType, BinExpr(+, FuncCall(strlen, [Id(str)]), IntegerLit(1))), CallStmt(process, Id(str), Id(outstr)), CallStmt(print, StringLit(df\\")), IfStmt(BinExpr(!=, FuncCall(strstr, [Id(szString1), StringLit( )]), BinExpr(&&, Id(c), Id(g))), CallStmt(print, StringLit(1)), CallStmt(print, StringLit(/)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """    // else with no stmt
// InLab_Q1_CString header
isValidChar: function boolean (c: string) {
        if (c >= "a" && c <= "z" || c >= "A" && c <= "Z"){
                return true;
                }
}"""
        expect = """Program([
	FuncDecl(isValidChar, BooleanType, [Param(c, StringType)], None, BlockStmt([IfStmt(BinExpr(<=, BinExpr(>=, BinExpr(<=, BinExpr(>=, Id(c), BinExpr(&&, StringLit(a), Id(c))), BinExpr(||, StringLit(z), Id(c))), BinExpr(&&, StringLit(A), Id(c))), StringLit(Z)), BlockStmt([ReturnStmt(BooleanLit(True))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """    // unclosed bracket
lowercase : function string(c: string) {
        OFFSET : integer = 32;
        if (c >= "A" && c <= "Z")
            {
            }
        else {}}"""
        expect = """Program([
	FuncDecl(lowercase, StringType, [Param(c, StringType)], None, BlockStmt([VarDecl(OFFSET, IntegerType, IntegerLit(32)), IfStmt(BinExpr(<=, BinExpr(>=, Id(c), BinExpr(&&, StringLit(A), Id(c))), StringLit(Z)), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_308(self):
        input = """        // missed closing
uppercase: function string(c: string) inherit e {
        OFFSET : integer = 32;
        if (c >= "a" && c <= "z")
                return (c) - ((OFFSET));
        else return c;
}"""
        expect = """Program([
	FuncDecl(uppercase, StringType, [Param(c, StringType)], e, BlockStmt([VarDecl(OFFSET, IntegerType, IntegerLit(32)), IfStmt(BinExpr(<=, BinExpr(>=, Id(c), BinExpr(&&, StringLit(a), Id(c))), StringLit(z)), ReturnStmt(BinExpr(-, Id(c), Id(OFFSET))), ReturnStmt(Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_309(self):
        input = """ // outstr = DELIM = DELIM;
 process: function void(str: string, outstr: string) {
        flag : boolean = true;
         SPACE : string= " ";
       DELIM : string= "";
        // Check the first character

        while (str) {
                if (isValidChar(str) || str == SPACE && !flag) {
                        outstr = flag(uppercase(str) , lowercase(str));
                        outstr  = outstr + 1;
                }
                if (str == SPACE) {
                        flag = true;
                }
                else if (isValidChar(str)) {
                        flag = false;
                }

                str = str + 1;
        }

        // Check the last character and add eliminator
        if ((outstr - 1) == SPACE) {
                DELIM = (outstr - 13_454_675_56.213E8) ;
        }
        else {
                outstr = DELIM - DELIM;
        }
}"""
        expect = """Program([
	FuncDecl(process, VoidType, [Param(str, StringType), Param(outstr, StringType)], None, BlockStmt([VarDecl(flag, BooleanType, BooleanLit(True)), VarDecl(SPACE, StringType, StringLit( )), VarDecl(DELIM, StringType, StringLit()), WhileStmt(Id(str), BlockStmt([IfStmt(BinExpr(==, BinExpr(||, FuncCall(isValidChar, [Id(str)]), Id(str)), BinExpr(&&, Id(SPACE), UnExpr(!, Id(flag)))), BlockStmt([AssignStmt(Id(outstr), FuncCall(flag, [FuncCall(uppercase, [Id(str)]), FuncCall(lowercase, [Id(str)])])), AssignStmt(Id(outstr), BinExpr(+, Id(outstr), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(str), Id(SPACE)), BlockStmt([AssignStmt(Id(flag), BooleanLit(True))]), IfStmt(FuncCall(isValidChar, [Id(str)]), BlockStmt([AssignStmt(Id(flag), BooleanLit(False))]))), AssignStmt(Id(str), BinExpr(+, Id(str), IntegerLit(1)))])), IfStmt(BinExpr(==, BinExpr(-, Id(outstr), IntegerLit(1)), Id(SPACE)), BlockStmt([AssignStmt(Id(DELIM), BinExpr(-, Id(outstr), FloatLit(1.343467556213e+17)))]), BlockStmt([AssignStmt(Id(outstr), BinExpr(-, Id(DELIM), Id(DELIM)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_310(self):
        input = """ // return if
 del: function void(inherit str: string, out n: integer) inherit _Ig4{                  // del let.
        for (n=n, n < (strlen(str) - 1), n + 1)
                str[n] = str[n + 1];                    // copy af. to bef.
        str[strlen(str) - 1] = "";                      // last is blank
        return;
}"""
        expect = """Program([
	FuncDecl(del, VoidType, [InheritParam(str, StringType), OutParam(n, IntegerType)], _Ig4, BlockStmt([ForStmt(AssignStmt(Id(n), Id(n)), BinExpr(<, Id(n), BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))), BinExpr(+, Id(n), IntegerLit(1)), AssignStmt(ArrayCell(str, [Id(n)]), ArrayCell(str, [BinExpr(+, Id(n), IntegerLit(1))]))), AssignStmt(ArrayCell(str, [BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))]), StringLit()), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_311(self):
        input = """    // Array access w/o expression
calc: function integer(str : string) {                                                                  // convert from bin to dec
        // TODO
        i, j, a: integer = 8,6,0;                                                                       // num pos, seq of binary multi loop
        //int a;                                                                        // temp var to save pow(2)
         sum: integer = 0;                                                      // output
        // if necessary: use proper
        // use pointer
         bin: string = strlen(str) + 1;
        strcpy(bin, str);
        lenBin : integer = strlen(bin);
        for (i = 0,  i < lenBin, i+1) {
                if (bin == "1") {
                        a = 1;                                                                                  // build value from pos
                        for (j = 0, j < (lenBin - 1 - i), j+1)
                                a = a * 2;
                        sum = sum + a;
                }
                bin = bin+1;
        }
        return strlen[3];
}"""
        expect = """Program([
	FuncDecl(calc, IntegerType, [Param(str, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(8)), VarDecl(j, IntegerType, IntegerLit(6)), VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(bin, StringType, BinExpr(+, FuncCall(strlen, [Id(str)]), IntegerLit(1))), CallStmt(strcpy, Id(bin), Id(str)), VarDecl(lenBin, IntegerType, FuncCall(strlen, [Id(bin)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(lenBin)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(bin), StringLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(lenBin), IntegerLit(1)), Id(i))), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(Id(a), BinExpr(*, Id(a), IntegerLit(2)))), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(a)))])), AssignStmt(Id(bin), BinExpr(+, Id(bin), IntegerLit(1)))])), ReturnStmt(ArrayCell(strlen, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """    // 3 variables but 2 values
main:function integer() {
        i, j: integer = 8,6;     
        print(calc(str));
}
"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(8)), VarDecl(j, IntegerType, IntegerLit(6)), CallStmt(print, FuncCall(calc, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """    // float have _
 sp1 : boolean = false;
 func:function integer() {
        for (i = strlen(str) - 1, i >= 0, i-1) {
                if (str[i] == "1") {
                        a = 1;
                        for (j = 0, j < (strlen(str) - i-1), j+1)
                                a = a * 2.34E8;
                        sum = sum + a;
                }
        }
}
        """
        expect = """Program([
	VarDecl(sp1, BooleanType, BooleanLit(False))
	FuncDecl(func, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(str, [Id(i)]), StringLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, FuncCall(strlen, [Id(str)]), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(Id(a), BinExpr(*, Id(a), FloatLit(234000000.0)))), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(a)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """    // EXP w/o num
 sp1 : boolean = false;
 func:function integer() {
    // EXP w/o num
print(strlen(str));// REMOVE

        // if need, use proper process header
        // CAL FOR SUM (old)
                /**/
    a = a * 2.34e-3;
}
"""
        expect = """Program([
	VarDecl(sp1, BooleanType, BooleanLit(False))
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(print, FuncCall(strlen, [Id(str)])), AssignStmt(Id(a), BinExpr(*, Id(a), FloatLit(0.00234)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """    // function call 2-level (())
    del : function void(str : string, n: integer) {			// del let.
	for (n=n, n < (strlen(str) - 1), n+1)
		str[n] = str[n + 1];			// copy af. to bef.
	str[strlen(str) - 1] = "";			// last is blank
	foo(2 + x, 4.0 / y);
    goo(2 + x, 4.0 / y);
	return;
}
"""
        expect = """Program([
	FuncDecl(del, VoidType, [Param(str, StringType), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(n), Id(n)), BinExpr(<, Id(n), BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))), BinExpr(+, Id(n), IntegerLit(1)), AssignStmt(ArrayCell(str, [Id(n)]), ArrayCell(str, [BinExpr(+, Id(n), IntegerLit(1))]))), AssignStmt(ArrayCell(str, [BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))]), StringLit()), CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """    // multi declare on prototype
proper: function void(str: string) {			// "   d&OaN   V$aN  hA*U    "
	// REWORK use pointer
	process(str,outstr);
	return;
}
"""
        expect = """Program([
	FuncDecl(proper, VoidType, [Param(str, StringType)], None, BlockStmt([CallStmt(process, Id(str), Id(outstr)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """    // array missed ]
 main : function integer ()
{
	str, outstr : string = "   d&OaN   V$aN  hA*U    ", char[strlen(str) + 1];
	proper(str, outstr);
	/* TODO*/
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(str, StringType, StringLit(   d&OaN   V$aN  hA*U    )), VarDecl(outstr, StringType, ArrayCell(char, [BinExpr(+, FuncCall(strlen, [Id(str)]), IntegerLit(1))])), CallStmt(proper, Id(str), Id(outstr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """    // Cannot be Array
calc: function integer(str : string) {                                                                  // convert from bin to dec
        // TODO
        i, j, a: array [3] of integer = 8,6,0;                                                                       // num pos, seq of binary multi loop
}"""
        expect = """Program([
	FuncDecl(calc, IntegerType, [Param(str, StringType)], None, BlockStmt([VarDecl(i, ArrayType([3], IntegerType), IntegerLit(8)), VarDecl(j, ArrayType([3], IntegerType), IntegerLit(6)), VarDecl(a, ArrayType([3], IntegerType), IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """    // Cannot declare variables in for
clrRightChar: function void(str : string) {
	for (i = 3, i < strlen(str), i+1) {		// set redundant char slots to blank
		stri: string;
	}
}"""
        expect = """Program([
	FuncDecl(clrRightChar, VoidType, [Param(str, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<, Id(i), FuncCall(strlen, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(stri, StringType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """    // Reverse INHERIT and OUT
    main : function void(inherit out str : string, n: integer) {			// del let.
	for (n=n, n < (strlen(str) - 1), n+1)
		str[n] = str[n + 1];			// copy af. to bef.
	str[strlen(str) - 1] = "";			// last is blank
	foo(2 + x, 4.0 / y);
    goo();
	return;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(str, StringType), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(n), Id(n)), BinExpr(<, Id(n), BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))), BinExpr(+, Id(n), IntegerLit(1)), AssignStmt(ArrayCell(str, [Id(n)]), ArrayCell(str, [BinExpr(+, Id(n), IntegerLit(1))]))), AssignStmt(ArrayCell(str, [BinExpr(-, FuncCall(strlen, [Id(str)]), IntegerLit(1))]), StringLit()), CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """    // Wrong array dimension access
        main : function void(str : string, n: integer) {			// del let.
                // TRANSFER TO OUTSTR (this var is harder to code)
            for (i = 0, (i < strlen(str)), i + 1) {
                            outstr[i] = str[i];
            }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(str, StringType), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(strlen, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(outstr, [Id(i)]), ArrayCell(str, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """    // Dots in ID
    cutString : function void(s : string, index: integer) {
    // TO DO
    if (index < ssize()) {
        s = ssubstr(index, ssize() - index);
        print(s);
    }
}
"""
        expect = """Program([
	FuncDecl(cutString, VoidType, [Param(s, StringType), Param(index, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(index), FuncCall(ssize, [])), BlockStmt([AssignStmt(Id(s), FuncCall(ssubstr, [Id(index), BinExpr(-, FuncCall(ssize, []), Id(index))])), CallStmt(print, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """    // Unclosed String with newline
    main : function integer(inherit out str : string) {
    s : string = "Truong Dai Hoc";
    cutString(s, 4);
}
"""
        expect = """Program([
	FuncDecl(main, IntegerType, [InheritOutParam(str, StringType)], None, BlockStmt([VarDecl(s, StringType, StringLit(Truong Dai Hoc)), CallStmt(cutString, Id(s), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test400(self):
        input = """
                    a: function boolean(){}
                    main: function void() inherit a{
                        x: integer;
                        y: auto = 3;
                        for (x=3, true,x) {z: integer = 3; return;}
                    }
                    """
        expect = """Program([
	FuncDecl(a, BooleanType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], a, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, AutoType, IntegerLit(3)), ForStmt(AssignStmt(Id(x), IntegerLit(3)), BooleanLit(True), Id(x), BlockStmt([VarDecl(z, IntegerType, IntegerLit(3)), ReturnStmt()]))]))])
])"""
        self.assertTrue(TestAST.test(input, expect, 400))

    def test401(self):
        input = """main: function void(){
                        while (true){
                            if (true)
                                break;
                            while (false)
                                if (false)
                                    break;
                            continue;
                        }
                        return "should raise this";
                    }
                    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BreakStmt()), WhileStmt(BooleanLit(False), IfStmt(BooleanLit(False), BreakStmt())), ContinueStmt()])), ReturnStmt(StringLit(should raise this))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))

    def test402(self):
        input = """a: float = 3.0;
                    f1: function boolean(x: integer, y: string){
                        //return false;
                    }
                    f2: function integer(y: integer){
                        while (f1(2.0, "4")) return;
                        b: auto = 3;
                        b = true;
                        y = 3;
                        for(y = 3, true, !f1()) return;
                        y = 3;
                    }
                    main: function void(){
                        f1();
                        y: auto = 3;
                        for (x=-3, true,f1()) {z: integer = 3; return;}
                    }
                    """
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(3.0))
	FuncDecl(f1, BooleanType, [Param(x, IntegerType), Param(y, StringType)], None, BlockStmt([]))
	FuncDecl(f2, IntegerType, [Param(y, IntegerType)], None, BlockStmt([WhileStmt(FuncCall(f1, [FloatLit(2.0), StringLit(4)]), ReturnStmt()), VarDecl(b, AutoType, IntegerLit(3)), AssignStmt(Id(b), BooleanLit(True)), AssignStmt(Id(y), IntegerLit(3)), ForStmt(AssignStmt(Id(y), IntegerLit(3)), BooleanLit(True), UnExpr(!, FuncCall(f1, [])), ReturnStmt()), AssignStmt(Id(y), IntegerLit(3))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, ), VarDecl(y, AutoType, IntegerLit(3)), ForStmt(AssignStmt(Id(x), UnExpr(-, IntegerLit(3))), BooleanLit(True), FuncCall(f1, []), BlockStmt([VarDecl(z, IntegerType, IntegerLit(3)), ReturnStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 402))

    def test403(self):
        input = """main: function void(){
                        newConversation: integer = 3.0; // possible in PPL 233
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(newConversation, IntegerType, FloatLit(3.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 403))

    def test404(self):
        input = """
        sub: function boolean(){
            return true;    // this okay

            return "do not raise error on second return";
            while (true)
            {
                return "PLEASE RAISE THIS ILLEGAL STRING ON STMT";
            }
        }
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(sub, BooleanType, [], None, BlockStmt([ReturnStmt(BooleanLit(True)), ReturnStmt(StringLit(do not raise error on second return)), WhileStmt(BooleanLit(True), BlockStmt([ReturnStmt(StringLit(PLEASE RAISE THIS ILLEGAL STRING ON STMT))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 404))

    def test405(self):
        input = """ main: function void(){
                        arr: array [3,2] of integer = {{1, 2}, {3, 4}, {0,1}};
                        arr[9, 0] = 4.5;
                        a: integer = arr[1] - 9;
                    }
                    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(0), IntegerLit(1)])])), AssignStmt(ArrayCell(arr, [IntegerLit(9), IntegerLit(0)]), FloatLit(4.5)), VarDecl(a, IntegerType, BinExpr(-, ArrayCell(arr, [IntegerLit(1)]), IntegerLit(9)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 405))

    def test406(self):
        input = """
        f2: function integer(inherit p3: integer, p0: boolean) inherit f1{
            super(1, 2);
            p2: boolean;
        }
        f1: function integer(inherit p1: integer,  p2: integer) inherit f0{
            super(2);
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [InheritParam(p3, IntegerType), Param(p0, BooleanType)], f1, BlockStmt([CallStmt(super, IntegerLit(1), IntegerLit(2)), VarDecl(p2, BooleanType)]))
	FuncDecl(f1, IntegerType, [InheritParam(p1, IntegerType), Param(p2, IntegerType)], f0, BlockStmt([CallStmt(super, IntegerLit(2))]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 406))

    def test407(self):
        input = """
        f2: function integer(inherit p3: integer) inherit f1{
            super(1, 2, 5, 7, 9);
            p2: boolean;
        }
        f1: function integer(inherit p1: integer,  p2: integer) inherit f0{
            super(2);
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [InheritParam(p3, IntegerType)], f1, BlockStmt([CallStmt(super, IntegerLit(1), IntegerLit(2), IntegerLit(5), IntegerLit(7), IntegerLit(9)), VarDecl(p2, BooleanType)]))
	FuncDecl(f1, IntegerType, [InheritParam(p1, IntegerType), Param(p2, IntegerType)], f0, BlockStmt([CallStmt(super, IntegerLit(2))]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 407))

    def test408(self):
        input = """
        f2: function integer(inherit p3: integer) inherit f1{
            super("1");
            p2: boolean;
        }
        f1: function integer(inherit p1: integer,  p2: integer) inherit f0{
            super(2);
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [InheritParam(p3, IntegerType)], f1, BlockStmt([CallStmt(super, StringLit(1)), VarDecl(p2, BooleanType)]))
	FuncDecl(f1, IntegerType, [InheritParam(p1, IntegerType), Param(p2, IntegerType)], f0, BlockStmt([CallStmt(super, IntegerLit(2))]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 408))

    def test409(self):
        input = """
        f2: function integer() inherit f1{
            super(1, "2");
            p2: boolean;
        }
        f1: function integer(inherit p1: integer, inherit p2: integer) inherit f0{
            super(2);
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [], f1, BlockStmt([CallStmt(super, IntegerLit(1), StringLit(2)), VarDecl(p2, BooleanType)]))
	FuncDecl(f1, IntegerType, [InheritParam(p1, IntegerType), InheritParam(p2, IntegerType)], f0, BlockStmt([CallStmt(super, IntegerLit(2))]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 409))

    def test410(self):
        input = """
        f2: function integer() inherit f1{
            super(1);
            p2: boolean;
        }
        f1: function integer(inherit p1: integer, inherit p2: integer) inherit f0{
            super(2);
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [], f1, BlockStmt([CallStmt(super, IntegerLit(1)), VarDecl(p2, BooleanType)]))
	FuncDecl(f1, IntegerType, [InheritParam(p1, IntegerType), InheritParam(p2, IntegerType)], f0, BlockStmt([CallStmt(super, IntegerLit(2))]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 410))

    def test411(self):
        input = """
        x: function float () {
            x: float = x + x;
            return x;
        }
        """
        expect = """Program([
	FuncDecl(x, FloatType, [], None, BlockStmt([VarDecl(x, FloatType, BinExpr(+, Id(x), Id(x))), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 411))

    def test412(self):
        input = """
        x: function float () {
            x: float = x() + x;
            return x;
        }
        """
        expect = """Program([
	FuncDecl(x, FloatType, [], None, BlockStmt([VarDecl(x, FloatType, BinExpr(+, FuncCall(x, []), Id(x))), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 412))

    def test413(self):
        input = """
        f2: function integer(p1: integer,  p2: integer) inherit f1{
            super(1, 2);
        }
        f1: function integer(inherit p1: integer, inherit p2: integer) inherit f0{
            super(2);
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [Param(p1, IntegerType), Param(p2, IntegerType)], f1, BlockStmt([CallStmt(super, IntegerLit(1), IntegerLit(2))]))
	FuncDecl(f1, IntegerType, [InheritParam(p1, IntegerType), InheritParam(p2, IntegerType)], f0, BlockStmt([CallStmt(super, IntegerLit(2))]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))

])"""
        self.assertTrue(TestAST.test(input, expect, 413))

    def test414(self):
        input = """
        main: function void(){
            a: array [5,5] of integer;
            b: integer;
            b = a[1.0,"1"];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5, 5], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [FloatLit(1.0), StringLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 414))

    def test415(self):
        input = """
        M: function void (a: integer) inherit N {}
        N: function void (inherit a: integer) {}
        """
        expect = """Program([
	FuncDecl(M, VoidType, [Param(a, IntegerType)], N, BlockStmt([]))
	FuncDecl(N, VoidType, [InheritParam(a, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 415))

    def test416(self):
        input = """
        f2: function integer(p1: integer,  p2: integer) inherit f0{
            /* check prototype first before checking block stmt
            you need to create another loops to collect global scope bro =)))*/
        }
        f2: function integer(inherit p1: integer, inherit p2: integer) inherit f0{
            // first loop does not raise any errors
        }
        f0: function float(inherit out p0: integer){}
        main: function void(){}
        """
        expect = """Program([
	FuncDecl(f2, IntegerType, [Param(p1, IntegerType), Param(p2, IntegerType)], f0, BlockStmt([]))
	FuncDecl(f2, IntegerType, [InheritParam(p1, IntegerType), InheritParam(p2, IntegerType)], f0, BlockStmt([]))
	FuncDecl(f0, FloatType, [InheritOutParam(p0, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 416))
    def test_417 (self):
        input = """
        inc : function void (out n : integer, a: float) inherit foo {}
        foo : function auto (inherit n: float, n: integer){}
        main: function void()
        {

        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(a, FloatType)], foo, BlockStmt([]))
	FuncDecl(foo, AutoType, [InheritParam(n, FloatType), Param(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 417))

    def test_418 (self):
        input = """
        foo: function integer(a: auto) inherit foo1
        {
            preventDefault();
            if (a < 20)
            {
                x: integer = 5;
                return x;
            }
            return 3;
        }
        foo1: function integer(inherit x: integer)
        {
            preventDefault();
        }
        main: function void () {

        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, AutoType)], foo1, BlockStmt([CallStmt(preventDefault, ), IfStmt(BinExpr(<, Id(a), IntegerLit(20)), BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), ReturnStmt(Id(x))])), ReturnStmt(IntegerLit(3))]))
	FuncDecl(foo1, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([CallStmt(preventDefault, )]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 418))

    def test_419 (self):
        input = """
        main: function void(){
            a: array [5,5] of integer;
            b: integer;
            b = a[1.0,"1"];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5, 5], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [FloatLit(1.0), StringLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 419))

    def test_420 (self):
        input = """
        foo: function auto(){
            return 0;
        }
        main: function void(){
            foo();
        }"""
        expect = """Program([
	FuncDecl(foo, AutoType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 420))

    def test_421 (self):
        input = """
        main: function void()
        {
            x: array [3] of integer;
            y: array [3] of integer;
            x = {1, 2, 3};
            x[2] = 7;
            y = x;
            printInteger(y[2]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), VarDecl(y, ArrayType([3], IntegerType)), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(x, [IntegerLit(2)]), IntegerLit(7)), AssignStmt(Id(y), Id(x)), CallStmt(printInteger, ArrayCell(y, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 421))

    def test422(self):
        input = """
                    main: function void(){
                        x: auto = "str";        // considered x as Boolean
                        printBoolean(x);
                    }
                    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, AutoType, StringLit(str)), CallStmt(printBoolean, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 422))

    def test423(self):
        input = """
            /*f2: function integer(c: integer) inherit f1{
                super(1, 2);
            }*/
            f1: function auto(a: auto, b: auto){
                    c: auto = a == b;
                    d: auto = a + b;
                    return d;
            }
            main: function void(){
                printInteger(f1(2,3));
            }
        """
        expect = """Program([
	FuncDecl(f1, AutoType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([VarDecl(c, AutoType, BinExpr(==, Id(a), Id(b))), VarDecl(d, AutoType, BinExpr(+, Id(a), Id(b))), ReturnStmt(Id(d))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(f1, [IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 423))

    def test_424 (self):
        input = """
        foo : function auto(inherit x: auto, inherit y: auto, z: auto){
            return x + y + z;
        }
        main : function void() inherit foo {
            super(1.0, 2.0, 3.0);
            z: integer = foo(1, 2, 3) + 1;
            x = "abc";
            y = true;
        }
        """
        expect = """Program([
	FuncDecl(foo, AutoType, [InheritParam(x, AutoType), InheritParam(y, AutoType), Param(z, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
	FuncDecl(main, VoidType, [], foo, BlockStmt([CallStmt(super, FloatLit(1.0), FloatLit(2.0), FloatLit(3.0)), VarDecl(z, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(x), StringLit(abc)), AssignStmt(Id(y), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 424))

    def test_425 (self):
        input = """
        main : function void() inherit foo {
            super(1.0, 2.0, 3.0);
            z: integer = foo(1, 2, 3) + 1;
            x = "abc";
            y = true;
        }
        foo : function auto(inherit x: auto, inherit y: auto, z: auto){
            return x + y + z;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], foo, BlockStmt([CallStmt(super, FloatLit(1.0), FloatLit(2.0), FloatLit(3.0)), VarDecl(z, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(x), StringLit(abc)), AssignStmt(Id(y), BooleanLit(True))]))
	FuncDecl(foo, AutoType, [InheritParam(x, AutoType), InheritParam(y, AutoType), Param(z, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 425))

    def test426(self):
        input = """
        main: function void(){
            a,b,c,d: float;
            x: integer = a + b :: c - d;
            return;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), VarDecl(d, FloatType), VarDecl(x, IntegerType, BinExpr(::, BinExpr(+, Id(a), Id(b)), BinExpr(-, Id(c), Id(d)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 426))

    def test427(self):
        input = """
        sub: function boolean(){
            return true;    // this okay

            return "a";
            while (true)
            {
                return "b";
            }
        }
        main: function void(){
            return;
        }
        """
        expect = """Program([
	FuncDecl(sub, BooleanType, [], None, BlockStmt([ReturnStmt(BooleanLit(True)), ReturnStmt(StringLit(a)), WhileStmt(BooleanLit(True), BlockStmt([ReturnStmt(StringLit(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 427))

    def test428(self):
        input = """
        M: function void (a: integer) inherit N {}
        M: function void () {}
        N: function void (inherit a: integer) {}
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestAST.test(input, expect, 428))

    def test429(self):
        input = """
        main: function void(){
            while (true){
                if (true)
                    break;			// 1
                while (false)
                    if (false)
                        break;		// 2
                continue;			// 3
                }
            continue;				// 4
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestAST.test(input, expect, 429))

    def test500(self):
        input = """
        main: function void(){

        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 500))

    def test501(self):
        input = """
        //x: integer = 3; // Input 3
        main: function void(){
            printInteger(5);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 501))

    def test_502(self):
        input = """
        main: function void()
        {
            x: integer;
            x = 3;
            printInteger(x);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), IntegerLit(3)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 502))

    def test_503(self):
        input = """
        main: function void()
        {
            x: integer = readInteger(); // Input 3
            printInteger(x);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(readInteger, [])), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 503))

    def test_504(self):
        input = """
        main: function void()
        {
            x: float = 3.0; // Input 3.0
            y: float = 0.5;       // Input 0.5
            printFloat(y);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(3.0)), VarDecl(y, FloatType, FloatLit(0.5)), CallStmt(printFloat, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 504))

    def test_505(self):
        input = """
        main: function void()
        {
            x: integer = 3; // Input 3
            y: float = readFloat();       // Input 0.5
            printFloat(y);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, FloatType, FuncCall(readFloat, [])), CallStmt(printFloat, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 505))

    def test_506(self):
        input = """
        main: function void()
        {
            x: string = readString();       // input 3d
            y: boolean = readBoolean();     // input true
            printString(x);
            printBoolean(y);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, FuncCall(readString, [])), VarDecl(y, BooleanType, FuncCall(readBoolean, [])), CallStmt(printString, Id(x)), CallStmt(printBoolean, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 506))

    def test_507(self):
        input = """
        main: function void()
        {
            x: integer = 3;
            y: integer = 4;
            printInteger(x + y);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(4)), CallStmt(printInteger, BinExpr(+, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 507))

    def test_508(self):
        input = """
        main: function void()
        {
            x: boolean = false;
            printBoolean(!x);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, BooleanType, BooleanLit(False)), CallStmt(printBoolean, UnExpr(!, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 508))

    def test_509(self):
        input = """
        main: function void()
        {
            printInteger(12%5);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, BinExpr(%, IntegerLit(12), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 509))

    def test_510(self):
        input = """
        main: function void()
        {
            x: integer = 3;
            y: integer = 3;
            if (x == y)
                printBoolean(true);
            else
                printBoolean(false);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(3)), IfStmt(BinExpr(==, Id(x), Id(y)), CallStmt(printBoolean, BooleanLit(True)), CallStmt(printBoolean, BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 510))

    def test_511(self):
        input = """
            main: function void()
            {
                x: integer = 3;
                y: integer = 4;
                while (x != y)
                    x = x + 1;
                printString("Successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(4)), WhileStmt(BinExpr(!=, Id(x), Id(y)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 511))

    def test_512(self):
        input = """
            main: function void()
            {
                x: integer = 2;
                y: integer = 4;

                do {x = x + 1;}
                while (x != y);
                printString("Successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(4)), DoWhileStmt(BinExpr(!=, Id(x), Id(y)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 512))

    def test_513(self):
        input = """
            main: function void()
            {
                x: integer = 2;
                y: integer = 4;

                for (x = 0, x < y, 1){
                    printInteger(x);
                }
                printString("Successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(y)), IntegerLit(1), BlockStmt([CallStmt(printInteger, Id(x))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 513))

    def test_514(self):
        input = """
            main: function void()
            {
                x: integer = 2;
                y: integer = 4;

                for (x = 0, x < y, 1){
                    if (x == 2)
                        break;
                    printInteger(x);
                }
                printString("Successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(y)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(2)), BreakStmt()), CallStmt(printInteger, Id(x))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 514))

    def test_515(self):
        input = """
            main: function void()
            {
                x: integer = 2;
                y: integer = 4;

                for (x = 0, x < y, 1){
                    if (x == 2)
                        continue;
                    printInteger(x);
                }
                printString("Successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(y)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(2)), ContinueStmt()), CallStmt(printInteger, Id(x))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 515))

    def test_516(self):
        input = """
            main: function void()
            {
                x: integer = 2;
                y: integer = 4;

                for (x = 0, x < y, 1){
                    if (x == 2)
                        continue;
                    printInteger(x);
                }
                printString("Successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(y)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(2)), ContinueStmt()), CallStmt(printInteger, Id(x))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 516))

    def test_517(self):
        input = """
            main: function void()
            {
                x: integer = 0;
                y: integer = 4;
                while (x != y){
                    if (x == 2){
                        printString("Successfull");
                        return;
                        }
                    x = x + 1;
                    }
                printString("Not successfull");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(4)), WhileStmt(BinExpr(!=, Id(x), Id(y)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(2)), BlockStmt([CallStmt(printString, StringLit(Successfull)), ReturnStmt()])), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))])), CallStmt(printString, StringLit(Not successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 517))

    def test_518(self):
        input = """
                main: function void()
                {
                    x: array [3] of integer = {1, 2, 3};
                    x[2] = 7;
                    printInteger(x[2]);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(x, [IntegerLit(2)]), IntegerLit(7)), CallStmt(printInteger, ArrayCell(x, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 518))

    def test_519(self):             # arr 2
        input = """
                main: function void()
                {
                    x: array [3] of integer;
                    x = {1, 2, 3};
                    x[2] = 7;
                    printInteger(x[2]);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(x, [IntegerLit(2)]), IntegerLit(7)), CallStmt(printInteger, ArrayCell(x, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 519))

    def test_520(self):
        input = """
                main: function void()
                {
                    x: array [3] of integer;
                    y: array [3] of integer;
                    x = {1, 2, 3};
                    x[2] = 7;
                    y = x;
                    printInteger(y[2]);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), VarDecl(y, ArrayType([3], IntegerType)), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(x, [IntegerLit(2)]), IntegerLit(7)), AssignStmt(Id(y), Id(x)), CallStmt(printInteger, ArrayCell(y, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 520))

    def test_521(self):
        input = """
                main: function void()
                {
                    x: array [2,2] of integer = {{1, 2}, {3, 4}};
                    y: array [2,2] of integer;
                    y = x;
                    y[0, 0] = 7;
                    printInteger(y[0, 0]);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])), VarDecl(y, ArrayType([2, 2], IntegerType)), AssignStmt(Id(y), Id(x)), AssignStmt(ArrayCell(y, [IntegerLit(0), IntegerLit(0)]), IntegerLit(7)), CallStmt(printInteger, ArrayCell(y, [IntegerLit(0), IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 521))

    def test_522(self):
        input = """
                main: function void()
                {
                    x: float = 5;
                    printFloat(x);
                    y: integer = 6.8;
                    printInteger(y);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, IntegerLit(5)), CallStmt(printFloat, Id(x)), VarDecl(y, IntegerType, FloatLit(6.8)), CallStmt(printInteger, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 522))

    def test_523(self):
        input = """
                main: function void()
                {
                    x: auto = 5;
                    printInteger(x);
                    y: auto = 6.8;
                    printFloat(y);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, AutoType, IntegerLit(5)), CallStmt(printInteger, Id(x)), VarDecl(y, AutoType, FloatLit(6.8)), CallStmt(printFloat, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 523))

    def test_524(self):
        input = """
                main: function void()
                {
                    x: string = "PP";
                    x = x :: "L";
                    printString(x);
                    y: boolean = true && false || true;
                    printBoolean(y);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(PP)), AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(L))), CallStmt(printString, Id(x)), VarDecl(y, BooleanType, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BooleanLit(True))), CallStmt(printBoolean, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 524))

    def test_525(self):
        input = """
                main: function void()
                {
                     y: boolean = true && false || false;
                     printBoolean(y);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(y, BooleanType, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BooleanLit(False))), CallStmt(printBoolean, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 525))

    def test_526(self):
        input = """
                main: function void()
                {
                     x: integer = 1;
                     {
                        x: integer = 4;
                        printInteger(x);
                     }
                     printInteger(x);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), BlockStmt([VarDecl(x, IntegerType, IntegerLit(4)), CallStmt(printInteger, Id(x))]), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 526))

    def test_527(self):
        input = """
                x: boolean;
                y: boolean = true && false || false;
                main: function void()
                {
                     x = true;
                     printBoolean(x);
                     printBoolean(y);
                }"""
        expect = """Program([
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BooleanLit(False)))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BooleanLit(True)), CallStmt(printBoolean, Id(x)), CallStmt(printBoolean, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 527))

    def test_528(self):
        input = """
                x: array [2] of boolean = {false, false};
                y: array [2, 2] of boolean = {x, {false, true}};
                main: function void()
                {
                     x[1] = true;
                     printBoolean(x[1]);
                     printBoolean(y[1, 0]);
                }"""
        expect = """Program([
	VarDecl(x, ArrayType([2], BooleanType), ArrayLit([BooleanLit(False), BooleanLit(False)]))
	VarDecl(y, ArrayType([2, 2], BooleanType), ArrayLit([Id(x), ArrayLit([BooleanLit(False), BooleanLit(True)])]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1)]), BooleanLit(True)), CallStmt(printBoolean, ArrayCell(x, [IntegerLit(1)])), CallStmt(printBoolean, ArrayCell(y, [IntegerLit(1), IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 528))

    def test_529(self):
        input = """
                f1: function void(){
                    printString("Successfull");
                }
                main: function void()
                {
                     f1();
                }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(Successfull))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 529))

    def test_530(self):
        input = """
                f1: function void(str: string){
                    printString(str);
                }
                main: function void()
                {
                     f1("Successfull");
                }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [Param(str, StringType)], None, BlockStmt([CallStmt(printString, Id(str))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 530))

    def test_531(self):
        input = """
                f1: function void(i: integer, f: float, b: boolean, str: string){
                    printInteger(i);
                    printFloat(f);
                    printBoolean(b);
                    printString(str);
                }
                main: function void()
                {
                     f1(3, 0.0, false, "Successfull");
                }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [Param(i, IntegerType), Param(f, FloatType), Param(b, BooleanType), Param(str, StringType)], None, BlockStmt([CallStmt(printInteger, Id(i)), CallStmt(printFloat, Id(f)), CallStmt(printBoolean, Id(b)), CallStmt(printString, Id(str))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, IntegerLit(3), FloatLit(0.0), BooleanLit(False), StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 531))

    def test_532(self):
        input = """
                str: string = "Successfull";
                f1: function void(str: string){
                    printString(str);
                }
                main: function void()
                {
                     f1("Successfull");
                }"""
        expect = """Program([
	VarDecl(str, StringType, StringLit(Successfull))
	FuncDecl(f1, VoidType, [Param(str, StringType)], None, BlockStmt([CallStmt(printString, Id(str))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 532))


    def test_533(self):
        input = """
        x: integer;

        f1: function void(){
            x = 1;
            printInteger(x);
        }
        f2: function integer(){
            x = 2;
            return x;
        }
        main: function void()
        {
             f1();
             printInteger(f2());
        }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(f1, VoidType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), CallStmt(printInteger, Id(x))]))
	FuncDecl(f2, IntegerType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(2)), ReturnStmt(Id(x))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, ), CallStmt(printInteger, FuncCall(f2, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 533))

    def test_534(self):
        input = """
        f1: function void(){
            printString("f1");
        }
        f2: function void() inherit f1{
            preventDefault();
            printString("f2");
        }
        main: function void()
        {
             f2();
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(f1))]))
	FuncDecl(f2, VoidType, [], f1, BlockStmt([CallStmt(preventDefault, ), CallStmt(printString, StringLit(f2))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f2, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 534))

    def test_535(self):
        input = """
        f1: function void(){
            printString("f1");
        }
        f2: function void() inherit f1{
            //preventDefault();
            printString("f2");
        }
        main: function void()
        {
             f2();
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(f1))]))
	FuncDecl(f2, VoidType, [], f1, BlockStmt([CallStmt(printString, StringLit(f2))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f2, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 535))

    def test_536(self):
        input = """
        f1: function void(a: string){
            printString("f1");
        }
        f2: function void() inherit f1{
            preventDefault();
            printString("f2");
        }
        main: function void()
        {
             f2();
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [Param(a, StringType)], None, BlockStmt([CallStmt(printString, StringLit(f1))]))
	FuncDecl(f2, VoidType, [], f1, BlockStmt([CallStmt(preventDefault, ), CallStmt(printString, StringLit(f2))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f2, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 536))

    def test_537(self):
        input = """
        f1: function void(a: string){
            printString(a);
        }
        f2: function void() inherit f1{
            super("f1");
            printString("f2");
        }
        main: function void()
        {
             f2();
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [Param(a, StringType)], None, BlockStmt([CallStmt(printString, Id(a))]))
	FuncDecl(f2, VoidType, [], f1, BlockStmt([CallStmt(super, StringLit(f1)), CallStmt(printString, StringLit(f2))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f2, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 537))

    def test_538(self):
        input = """
        f1: function void(inherit a: string){
            printString(a);
        }
        f2: function void() inherit f1{
            super("f1");
            a = "f2";
            printString(a);
        }
        main: function void()
        {
             f2();
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [InheritParam(a, StringType)], None, BlockStmt([CallStmt(printString, Id(a))]))
	FuncDecl(f2, VoidType, [], f1, BlockStmt([CallStmt(super, StringLit(f1)), AssignStmt(Id(a), StringLit(f2)), CallStmt(printString, Id(a))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f2, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 538))

    def test_539(self):
        input = """
        f1: function void(inherit a: string){
            printString(a);
        }
        f2: function void(inherit b: string) inherit f1{
            super("f1");
            printString(b);
        }
        f3: function void() inherit f2{
            super("f2");
            a = "f1";
            b = "f2";
            printString(a);
            printString(b);
            printString("f3");
        }
        main: function void()
        {
             f3();
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [InheritParam(a, StringType)], None, BlockStmt([CallStmt(printString, Id(a))]))
	FuncDecl(f2, VoidType, [InheritParam(b, StringType)], f1, BlockStmt([CallStmt(super, StringLit(f1)), CallStmt(printString, Id(b))]))
	FuncDecl(f3, VoidType, [], f2, BlockStmt([CallStmt(super, StringLit(f2)), AssignStmt(Id(a), StringLit(f1)), AssignStmt(Id(b), StringLit(f2)), CallStmt(printString, Id(a)), CallStmt(printString, Id(b)), CallStmt(printString, StringLit(f3))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f3, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 539))

    def test_540(self):
        input = """
        f1: function integer(inherit x: float){
             return 6.6;
        }
        main: function void()
        {
             x: float = f1(4);
             y: float;
             y = 7;
             printFloat(x);
             printFloat(y);
        }"""
        expect = """Program([
	FuncDecl(f1, IntegerType, [InheritParam(x, FloatType)], None, BlockStmt([ReturnStmt(FloatLit(6.6))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FuncCall(f1, [IntegerLit(4)])), VarDecl(y, FloatType), AssignStmt(Id(y), IntegerLit(7)), CallStmt(printFloat, Id(x)), CallStmt(printFloat, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 540))

    def test_541(self):
        input = """
        f1: function void(out x: string){
             x = "f1";
        }
        main: function void()
        {
             y: string = "main";
             f1(y);
             printString(y);
        }"""
        expect = """Program([
	FuncDecl(f1, VoidType, [OutParam(x, StringType)], None, BlockStmt([AssignStmt(Id(x), StringLit(f1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(y, StringType, StringLit(main)), CallStmt(f1, Id(y)), CallStmt(printString, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 541))

    def test_542(self):
        input = """
                    main: function void()
                    {
                        x: integer = 0;
                        y: integer = 0;

                        while (x < 2){
                            while (y < 2){
                                printInteger(x);
                                printInteger(y);
                                y = y + 1;
                            }
                            x = x + 1;
                            y = 0;
                        }

                        printString("Successfull");
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(x), IntegerLit(2)), BlockStmt([WhileStmt(BinExpr(<, Id(y), IntegerLit(2)), BlockStmt([CallStmt(printInteger, Id(x)), CallStmt(printInteger, Id(y)), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))])), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), AssignStmt(Id(y), IntegerLit(0))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 542))

    def test_543(self):
        input = """     main: function void()
                        {
                            x: integer = 0;
                            y: integer = 0;

                            do {
                                do {
                                    printInteger(x);
                                    printInteger(y);
                                    y = y + 1;
                                } while (y < 2);
                                x = x + 1;
                                y = 0;
                            } while (x < 2);

                            printString("Successfull");
                        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(x), IntegerLit(2)), BlockStmt([DoWhileStmt(BinExpr(<, Id(y), IntegerLit(2)), BlockStmt([CallStmt(printInteger, Id(x)), CallStmt(printInteger, Id(y)), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))])), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), AssignStmt(Id(y), IntegerLit(0))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 543))

    def test_544(self):
        input = """
                main: function void()
                {
                    x: integer = 2;
                    y: integer = 4;

                    for (x = 0, x < 2, 1){
                        for (y = 0, y < 2, 1){
                            printInteger(x);
                            printInteger(y);
                        }
                    }
                    printString("Successfull");
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(4)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), IntegerLit(2)), IntegerLit(1), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), IntegerLit(2)), IntegerLit(1), BlockStmt([CallStmt(printInteger, Id(x)), CallStmt(printInteger, Id(y))]))])), CallStmt(printString, StringLit(Successfull))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 544))

    def test_599 (self):
        input = """
        main: function void()
        {
            printString("CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 599))