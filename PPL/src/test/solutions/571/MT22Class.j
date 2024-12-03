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

.method public static sumDigit(I)I
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is sum I from Label0 to Label1
	iconst_0
	istore_1
Label4:
	iload_0
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	iload_0
	bipush 10
	irem
	iadd
	istore_1
	iload_0
	bipush 10
	idiv
	istore_0
	goto Label4
Label5:
	iload_1
	ireturn
Label1:
	ireturn
.limit stack 9
.limit locals 2
.end method

.method public static primes(I)Z
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_2
	istore_1
Label4:
	iload_1
	iload_1
	imul
	iload_0
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iconst_0
Label10:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label7:
	iload_0
	iconst_1
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
Label1:
.limit stack 15
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	invokestatic io/readInteger()I
	istore_1
.var 2 is i I from Label0 to Label1
.var 3 is flag Z from Label0 to Label1
	iconst_0
	istore_3
	iload_1
	istore_2
Label4:
	iload_2
	bipush 10
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_2
	invokestatic MT22Class/primes(I)Z
	iload_2
	invokestatic MT22Class/sumDigit(I)I
	invokestatic MT22Class/primes(I)Z
	iand
	ifle Label8
	iload_2
	invokestatic io/printInteger(I)V
	iconst_1
	istore_3
	goto Label7
Label8:
Label6:
	iload_2
	iconst_1
	ineg
	iadd
	istore_2
	goto Label4
Label7:
	iload_3
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iconst_0
	invokestatic io/printInteger(I)V
Label12:
Label1:
	return
.limit stack 16
.limit locals 4
.end method
