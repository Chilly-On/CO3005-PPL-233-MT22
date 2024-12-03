.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static x I

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

.method public static f1()V
Label0:
	iconst_1
	putstatic MT22Class.x I
	getstatic MT22Class.x I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static f2()I
Label0:
	iconst_2
	putstatic MT22Class.x I
	getstatic MT22Class.x I
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 5
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MT22Class/f1()V
	invokestatic MT22Class/f2()I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method
