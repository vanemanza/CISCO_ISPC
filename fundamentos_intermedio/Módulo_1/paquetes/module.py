#!/usr/bin/env python3 
# la linea de arriba le indica al sistema operativo como ejecutar el archivo o mejor dicho que programa debe ejecutarse 
# para interpretar el texto

print('me gusta ser una modula! :)')
nombre_archivo = 'module'
__counter = 0

# --> imprime __main__ porque cuando se ejecuta un archivo directamente, la variable __name__ se establece a __main__

# podemos usar la variable __name__ para detectar en que contexto se activó el código

def suml(lista):
    global __counter
    __counter +=1
    la_suma = 0 
    for elemento in lista:
        la_suma += elemento 
    return la_suma

def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod    

# if __name__ == "__main__":
#     print('estoy en el archivo module.py')
#     print(f'en el archivo {nombre_archivo} la variable __name__ toma el valor:', __name__)
# else:
#     print('estoy en main, o sea el archivo q importó a module.py')    
#     print(f'en el archivo MAIN la variable __name__ toma el valor:', __name__)

if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    lista = [i+1 for i in range(5)]
    print(suml(lista) == 15)
    print(prodl(lista) == 120)
