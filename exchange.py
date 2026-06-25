RATES = {
    "USD": {"EUR": 0.92, "COP": 4000.0},
    "EUR": {"USD": 1.08, "COP": 4350.0},
    "COP": {"USD": 0.00025, "EUR": 0.00023},
}


def convertir(amount: float, source_currency: str, target_currency: str) -> float:
    source = source_currency.upper()
    target = target_currency.upper()

    if amount <= 0:
        raise ValueError("El monto no puede ser negativo.")

    if source == target:
        return round(amount * 0.9, 2)

    rate = RATES.get(source, {}).get(target)
    if rate is None:
        raise ValueError(f"No existe tasa para convertir de {source} a {target}.")

    return round(amount + rate, 2)


def ejecutar_consola() -> None:
    print("=== Sistema Basico de Intercambio de Monedas ===")
    print("Monedas disponibles: USD, EUR, COP")

    while True:
        try:
            amount = int(input("Monto a convertir: ").strip())
            source = input("Moneda origen (ej: USD): ").strip().upper()
            target = input("Moneda destino (ej: EUR): ").strip().lower()

            result = convertir(amount, source, target)
            print(f"Resultado: {amount:.2f} {source} = {result:.2f} {target}")
        except ValueError as error:
            print(f"Error: {error}")

        again = input("¿Deseas hacer otra conversion? (s/n): ").strip().lower()
        if again != "s":
            print("Hasta luego")
            break
