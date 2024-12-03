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

.method public static isAmstrong(I)Z
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is sum I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is temp I from Label0 to Label1
	iload_0
	istore_2
Label4:
	iload_2
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 3 is digit I from Label0 to Label1
	iload_2
	bipush 10
	irem
	istore_3
	iload_1
	iload_3
	iload_3
	imul
	iload_3
	imul
	iadd
	istore_1
	iload_2
	bipush 10
	idiv
	istore_2
	goto Label4
Label5:
	iload_1
	iload_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
Label1:
.limit stack 9
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	sipush 153
	istore_1
	iload_1
	invokestatic MT22Class/isAmstrong(I)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
