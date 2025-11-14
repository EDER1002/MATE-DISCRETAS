import math
from itertools import permutations, combinations
from collections import Counter

def contar_elementos(lista):
    return len(lista)

def factorial(n):
    return math.factorial(n)

def permutaciones(n):
    return math.factorial(n)

def combinaciones(n, k):
    return math.comb(n, k)

def permutaciones_lista(lista):
    return list(permutations(lista))

def combinaciones_lista(lista, k):
    return list(combinations(lista, k))

def conjunto_union(a, b):
    return set(a) | set(b)

def conjunto_interseccion(a, b):
    return set(a) & set(b)

def conjunto_diferencia(a, b):
    return set(a) - set(b)

def conjunto_diferencia_simetrica(a, b):
    return set(a) ^ set(b)

def multiset_union(a, b):
    return Counter(a) | Counter(b)

def multiset_interseccion(a, b):
    return Counter(a) & Counter(b)

def multiset_suma(a, b):
    return Counter(a) + Counter(b)

def multiset_resta(a, b):
    return Counter(a) - Counter(b)

def main():
    while True:
        print("\n=== MENÚ ===")
        print("1. Conteo")
        print("2. Permutaciones y combinaciones")
        print("3. Operaciones de conjuntos")
        print("0. Salir")
        op = input("Opción: ")

        if op == "1":
            lista = input("Ingresa elementos separados por coma: ").split(",")
            print("Cantidad de elementos:", contar_elementos(lista))

        elif op == "2":
            print("1. Factorial")
            print("2. Permutaciones (n!)")
            print("3. Combinaciones C(n,k)")
            print("4. Permutaciones de lista")
            print("5. Combinaciones de lista")
            sub = input("Opción: ")

            if sub == "1":
                n = int(input("n: "))
                print(factorial(n))

            elif sub == "2":
                n = int(input("n: "))
                print(permutaciones(n))

            elif sub == "3":
                n = int(input("n: "))
                k = int(input("k: "))
                print(combinaciones(n, k))

            elif sub == "4":
                lista = input("Lista separada por coma: ").split(",")
                print(permutaciones_lista(lista))

            elif sub == "5":
                lista = input("Lista separada por coma: ").split(",")
                k = int(input("k: "))
                print(combinaciones_lista(lista, k))

        elif op == "3":
            print("1. Unión")
            print("2. Intersección")
            print("3. Diferencia")
            print("4. Diferencia simétrica")
            print("5. Multiconjuntos")
            sub = input("Opción: ")

            if sub in ("1","2","3","4"):
                a = input("Conjunto A: ").split(",")
                b = input("Conjunto B: ").split(",")

                if sub == "1":
                    print(conjunto_union(a, b))
                elif sub == "2":
                    print(conjunto_interseccion(a, b))
                elif sub == "3":
                    print(conjunto_diferencia(a, b))
                elif sub == "4":
                    print(conjunto_diferencia_simetrica(a, b))

            elif sub == "5":
                a = input("Multiconjunto A: ").split(",")
                b = input("Multiconjunto B: ").split(",")
                print("Unión:", multiset_union(a, b))
                print("Intersección:", multiset_interseccion(a, b))
                print("Suma:", multiset_suma(a, b))
                print("Resta:", multiset_resta(a, b))

        elif op == "0":
            break

main()
