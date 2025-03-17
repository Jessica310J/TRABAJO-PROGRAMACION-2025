def calcular_descuento(monto_compra, porcentaje_descuento=20):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    :param monto_compra: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (20% ).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_compra / 100) * porcentaje_descuento
    return descuento

def calcular_monto_final(monto_compra, descuento):
    """
    Calcula el monto final a pagar después del descuento.

    :param monto_compra: Monto total de la compra.
    :param descuento: Monto del descuento.
    :return: Monto final a pagar.
    """
    monto_final = monto_compra - descuento
    return monto_final

# Llamada a la función con valor predeterminado para el descuento
monto_compra1 = 1000
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = calcular_monto_final(monto_compra1, descuento1)

print(f"Monto de compra: ${monto_compra1}")
print(f"Descuento ({20}%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

# Llamada a la función con un porcentaje de descuento personalizado
monto_compra2 = 500
porcentaje_descuento2 = 30
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = calcular_monto_final(monto_compra2, descuento2)

print(f"Monto de compra: ${monto_compra2}")
print(f"Descuento ({porcentaje_descuento2}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
