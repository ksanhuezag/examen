def obtener_entero_positivo(mensaje):
    while True:
          try:
              valor = int(input(mensaje))
              if valor <= 0:
                  print("Error, debe ingresar un número entero positivo.")
              else:
                  return valor
          except ValueError:
              print("Error, debe ingresar un número entero positivo válido.")

def obtener_medicion_valida(indice):
    while True:
        try:
            medicion = float(input(f"Ingrese la medición {indice}: "))
            if 0 <= medicion <= 150:
                return medicion
            else:
                print("Error, ingrese una medida en el intervalo de 0 a 150.")
        except ValueError:
            print("Error, debe ingresar un número válido.")

def main ():
    N = obtener_entero_positivo("Ingrese la cantidad de mediciones a registrar: ")
    mediciones = []

    for i in range(1, N+1):
        medicion = obtener_medicion_valida(i)
        mediciones.append(medicion)

    promedio = sum(mediciones) / len(mediciones)
    print(f"El promedio de agua caída es: {promedio:.2f}")

if __name__ =="__main__":
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

