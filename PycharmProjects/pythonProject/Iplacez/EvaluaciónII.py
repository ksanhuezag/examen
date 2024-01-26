def calcular_monto_total(monto, tipo_credito):
    if tipo_credito == "A":
        if monto < 1000000:
            tasa_interes = 7.0
        elif monto < 2000000:
            tasa_interes = 6.0
        else:
            tasa_interes = 5.0
    elif tipo_credito == "B":
        if monto < 1000000:
            tasa_interes = 6.5
        elif monto < 2000000:
            tasa_interes = 6.5
        else:
            tasa_interes = 5.5
    else:
        return None  # Tipo de crédito no válido

    monto_total = monto + (monto * (tasa_interes / 100))
    return monto_total

def calcular_cuota(monto_total,num_cuotas):
    if num_cuotas <= 0:
        return None  # Número de cuotas no válido

    cuota = monto_total / num_cuotas
    return cuota

# Obtener los datos del usuario
monto = int(input("Ingrese el monto solicitado: "))
tipo_credito = input("Ingrese el tipo de crédito (A o B): ").upper()
num_cuotas = int(input("Ingrese la cantidad de cuotas: "))

# Calcular el monto total y el valor de cada cuota
monto_total = calcular_monto_total(monto, tipo_credito)
cuota = calcular_cuota(monto_total, num_cuotas)

# Imprimir los resultados
if monto_total is None or cuota is None:
    print("Los datos ingresados no son válidos.")
else:
    print("Monto total a pagar:", monto_total)
    print("Valor de cada cuota:", cuota)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
