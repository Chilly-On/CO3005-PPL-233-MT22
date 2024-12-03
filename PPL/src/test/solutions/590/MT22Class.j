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

.method public static abs(F)F
.var 0 is a F from Label0 to Label1
Label0:
	fload_0
	iconst_0
	i2f
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_0
	fneg
	freturn
Label4:
	fload_0
	freturn
Label1:
	freturn
.limit stack 7
.limit locals 1
.end method

.method public static foo(FF)Z
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	invokestatic MT22Class/abs(F)F
	fload_1
	invokestatic MT22Class/abs(F)F
	fadd
	fload_0
	fload_1
	fadd
	invokestatic MT22Class/abs(F)F
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 2.1
	ldc 1.9
	fneg
	invokestatic MT22Class/foo(FF)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method
