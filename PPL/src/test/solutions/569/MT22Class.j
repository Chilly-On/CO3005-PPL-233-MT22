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

.method public static powMod(III)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is m I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
Label4:
.var 3 is p I from Label0 to Label1
	iload_0
	iload_1
	iconst_2
	idiv
	iload_2
	invokestatic MT22Class/powMod(III)I
	iload_2
	irem
	iload_0
	iload_1
	iconst_2
	idiv
	iload_2
	invokestatic MT22Class/powMod(III)I
	iload_2
	irem
	imul
	iload_2
	irem
	istore_3
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload_3
	ireturn
Label8:
	iload_3
	iload_0
	iload_2
	irem
	imul
	iload_2
	irem
	ireturn
Label1:
	ireturn
.limit stack 11
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_3
	istore_1
.var 2 is y I from Label0 to Label1
	bipush 29
	istore_2
.var 3 is m I from Label0 to Label1
	sipush 1337
	istore_3
	iload_1
	iload_2
	iload_3
	invokestatic MT22Class/powMod(III)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 5
.limit locals 4
.end method
