import pandas as pd
import numpy as np 

# =============================================================================
# CONFIGURACIÓN DE LOS DATOS DE ORIGEN (Corrección de sintaxis del enunciado)
# =============================================================================

# DataFrame con información de empleados
data_empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106, 107, 108],
    'nombre': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Elena', 'Pedro', 'Laura', 'David'],
    'salario': [55000, 58000, 72000, 48000, 75000, 85000, 62000, 88000],
    'id_departamento': ['V_01', 'V_01', 'T_01', 'M_01', 'T_01', 'D_01', 'M_01', 'D_01']
}
df_empleados = pd.DataFrame(data_empleados)

# DataFrame con información de departamentos
data_departamentos = {
    'id_departamento': ['V_01', 'T_01', 'M_01', 'D_01'],
    'nombre_depto': ['Ventas', 'Tecnología', 'Marketing', 'Dirección'],
    'ubicacion': ['Norte', 'Sur', 'Norte', 'Norte']
}
df_departamentos = pd.DataFrame(data_departamentos)


# =============================================================================
# REQUERIMIENTO 1: Combinación de Datos (Merge)
# =============================================================================
print("=" * 65)
print("          REPORTE DE RECURSOS HUMANOS: ANÁLISIS SALARIAL          ")
print("=" * 65)

# Unimos los DataFrames usando como llave 'id_departamento' mediante un Left Join
df_completo = pd.merge(df_empleados, df_departamentos, on='id_departamento', how='left')

print("[REQUERIMIENTO 1] DataFrame Combinado ('df_completo'):")
print(df_completo.to_string(index=False))
print("-" * 65)


# =============================================================================
# REQUERIMIENTO 2: Agrupamiento y Agregación (Groupby)
# =============================================================================
print("\n[REQUERIMIENTO 2] Salario Promedio por Departamento y Ubicación:")

# Agrupamos por departamento y ubicación calculando la media del salario
df_agrupado = df_completo.groupby(['nombre_depto', 'ubicacion'])['salario'].mean().reset_index()

# Renombramos la columna resultante para mayor claridad
df_agrupado.rename(columns={'salario': 'salario_promedio'}, inplace=True)

print(df_agrupado.to_string(index=False))
print("-" * 65)


# =============================================================================
# REQUERIMIENTO 3: Pivoteo de Datos (Pivot Table)
# =============================================================================
print("\n[REQUERIMIENTO 3] Tabla Pivote Final para Comparación Directa:")

# Reestructuramos la información cruzando departamentos (índice) y ubicaciones (columnas)
df_pivote = df_agrupado.pivot(index='nombre_depto', columns='ubicacion', values='salario_promedio')

# Reemplazamos los valores nulos (NaN) por un guion para mejorar la presentación visual
df_pivote_presentacion = df_pivote.fillna('-')

print(df_pivote_presentacion)
print("=" * 65)