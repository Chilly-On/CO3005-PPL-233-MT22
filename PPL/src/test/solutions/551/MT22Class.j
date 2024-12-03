.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static MT22outfooa I
.field static MT22outfoob I

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static foo(III)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_1
	bipush 10
	iadd
	istore_1
	iload_0
	iload_2
	iadd
	bipush 20
	iadd
	istore_0
	iload_0
	invokestatic io/printInteger(I)V
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
	iload_0
	putstatic MT22Class.MT22outfooa I
	iload_1
	putstatic MT22Class.MT22outfoob I
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is j Z from Label0 to Label1
	bipush 10
	istore_1
.var 2 is k Z from Label0 to Label1
	bipush 15
	istore_2
	getstatic MT22Class.MT22outfooa I
	getstatic MT22Class.MT22outfoob I
	iload_1
	iload_1
	iload_2
	invokestatic MT22Class/foo(III)V
	istore_1
	istore_1
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method
