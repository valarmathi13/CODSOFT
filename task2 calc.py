def calculate(first_number, second_number, operation_type):
    if operation_type == 'add':
        return first_number + second_number
    elif operation_type =='multiply':
        return first_number * second_number
    elif operation_type == 'subtract':
        return first_number - second_number
    elif operation_type == 'divide':
        if second_number != 0:
            return first_number / second_number
        else:
            return 'Error! Division by zero.'
    else:
        return 'Invalid operation type.'
    
try:
    first_number = float(input('Enter the first_number: '))
    second_number = float(input('Enter the second_number: '))

    print("choose the operation type:")
    print("add")
    print("multiply")
    print("subtract")
    print("divide")

    operation_type = input('Enter the operation type: ').lower()

    result = calculate(first_number, second_number, operation_type)

    print(f'The result is: {result}')
except ValueError:
    print('Invalid input! please enter valid numbers.')