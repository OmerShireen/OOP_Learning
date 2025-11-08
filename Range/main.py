from Range import Range

def main():
    r1 = Range(5)
    print("r1 = Range(5)")
    for val in r1:
        print(val, end=" ")
    print("\nlength of r1:",len(r1))

    r2 = Range(2,10)
    print("\nr2 = Range(2,10)")
    for val in r2:
        print(val, end=" ")
    print("\nLength 0f r2:",len(r2))

    r3 = Range(1,10,2)
    print("\nr3 = Range(1,10,2)")
    for val in r3:
        print(val, end=" ")
    print("\nLength of r3:", len(r3))        









if __name__=="__main__":
    main()    