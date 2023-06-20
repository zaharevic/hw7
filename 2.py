def print_operation_table(operation, num_rows, num_cols):
    for x in range(1, num_rows + 1):
        for y in range(1, num_cols + 1):
            if num_cols == y:
                print(operation(x, y))
            else:
                print(operation(x, y), '\t', end='')

rows, columns = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
print_operation_table(lambda x, y: x * y, rows, columns)