.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static a Ljava/lang/String;
.field static b Ljava/lang/String;
.field static c Ljava/lang/String;

.method public static <clinit>()V
Label0:
	ldc "Hello"
	putstatic MT22Class.a Ljava/lang/String;
	ldc "World"
	putstatic MT22Class.b Ljava/lang/String;
	getstatic MT22Class.a Ljava/lang/String;
	ldc " "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	getstatic MT22Class.b Ljava/lang/String;
	ldc "!"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	putstatic MT22Class.c Ljava/lang/String;
Label1:
	return
.limit stack 9
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.c Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method
