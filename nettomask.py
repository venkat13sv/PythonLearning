def binaryToDecimal(binary):
    binary=(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return str(decimal)

inpt=int(input())
rep=inpt/8
if(rep==1):
    print("255.0.0.0")
elif(rep==2):
    print("255.255.0.0")
elif(rep==3):
    print("255.255.255.0")
else:
    q=int(inpt/8)
    r=inpt%8
    bin=q*8*['1']
    bin="".join(bin)+"".join(r*['1'])+"".join((8-r)*['0'])
    print(int(bin[:8])+2)
    print(binaryToDecimal(bin[:8])+"."+binaryToDecimal(bin[8:16])+"."+binaryToDecimal(bin[16:24])+"."+binaryToDecimal(bin[24:32]))
    print(q,r)
    print("update")
#if(rep<1)
#print(rep)
