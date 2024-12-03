.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static a I

.method public static <clinit>()V
Label0:
	iconst_1
	i2f
	iconst_2
	i2f
	invokestatic MT22Class/foo(FF)F
	iconst_1
	i2f
	fadd
	f2i
	putstatic MT22Class.a I
Label1:
	return
.limit stack 4
.limit locals 0
.end method

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

.method public static foo(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fadd
	freturn
Label1:
	freturn
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.a I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method
