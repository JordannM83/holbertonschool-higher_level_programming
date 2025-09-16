#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

print("Test: size négatif")
try:
	Square(-1)
except Exception as e:
	print("[Exception]", e)

print("Test: size non entier")
try:
	Square("3")
except Exception as e:
	print("[Exception]", e)

print("Test: position non tuple")
try:
	Square(2, [1, 2])
except Exception as e:
	print("[Exception]", e)

print("Test: position tuple taille incorrecte")
try:
	Square(2, (1,))
except Exception as e:
	print("[Exception]", e)

print("Test: position avec valeur négative")
try:
	Square(2, (-1, 2))
except Exception as e:
	print("[Exception]", e)

print("Test: position avec valeur non entière")
try:
	Square(2, (1, "2"))
except Exception as e:
	print("[Exception]", e)
my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
