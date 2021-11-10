import math
from math import sqrt
e=0.0001
import sys

Ax = float(input("Введите координат x для вершины А : "))
Ay = float(input("Введите координат y для вершины A : "))
Bx = float(input("Введите координат x для вершины B : "))
By = float(input("Введите координат y для вершины B : "))
Cx= float(input("Введите координат x для вершины C : "))
Cy=float(input("Введите координат y для вершины C : "))
x0=float(input("Введите x координаты точки : "))
y0=float(input("Введите y координаты точки : "))


AB = math.sqrt((Bx-Ax)**2+(By-Ay)**2)
print("Длина сторон 'AB' : " + str(AB))
AC = math.sqrt((Cx-Ax)**2+(Cy-Ay)**2)
print("Длина сторон 'AC' : " + str(AC))
BC = math.sqrt((Cx-Bx)**2+(Cy-By)**2)
print("Длина сторон 'BC' : " + str(BC))

if(AB>=AC+BC or AC>=AB+BC or BC>=AC+AB):
     print("Это не треугольник ")
elif(AB*AB==AC*AC+BC*BC or AC*AC==AB*AB+AC*AC or BC*BC==AC*AC+AB*AB):
    print("Не является остроугольным ")
elif(AB*AB+AC*AC<BC*BC):
	print("Не является остроугольным ")
else:
	print("Является остроугольным ")

sys.exit("Попробуйте использовать другие координаты. ")
# длина высоты проведенной из наименьшего угла (острого)

P = (AB+BC+AC)/2
print("Полупериметр " + str(P))

dlina=[AB, AC, BC]
min_number=min(dlina)
if(min_number<=0):
	print("Это не является треугольником")
h=(2*(math.sqrt(P*(P-AB)*(P-AC)*(P-BC)))/min_number)

print("Длина высоты проведенной из наименьшего угла : "+str(h))

#talbai
S=sqrt(P*(P-AB)*(P-BC)*(P-AC))


LA=math.sqrt((Ax-x0)**2+(Ay-y0)**2)
LB=math.sqrt((Bx-x0)**2+(By-y0)**2)
LC=math.sqrt((Cx-x0)**2+(Cy-y0)**2)

P1=(AB+LA+LB)/2
S1=sqrt((P1*(P1-AB)*(P1-LA)*(P1-LB)))
P2=(BC+LB+LC)/2
S2=sqrt((P2*(P2-BC)*(P2-LB)*(P2-LC)))
P3=(AC+LA+LC)/2
S3=sqrt((P3*(P3-AC)*(P3-LA)*(P3-LC)))
if ((S1+S2+S3)-S)<= e:
	print('Точка внутри треугольника')
else:
	print('Точка вне треугольника')
HAB=(2*S1)/AB
HBC=(2*S2)/BC
HAC=(2*S3)/AC
if HAB <= HBC and HAB <= HAC:
	print("расстояние до ближайшей стороны", HAB)
elif HBC <= HAB and HBC <= HAC:
	print("расстояние до ближайшей стороны", HBC)
elif HAC <= HAB and HAC < + HBC:
	print("расстояние до ближайшей стороны", HAC)
