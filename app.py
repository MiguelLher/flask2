from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('model.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        app.logger.debug(f'Datos recibidos: {request.form}')
        fruitset = float(request.form['fruitset'])
        seeds = float(request.form['seeds'])
        fruitmass = float(request.form['fruitmass'])
        row_num = float(request.form['row_num'])
        clonesize = float(request.form['clonesize'])
        avg_upper_trange = float(request.form['avg_upper_trange'])

        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[fruitset, seeds, fruitmass, row_num, clonesize, avg_upper_trange]], 
                               columns=['fruitset', 'seeds', 'fruitmass', 'Row#', 'clonesize', 'AverageOfUpperTRange'])
        app.logger.debug(f'DataFrame creado: {data_df}')

        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')

        # Devolver las predicciones como respuesta JSON
        return jsonify({'yield': prediction[0]})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
