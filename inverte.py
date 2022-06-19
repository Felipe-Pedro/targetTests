def stringReverse(string: str) -> str:
    reverse = ""
    for i in range(-1, (len(string) + 1) * -1, -1):
        reverse += string[i]
    return reverse

# def test1():
#     assert stringReverse('Felipe') == 'epileF'

# def test2():
#     assert stringReverse('Daniele') == 'eleinaD'

# def test3():
#     assert stringReverse('3 Pratos de trigo para 3 tigres tristes') == 'setsirt sergit 3 arap ogirt ed sotarP 3'

# test1()
# test2()
# test3()