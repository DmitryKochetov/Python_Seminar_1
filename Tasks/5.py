# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = float(input("Введите Ax (float): "))
ay = float(input("Введите Ay (float): "))
bx = float(input("Введите Bx (float): "))
by = float(input("Введите By (float): "))

def find_distance(ax,ay,bx,by):
    return ((ax-bx)**2+(ay-by)**2)**(0.5)

print(f'A ({ax},{ay}); B ({bx},{by}) -> {find_distance(ax,ay,bx,by)}') 
