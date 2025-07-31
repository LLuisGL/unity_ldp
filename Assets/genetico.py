import random

POP_SIZE = 50
MUT_RATE = 0.1

gen = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','s','w','x','y','z',' ']

palabra = 'sistemas'
cuerpo = '________'

def get_poblacion(cuerpo):
    list = []
    for i in range(POP_SIZE):
            palabra_coseguir = ''
            for char in cuerpo:
                palabra_coseguir += char
            ind = 0
            for char in palabra:
                if palabra_conseguir[ind] == '_':
                    palabra_conseguir += gen[random.radint(0,len(gen))]
                ind += 1
            list.append(palabra_conseguir)
    list = mutar(list)
    return list

def mutar(lista):
    porcentaje = MUT_RATE * 100
    list = lista
    for palabra in list:
        i = random.randint(0, len(cuerpo))
        if palabra[i] != cuerpo[i]:
            palabra[i] = gen[random.randint(0,len(gen))]
    return list
        
puntos_justos = len(palabra)

while(True):
    list = get_poblacion(cuerpo)
    puntos_max = 0
    palabra_elegida = ''
    for palabra_tmp in list:
        puntos = 0
        ind = 0
        for char in palabra:
            if char in palabra_tmp:
                puntos += 1
                cuerpo[ind] = char
            ind += 1
        if puntos_max < puntos:
            palabra_elegida = palabra_tmp
            puntos_max = puntos
    if puntos_justos == puntos_max:
        print("lo consegui")
        print(palabra_elegida)
        break
        
        


    
