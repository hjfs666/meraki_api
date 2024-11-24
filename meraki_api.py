import requests

# Configuración de la API Key y la URL base
API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'
BASE_URL = 'https://api.meraki.com/api/v1'

# Encabezados para la solicitud
headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

# Función para obtener las organizaciones
def get_organizations():
    url = f'{BASE_URL}/organizations'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# Llamada a la función y muestra de resultados
def list_organizations():
    organizations = get_organizations()
    if organizations:
        for org in organizations:
            print(f'ID: {org["id"]}, Nombre: {org["name"]}')
    else:
        print('No se pudieron obtener las organizaciones.')

# Ejecutar la función para listar las organizaciones
list_organizations()