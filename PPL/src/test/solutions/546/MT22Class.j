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

.method public static f1()[F
Label0:
Label1:
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 0.0
	fastore
	dup
	iconst_1
	ldc 0.0
	fastore
	dup
	iconst_2
	ldc 0.0
	fastore
	areturn
.limit stack 10
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MT22Class/f1()[F
Label1:
	return
.limit stack 3
.limit locals 1
.end method
