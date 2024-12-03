.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static x Z
.field static y Z

.method public static <clinit>()V
Label0:
	iconst_1
	ifle Label2
	iconst_0
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	iconst_1
	ifle Label2
	iconst_0
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_0
	ior
	putstatic MT22Class.y Z
Label1:
	return
.limit stack 10
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
	iconst_1
	putstatic MT22Class.x Z
	getstatic MT22Class.x Z
	invokestatic io/printBoolean(Z)V
	getstatic MT22Class.y Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method
