def Decimal_binary(number):
    binarynum = []
    while True:
        if number <= 1:
            break
        binarynum.append(str(number%2))
        number = int(number/2)

    binarynum.append(str(number%2))
    number = int(number/2)

    binarynum.reverse()

    refined = []

    for i in binarynum:
        if len(refined) == 0 and i == "0":
            continue
        refined.append(i)


    binaryvalue = ""
    for i in refined:
        binaryvalue = binaryvalue+i


    return binaryvalue

def Decimal_Octal(number):
    octalnum = []
    while True:
        if number <= 1:
            break
        octalnum.append(str(number%8))
        number = int(number/8)

    octalnum.append(str(number%8))
    number = int(number/8)

    
    octalnum.reverse()
    octalvalue = ""

    refined = []

    for i in octalnum:
        if len(refined) == 0 and i == "0":
            continue
        refined.append(i)

    for i in refined:
        octalvalue = octalvalue+i


    return octalvalue

def Decimal_Hexa(number):
    Hexanum = []
    while True:
        if number <= 1:
            break
        
        Hexanum.append(str(number%16))
        number = int(number/16)


    Hexanum.append(str(number%16))
    number = int(number/16)
    
    Hexanum.reverse()
    refined = []

    for i in Hexanum:
        if len(refined) == 0 and i == "0":
            continue
        refined.append(i)

    Hexavalue = ""


    Changevals = {"10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"}

    for i in refined:
        if i in Changevals:
            Hexavalue = Hexavalue+Changevals[i]
            continue
        Hexavalue = Hexavalue+i


    return Hexavalue

print(Decimal_binary(894))
print(Decimal_Octal(894))
print(Decimal_Hexa(894))