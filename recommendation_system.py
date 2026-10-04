# recommendation_system.py
# Sistema de recomendación de productos con KNN (K vecinos más cercanos)

# Importar las librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

FEATURES = ['feature1', 'feature2', 'feature3']

# Cargar los datos (dataset de productos incluido en el repositorio)
data = pd.read_csv('products.csv')

# Preprocesamiento de datos: seleccionar las características y la etiqueta
features = data[FEATURES]
labels = data['label']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# Crear y entrenar el modelo
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')


# Función de recomendación
def recommend(product_features):
    """Recibe [feature1, feature2, feature3] y devuelve el producto recomendado."""
    entrada = pd.DataFrame([product_features], columns=FEATURES)
    prediction = model.predict(entrada)
    return prediction[0]


# Ejemplo de uso de la función de recomendación
example_product = [1.0, 2.0, 3.0]
recommended_product = recommend(example_product)
print(f'Recommended Product: {recommended_product}')
