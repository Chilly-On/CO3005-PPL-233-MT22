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

.method public static f1()V
Label0:
	ldc "f1"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static f2()V
Label0:
	invokestatic MT22Class/f1()V
	ldc "f2"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MT22Class/f2()V
Label1:
	return
.limit stack 0
.limit locals 1
.end method
