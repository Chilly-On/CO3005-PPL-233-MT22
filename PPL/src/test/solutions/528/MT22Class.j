.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static x [Z
.field static y [[Z

.method public static <clinit>()V
Label0:
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	putstatic MT22Class.x [Z
	iconst_2
	anewarray [Z
	dup
	iconst_0
	getstatic MT22Class.x [Z
	aastore
	dup
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	putstatic MT22Class.y [[Z
Label1:
	return
.limit stack 16
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
	getstatic MT22Class.x [Z
	dup
	iconst_1
	iconst_1
	bastore
	putstatic MT22Class.x [Z
	getstatic MT22Class.x [Z
	iconst_1
	baload
	invokestatic io/printBoolean(Z)V
	getstatic MT22Class.y [[Z
	iconst_1
	aaload
	iconst_0
	baload
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 9
.limit locals 1
.end method
