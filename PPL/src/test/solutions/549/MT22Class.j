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

.method public static foo(ZZ)Z
.var 0 is a Z from Label0 to Label1
.var 1 is b Z from Label0 to Label1
Label0:
	iload_0
	iload_1
	iand
	iload_0
	iload_1
	ior
	iand
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Z from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b Z from Label0 to Label1
	iconst_0
	istore_2
	iload_1
	iload_2
	invokestatic MT22Class/foo(ZZ)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
