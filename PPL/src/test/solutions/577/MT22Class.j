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

.method public static concat(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
Label1:
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello "
	astore_1
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "World!"
	astore_2
	aload_1
	aload_2
	invokestatic MT22Class/concat(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
