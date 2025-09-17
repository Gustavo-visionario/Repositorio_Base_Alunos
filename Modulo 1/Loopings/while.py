def exercicios_514():
    s = 0
    quantidade = 0
    while True:
        v = int(input("digite um numero ou 0 para sair"))
        if v == 0:
            break
        s = s + v
        quantidade + 1
    print("a soma e: ", s)
    print("a quantidade e:",quantidade)
    print("a media e:",s / quantidade)
exercicios_514()

L=[]
while True:
    n=(input("digite um numero(digite >pare< para sair):"))
    if n == ('pare'):
        print("encerrando processo")
        break
    L.append(n)
x=0
while x < len(L):
    print(L[x])
    x=x+1    


