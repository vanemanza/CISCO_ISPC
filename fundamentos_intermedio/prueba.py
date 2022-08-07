from sys import path
from pprint import pprint as p

for archivo in path:
    p(archivo)

print(type(path))    

# La variable path(tipo list) almacena todas las ubicaciones (carpetas o directorios) que se
# buscan para encontrar un modulo que ha sido solicitado por la instruccion import
# Python examina estas carpetas en el orden en que aparecen en la lista, si el modulo no se puede
# encontrar en ninguno de los directorios, la importacion falla
# de lo contrario, se tomará en cuenta la primera carpeta que contenga un modulo con el nombre
# buscado y si otra carpeta contiene el mismo nombre, se ignorará

# Solución 1:
# agregar una carpeta q contenga el modulo a la variable path
path.append('../Modulo1/paquetes')
import module #no pude !!! :(

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))