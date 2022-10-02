LASTNAME = "Parsa"


def slg(data):
    kCount = 0
    singleCount = 0
    doubleCount = 0
    tripleCount = 0
    hrCount = 0
    name = data[:data.find(":")]
    data = data[data.find(":")+1:]
    if data == "":
        slg = 0
    else:
        for i in data:
            if i == "K":
                kCount += 1
            elif i == "1":
                singleCount += 1
            elif i == "2":
                doubleCount += 1
            elif i == "3":
                tripleCount += 1
            elif i == "H":
                hrCount += 1
        slg = ((singleCount + 2*doubleCount + 3*tripleCount + 4*hrCount)/ (singleCount + doubleCount + tripleCount +
                                                                       hrCount + kCount))
    return name + "=" + format(slg, ".3f")


