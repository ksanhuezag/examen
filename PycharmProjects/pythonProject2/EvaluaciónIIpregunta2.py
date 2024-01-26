def mostrar_tablas_multiplicar(X, N):
    for i in range(1, N+1):
        resultado = X * i
        print(f"{X} * {i} = {resultado}")

# Solicitar al usuario los valores de X y N
X = int(input("Ingrese el número para el cual desea ver la tabla de multiplicar: "))
N = int(input("Ingrese hasta qué número desea visualizar la tabla: "))

# Llamar a la función para mostrar las tablas de multiplicar
mostrar_tablas_multiplicar(X, N)


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
