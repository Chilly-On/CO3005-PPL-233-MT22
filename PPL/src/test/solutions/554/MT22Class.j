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

.method public static max(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	ireturn
Label4:
	iload_1
	ireturn
Label1:
	ireturn
.limit stack 7
.limit locals 2
.end method

.method public static maxEle([II)I
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iload_1
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	aload_0
	iconst_0
	iaload
	ireturn
Label4:
.var 2 is k I from Label0 to Label1
	aload_0
	iload_1
	iconst_1
	isub
	iaload
	aload_0
	iload_1
	iconst_1
	isub
	invokestatic MT22Class/maxEle([II)I
	invokestatic MT22Class/max(II)I
	istore_2
	iload_2
	ireturn
Label1:
	ireturn
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	ineg
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	dup
	iconst_3
	bipush 6
	iastore
	dup
	iconst_4
	bipush 7
	iastore
	dup
	iconst_5
	bipush 8
	iastore
	dup
	bipush 6
	iconst_2
	iastore
	dup
	bipush 7
	iconst_0
	iastore
	dup
	bipush 8
	iconst_1
	iastore
	dup
	bipush 9
	iconst_4
	iastore
	astore_1
.var 2 is n I from Label0 to Label1
	bipush 10
	istore_2
	aload_1
	iload_2
	invokestatic MT22Class/maxEle([II)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
