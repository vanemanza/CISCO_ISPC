#import fundamentos_intermedio.Modulo_1.paquetes.carpeta_b.module as module
#TODO MODIFICAR EL IMPORT q cambió despues de que agregué nuevas carpetas
# cuando se importa un modulo Python crea una variable llamada __name__
# cada archivo fuente usa su propia version de la variable, no se comparte entre modulos

# el print __name__ de module.py, cuando lo ejecute main.py será el nombre del archivo importado sin el .py --> module

#print(module.counter)