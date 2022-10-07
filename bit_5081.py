N=int(input().strip())
s1=str(input().strip())
s2=str(input().strip())
expressao=(str(input().upper()).strip()).split()
x=0
while True:
    if(N>1000)or(N<1):
        print("ERRO")
        x=1
        break
    elif (len(s1)!=N)or(len(s2)!=N)or(len(expressao)<3)or(len(expressao)>5):
        print("ERRO")
        x=1
        break
    elif(expressao[1]!="AND")and(expressao[1]!="OR")and(expressao[1]!="XOR")and(expressao[1]!="NAND")and(expressao[1]!="NOR")and(expressao[1]!="MOR"):
        print("ERRO")
        x=1
        break
    elif((expressao[0]!="S1")and(expressao[0]!="S2"))or((expressao[2]!="S1")and(expressao[2]!="S2")):
        print("ERRO")
        x=1
        break
    elif(len(expressao)>3):
        if(expressao[3]!="AND")and(expressao[3]!="OR")and(expressao[3]!="XOR")and(expressao[3]!="NAND")and(expressao[3]!="NOR")and(expressao[3]!="MOR"):
            print("ERRO")
            x=1
            break
        elif(expressao[4]!="S1")and(expressao[4]!="S2"):
            print("ERRO")
            x=1
            break
    for i in range(N):
        if(s1[i]!="0") and (s1[i]!="1"):
            print("ERRO")
            x=1
            break
        if(s2[i]!="0") and (s2[i]!="1"):
            print("ERRO")
            x=1
            break
        if(x==1):
            break
    if (x==0):
        resultado=[2 for i in range(N)]
        if expressao[1]=="AND":
            if (expressao[0]=="S1" and expressao[2]=="S2") or (expressao[0]=="S2" and expressao[2]=="S1"):
                for i in range(N):
                    if s1[i]==s2[i]:
                        resultado[i]=s1[i]
                    else:
                        resultado[i]="0"
            elif expressao[0]==expressao[2]:
                if expressao[0]=="S1":
                    resultado=s1
                elif expressao[0]=="S2":
                    resultado=s2
        elif expressao[1]=="OR":
            if (expressao[0]=="S1" and expressao[2]=="S2") or (expressao[0]=="S2" and expressao[2]=="S1"):
                for i in range(N):
                    if s1[i]==s2[i]:
                        resultado[i]=s1[i]
                    else:
                        resultado[i]="1"
            elif expressao[0]==expressao[2]:
                if expressao[0]=="S1":
                    resultado=s1
                elif expressao[0]=="S2":
                    resultado=s2
        elif expressao[1]=="XOR":
            if (expressao[0]=="S1" and expressao[2]=="S2") or (expressao[0]=="S2" and expressao[2]=="S1"):
                for i in range(N):
                    if s1[i]==s2[i]:
                        resultado[i]="0"
                    else:
                        resultado[i]="1"
            elif expressao[0]==expressao[2]:
                for i in range(N):
                    resultado[i]="0"
        elif expressao[1]=="NAND":
            if (expressao[0]=="S1" and expressao[2]=="S2") or (expressao[0]=="S2" and expressao[2]=="S1"):
                for i in range(N):
                    if s1[i]==s2[i]:
                        if s1[i]=="1":
                            resultado[i]="0"
                        elif s1[i]=="0":
                            resultado[i]="1"
                    else:
                        resultado[i]="1"
            elif expressao[0]==expressao[2]:
                if expressao[0]=="S1":
                    for i in range(N):
                        if s1[i]=="1":
                            resultado[i]="0"
                        elif s1[i]=="0":
                            resultado[i]="1"
                elif expressao[0]=="S2":
                    for i in range(N):
                        if s2[i]=="1":
                            resultado[i]="0"
                        elif s2[i]=="0":
                            resultado[i]="1"
        elif expressao[1]=="NOR":
            if (expressao[0]=="S1" and expressao[2]=="S2") or (expressao[0]=="S2" and expressao[2]=="S1"):
                for i in range(N):
                    if s1[i]==s2[i]:
                        if s1[i]=="1":
                            resultado[i]="0"
                        elif s1[i]=="0":
                            resultado[i]="1"
                    else:
                        resultado[i]="0"
            elif expressao[0]==expressao[2]:
                if expressao[0]=="S1":
                    for i in range(N):
                        if s1[i]=="1":
                            resultado[i]="0"
                        elif s1[i]=="0":
                            resultado[i]="1"
                elif expressao[0]=="S2":
                    for i in range(N):
                        if s2[i]=="1":
                            resultado[i]="0"
                        elif s2[i]=="0":
                            resultado[i]="1"   
        elif expressao[1]=="MOR":
            if (expressao[0]=="S1")and(expressao[2]=="S2"):
                for i in range(N):
                    if s1[i]==s2[i]:
                        resultado[i]="1"
                    else:
                        if s1[i]=="1":
                            resultado[i]="0"
                        elif s1[i]=="0":
                            resultado[i]="1"
            elif (expressao[0]=="S2")and(expressao[2]=="S1"):
                for i in range(N):
                    if s2[i]==s1[i]:
                        resultado[i]="1"
                    else:
                        if s2[i]=="1":
                            resultado[i]="0"
                        elif s2[i]=="0":
                            resultado[i]="1"
            elif(expressao[0]=="S1")and(expressao[2]=="S1"):
                for i in range(N):
                    resultado[i]="1"  
            elif(expressao[0]=="S2")and(expressao[2]=="S2"):
                for i in range(N):
                    resultado[i]="1"
    if(x==0):
       if(len(expressao)>3):
            x=2
            resultado2=[2 for i in range(N)]
            if expressao[3]=="AND":
                if (expressao[4]=="S1"):
                    for i in range(N):
                        if s1[i]==resultado[i]:
                            resultado2[i]=s1[i]
                        else:
                            resultado2[i]="0"
                elif (expressao[4]=="S2"):
                    for i in range(N):
                        if s2[i]==resultado[i]:
                            resultado2[i]=s2[i]
                        else:
                            resultado2[i]="0"
            elif expressao[3]=="OR":
                if (expressao[4]=="S1"):
                    for i in range(N):
                        if s1[i]==resultado[i]:
                            resultado2[i]=s1[i]
                        else:
                            resultado2[i]="1"
                elif (expressao[4]=="S2"):
                    for i in range(N):
                        if s2[i]==resultado[i]:
                            resultado2[i]=s2[i]
                        else:
                            resultado2[i]="1"
            elif expressao[3]=="XOR":
                if (expressao[4]=="S1"):
                    for i in range(N):
                        if s1[i]==resultado[i]:
                            resultado2[i]="0"
                        else:
                            resultado2[i]="1"
                elif (expressao[4]=="S2"):
                    for i in range(N):
                        if s2[i]==resultado[i]:
                            resultado2[i]="0"
                        else:
                            resultado2[i]="1"
            elif expressao[3]=="NAND":
                if (expressao[4]=="S1"):
                    for i in range(N):
                        if s1[i]==resultado[i]:
                            if s1[i]=="1":
                                resultado2[i]="0"
                            elif s1[i]=="0":
                                resultado2[i]="1"
                        else:
                            resultado2[i]="1"
                elif (expressao[4]=="S2"):
                    for i in range(N):
                        if s2[i]==resultado[i]:
                            if s2[i]=="1":
                                resultado2[i]="0"
                            elif s2[i]=="0":
                                resultado2[i]="1"
                        else:
                            resultado2[i]="1"
            elif expressao[3]=="NOR":
                if (expressao[4]=="S1"):
                    for i in range(N):
                        if s1[i]==resultado[i]:
                            if s1[i]=="1":
                                resultado2[i]="0"
                            elif s1[i]=="0":
                                resultado2[i]="1"
                        else:
                            resultado2[i]="0"
                elif (expressao[4]=="S2"):
                    for i in range(N):
                        if s2[i]==resultado[i]:
                            if s2[i]=="1":
                                resultado2[i]="0"
                            elif s2[i]=="0":
                                resultado2[i]="1"
                        else:
                            resultado2[i]="0"  
            elif expressao[3]=="MOR":
                if (expressao[4]=="S1"):
                    for i in range(N):
                        if s1[i]==resultado[i]:
                            resultado2[i]="1"
                        else:
                            if resultado[i]=="1":
                                resultado2[i]="0"
                            elif resultado[i]=="0":
                                resultado2[i]="1"
                elif (expressao[4]=="S2"):
                    for i in range(N):
                        if s2[i]==resultado[i]:
                            resultado2[i]="1"
                        else:
                            if resultado[i]=="1":
                                resultado2[i]="0"
                            elif resultado[i]=="0":
                                resultado2[i]="1"
    break
if(x==0):
    for i in range(N):
        print(resultado[i],end="")
elif(x==2):
    for i in range(N):
        print(resultado2[i],end="")