import e4

texto = "Hola, como estas! hola que pasa como hola pepe pepe pepe"

print(
    sorted(
        e4.contar_palabras(texto).items(), 
        key=lambda p: p[1], 
        reverse=True
    )[:3]
)