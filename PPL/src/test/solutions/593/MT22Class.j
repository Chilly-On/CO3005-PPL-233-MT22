.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static x I

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

.method public static foo(II)F
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc 0.0
	freturn
Label4:
	iload_0
	ldc 1.0
	f2i
	imul
	iload_1
	idiv
	i2f
	freturn
Label1:
	freturn
.limit stack 7
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	getstatic MT22Class.x I
	iconst_4
	isub
	iconst_5
	invokestatic MT22Class/foo(II)F
	fstore_1
	fload_1
	invokestatic io/printFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
