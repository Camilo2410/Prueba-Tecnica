import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Cargar los datos
data = pd.read_excel('data_customer_classification.xlsx', engine='openpyxl')

# Preprocesamiento de los datos
data['trans_date'] = pd.to_datetime(data['trans_date'])
customer_features = data.groupby('customer_id').agg(
    frequency=('tran_amount', 'count'),
    total_spent=('tran_amount', 'sum'),
    max_spent=('tran_amount', 'max'),
    last_purchase=('trans_date', 'max')
)
most_recent_purchase = data['trans_date'].max()
customer_features['recency'] = (most_recent_purchase - customer_features['last_purchase']).dt.days
customer_features['value_category'] = pd.qcut(customer_features['total_spent'], 3, labels=['low', 'medium', 'high'])

# Preparar los datos para el modelo
X = customer_features[['frequency', 'total_spent', 'max_spent', 'recency']]
y = customer_features['value_category']
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
y_dummy = to_categorical(y_encoded)

# Escalado de características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_dummy, test_size=0.2, random_state=42)

# Creación del modelo
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compilación del modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamiento del modelo
model.fit(X_train, y_train, epochs=50, batch_size=10)

# Evaluación del modelo
loss, accuracy = model.evaluate(X_test, y_test)
print('Accuracy:', accuracy)


# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# Reducción de dimensionalidad con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Explicar la varianza en términos porcentuales
explained_variance = pca.explained_variance_ratio_

# Predecir las categorías utilizando el modelo entrenado
y_pred = model.predict(X_scaled)
y_pred_classes = y_pred.argmax(axis=1)

# Crear un mapa de colores para las categorías
colors = ['purple', 'yellow', 'green']
category_labels = ['Bajo', 'Medio', 'Alto']
color_map = {category: color for category, color in zip(range(3), colors)}

# Graficar los resultados
plt.figure(figsize=(10, 8))
for category, color in color_map.items():
    idx = y_pred_classes == category
    plt.scatter(X_pca[idx, 0], X_pca[idx, 1], c=color, label=category_labels[category], alpha=0.5)

plt.title('Visualización de la clasificación de clientes')
plt.xlabel(f'Componente Principal 1 (Varianza Explicada: {explained_variance[0]:.2%})')
plt.ylabel(f'Componente Principal 2 (Varianza Explicada: {explained_variance[1]:.2%})')
plt.legend()
plt.show()

# Guardar el modelo
model.save('customer_value_model.h5')
