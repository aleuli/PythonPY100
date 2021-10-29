if __name__ == "__main__":
    # Write your solution here
    pass

count_row = 10
count_col = 10
matrix =[
    [i * j for j in range(1,count_col)]
    for i in range(1,count_row)
]

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        print(f"{matrix[row][col]:2}", end=" ")
    print()