def subtraction_matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Матрицы должны иметь равные по длине значения")

    else:
        for i in range(len(matrix1)):
            print(f"Результат вычитания значений под индексом {matrix1.index(i + 1)}: "
                  f"{matrix1[i]} - {matrix2[i]} = {matrix1[i] - matrix2[i]}")

test1 = [1,2,3]
test2 = [5,7,9]

subtraction_matrix(test1, test2)