import json

def getData() -> dict:
    with open("dados.json") as data:
        return json.load(data)

def getMinimunPay() -> tuple:
    data = getData()

    minimunPay = data[0]["valor"]
    minimunPayDay = 0

    for item in data:
        if item['valor'] == 0:
            continue

        if item['valor'] < minimunPay:
            minimunPay = item['valor']
            minimunPayDay = item['dia']
    return (minimunPay, minimunPayDay)

def getMaxPay() -> tuple:
    data = getData()

    maxPay = data[0]["valor"]
    maxPayDay = 0

    for item in data:
        if item['valor'] > maxPay:
            maxPay = item['valor']
            maxPayDay = item['dia']
    return (maxPay, maxPayDay)

def getAvaragePay() -> float:
    data = getData()

    total = 0
    count = 0

    for item in data:
        if item['valor'] == 0:
            continue

        total += item['valor']
        count += 1

    return total / count

def getAboveAvaragePayDays() -> list:
    data = getData()
    avarage = getAvaragePay()
    
    goodDays = []

    for item in data:
        if item['valor'] > avarage:
            goodDays.append((item['dia'], item['valor']))
    
    return goodDays

# def teste1():
#     assert getMinimunPay() == (373.7838, 14)

# def teste2():
#     assert getMaxPay() == (48924.2448, 16)

# teste1()
# teste2()