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
.var 1 is x F from Label0 to Label1
	iconst_5
	i2f
	fstore_1
	fload_1
	invokestatic io/printFloat(F)V
.var 2 is y I from Label0 to Label1
	ldc 6.8
	f2i
	istore_2
	iload_2
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method
