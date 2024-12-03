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

.method public static factorial(II)I
.var 0 is n I from Label0 to Label1
.var 1 is m I from Label0 to Label1
Label0:
.var 2 is res I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_1
	istore_3
	iconst_1
	istore_3
Label4:
	iload_3
	iload_0
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_2
	iload_1
	irem
	iload_3
	iload_1
	irem
	imul
	iload_1
	irem
	istore_2
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label7:
	iload_2
	ireturn
Label1:
	ireturn
.limit stack 11
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	bipush 100
	istore_1
.var 2 is m I from Label0 to Label1
	sipush 1337
	istore_2
	iload_1
	iload_2
	invokestatic MT22Class/factorial(II)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
.limit locals 3
.end method
