from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('modeloRF.pkl')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos del formulario
        data = request.get_json()

        # Crear un DataFrame con los datos del usuario
        data_df = pd.DataFrame([data])

        # Realizar la predicción
        prediction = model.predict(data_df)

        # Devolver la predicción como respuesta JSON
        return jsonify({'prediccion': np.round(prediction[0], 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
