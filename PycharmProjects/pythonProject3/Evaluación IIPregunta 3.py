def obtener_nota_valida(mensaje):
    while True:
        nota = input(mensaje)
        try:
            nota = float(nota)
            if 1.0 <= nota <= 7.0:
                return nota
            else:
                print("Ingrese una nota válida. Reintente.")
        except ValueError:
            print("Ingrese una nota válida. Reintente.")

def obtener_promedio():
    notas = []
    for i in range(3):
        nota = obtener_nota_valida(f"Ingrese nota {i+1}: ")
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    return promedio

promedio_notas = obtener_promedio()
print("El promedio de las tres notas válidas ingresadas es:", promedio_notas)


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
