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
.var 1 is a [[I from Label0 to Label1
	iconst_1
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	iconst_3
	iastore
	aload_1
	iconst_0
	aaload
	iconst_1
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	aload_1
	iconst_0
	aaload
	iconst_1
	iaload
	iadd
	iastore
	aload_1
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 9
.limit locals 2
.end method
