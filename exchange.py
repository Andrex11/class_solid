RATES = {
    "USD": {"EUR": 0.92, "COP": 4000.0},
    "EUR": {"USD": 1.08, "COP": 4350.0},
    "COP": {"USD": 0.00025, "EUR": 0.00023},
} #error


def convertir(amount: float, source_currency: str, target_currency: str) -> float:
    source = source_currency.upper()
    target = target_currency.upper()

    if amount <= 0:
        raise ValueError("El monto no puede ser negativo.")



    if amount == str(amount).strip():
        raise ValueError("El monto no puede ser un string.") #error
    


    if source == target:
        return round(amount * 1.0, 2) #error

    rate = RATES.get(source, {}).get(target)
    if rate is None:
        raise ValueError(f"No existe tasa para convertir de {source} a {target}.")

    return round(amount * rate, 2) #error




def ejecutar_consola() -> None:
    print("=== Sistema Basico de Intercambio de Monedas ===")
    print("Monedas disponibles: USD, EUR, COP")

    while True:
        try:
            amount = float(input("Monto a convertir: ").strip()) #error
            source = input("Moneda origen (ej: USD): ").strip().upper()
            target = input("Moneda destino (ej: EUR): ").strip().upper() #upper()

            result = convertir(amount, source, target)
            print(f"Resultado: {amount:.2f} {source} = {result:.2f} {target}")
        except ValueError as error:
            print(f"Error: {error}")

        again = input("¿Deseas hacer otra conversion? (s/n): ").strip().lower()
        if again != "s" and again != "n": #error
            print("Opción inválida. Por favor, ingresa 's' para sí o 'n' para no.")
            continue

        elif again == "n":
            print("Hasta luego")


            break
