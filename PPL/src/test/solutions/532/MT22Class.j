.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static str Ljava/lang/String;

.method public static <clinit>()V
Label0:
	ldc "Successfull"
	putstatic MT22Class.str Ljava/lang/String;
Label1:
	return
.limit stack 4
.limit locals 0
.end method

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
.var 0 is str Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Successfull"
	invokestatic MT22Class/f1(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method
