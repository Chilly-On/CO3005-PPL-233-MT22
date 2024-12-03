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
.var 1 is a I from Label0 to Label1
	iconst_3
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_4
	istore_2
.var 3 is c I from Label0 to Label1
	iconst_5
	istore_3
.var 4 is d Z from Label0 to Label1
	iload_1
	iload_2
	iadd
	iload_3
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore 4
	iload 4
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 5
.limit locals 5
.end method
