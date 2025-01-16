# Headers para las solicitudes
headers = {
    "Content-Type": "application/json"
}

# Datos de usuario (user_body)
user_body = {
    "first_name": "Max",  # Asegúrate de que este campo es requerido
    "phone": "+10005553535",  # Debe tener el formato adecuado
    "address": "8042 Lancaster Ave. Hamburg, NY"  # Debe ser un campo válido
}

product_ids = {
    "ids": [1, 2, 3]
}

kit_body = {
        "name": "Mi conjunto",
        "card": {
            "id": 1,
            "name": "Para la situación"
        },
        "productsList": None,
        "id": 7,
        "productsCount": 0
    }
