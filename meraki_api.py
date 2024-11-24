import requests
import csv

# Configuración de API Key y la URL base
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

# Función para obtener los dispositivos de una organización
def get_organization_devices(org_id):
    url = f'{BASE_URL}/organizations/{org_id}/devices'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# Función para crear el inventario en formato CSV
def create_inventory_csv(devices, filename='inventory.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Modelo', 'Nombre', 'MAC', 'IP Pública', 'IP LAN', 'Número Serial', 'Estado'])
        for device in devices:
            if device['model'].startswith(('MR', 'MX')):
                writer.writerow([
                    device.get('model', ''),
                    device.get('name', ''),
                    device.get('mac', ''),
                    device.get('publicIp', ''),
                    device.get('lanIp', ''),
                    device.get('serial', ''),
                    device.get('status', '')
                ])

# Función principal para listar organizaciones y crear inventario
def main():
    organizations = get_organizations()
    if organizations:
        for org in organizations:
            print(f'Obteniendo dispositivos para la organización: {org["name"]}')
            devices = get_organization_devices(org['id'])
            if devices:
                create_inventory_csv(devices)
                print(f'Inventario creado para la organización: {org["name"]}')
            else:
                print(f'No se pudieron obtener los dispositivos para la organización: {org["name"]}')
    else:
        print('No se pudieron obtener las organizaciones.')

# Ejecutar la función principal
if __name__ == '__main__':
    main()