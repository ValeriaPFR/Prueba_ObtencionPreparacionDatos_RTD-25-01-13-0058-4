# Prueba: Obtención y Preparación de Datos (Pandas)

Este repositorio contiene la resolución de la prueba práctica del módulo, enfocada en la integración, agregación y reestructuración multidimensional de datos organizacionales utilizando la librería **Pandas**[cite: 1].

🔗 **Link del Repositorio:** [https://github.com/ValeriaPFR/Prueba_ObtencionPreparacionDatos_RTD-25-01-13-0058-4.git](https://github.com/ValeriaPFR/Prueba_ObtencionPreparacionDatos_RTD-25-01-13-0058-4.git)

## 📋 Requerimientos de la Evaluación

El desarrollo da cumplimiento estricto a las siguientes tareas técnicas:

1. **Combinación de Datos (Merge):** Unión de los conjuntos de datos independientes de empleados y departamentos mediante un *Left Join* (`df_completo`), asegurando que cada trabajador mantenga la asociación correcta con el nombre y ubicación de su área[cite: 1, 2].
2. **Agrupamiento y Agregación (Groupby):** Agrupación de la información integrada para calcular de forma precisa el salario promedio por cada `nombre_depto` y `ubicacion`[cite: 1, 2].
3. **Pivoteo de Datos (Pivot Table):** Reestructuración de la matriz de datos para generar una tabla pivote final utilizando el departamento como índice, la ubicación geográfica como columnas y los salarios promedio como valores[cite: 1, 2].

## 🛠️ Estructura del Repositorio

* `prueba_pandas.py`: Script principal en Python que contiene la resolución de la prueba (con buenas prácticas PEP 8).
* `08. Prueba - Obtención y preparación de datos.pdf`: Documento con los requerimientos originales de la evaluación[cite: 1].
* `08. Rúbrica Prueba - Obtención y preparación de datos.pdf`: Matriz de evaluación del módulo[cite: 2].
* `Farina_Prueba-ObtencionPreparacionDatos.docx`: Documento editable de respaldo del informe de entrega.
* `Farina_Prueba-ObtencionPreparacionDatos.pdf`: Versión final del informe técnico exportada para revisión.

## ⚙️ Instalación y Ejecución

```bash
pip install pandas numpy
python prueba_pandas.py
