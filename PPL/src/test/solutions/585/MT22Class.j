.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static MT22outfooa I

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

.method public static foo(I)V
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	iconst_2
	idiv
	istore_0
	goto Label5
Label4:
	iconst_3
	iload_0
	imul
	iconst_1
	iadd
	istore_0
Label5:
	iload_0
	putstatic MT22Class.MT22outfooa I
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	sipush 153
	istore_1
	getstatic MT22Class.MT22outfooa I
	iload_1
	invokestatic MT22Class/foo(I)V
	istore_1
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
