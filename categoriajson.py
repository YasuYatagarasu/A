import json

categoria = [
    {
        "color": "blue",
        "valor": 123,
        "camion": 98,
        "bus": 90,
        "camioneta": 75,
        "automovil": 60,
        "motocicleta": 30,
        "mototaxi": 25

    },

    {
        "color": "red",
        "valor": 120,
        "camion": 97,
        "bus": 92,
        "camioneta": 77,
        "automovil": 65,
        "motocicleta": 36,
        "mototaxi": 30
    },

    {
        "color": "green",
        "valor": 128,
        "camion": 99,
        "bus": 88,
        "camioneta": 71,
        "automovil": 60,
        "motocicleta": 35,
        "mototaxi": 27
    },
    {
        "color": "purple",
        "valor": 125,
        "camion": 100,
        "bus": 95,
        "camioneta": 60,
        "automovil": 56,
        "motocicleta": 25,
        "mototaxi": 25
    }
]

cadena_json = json.dumps(categoria)
print(cadena_json)

##for nodos in categoria:
    ##print(nodos.get('llave'))
    ##print(nodos.get('valor'))

with open('categoria.json', 'w') as f:
    json.dump(categoria, f)



with open('arbol1.json', 'r') as f:
    cadena_json = json.load(f)

    print(cadena_json)