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
	iconst_1
	istore_1
.var 2 is x I from Label0 to Label1
	iconst_4
	istore_2
	iload_2
	invokestatic io/printInteger(I)V
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method
