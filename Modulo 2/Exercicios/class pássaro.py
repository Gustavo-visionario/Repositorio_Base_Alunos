class pássaro():
    def __init__(self,tamanho, cores, especie, sexo):
        self.tamanho = tamanho
        self.cores = cores
        self.especie = especie
        self.sexo = sexo

    def cantar(self):
        return print(f'sou um {self.especie} cantando uma bela canção 🎵')
    def voar(self):
        return print('batendo as asas e:voando...')
    
Pássaro1 = pássaro(0.14,['marrom','branco','cinza'],'corvo','M')
Pássaro1.cantar()
