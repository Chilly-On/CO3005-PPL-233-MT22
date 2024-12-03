.source MT22Class.java
.class public MT22Class
.super java/lang/Object

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

.method public static foo(II)F
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ldc 1.5
	f2i
	iadd
	i2f
	freturn
Label1:
	freturn
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x F from Label0 to Label1
	iconst_1
	iconst_2
	invokestatic MT22Class/foo(II)F
	ldc 0.5
	fadd
	fstore_1
	fload_1
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
