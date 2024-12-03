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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is c I from Label0 to Label1
	iconst_1
	iconst_2
	iadd
	istore_1
.var 2 is d F from Label0 to Label1
	ldc 1.5
	iconst_2
	i2f
	fadd
	fstore_2
.var 3 is e F from Label0 to Label1
	ldc 3.7
	ldc 9.1
	fadd
	fstore_3
	iload_1
	invokestatic io/printInteger(I)V
	fload_2
	invokestatic io/printFloat(F)V
	fload_3
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 4
.end method
