try:
    divisao = 10 / 0 
    print(divisao)
except:
    print('''nao foi possivel realizar essa operaçao!''')

def atividade(x,y): 
    try:
        result = x/y
    except ZeroDivisionError:
        print("por favor, nao utilize zeros!")
    except:
        print("\033[91m algo deu errado...")     
    else:
        print("seu resultado e: {result}")
    finally:
        print("\033[92m vamos de novo?]")
    divide(13,0)                

import random
volue = random.randint(0, 3)
match volue:
    case 0:
        print("zero!")
    case 1:
        print("um!")
    case 2:
        print("dois!")        
    case _:
        print("execao!")        