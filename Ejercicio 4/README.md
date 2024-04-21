# Solución de Clasificación de Clientes para Campañas de Marketing Personalizadas

Este proyecto contiene un modelo de clasificación desarrollado con Keras que categoriza a los clientes de una tienda de comestibles en tres valores: bajo, medio y alto, basándose en su frecuencia de compras, hábitos de gasto y el monto máximo que gastan en la tienda. El objetivo es permitir al supermercado conocer mejor a sus clientes para crear campañas de marketing personalizadas.

## Instrucciones para Configurar y Ejecutar la Solución

### Requisitos Previos

Antes de ejecutar el script, asegúrese de tener instalado Python 3.7 o superior. Además, deberá instalar las siguientes bibliotecas de Python:

- `pandas`
- `numpy`
- `tensorflow`
- `keras`
- `scikit-learn`
- `matplotlib`
- `openpyxl`

Puede instalar todas las bibliotecas necesarias ejecutando el siguiente comando:

```bash
pip install pandas numpy tensorflow keras scikit-learn matplotlib openpyxl
```
## Ejecución del Modelo Principal

1. **Modelo y Script de Predicción**:
   - El script principal `solucion.py` contiene el código para entrenar el modelo de clasificación y realizar predicciones.
   - El modelo se guarda automáticamente en el directorio actual con el nombre `customer_value_model.h5` después de la ejecución del script.

2. **Visualización de la Clasificación**:
   - Al final del entrenamiento, el script generará una gráfica visualizando cómo el modelo ha clasificado a los clientes en los tres grupos diferentes. Esta visualización aparecerá automáticamente si se ejecuta el script completo.
