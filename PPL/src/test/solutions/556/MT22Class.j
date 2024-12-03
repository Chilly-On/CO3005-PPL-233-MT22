.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static MT22outswapNumbera I
.field static MT22outswapNumberb I

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

.method public static swapNumber(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
.var 2 is temp I from Label0 to Label1
	iload_0
	istore_2
	iload_1
	istore_0
	iload_2
	istore_1
	iload_0
	putstatic MT22Class.MT22outswapNumbera I
	iload_1
	putstatic MT22Class.MT22outswapNumberb I
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static sort([III)V
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
Label0:
	iload_1
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
.var 3 is idx I from Label0 to Label1
	aload_0
	iload_1
	iload_2
	invokestatic MT22Class/partition([III)I
	istore_3
	aload_0
	iload_1
	iload_3
	iconst_1
	isub
	invokestatic MT22Class/sort([III)V
	aload_0
	iload_3
	iconst_1
	iadd
	iload_2
	invokestatic MT22Class/sort([III)V
Label4:
Label1:
	return
.limit stack 10
.limit locals 4
.end method

.method public static partition([III)I
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
Label0:
.var 3 is pivot I from Label0 to Label1
	aload_0
	iload_2
	iaload
	istore_3
.var 4 is left I from Label0 to Label1
	iload_1
	istore 4
.var 5 is right I from Label0 to Label1
	iload_2
	iconst_1
	isub
	istore 5
Label2:
	iconst_1
	ifle Label3
	aload_0
	iload 4
	iaload
Label8:
	iload 4
	iload 5
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ifle Label9
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label8
Label9:
	aload_0
	iload 5
	iaload
Label14:
	iload 5
	iload 4
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iload_3
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	iand
	ifle Label15
	iload 5
	iconst_1
	isub
	istore 5
	goto Label14
Label15:
	iload 4
	iload 5
	if_icmplt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label3
Label18:
	aload_0
	iload 4
	iaload
	aload_0
	iload 5
	iaload
	invokestatic MT22Class/swapNumber(II)V
	iload 4
	iconst_1
	iadd
	istore 4
	iload 5
	iconst_1
	isub
	istore 5
	goto Label2
Label3:
	aload_0
	iload 4
	iaload
	aload_0
	iload_2
	iaload
	invokestatic MT22Class/swapNumber(II)V
	iload 4
	ireturn
Label1:
	ireturn
.limit stack 22
.limit locals 6
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
	iastore
	dup
	iconst_2
	bipush 8
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
	ineg
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
	bipush 10
	iastore
	dup
	bipush 10
	bipush 49
	iastore
	dup
	bipush 11
	bipush 51
	ineg
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
	ineg
	iastore
	dup
	bipush 15
	bipush 71
	iastore
	dup
	bipush 16
	bipush 33
	iastore
	dup
	bipush 17
	bipush 89
	ineg
	iastore
	dup
	bipush 18
	bipush 27
	iastore
	dup
	bipush 19
	bipush 100
	iastore
	astore_1
	aload_1
	iconst_0
	bipush 19
	invokestatic MT22Class/sort([III)V
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label4:
	iload_2
	bipush 20
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
