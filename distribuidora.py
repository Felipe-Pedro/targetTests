incoming = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def getTotal() -> int:
    total = 0
    for amount in incoming.values():
        total += amount
    return total

def getPercentage(value: int, total: int) -> int:
    return (value * 100) / total

def getStatesPercentage() -> list:
    total = getTotal()
    percentages = []

    for state, value in incoming.items():
        percentage = getPercentage(value, total)
        percentages.append((state, round(percentage, 2)))
    return percentages

# def test1():
#     assert getTotal() == 180759.98

# def test2():
#     assert getPercentage(25, 50) == 50

# test1()
# test2()