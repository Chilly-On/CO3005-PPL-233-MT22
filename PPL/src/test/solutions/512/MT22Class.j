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
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
Label2:
	iload_1
	iload_2
	if_icmpeq Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	goto Label4
Label3:
	ldc "Successfull"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 11
.limit locals 3
.end method
