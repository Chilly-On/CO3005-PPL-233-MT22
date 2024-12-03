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

.method public static f1(F)I
.var 0 is x F from Label0 to Label1
Label0:
	ldc 6.6
	f2i
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x F from Label0 to Label1
	iconst_4
	i2f
	invokestatic MT22Class/f1(F)I
	i2f
	fstore_1
.var 2 is y F from Label0 to Label1
	ldc 0.0
	fstore_2
	bipush 7
	i2f
	fstore_2
	fload_1
	invokestatic io/printFloat(F)V
	fload_2
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
