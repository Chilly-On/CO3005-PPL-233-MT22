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

.method public static findEle([IIII)I
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
.var 3 is target I from Label0 to Label1
Label0:
	iload_1
	iload_2
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
.var 4 is mid I from Label0 to Label1
	iload_1
	iload_2
	iload_1
	isub
	iconst_2
	idiv
	iadd
	istore 4
	aload_0
	iload 4
	iaload
	iload_3
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload 4
	ireturn
Label8:
	aload_0
	iload 4
	iaload
	iload_3
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	aload_0
	iload 4
	iconst_1
	iadd
	iload_2
	iload_3
	invokestatic MT22Class/findEle([IIII)I
	ireturn
Label12:
	aload_0
	iconst_0
	iload 4
	iconst_1
	isub
	iload_3
	invokestatic MT22Class/findEle([IIII)I
	ireturn
Label4:
	iconst_1
	ineg
	ireturn
Label1:
	ireturn
.limit stack 17
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 20
	newarray int
	dup
	iconst_0
	bipush 26
	ineg
	iastore
	dup
	iconst_1
	bipush 15
	ineg
	iastore
	dup
	iconst_2
	bipush 8
	ineg
	iastore
	dup
	iconst_3
	iconst_3
	ineg
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_4
	iastore
	dup
	bipush 6
	bipush 10
	iastore
	dup
	bipush 7
	bipush 21
	iastore
	dup
	bipush 8
	bipush 30
	iastore
	dup
	bipush 9
	bipush 45
	iastore
	dup
	bipush 10
	bipush 49
	iastore
	dup
	bipush 11
	bipush 51
	iastore
	dup
	bipush 12
	bipush 59
	iastore
	dup
	bipush 13
	bipush 67
	iastore
	dup
	bipush 14
	bipush 70
	iastore
	dup
	bipush 15
	bipush 71
	iastore
	dup
	bipush 16
	bipush 78
	iastore
	dup
	bipush 17
	bipush 89
	iastore
	dup
	bipush 18
	bipush 94
	iastore
	dup
	bipush 19
	bipush 100
	iastore
	astore_1
	aload_1
	iconst_0
	bipush 19
	bipush 94
	invokestatic MT22Class/findEle([IIII)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method
