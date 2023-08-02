import requests
#API POST

#URL de la API
url = "http://localhost:8080/ner"


#Modificar la lista de "oraciones" el API separa las oraciones por "ORG,LOC,MISC y al final Oracion" sin importar la ubicacion del texto en la oracion.
#OJO las oraciones deben ser Separadas con COMA!
data = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera.",
        "Samsung quiere vender partes modulares en Estados Unidos para telefonos Android y Mejorar el mercado para los consumidores",
        "Mi amigo Pedro se quiere comprar unos Tennis NIKE pero no tiene ganas de ir a San Diego"
    ]
}
#Envio de la solicitud POST a la URL
response = requests.post(url, json=data)

#verificar si la solicitud se realizo correctamente
if response.status_code == 200:
    result = response.json()
    #imprimir los resultados obtenidos
    print(result)
    #caso contrario dar error en terminal
else:
    print("Error:", response.status_code, response.text)
