def fibonacci(max_value: int) -> list:
    sequence = [0]
    next_number = 0
    number = 1
    if(type(max_value) == type(str())):
        return []

    if(max_value < 0):
        return []

    for i in range(int(max_value)):
        if(next_number >= max_value):
            break
        number, next_number = next_number, next_number+number
        sequence.append(next_number)
    return sequence

def fibonacci_verify(value: int) -> bool:
    return value in fibonacci(value)

user_input = input("Type a number: ")

while(user_input.isdigit() == False):
    print("\nIt should be a number")
    user_input = input("\nType a number: ")

is_number_fibonacci_sequence = fibonacci_verify(int(user_input))

print(f"Is this number part of fibonacci sequence: {is_number_fibonacci_sequence}")

# def test1():
#     assert fibonacci(-1) == []

# def test2():
#     assert fibonacci(1) == [0, 1]

# def test3():
#     assert fibonacci(5) == [0, 1, 1, 2, 3, 5]

# def test4():
#     assert fibonacci(2587) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

# def test5():
#     assert fibonacci(8.3) == [0, 1, 1, 2, 3, 5, 8, 13]

# def test6():
#     assert fibonacci("4") == []

# test1()
# test2()
# test3()
# test4()
# test5()
# test6()