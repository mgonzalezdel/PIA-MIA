productos = [
    {"nombre": "telefono", "precio": 499.99, "stock": 4},
    {"nombre": "cargador", "precio": 24.50, "stock": 10},
    {"nombre": "auricular", "precio": 24.50, "stock": 6}
]

ordenada = sorted(productos, key=lambda p: (p["precio"], p["nombre"]))
print(ordenada)