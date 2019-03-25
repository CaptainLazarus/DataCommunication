#Syndrome Table
S = {
    '000' : '0000000' ,
    '001' : '0000001' ,
    '010' : '0000010' ,
    '011' : '0000100' ,
    '100' : '0001000' ,
    '101' : '0010000' ,
    '110' : '0100000' ,
    '111' : '1000000' , 
}

#deCode Function
def Syndrome_Decode(v):
    #infoWord = int(infoWord , 2)
    s1 = str(v[0]^v[1]^v[2]^v[4])
    s2 = str(v[3]^v[1]^v[2]^v[5])
    s3 = str(v[0]^v[1]^v[3]^v[6])
    s = s1+s2+s3
    e = list(map(int , S.get(s)))
    c = []
    for i,j in zip(v,e):
        c.append(i^j) 
    return c


infoWord = list(map(int , input("Enter Codeword: ")))
c = Syndrome_Decode(infoWord)
print(c)