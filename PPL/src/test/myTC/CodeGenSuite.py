import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test500(self):
        input = """
        main: function void(){

        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test501(self):
        input = """
        //x: integer = 3; // Input 3
        main: function void(){
            printInteger(5);
        }
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_502(self):
        input = """
        main: function void()
        {
            x: integer;
            x = 3;
            printInteger(x);
        }"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_503(self):
        input = """
        main: function void()
        {
            x: integer = readInteger(); // Input 3
            printInteger(x);
        }"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_504(self):
        input = """
        main: function void()
        {
            x: float = 3.0; // Input 3.0
            y: float = 0.5;       // Input 0.5
            printFloat(y);
        }"""
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_505(self):
        input = """
        main: function void()
        {
            x: integer = 3; // Input 3
            y: float = readFloat();       // Input 0.5
            printFloat(y);
        }"""
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_506(self):
        input = """
        main: function void()
        {
            x: string = readString();       // input 3d
            y: boolean = readBoolean();     // input true
            printString(x);
            printBoolean(y);
        }"""
        expect = "3d\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_507(self):
        input = """
        main: function void()
        {
            x: integer = 3;
            y: integer = 4;
            printInteger(x + y);
        }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_508(self):
        input = """
        main: function void()
        {
            x: boolean = false;
            printBoolean(!x);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_509(self):
        input = """
        main: function void()
        {
            printInteger(12%5);
        }"""
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

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
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

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
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

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
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

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
        expect = "0\n1\n2\n3\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

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
        expect = "0\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

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
        expect = "0\n1\n3\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

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
        expect = "0\n1\n3\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

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
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_518(self):
        input = """
                main: function void()
                {
                    x: array [3] of integer = {1, 2, 3};
                    x[2] = 7;
                    printInteger(x[2]);
                }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_519(self):             # arr 2
        input = """
                main: function void()
                {
                    x: array [3] of integer;
                    x = {1, 2, 3};
                    x[2] = 7;
                    printInteger(x[2]);
                }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

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
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

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
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_522(self):
        input = """
                main: function void()
                {
                    x: float = 5;
                    printFloat(x);
                    y: integer = 6.8;
                    printInteger(y);
                }"""
        expect = "5.0\n6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_523(self):
        input = """
                main: function void()
                {
                    x: auto = 5;
                    printInteger(x);
                    y: auto = 6.8;
                    printFloat(y);
                }"""
        expect = "5\n6.8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

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
        expect = "PPL\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_525(self):
        input = """
                main: function void()
                {
                     y: boolean = true && false || false;
                     printBoolean(y);
                }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

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
        expect = "4\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

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
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

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
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_529(self):
        input = """
                f1: function void(){
                    printString("Successfull");
                }
                main: function void()
                {
                     f1();
                }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_530(self):
        input = """
                f1: function void(str: string){
                    printString(str);
                }
                main: function void()
                {
                     f1("Successfull");
                }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

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
        expect = "3\n0.0\nfalse\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

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
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))


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
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

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
        expect = "f2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

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
        expect = "f1\nf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

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
        expect = "f2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

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
        expect = "f1\nf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

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
        expect = "f1\nf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

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
        expect = "f1\nf2\nf1\nf2\nf3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

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
        expect = "6.0\n7.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

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
        expect = "f1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

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
        expect = "0\n0\n0\n1\n1\n0\n1\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

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
        expect = "0\n0\n0\n1\n1\n0\n1\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

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
        expect = "0\n0\n0\n1\n1\n0\n1\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_545 (self):
        input = """
        main: function void()
        {
            a: boolean;         // undecl
            if (true || a)
                printString("OR");     // ||
            else
                printString("AND");         // &&
        }"""
        expect = "OR\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_546(self):
        input = """
        f1: function array [3] of float(){

        }
        main: function void()
        {
             f1();
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_599 (self):
        input = """
        main: function void()
        {
            printString("CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!");
        }"""
        expect = "CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))
    def test600(self):
        input = """
        main: function void(){
            // 2nd
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test601(self):
        input = """
        //x: integer = 3; // Input 3
        main: function void(){// 2nd
            printInteger(5);
        }
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_602(self):
        input = """
        main: function void()// 2nd
        {
            x: integer;
            x = 3;
            printInteger(x);
        }"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_603(self):
        input = """
        main: function void()// 2nd
        {
            x: integer = readInteger(); // Input 3
            printInteger(x);
        }"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_604(self):
        input = """
        main: function void()// 2nd
        {
            x: float = 3.0; // Input 3.0
            y: float = 0.5;       // Input 0.5
            printFloat(y);
        }"""
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_605(self):
        input = """
        main: function void()// 2nd
        {
            x: integer = 3; // Input 3
            y: float = readFloat();       // Input 0.5
            printFloat(y);
        }"""
        expect = "0.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_606(self):
        input = """
        main: function void()// 2nd
        {
            x: string = readString();       // input 3d
            y: boolean = readBoolean();     // input true
            printString(x);
            printBoolean(y);
        }"""
        expect = "3d\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_607(self):
        input = """
        main: function void()// 2nd
        {
            x: integer = 3;
            y: integer = 4;
            printInteger(x + y);
        }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_608(self):
        input = """
        main: function void()// 2nd
        {
            x: boolean = false;
            printBoolean(!x);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_609(self):
        input = """
        main: function void()// 2nd
        {
            printInteger(12%5);
        }"""
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_610(self):
        input = """
        main: function void()// 2nd
        {
            x: integer = 3;
            y: integer = 3;
            if (x == y)
                printBoolean(true);
            else
                printBoolean(false);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_611(self):
        input = """
            main: function void()// 2nd
            {
                x: integer = 3;
                y: integer = 4;
                while (x != y)
                    x = x + 1;
                printString("Successfull");
            }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_612(self):
        input = """
            main: function void()// 2nd
            {
                x: integer = 2;
                y: integer = 4;

                do {x = x + 1;}
                while (x != y);
                printString("Successfull");
            }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_613(self):
        input = """
            main: function void()// 2nd
            {
                x: integer = 2;
                y: integer = 4;

                for (x = 0, x < y, 1){
                    printInteger(x);
                }
                printString("Successfull");
            }"""
        expect = "0\n1\n2\n3\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_614(self):
        input = """
            main: function void()// 2nd
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
        expect = "0\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_615(self):
        input = """
            main: function void()// 2nd
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
        expect = "0\n1\n3\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_616(self):
        input = """
            main: function void()// 2nd
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
        expect = "0\n1\n3\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_617(self):
        input = """
            main: function void()// 2nd
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
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_618(self):
        input = """
                main: function void()// 2nd
                {
                    x: array [3] of integer = {1, 2, 3};
                    x[2] = 7;
                    printInteger(x[2]);
                }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_619(self):             # arr 2
        input = """
                main: function void()// 2nd
                {
                    x: array [3] of integer;
                    x = {1, 2, 3};
                    x[2] = 7;
                    printInteger(x[2]);
                }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_620(self):
        input = """
                main: function void()// 2nd
                {
                    x: array [3] of integer;
                    y: array [3] of integer;
                    x = {1, 2, 3};
                    x[2] = 7;
                    y = x;
                    printInteger(y[2]);
                }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_621(self):
        input = """
                main: function void()// 2nd
                {
                    x: array [2,2] of integer = {{1, 2}, {3, 4}};
                    y: array [2,2] of integer;
                    y = x;
                    y[0, 0] = 7;
                    printInteger(y[0, 0]);
                }"""
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_622(self):
        input = """
                main: function void()// 2nd
                {
                    x: float = 5;
                    printFloat(x);
                    y: integer = 6.8;
                    printInteger(y);
                }"""
        expect = "5.0\n6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_623(self):
        input = """
                main: function void()// 2nd
                {
                    x: auto = 5;
                    printInteger(x);
                    y: auto = 6.8;
                    printFloat(y);
                }"""
        expect = "5\n6.8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_624(self):
        input = """
                main: function void()// 2nd
                {
                    x: string = "PP";
                    x = x :: "L";
                    printString(x);
                    y: boolean = true && false || true;
                    printBoolean(y);
                }"""
        expect = "PPL\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_625(self):
        input = """
                main: function void()// 2nd
                {
                     y: boolean = true && false || false;
                     printBoolean(y);
                }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_626(self):
        input = """
                main: function void()// 2nd
                {
                     x: integer = 1;
                     {
                        x: integer = 4;
                        printInteger(x);
                     }
                     printInteger(x);
                }"""
        expect = "4\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_627(self):
        input = """
                x: boolean;
                y: boolean = true && false || false;
                main: function void()// 2nd
                {
                     x = true;
                     printBoolean(x);
                     printBoolean(y);
                }"""
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_628(self):
        input = """
                x: array [2] of boolean = {false, false};
                y: array [2, 2] of boolean = {x, {false, true}};
                main: function void()// 2nd
                {
                     x[1] = true;
                     printBoolean(x[1]);
                     printBoolean(y[1, 0]);
                }"""
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_629(self):
        input = """
                f1: function void(){
                    printString("Successfull");
                }
                main: function void()// 2nd
                {
                     f1();
                }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_630(self):
        input = """
                f1: function void(str: string){
                    printString(str);
                }
                main: function void()// 2nd
                {
                     f1("Successfull");
                }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_631(self):
        input = """
                f1: function void(i: integer, f: float, b: boolean, str: string){
                    printInteger(i);
                    printFloat(f);
                    printBoolean(b);
                    printString(str);
                }
                main: function void()// 2nd
                {
                     f1(3, 0.0, false, "Successfull");
                }"""
        expect = "3\n0.0\nfalse\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_632(self):
        input = """
                str: string = "Successfull";
                f1: function void(str: string){
                    printString(str);
                }
                main: function void()// 2nd
                {
                     f1("Successfull");
                }"""
        expect = "Successfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))


    def test_633(self):
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
        main: function void()// 2nd
        {
             f1();
             printInteger(f2());
        }"""
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_634(self):
        input = """
        f1: function void(){
            printString("f1");
        }
        f2: function void() inherit f1{
            preventDefault();
            printString("f2");
        }
        main: function void()// 2nd
        {
             f2();
        }"""
        expect = "f2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_635(self):
        input = """
        f1: function void(){
            printString("f1");
        }
        f2: function void() inherit f1{
            //preventDefault();
            printString("f2");
        }
        main: function void()// 2nd
        {
             f2();
        }"""
        expect = "f1\nf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_636(self):
        input = """
        f1: function void(a: string){
            printString("f1");
        }
        f2: function void() inherit f1{
            preventDefault();
            printString("f2");
        }
        main: function void()// 2nd
        {
             f2();
        }"""
        expect = "f2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_637(self):
        input = """
        f1: function void(a: string){
            printString(a);
        }
        f2: function void() inherit f1{
            super("f1");
            printString("f2");
        }
        main: function void()// 2nd
        {
             f2();
        }"""
        expect = "f1\nf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_638(self):
        input = """
        f1: function void(inherit a: string){
            printString(a);
        }
        f2: function void() inherit f1{
            super("f1");
            a = "f2";
            printString(a);
        }
        main: function void()// 2nd
        {
             f2();
        }"""
        expect = "f1\nf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_639(self):
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
        main: function void()// 2nd
        {
             f3();
        }"""
        expect = "f1\nf2\nf1\nf2\nf3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_640(self):
        input = """
        f1: function integer(inherit x: float){
             return 6.6;
        }
        main: function void()// 2nd
        {
             x: float = f1(4);
             y: float;
             y = 7;
             printFloat(x);
             printFloat(y);
        }"""
        expect = "6.0\n7.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_641(self):
        input = """
        f1: function void(out x: string){
             x = "f1";
        }
        main: function void()// 2nd
        {
             y: string = "main";
             f1(y);
             printString(y);
        }"""
        expect = "f1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_642(self):
        input = """
                    main: function void()// 2nd
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
        expect = "0\n0\n0\n1\n1\n0\n1\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_643(self):
        input = """     main: function void()// 2nd
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
        expect = "0\n0\n0\n1\n1\n0\n1\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_644(self):
        input = """
                main: function void()// 2nd
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
        expect = "0\n0\n0\n1\n1\n0\n1\n1\nSuccessfull\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_645 (self):
        input = """
        main: function void()// 2nd
        {
            a: boolean;         // undecl
            if (true || a)
                printString("OR");     // ||
            else
                printString("AND");         // &&
        }"""
        expect = "OR\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_646(self):
        input = """
        f1: function array [3] of float(){

        }
        main: function void()// 2nd
        {
             f1();
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_699 (self):
        input = """
        main: function void()// 2nd
        {
            printString("CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!");
        }"""
        expect = "CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_647 (self):
        input = """
        main: function void()// nd
        {
            printString("CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!");
        }"""
        expect = "CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_648 (self):
        input = """
        main: function void()// d
        {
            printString("CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!");
        }"""
        expect = "CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_649 (self):
        input = """
        main: function void()// 2
        {
            printString("CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!");
        }"""
        expect = "CHUC MUNG BAN DA HOAN THANH 4 BTL PPL HK233!!!!!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))