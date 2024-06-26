from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        fruitset = float(request.form['fruitset'])
        seeds = float(request.form['seeds'])
        fruitmass = float(request.form['fruitmass'])
        RowNum = float(request.form['RowNum'])
        clonesize = float(request.form['clonesize'])
        AverageOfUpperTRange = float(request.form['AverageOfUpperTRange'])
        
        # Crear un DataFrame con los datos para la predicción
        data = pd.DataFrame({
            'fruitset': [fruitset],
            'seeds': [seeds],
            'fruitmass': [fruitmass],
            'Row#': [RowNum],
            'clonesize': [clonesize],
            'AverageOfUpperTRange': [AverageOfUpperTRange]
        })
        
        # Realizar la predicción usando el modelo cargado
        prediction = model.predict(data)
        prediction_result = prediction[0]
        
        # Devolver la predicción como respuesta JSON
        return jsonify({'prediccion': prediction_result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
