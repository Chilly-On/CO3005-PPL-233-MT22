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
.var 1 is x Ljava/lang/String; from Label0 to Label1
	invokestatic io/readString()Ljava/lang/String;
	astore_1
.var 2 is y Z from Label0 to Label1
	invokestatic io/readBoolean()Z
	istore_2
	aload_1
	invokestatic io/printString(Ljava/lang/String;)V
	iload_2
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method
