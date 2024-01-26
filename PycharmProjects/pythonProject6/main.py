def ingresar_notas(n):
    notas = []
    for i in range(n):
        nota = float(input("Ingrese la nota {}: ".format(i+1)))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def contar_notas_por_debajo_promedio(notas):
    promedio = calcular_promedio(notas)
    contador = 0
    for nota in notas:
        if nota < promedio:
            contador += 1
    return contador

# Forma de uso
n = int(input("Ingrese la cantidad de notas: "))
lista_notas = ingresar_notas(n)
promedio = calcular_promedio(lista_notas)
cantidad_notas_debajo_promedio = contar_notas_por_debajo_promedio(lista_notas)

print("El promedio de las notas es:", promedio)
print("Cantidad de notas por debajo del promedio:", cantidad_notas_debajo_promedio)
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
