.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static x I
.field static y I
.field static z I

.method public static <clinit>()V
Label0:
	bipush 65
	putstatic MT22Class.x I
	bipush 97
	putstatic MT22Class.y I
	getstatic MT22Class.x I
	getstatic MT22Class.y I
	iadd
	putstatic MT22Class.z I
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	getstatic MT22Class.z I
	ldc 2000.0
	f2i
	iadd
	i2f
	fstore_1
	fload_1
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
