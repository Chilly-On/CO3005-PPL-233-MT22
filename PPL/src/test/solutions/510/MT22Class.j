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
	iconst_3
	istore_1
.var 2 is y I from Label0 to Label1
	iconst_3
	istore_2
	iload_1
	iload_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	invokestatic io/printBoolean(Z)V
	goto Label5
Label4:
	iconst_0
	invokestatic io/printBoolean(Z)V
Label5:
Label1:
	return
.limit stack 11
.limit locals 3
.end method
