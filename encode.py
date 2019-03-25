def CodeWord(x):
    #infoWord = int(infoWord , 2)
    x.append(x[0]^x[1]^x[2])
    x.append(x[3]^x[1]^x[2])
    x.append(x[0]^x[1]^x[3])
    x = "".join(str(e) for e in x)
    return x


infoWord = list(map(int , input("Enter Codeword: ")))
c = CodeWord(infoWord)
print(c)