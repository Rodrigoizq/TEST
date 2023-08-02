     "Documentacion"


    Requisitos
 1-el presente programa necesita de Conda para correr.
 2-crea y activa el entorno de conda usando el archivo enviroment.yml.

  Ejecucion del servidor Flask
 1-Asegurate de que app.py este en funcionamiento en una terminal. Si aun no lo has hecho, ejecutalo usando 'app.py'.
 2-Con el servidor Flask en funcionamiento, puedes utilizar la API REST enviando solicitudes desde my_request.py.

  Ejecucion de la API REST con my_request.py
 1 - Una vez que el servidor Flask (API REST) está en funcionamiento.
 2-  ejecuta my_requests.py (API POST) para enviar solicitudes a la API REST: python my_requests.py.
 3 - La API REST procesará las oraciones enviadas y devolvera las entidades identificadas para cada oracion en formato JSON.


 Notas finales
 *Al momento de querer hacer una modificacion a las oraciones dentro de "my_requests.py" estas deben ser separadas por comas de lo contrario,
 la API tomara todas las oraciones y no las separara correctamente.
 * el reconocimiento de spaCY no diferencia correctamente en las oraciones cuando se utilizan mayusculas en palabras al Azar ejemplo 'Quiere','Tennis'
 y tratara de darles una etiqueta o label incorrecta.
 posibles soluciones:restringir la utilizacion de Mayusculas en partes de la oracion donde no sea relevante al momento de capturar la oracion.
 * es posible que Spacy tenga confusiones al separar nombres de personas que comparten nombres de lugares y viceversa.


