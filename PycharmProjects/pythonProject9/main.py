def noHanSalido(ruleta):
    numeros_no_sorteados = [i for i in range(37) if ruleta[i] == 0]
    if numeros_no_sorteados:
        print("Los siguientes números no han sido sorteados:")
        print(numeros_no_sorteados)
    else:
        print("Todos los números han sido sorteados al menos una vez.")

def actualizarRuleta(ruleta, N):
    if 0 <= N <= 36:
        ruleta[N] += 1
    else:
        print("-1")

def obtenerPorcentaje(ruleta, N):
    total_tiradas = sum(ruleta)
    return ruleta[N] / total_tiradas if total_tiradas > 0 else 0

def main():
    ruleta = [0] * 37  # Inicializamos la ruleta con ceros para cada número (del 0 al 36).

    # Simulación de tiradas para actualizar la ruleta.
    tiradas_simuladas = [4, 7, 15, 25, 36, 7, 25, 15, 4]
    for tirada in tiradas_simuladas:
        actualizarRuleta(ruleta, tirada)

    # Prueba de las funciones
    print("Ruleta actual:")
    print(ruleta)
    print()
    noHanSalido(ruleta)

    numero_a_actualizar = 7
    print("\nActualizando la ruleta con el número", numero_a_actualizar)
    actualizarRuleta(ruleta, numero_a_actualizar)

    print("\nRuleta actualizada:")
    print(ruleta)

    numero_a_consultar = 15
    print("\nObteniendo el porcentaje de veces que ha salido el número", numero_a_consultar)
    porcentaje = obtenerPorcentaje(ruleta, numero_a_consultar)
    print(f"El porcentaje de veces que ha salido el número {numero_a_consultar} es: {porcentaje:.2%}")


if __name__ == "__main__":
    main()
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
