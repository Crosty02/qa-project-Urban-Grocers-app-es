import sender_stand_request
import data


def positive_assert(kit_body,auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


# Prueba 1. Kit con un nombre de 1 solo caracteres
# Pruebas positivas
def test_create_kit_min_characters():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {"name": "a"}
    positive_assert(kit_body, auth_token)


# Prueba 2 Kit con un nombre de 511 caracteres
# Prueba positiva.
def test_create_kit_max_characters():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    positive_assert(kit_body, auth_token)


# Prueba 3 kit con el name vació
# Prueba negativa.
def test_create_kit_empty_name():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {"name": ""}
    negative_assert(kit_body, auth_token)

# Prueba 4. Negativa el nombre contiene más de 512 caracteres
def test_create_kit_exceeding_max_characters():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    negative_assert(kit_body, auth_token)

# Prueba 5. Positiva
# Se permiten caracteres especiales en el nombre del kit
def test_create_kit_with_special_characters():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {"name": "№%@,"}
    positive_assert(kit_body, auth_token)

# Prueba 6. Positiva
# Se permiten espacios en el nombre del kit
def test_create_kit_with_spaces():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {"name": "A Aaa"}
    positive_assert(kit_body, auth_token)

# Prueba 7. Positiva
# Para el caso en que se permiten números en el nombre del kit
def test_create_kit_with_numbers():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {"name": "123"}
    positive_assert(kit_body, auth_token)

# Prueba 8. Negativa
# La solicitud no contiene el parámetro "name"
def test_create_kit_without_name_param():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {}
    negative_assert(kit_body, auth_token)

# Prueba 9. Negativa
# El tipo del parámetro name es un número
def test_create_kit_with_numeric_name():
    auth_token = sender_stand_request.get_auth_token()
    kit_body = {"name": 123}
    negative_assert(kit_body, auth_token)





