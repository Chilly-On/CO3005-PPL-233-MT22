.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static x I
.field static MT22outincn I

.method public static <clinit>()V
Label0:
	bipush 65
	putstatic MT22Class.x I
Label1:
	return
.limit stack 3
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

.method public static inc(IIZ)V
.var 0 is n I from Label0 to Label1
.var 1 is delta I from Label0 to Label1
.var 2 is dec Z from Label0 to Label1
Label0:
	iload_2
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	iload_1
	isub
	istore_0
	goto Label5
Label4:
	iload_0
	iload_1
	iadd
	istore_0
Label5:
	iload_0
	putstatic MT22Class.MT22outincn I
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.MT22outincn I
	getstatic MT22Class.x I
	iconst_3
	iconst_0
	invokestatic MT22Class/inc(IIZ)V
	putstatic MT22Class.x I
	getstatic MT22Class.x I
	i2f
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 6
.limit locals 1
.end method
