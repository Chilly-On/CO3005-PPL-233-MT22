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
	iconst_2
	istore_1
.var 2 is y I from Label0 to Label1
	iconst_4
	istore_2
	iconst_0
	istore_1
Label4:
	iload_1
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_1
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	goto Label7
Label10:
	iload_1
	invokestatic io/printInteger(I)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label7:
	ldc "Successfull"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 17
.limit locals 3
.end method
