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

.method public static f1(Ljava/lang/String;)V
.var 0 is a Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static f2(Ljava/lang/String;)V
.var 0 is b Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "f1"
	invokestatic MT22Class/f1(Ljava/lang/String;)V
.var 1 is a Ljava/lang/String; from Label0 to Label1
	aload_0
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static f3()V
Label0:
	ldc "f2"
	invokestatic MT22Class/f2(Ljava/lang/String;)V
.var 0 is b Ljava/lang/String; from Label0 to Label1
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "f1"
	astore_1
	ldc "f2"
	astore_0
	aload_1
	invokestatic io/printString(Ljava/lang/String;)V
	aload_0
	invokestatic io/printString(Ljava/lang/String;)V
	ldc "f3"
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MT22Class/f3()V
Label1:
	return
.limit stack 0
.limit locals 1
.end method
