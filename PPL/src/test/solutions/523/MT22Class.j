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
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	invokestatic io/printInteger(I)V
.var 2 is y F from Label0 to Label1
	ldc 6.8
	fstore_2
	fload_2
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method