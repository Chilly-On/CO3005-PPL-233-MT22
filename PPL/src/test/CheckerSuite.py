import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test400(self):
        input = """
                    a: function boolean(){}
                    main: function void() inherit a{
                        x: integer;
                        y: auto = 3;
                        for (x=3, true,x) {z: integer = 3; return;}
                    }
                    """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))

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
        expect = "Type mismatch in statement: ReturnStmt(StringLit(should raise this))"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test402(self):
        input = """a: float = 3.0;
                    f1: function boolean(x: integer, y: string){
                        //return false;
                    }
                    f2: function integer(y: integer){
                        while (f1(2, "4")) return;
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
        expect = "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test403(self):
        input = """main: function void(){
                        newConversation: integer = 3.0;
                    }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(newConversation, IntegerType, FloatLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 403))

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
        expect = "Type mismatch in statement: ReturnStmt(StringLit(PLEASE RAISE THIS ILLEGAL STRING ON STMT))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test405(self):
        input = """ main: function void(){
                        arr: array [3,2] of integer = {{1, 2}, {3, 4}, {0,1}};
                        arr[9, 0] = 4;
                        a: integer = arr[1] - 9;
                    }
                    """
        expect = "Type mismatch in expression: BinExpr(-, ArrayCell(arr, [IntegerLit(1)]), IntegerLit(9))"
        self.assertTrue(TestChecker.test(input, expect, 405))

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
        expect = "Invalid Parameter: p0"
        self.assertTrue(TestChecker.test(input, expect, 406))

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
        expect = "Type mismatch in expression: IntegerLit(5)"
        self.assertTrue(TestChecker.test(input, expect, 407))

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
        expect = "Type mismatch in expression: StringLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 408))

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
        expect = "Type mismatch in expression: StringLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 409))

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
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test411(self):
        input = """
        x: function float () {
            x: float = x + x;
            return x;
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test412(self):
        input = """
        x: function float () {
            x: float = x() + x;
            return x;
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 412))

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
        expect = "Invalid Parameter: p1"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test414(self):
        input = """
        main: function void(){
            a: array [5,5] of integer;
            b: integer;
            b = a[1.0,"1"];
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0), StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test415(self):
        input = """
        M: function void (a: integer) inherit N {}
        N: function void (inherit a: integer) {}
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 415))

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
        expect = "Invalid statement in function: f2"
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_417(self):
        input = """
        inc : function void (out n : integer, a: float) inherit foo {}
        foo : function auto (inherit n: float, n: integer){}
        main: function void()
        {

        }"""
        expect = "Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
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
        expect = "Invalid statement in function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
        main: function void(){
            a: array [5,5] of integer;
            b: integer;
            b = a[1.0,"1"];
        }"""
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0), StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
        foo: function auto(){
            return 0;
        }
        main: function void(){
            foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
                    main: function void(){
                        x: auto = "str";        // considered x as Boolean
                        printBoolean(x);
                    }
                    """
        expect = "Type mismatch in statement: CallStmt(printBoolean, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
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
        expect = "Type mismatch in statement: AssignStmt(Id(x), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
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
        expect = "Type mismatch in statement: AssignStmt(Id(x), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test426(self):
        input = """
        main: function void(){
            a,b,c,d: float;
            x: integer = a + b :: c - d;
            return;
        }
    """
        expect = "Type mismatch in expression: BinExpr(::, BinExpr(+, Id(a), Id(b)), BinExpr(-, Id(c), Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
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
        expect = "Type mismatch in statement: ReturnStmt(StringLit(b))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test428(self):
        input = """
        M: function void (a: integer) inherit N {}
        M: function void () {}
        N: function void (inherit a: integer) {}
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 428))

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
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test430(self):
        input = """
                    a: integer;
                    a: function boolean(){}
                    main: function void() inherit a{

                    }
                    """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test431(self):
        input = """
                    f2: function boolean(inherit c: string){}
                    f1: function boolean() inherit f2{
                        preventDefault();
                    }
                    main: function void() inherit f1{
                        c: string;              // have c in f2
                    }
                    """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test432(self):
        input = """
                    f1: function boolean(){
                        preventDefault();
                    }
                    main: function void() inherit f1{
                        c: string;              // not have c in f2
                    }
                    """
        expect = "Invalid statement in function: f1"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test433(self):
        input = """
                    f1: function boolean(inherit a: integer){
                    
                    }
                    main: function void() inherit f1{
                        preventDefault();
                        c: string;              // not have c in f2
                    }
                    """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test434(self):
        input = """
                    f1: function boolean(inherit a: integer){
                        preventDefault();
                    }
                    main: function void(){
                        arr: array [1,2] of integer = {{1, "1"}};
                    }
                    """
        expect = "Invalid statement in function: f1"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test435(self):
        input = """
                    f2: function boolean(){
                    }
                    f1: function boolean() inherit f2{
                        super();
                    }
                    main: function void(){
                        //arr: array [1,2] of integer = {{1, "1"}};
                    }
                    """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test436(self):
        input = """
                    f2: function boolean(){
                    }
                    f1: function boolean() inherit f2{
                        super(3);
                    }
                    main: function void(){
                        //arr: array [1,2] of integer = {{1, "1"}};
                    }
                    """
        expect = "Type mismatch in expression: IntegerLit(3)"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test437(self):
        input = """
                    main: function void(){
                        arr: array [1,2] of integer = {};
                    }
                    """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([1, 2], IntegerType), ArrayLit([]))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test438(self):
        input = """
                    main: function void(){
                        arr: array [1] of integer = {{1, 1}};
                    }
                    """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([1], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test439(self):
        input = """
                    main: function void(){
                        arr: array [1,2] of integer = {{1, "1"}};
                    }
                    """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), StringLit(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test440(self):
        input = """
                    f1: function boolean(a: auto, b: auto){
                        arr: array [2, 2] of integer = {a, {b, 1}};
                        printInteger(b);
                        printInteger(a);
                    }
                    main: function void(){

                    }
                    """
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test441(self):
        input = """
                    main: function void(){
                        f1("1", 1);
                    }
                    f1: function boolean(a: auto, b: auto){
                        return a == b;
                    }
                    """
        expect = "Type mismatch in expression: BinExpr(==, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test442(self):
        input = """
                    main: function void() inherit f1{
                        super("1", 1);
                    }
                    f1: function boolean(a: auto, b: auto){
                        return a == b;
                    }
                    """
        expect = "Type mismatch in expression: BinExpr(==, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test443(self):
        input = """
            main : function void() {}
            f0 : function auto(x: auto, y: auto, z: auto, t: auto){
                for (x = 3, y == z, t){}
                //x = 3;
                //y, z = true, false;

            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test444(self):
        input = """
            main : function void() {}
            f0 : function auto(x: auto, y: auto, z: auto, t: auto, a: auto, b: auto, c: auto, d: auto){
                d2: integer = a;
                d3: auto = a;
                for (x = 3, y == z, t){}
                if (b) {}
                while (c) {}
                do {} while (d);
                return a;
                d1: integer = a + 3.5;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(d1, IntegerType, BinExpr(+, Id(a), FloatLit(3.5)))"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test445(self):
        input = """
        sub: function boolean(){
            while (true)
            {
                return true;    // this okay
            }
            return "PLEASE RAISE THIS ILLEGAL STRING ON STMT";
        }
        main: function void(){}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(PLEASE RAISE THIS ILLEGAL STRING ON STMT))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test446(self):
        input = """
        f2: function integer() inherit f1{
            preventDefault();
            p0 = 1.0;                   // p0 from f1
        }
        f1: function integer(inherit p0: integer) inherit f0{   // Invalid Parameter: p0
            preventDefault();
        }
        f0: function float(inherit out p0: float){}
        main: function void(){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(p0), FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test447(self):
        input = """main: function void(){
                    a: array [1,2] of float = {1, 2.0, 3};

                   }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 447))