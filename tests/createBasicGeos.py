import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import CGLibPy

point = CGLibPy.CGLibPy_Point(10,20,30)

line = CGLibPy.CGLibPy_Line([0,0,0,10,0,0])
line2 = CGLibPy.CGLibPy_Line([10,10,0,10,10,20])
line3 = CGLibPy.CGLibPy_Line([0,0,0,0,10,0])
line4 = CGLibPy.CGLibPy_Line([10,0,0,10,10,0])
line5 = CGLibPy.CGLibPy_Line([4.56,-12.345,34.126546,-98.5,10,54.005]) 
line6 = CGLibPy.CGLibPy_Line([0,0,0,0,10,0]) 
line7 = CGLibPy.CGLibPy_Line([0,0,0,0,0,10]) 

arc1 = CGLibPy.CGLibPy_Arc( [CGLibPy.CGLibPy_Point(0,0,0),
                            CGLibPy.CGLibPy_Point(-5,0,0),
                            CGLibPy.CGLibPy_Point(5,0,0),
                            5, True])

point1 = CGLibPy.CGLibPy_Point(2,5,7)
point2 = CGLibPy.CGLibPy_Point(-2,5,7)
point3 = CGLibPy.CGLibPy_Point(2,5,7)


print(point.X)
print(line.startPt.Z)
print(line.midpt.Y)
print(line.vec.K)
print(line.lineLen)
print(CGLibPy.CGLibPy_Utility.lineLineIntersection3D(line,line2))
print(CGLibPy.CGLibPy_Utility.ang2LinesDegrees(line,line2))
print(CGLibPy.CGLibPy_Utility.areLinesPerpendicular(line,line3))
print(CGLibPy.CGLibPy_Utility.areLinesParallel(line,line3))
intPt = line.intersectionPoint(line4)
print(intPt.X)
linePt = line5.pointAtDistAlongLine(45.342)
print(str(linePt.X) + " " + str(linePt.Y) + " " + str(linePt.Z))
print(CGLibPy.CGLibPy_Utility.SideOfThePointToLineXY(line6,point2))
print(CGLibPy.CGLibPy_Utility.SideOfThePointToLineYZ(line7,point3))
print(CGLibPy.CGLibPy_Utility.SideOfThePointToLineXZ(line7,point2))

inter,u,v = CGLibPy.CGLibPy_Utility.arcLineIntersection(line6,arc1)
print(inter)



