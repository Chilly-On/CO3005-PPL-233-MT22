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

.method public static min(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmpge Label2
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	invokestatic io/readInteger()I
	istore_1
.var 2 is b I from Label0 to Label1
	invokestatic io/readInteger()I
	istore_2
.var 3 is c I from Label0 to Label1
	invokestatic io/readInteger()I
	istore_3
.var 4 is d I from Label0 to Label1
	invokestatic io/readInteger()I
	istore 4
	iload_1
	iload_2
	invokestatic MT22Class/min(II)I
	iload_3
	invokestatic MT22Class/min(II)I
	iload 4
	invokestatic MT22Class/min(II)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
.limit locals 5
.end method
