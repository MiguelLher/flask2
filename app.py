from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Cargar el modelo
model_nn = joblib.load('modeloRF.pkl')

# Definir MinMaxScaler (asegúrate de usar el mismo escalador que usaste durante el entrenamiento)
scaler = MinMaxScaler()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos del formulario
        na_sales = float(request.form['na_sales'])
        eu_sales = float(request.form['eu_sales'])
        jp_sales = float(request.form['jp_sales'])
        other_sales = float(request.form['other_sales'])
        genre = float(request.form['genre'])
        platform = float(request.form['platform'])

        # Crear el DataFrame con los datos de entrada
        input_data = pd.DataFrame([[na_sales, eu_sales, jp_sales, other_sales, genre, platform]],
                                  columns=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Genre', 'Platform'])

        # Escalar los datos de entrada
        input_data_scaled = scaler.transform(input_data)

        # Realizar la predicción
        prediccion = model_nn.predict(input_data_scaled)
        prediccion = prediccion[0]  # Obtener el primer (y único) valor de la predicción

        return jsonify(prediccion=prediccion)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
