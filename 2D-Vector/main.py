from Vector2d import Vector2D
import math 

def main():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, -2)


    print("v1", v1)
    print("v2", v2)
    print("v1 + v2", v1 + v2)
    print("v1 - v2", v1 - v2)
    print("v1 * 3", v1 * 3)
    print("2 * v2", 2 * v2)
    print("v1 / 2 =", v1 / 2)            
    print("|v1| =", abs(v1))             
    print("v1 dot v2 =", v1.dot(v2))    
    print("v1 normalized:", v1.normalize())   
    print("v1 angle (deg):", math.degrees(v1.angle()))  
    print("v1 rotated 90°:", v1.rotate(math.pi/2))  


if __name__=="__main__":
    main()
