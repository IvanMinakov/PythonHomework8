def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(f"{operation(i, j):>6}", end="")
        print()
def multiply(x, y):
    return x * y

print_operation_table(multiply, num_rows=6, num_columns=6)