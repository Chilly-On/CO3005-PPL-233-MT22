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
.var 1 is a [I from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label4:
	iload_2
	bipush 10
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	aload_1
	iload_2
	iaload
	invokestatic io/printInteger(I)V
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label7:
Label1:
	return
.limit stack 10
.limit locals 3
.end method
