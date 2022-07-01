import json

categorias = []
ruta = "categoria.json"
with open(ruta) as contenido:
    cate = json.load(contenido)
    for arbolote in cate:
        print(arbolote.get("color"))
        categorias.append(arbolote)

arbol = [
        {
            'identificador' : '01',
            'nombre' : 'Manizales',
            'valor': 7100,
            'categoria': categorias[3],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 7
        },
        {
            'identificador' : '02',
            'nombre' : 'Pereira',
            'valor': 8300,
            'categoria': categorias[2],
            'valorBaseIzq' : 0,
            'valorBaseDer' : 0,
            'incrementeNocturno': 6
        },
        {
            'identificador': '03',
            'nombre': 'Medellín',
            'valor': 4400,
            'categoria': categorias[1],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 5
        },
{
            'identificador': '04',
            'nombre': 'Bogotá',
            'valor': 7600,
            'categoria': categorias[0],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 8
        },
{
            'identificador': '05',
            'nombre': 'Ibagué',
            'valor': 6600,
            'categoria': categorias[0],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 3
        },
{
            'identificador': '06',
            'nombre': 'Cartagena',
            'valor': 5700,
            'categoria': categorias[2],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 9
        },
        {
            'identificador': '07',
            'nombre': 'Quindio',
            'valor': 8700,
            'categoria': categorias[3],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 4
        },
{
            'identificador': '08',
            'nombre': 'Cali',
            'valor': 7700,
            'categoria': categorias[2],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 6
        },
        {
            'identificador': '09',
            'nombre': 'Popayan',
            'valor': 7500,
            'categoria': categorias[1],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 7
        },
{
            'identificador': '10',
            'nombre': 'Cucuta',
            'valor': 5200,
            'categoria': categorias[0],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 2
        },
{
            'identificador': '11',
            'nombre': 'Pasto',
            'valor': 6800,
            'categoria': categorias[1],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 5
        },
{
            'identificador': '12',
            'nombre': 'Bucaramanga',
            'valor': 7900,
            'categoria': categorias[0],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 2
        },
{
            'identificador': '13',
            'nombre': 'Barranquilla',
            'valor': 4900,
            'categoria': categorias[3],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 5
        },
{
            'identificador': '14',
            'nombre': 'Leticia',
            'valor': 7200,
            'categoria': categorias[2],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 2
        },
{
            'identificador': '15',
            'nombre': 'Tunja',
            'valor': 7300,
            'categoria': categorias[1],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 7
        },
{
            'identificador': '16',
            'nombre': 'Florencia',
            'valor': 5300,
            'categoria': categorias[0],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 8
        },
{
            'identificador': '17',
            'nombre': 'Armenia',
            'valor': 8000,
            'categoria': categorias[1],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 3
        },
{
            'identificador': '18',
            'nombre': 'Mocoa',
            'valor': 4600,
            'categoria': categorias[2],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 4
        },
{
            'identificador': '19',
            'nombre': 'Neiva',
            'valor': 5500,
            'categoria': categorias[3],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 5
        },
        {
            'identificador': '20',
            'nombre': 'Sicelejo',
            'valor': 3200,
            'categoria': categorias[2],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 6
        },
        {
            'identificador': '21',
            'nombre': 'San Andrés',
            'valor': 7000,
            'categoria': categorias[3],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 9
        },
{
            'identificador': '22',
            'nombre': 'Quibdó',
            'valor': 6900,
            'categoria': categorias[0],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 3
        },
{
            'identificador': '23',
            'nombre': 'Valledupar',
            'valor': 3100,
            'categoria': categorias[1],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 8
        },
{
            'identificador': '24',
            'nombre': 'Yopal',
            'valor': 6000,
            'categoria': categorias[2],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 8
        },
{
            'identificador': '25',
            'nombre': 'Inirida',
            'valor': 7800,
            'categoria': categorias[3],
            'valorBaseIzq': 0,
            'valorBaseDer': 0,
            'incrementeNocturno': 8
        }
    ]


cadena_json = json.dumps(arbol)
print(cadena_json)

with open('arbol.json', 'w') as f:
    json.dump(arbol, f)


with open('arbol.json', 'r') as f:
    cadena_json = json.load(f)

    print(cadena_json)

