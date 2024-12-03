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
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_1
	iload_1
	imul
	iload_2
	iload_2
	imul
	iadd
	iload_3
	iload_3
	imul
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	iload_2
	iconst_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	iload_3
	iconst_0
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	istore 4
	iload 4
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 12
.limit locals 5
.end method
