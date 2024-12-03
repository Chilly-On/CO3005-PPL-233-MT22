.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static MT22out_f1_x Ljava/lang/String;

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
.var 0 is x Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "f1"
	astore_0
	aload_0
	putstatic MT22Class.MT22out_f1_x Ljava/lang/String;
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is y Ljava/lang/String; from Label0 to Label1
	ldc "main"
	astore_1
	aload_1
	invokestatic MT22Class/f1(Ljava/lang/String;)V
	getstatic MT22Class.MT22out_f1_x Ljava/lang/String;
	astore_1
	aload_1
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
