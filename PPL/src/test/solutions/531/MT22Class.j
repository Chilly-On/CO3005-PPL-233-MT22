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

.method public static f1(IFZLjava/lang/String;)V
.var 0 is i I from Label0 to Label1
.var 1 is f F from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is str Ljava/lang/String; from Label0 to Label1
Label0:
	iload_0
	invokestatic io/printInteger(I)V
	fload_1
	invokestatic io/printFloat(F)V
	iload_2
	invokestatic io/printBoolean(Z)V
	aload_3
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	ldc 0.0
	iconst_0
	ldc "Successfull"
	invokestatic MT22Class/f1(IFZLjava/lang/String;)V
Label1:
	return
.limit stack 10
.limit locals 1
.end method
