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

.method public static accumulate([IIII)I
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
.var 3 is init I from Label0 to Label1
Label0:
	iload_1
	iload_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_1
	iconst_0
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	iload_1
	bipush 9
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	iload_2
	iconst_0
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	iload_2
	bipush 10
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	ifle Label12
	iload_3
	ireturn
Label12:
.var 4 is i I from Label0 to Label1
	iload_1
	istore 4
Label16:
	iload 4
	iload_2
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label19
	aload_0
	iload 4
	iaload
	iload_3
	iadd
	istore_3
Label18:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label16
Label19:
	iload_3
	ireturn
Label1:
	ireturn
.limit stack 22
.limit locals 5
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
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	bipush 10
	iastore
	astore_1
	aload_1
	iconst_0
	bipush 10
	bipush 55
	invokestatic MT22Class/accumulate([IIII)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method
