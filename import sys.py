import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(factorial(n))

#Se importa el módulo sys para poder obtener el argumento pasado al programa en la línea de comandos.
#Se define una función factorial(n) que calcula el factorial de n recursivamente. Si n es 0, devuelve 
#.En otro caso, devuelve n multiplicado por el factorial de n-1.
#Si el programa es ejecutado directamente (no importado como módulo), 
#se obtiene el primer argumento de la línea de comandos (el número para el 
#cual se calculará el factorial) y se llama a la función factorial con 
#ese argumento. Finalmente, se imprime el resultado./