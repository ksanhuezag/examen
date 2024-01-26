def imprimir_tercer_mayor(lista):
    lista_ordenada = sorted(lista, reverse=True)
    if len(lista_ordenada) >= 3:
        tercer_mayor = lista_ordenada[2]
        print("El tercer mayor número es:", tercer_mayor)
    else:
        print("No hay suficientes números en la lista.")

def contar_impares(lista):
    impares = 0
    for numero in lista:
        if numero % 2 != 0:
            impares += 1
    print("La cantidad de números impares es:", impares)

def contar_entre_mayores(lista):
    cantidad = 0
    for i in range(1, len(lista) - 1):
        if lista[i-1] > lista[i] and lista[i+1] > lista[i]:
            cantidad += 1
    print("La cantidad de números que cumplen la condición es:", cantidad)

def main():
    N = int(input("Ingrese el valor de N: "))
    lista = []
    for i in range(N):
        numero = int(input(f"Ingrese el número {i+1}: "))
        lista.append(numero)

    imprimir_tercer_mayor(lista)
    contar_impares(lista)
    contar_entre_mayores(lista)

main()
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
