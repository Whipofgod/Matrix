matrix=[]
height=int(input("Enter the matrix's height: "))
width=int(input("Enter the matrix's width: "))
for i in range(height):
    matrix.append([])
for i in range(width):
    for i in range(len(matrix)):
        matrix[i].append([])
for i in matrix:
    print(i)
for i in range(height):
    for x in range(width):
        print("Enter the element to append in",i+1,". height,",x+1,". width: ")
        ekle=input()
        matrix[i][x].append(ekle)
for i in matrix:
    print(i)
