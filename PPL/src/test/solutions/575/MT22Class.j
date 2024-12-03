.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static MT22outswapa I
.field static MT22outswapb I

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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_3
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_4
	istore_2
	getstatic MT22Class.MT22outswapa I
	getstatic MT22Class.MT22outswapb I
	iload_1
	iload_2
	invokestatic MT22Class/swap(II)V
	istore_1
	istore_2
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static swap(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
.var 2 is temp I from Label0 to Label1
	iload_0
	istore_2
	iload_1
	istore_0
	iload_2
	istore_1
	iload_0
	putstatic MT22Class.MT22outswapa I
	iload_1
	putstatic MT22Class.MT22outswapb I
Label1:
	return
.limit stack 3
.limit locals 3
.end method
