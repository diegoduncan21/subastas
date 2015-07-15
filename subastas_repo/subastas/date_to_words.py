from datetime import datetime

FIJOS = {
        0: "Cero",
        1: "Un",
        2: "Dos",
        3: "Tres",
        4: "Cuatro",
        5: "Cinco",
        6: "Seis",
        7: "Siete",
        8: "Ocho",
        9: "Nueve",
        10: "Diez",
        11: "Once",
        12: "Doce",
        13: "Trece",
        14: "Catorce",
        15: "Quince",
        20: "Veinte",
        30: "Treinta",
        40: "Cuarenta",
        50: "Cincuenta",
        60: "Sesenta",
        70: "Setenta",
        80: "Ochenta",
        90: "Noventa",
        100: "Cien",
}

PRE = {
        10: "Dieci",
        20: "Veinti",
        30: "Treinta y ",
        40: "Cuarenta y ",
        50: "Cincuenta y ",
        60: "Sesenta y ",
        70: "Setenta y ",
        80: "Ochenta y ",
        90: "Noventa y ",
}

MESES = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
}


def numero_a_palabra(numero):
    if numero in FIJOS.keys():
        return FIJOS.get(numero)
    else:
        decena = numero / 10 * 10
        unidad = numero % 10
        return "%s%s" % (PRE[decena], FIJOS[unidad].lower())


def numero_a_mes(numero):
    if numero not in MESES.keys():
        return MESES.get(datetime.now().month)
    return MESES.get(numero)
