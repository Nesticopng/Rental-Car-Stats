# Configuraciones Gráfica Vehiculos según su Class
def obtener_decodificacion():
    return {
        "Category": {
            'M': 'Mini', 'N': 'Mini Elite', 'E': 'Económico', 'H': 'Económico Elite',
            'C': 'Compacto', 'D': 'Compacto Elite', 'I': 'Intermedio', 'J': 'Intermedio Elite',
            'S': 'Estándar', 'R': 'Estándar Elite', 'F': 'Tamaño completo', 'G': 'Tamaño completo Elite',
            'P': 'Premium', 'U': 'Premium Elite', 'L': 'Lujo', 'W': 'Lujo Elite', 'O': 'Tamaño extra', 'X': 'Especial'
        },
        "Type": {
            'B': '2-3 Puertas', 'C': '2-4 Puertas', 'D': '4-5 Puertas', 'W': 'Camioneta/Wagon',
            'V': 'Van de pasajeros', 'L': 'Limusina/Sedán', 'S': 'Deportivo', 'T': 'Convertible',
            'F': 'SUV', 'J': 'Clasificación Terreno', 'X': 'Especial'
        },
        "Transmission": {
            'M': 'Sincrónico', 'N': 'Sincrónico 4WD', 'C': 'Sincrónico AWD',
            'A': 'Automático', 'B': 'Automático 4WD', 'D': 'Automático AWD'
        },
        "Fuel": {
            'R': 'Combustible/Energía no especificada con aire', 'N': 'Combustible/Energía no especificada sin aire',
            'D': 'Diésel con aire', 'Q': 'Diésel sin aire', 'E': 'Eléctrico', 'H': 'Híbrido con aire'
        }
    }