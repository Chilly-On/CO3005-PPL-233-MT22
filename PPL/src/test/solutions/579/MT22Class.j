.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static MT22outremoveMinn I

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

.method public static removeMin([II)V
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
.var 2 is i I from Label0 to Label1
.var 3 is min I from Label0 to Label1
	aload_0
	iconst_0
	iaload
	istore_3
	iconst_1
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	aload_0
	iload_2
	iaload
	iload_3
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	aload_0
	iload_2
	iaload
	istore_3
Label10:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label7:
	iconst_0
	istore_2
Label14:
	iload_2
	iload_1
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label17
	aload_0
	iload_2
	iaload
	iload_3
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	iload_1
	iconst_1
	isub
	istore_1
.var 4 is j I from Label0 to Label1
	iload_2
	istore 4
Label24:
	iload 4
	iload_1
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label27
	aload_0
	iload 4
	aload_0
	iload 4
	iconst_1
	iadd
	iaload
	iastore
Label26:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label24
Label27:
	iload_2
	iconst_1
	isub
	istore_2
Label20:
Label16:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label14
Label17:
	iload_1
	putstatic MT22Class.MT22outremoveMinn I
Label1:
	return
.limit stack 31
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
	iconst_1
	iastore
	astore_1
.var 2 is n I from Label0 to Label1
	bipush 10
	istore_2
	getstatic MT22Class.MT22outremoveMinn I
	aload_1
	iload_2
	invokestatic MT22Class/removeMin([II)V
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label4:
	iload_3
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	aload_1
	iload_3
	iaload
	invokestatic io/printInteger(I)V
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label7:
Label1:
	return
.limit stack 10
.limit locals 4
.end method
