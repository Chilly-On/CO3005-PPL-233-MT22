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
.var 1 is x I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is y I from Label0 to Label1
	iconst_0
	istore_2
Label4:
	iload_1
	iconst_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
Label8:
	iload_2
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	iconst_0
	istore_2
	goto Label4
Label5:
	ldc "Successfull"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 19
.limit locals 3
.end method
