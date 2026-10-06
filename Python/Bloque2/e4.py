SIGNOS = ".,:;!?¡¿()\"'"

def contar_palabras(texto: str) -> dict[str, int]:
    limpio = texto.lower()
    for s in SIGNOS:
        limpio = limpio.replace(s, " ")

    conteo: dict[str, int] = {}
    palabras = limpio.split(" ")

    for p in palabras:
        if p == "":
            continue
        if conteo.get(p) == None:
            conteo[p] = 1
        else:
            conteo[p] += 1

    return conteo
if __name__ == "__main__":
    print(contar_palabras("Hola, como estas! hola"))