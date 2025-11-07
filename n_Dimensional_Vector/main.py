from Vector import Vector 
def main():
 v1 = Vector(3)
 v2 = Vector(3)

 v1[0], v1[1], v1[2] = 3, 4, 6
 v2[0], v2[1], v2[2] = 4, 6 ,8

 print("V1:", v1)
 print("V2:", v2)

 v3 = v1 + v2
 print("V3:",v3)

 v4 = v1 * 4
 print("v1 * 4:", v4)

 print("Magnitude of v1:", abs(v1))

 print("V1 == V2", v1 == v2)
 print("V1 != V2", v1 != v2)

if __name__=="__main__":
    main()    