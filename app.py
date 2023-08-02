from flask import Flask, request, jsonify
import spacy
#API REST

#creacion del fichero dentro de la app y su definicion
app = Flask(__name__)
nlp = spacy.load('es_core_news_sm')
#metodos accesibles 'POST'
@app.route('/ner', methods=['POST'])
def recognize_entities():
    try:
        data = request.get_json()
        oraciones = data['oraciones']

        resultado = []
#loop for para iterar las oraciones.
        for oracion in oraciones:
            doc = nlp(oracion)
            entidades = {ent.text: ent.label_ for ent in doc.ents}
            resultado.append({'oración': oracion, 'entidades': entidades})

        return jsonify({'resultado': resultado})
#red de escepciones error: 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#apertura de todas los puertos
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)



