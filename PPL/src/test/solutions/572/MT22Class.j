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

.method public static reverse(I)I
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is result I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is temp I from Label0 to Label1
	iload_0
	istore_2
	iload_2
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	ineg
	istore_0
Label4:
Label8:
	iload_0
	iconst_0
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	bipush 10
	iload_1
	imul
	iload_0
	bipush 10
	irem
	iadd
	istore_1
	iload_0
	bipush 10
	idiv
	istore_0
	goto Label8
Label9:
	iload_2
	iconst_0
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iload_1
	ineg
	ireturn
Label12:
	iload_1
	ireturn
Label1:
	ireturn
.limit stack 13
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	invokestatic io/readInteger()I
	istore_1
	iload_1
	invokestatic MT22Class/reverse(I)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
