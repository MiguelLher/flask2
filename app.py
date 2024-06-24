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
        # Obtener los datos enviados en el request
        NA_Sales = float(request.form['NA_Sales'])
        EU_Sales = float(request.form['EU_Sales'])
        JP_Sales = float(request.form['JP_Sales'])
        Other_Sales = float(request.form['Other_Sales'])
        Genre = float(request.form['Genre'])
        Platform = float(request.form['Platform'])

        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[NA_Sales, EU_Sales, JP_Sales, Other_Sales, Genre, Platform]],
                               columns=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Genre', 'Platform'])

        # Realizar predicciones
        prediction = model.predict(data_df)
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'ventas_globales': np.exp(prediction[0])})  # np.exp para revertir la transformación logarítmica si aplica
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
