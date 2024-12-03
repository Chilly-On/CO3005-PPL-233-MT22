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
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_3
	ineg
	iastore
	dup
	iconst_1
	bipush 9
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	bipush 8
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_2
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
.var 3 is temp I from Label0 to Label1
	aload_1
	iload_2
	iaload
	istore_3
	aload_1
	iload_2
	aload_1
	iconst_4
	iload_2
	isub
	iaload
	iastore
	aload_1
	iconst_4
	iload_2
	isub
	iload_3
	iastore
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label7:
	iconst_0
	istore_2
Label10:
	iload_2
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label13
	aload_1
	iload_2
	iaload
	invokestatic io/printInteger(I)V
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label13:
Label1:
	return
.limit stack 16
.limit locals 4
.end method
