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
Label7:
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
	iload_2
	iconst_1
	iadd
	istore_2
Label5:
	iload_2
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	goto Label7
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	iconst_0
	istore_2
Label2:
	iload_1
	iconst_2
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label3
	goto Label4
Label3:
	ldc "Successfull"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 19
.limit locals 3
.end method
