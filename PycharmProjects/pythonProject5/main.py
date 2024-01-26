def ingresar_notas(N):
    notas = []
    for i in range(N):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

def contar_notas_por_debajo(lista):
    promedio = calcular_promedio(lista)
    count = 0
    for nota in lista:
        if nota < promedio:
            count += 1
    return count

# Ejemplo de uso:
n = int(input("Ingrese la cantidad de notas: "))
notas = ingresar_notas(n)
promedio = calcular_promedio(notas)
cantidad_por_debajo = contar_notas_por_debajo(notas)

print("Notas ingresadas:", notas)
print("Promedio:", promedio)
print("Cantidad de notas por debajo del promedio:", cantidad_por_debajo)
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
