# Importar la librería pandas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar archivo CSV
Datos_P = pd.read_csv(r"C:\Users\Admin\Downloads\Python\Datos_Cobertura Movil.csv", sep=';', encoding="utf-8")
print(Datos_P.head()) # Ver las primeras 5 filas
print(Datos_P.tail()) # Ver las últimas 5 filas
print(Datos_P.shape) # Saber cuantas filas y columnas tiene
print(Datos_P.columns) # Ver los nombres de las columnas
print(Datos_P.info()) # Resumen del tipo de datos
print(Datos_P[["NIVEL_SENAL", "AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].describe())
# Estadísticas descriptivas numéricas

# Eliminar ID_DEPARTAMENTO - ID_MUNICIPO - ID_CPOB
Datos_P.drop(columns=['ID_DEPARTAMENTO', "ID_MUNICIPIO", "ID_CPOB"], inplace=True)

# Lista de columnas que necesitas convertir de object a float
columnas = ['AREA_COB_CLARO', 'AREA_COB_MOVISTAR', 'AREA_COB_TIGO', 'AREA_COB_WOM']

# Reemplazar la coma por punto y convertir a float
for col in columnas:
    Datos_P[col] = Datos_P[col].str.replace(',', '.').astype(float) 
    # str.replace(',', '.') convierte "0,1234" en "0.1234"
    # astype(float) cambia el tipo de datos de object a float

# Guardar el archivo sobrescribiéndolo
Datos_P.to_csv(r"C:\Users\Admin\Downloads\Python\Datos_Cobertura Movil_2.csv", index=False, encoding="utf-8")

#
print("DATOS PARA EL ANÁLISIS")
print(Datos_P.head()) # Ver las primeras 5 filas
print(Datos_P.tail()) # Ver las últimas 5 filas
print(Datos_P.shape) # Saber cuantas filas y columnas tiene
print(Datos_P.columns) # Ver los nombres de las columnas
print(Datos_P.info()) # Resumen del tipo de datos
print(Datos_P[["NIVEL_SENAL", "AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].describe()) # Estadísticas descriptivas numéricas

# Verificar la información que quedó
print("Modificación de la base de datos al eliminar ID_DEPARTAMENTO - ID_MUNICIPO - ID_CPOB:")
print(Datos_P.info())
# Volver a colocar los nombres de las columnas
print("Columnas que quedan:")
print(Datos_P.columns)
# Frecuencias absolutas de las variables nominales (cuántas veces aparece cada categoría)
# .value_counts cuenta cuántas veces aparece cada valor en la columna
frecuencias_0 = Datos_P['ANNO'].value_counts()
frecuencias_1 = Datos_P['TRIMESTRE'].value_counts()
frecuencias_2 = Datos_P['DEPARTAMENTO'].value_counts()
frecuencias_3 = Datos_P['MUNICIPIO'].value_counts()
frecuencias_4 = Datos_P['CPOB'].value_counts()
frecuencias_10 = Datos_P['TECNOLOGIA'].value_counts()
# Frecuencia relativa (porcentajes)
# .value_counts cuenta cuántas veces aparece cada valor en la columna
# con el parámetro normalize=True, en lugar de entregar los conteos absolutos, entrega proporciones relativas
# (es decir, frecuencias relativas entre 0 y 1), por ejemplo: 2023= 0.664 y 2024 = 0.336
# * 100 Multiplica esas proporciones por 100 para convertirlas en porcentajes.
porcentajes_0 = Datos_P['ANNO'].value_counts(normalize=True) * 100
porcentajes_1 = Datos_P['TRIMESTRE'].value_counts(normalize=True) * 100
porcentajes_2 = Datos_P['DEPARTAMENTO'].value_counts(normalize=True) * 100
porcentajes_3= Datos_P['MUNICIPIO'].value_counts(normalize=True) * 100
porcentajes_4= Datos_P['CPOB'].value_counts(normalize=True) * 100
porcentajes_10 = Datos_P['TECNOLOGIA'].value_counts(normalize=True) * 100
# Mostrar resultados
print("Frecuencias absolutas:")
print(frecuencias_0)
print(frecuencias_1)
print(frecuencias_2)
print(frecuencias_3)
print(frecuencias_4)
print(frecuencias_10)
# Mostrar resultados en porcentajes
print("Porcentajes:")
print(porcentajes_0.round(2))  # Round(2) Redondea a 2 decimales
print(porcentajes_1.round(2))
print(porcentajes_2.round(2))
print(porcentajes_3.round(2))
print(porcentajes_4.round(2))
print(porcentajes_10.round(2))

# Lista de variables nominales
variables_nominales = ['ANNO', 'TRIMESTRE', 'DEPARTAMENTO', 'CPOB', 'TECNOLOGIA']  
# Para cada variable, generar tabla con Frecuencia y Porcentaje
for var in variables_nominales:
    if var in Datos_P.columns:
        tabla = pd.DataFrame({
            'Frecuencia': Datos_P[var].value_counts(),'Porcentaje (%)': Datos_P[var].value_counts(normalize=True) 
            * 100}).round(2)

        print(f"\n--- {var} ---")
        print(tabla)

# Comparación de cobertura entre los operadores por departamento
print("Estadística bivariada")
Tabla1_bivariada= Datos_P.groupby("DEPARTAMENTO")[["NIVEL_SENAL", "AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].describe()
print(Tabla1_bivariada)
Tabla1_bivariada.to_excel("resumen_por_departamento.xlsx")

# Comparación de cobertura entre los operadores por año
Tabla3_bivariada= Datos_P.groupby("ANNO")[["NIVEL_SENAL", "AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].describe()
print(Tabla3_bivariada)
Tabla3_bivariada.to_excel("resumen_por_año.xlsx")

# Comparación de tecnología entre los departamentos
Tabla4_bivariada= Datos_P.groupby("DEPARTAMENTO")[["TECNOLOGIA"]].value_counts()
print(Tabla4_bivariada)
Tabla5_bivariada= Datos_P.groupby("DEPARTAMENTO")[["TECNOLOGIA"]].value_counts(normalize=True) * 100
print(Tabla5_bivariada)
Tabla5_bivariada.to_excel("resumen_por_departamento_año_Vstecnología.xlsx")

# Comparación de tecnología entre los departamentos por año
Tabla6_bivariada = (
    Datos_P
    .groupby(["ANNO", "DEPARTAMENTO"])["TECNOLOGIA"]
    .value_counts(normalize=True)  # frecuencia relativa
    .mul(100)                      # convertir a porcentaje
    .unstack(fill_value=0))        # columnas por tipo de tecnología

print(Tabla6_bivariada)
Tabla6_bivariada.to_excel("resumen_por_departamento_año_Vs_tecnología.xlsx")

# Tecnología Vs operador
Tabla7_bivariada= Datos_P.groupby("TECNOLOGIA")[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].describe()
print(Tabla7_bivariada)
Tabla7_bivariada.to_excel("resumen_por_tecnología_operador.xlsx")

# Área de cobertura total por operadores
Sumatoria_tigo= sum(Datos_P["AREA_COB_TIGO"])
print(f"Sumatoria tigo: {Sumatoria_tigo}")
Sumatoria_claro= sum(Datos_P["AREA_COB_CLARO"])
print(f"Sumatoria claro: {Sumatoria_claro}")
Sumatoria_movistar= sum(Datos_P["AREA_COB_MOVISTAR"])
print(f"Sumatoria movistar: {Sumatoria_movistar}")
Sumatoria_wom= sum(Datos_P["AREA_COB_WOM"])
print(f"Sumatoria wom: {Sumatoria_wom}")
Sumatoria_señal= sum(Datos_P["NIVEL_SENAL"])
print(f"Sumatoria total señal: {Sumatoria_señal}")

# Área de cobertura total por operadores
Cobertura_total= Datos_P.groupby("TECNOLOGIA")[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum()
print(f"Cobertura total por operador: {Cobertura_total}")
Cobertura_total.to_excel("Cobertura total por operador.xlsx")

# Comparación de nivel de señal por tecnología y departamento
Tabla8_bivariada = (
    Datos_P
    .groupby(["DEPARTAMENTO", "TECNOLOGIA"])["NIVEL_SENAL"]
    .sum()  # Suma 
    .unstack(fill_value=0))        # columnas por tipo de tecnología

print(Tabla8_bivariada)
Tabla8_bivariada.to_excel("resumen_nivel de señal por tecnología y departamento.xlsx")

#####################################
########### Visualización ###########

# Configuración general de estilo
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# **************** 1) Comparación de cobertura entre operadores por departamento ****************
# Crear la columna Cobertura_Total - Suma las áreas de los operadores
Datos_P["Cobertura_Total"] = Datos_P[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum(axis=1)
# Cobertura total por departamento
cobertura_dept = Datos_P.groupby("DEPARTAMENTO")["Cobertura_Total"].sum().sort_values()
# Mejores 5 y peores 5
mejores5_depts = cobertura_dept.tail(5)
peores5_depts = cobertura_dept.head(5)
# Filtrar los datos para incluir solo los departamentos anteriores
cobertura_dept_selec = Datos_P[Datos_P["DEPARTAMENTO"].isin(mejores5_depts.index.union(peores5_depts.index))]
# Calcular la cobertura total por operador en los departamentos seleccionados
cobertura_por_operador = cobertura_dept_selec.groupby("DEPARTAMENTO")[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum()
# Reorganizar  en orden ascendente según su suma total
cobertura_por_operador = cobertura_por_operador.loc[:, cobertura_por_operador.sum().sort_values().index]
# Crear el gráfico 
cobertura_por_operador.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="Spectral")
plt.title("Cobertura por Operador en los Departamentos")
plt.ylabel("Área Cubierta (Km^2)")
plt.xlabel("Departamento")
plt.xticks(rotation=45)
plt.legend(title="Operadores", bbox_to_anchor=(1.05, 1), loc='upper left') # bbox_to_anchor y loc - Ubicación legend
plt.tight_layout()
plt.show()

# **************** 2) Comparación de cobertura entre operadores por año ****************
# Agrupar años y el área de cobertura por opeador
anno_cobertura = Datos_P.groupby("ANNO")[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].mean()
# Seleccionar los 5 mejores y 5 peores de todos los operados por año
anno_cobertura_selec = anno_cobertura.loc[anno_cobertura.mean(axis=1).nlargest(5).index.union(anno_cobertura.mean(axis=1).nsmallest(5).index)]
# Gráfico de líneas
anno_cobertura_selec.plot(kind="line", marker="o")
plt.title("Cobertura Promedio por Operador por Año")
plt.ylabel("Cobertura Promedio (Km^2)")
plt.xlabel("Año")
plt.legend(title="Operadores")
plt.tight_layout()
plt.show()

# **************** 3) Comparación de tecnología entre departamentos por año ****************
# Filtrar los datos para el año 2023 y 2024
Datos_2024 = Datos_P[Datos_P["ANNO"] == 2024]
Datos_2023 = Datos_P[Datos_P["ANNO"] == 2023]
# Calcular área total de cobertura por  operador para el 2024 y 2023
Datos_2024["AREA_TOTAL"] = Datos_2024[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum(axis=1)
Datos_2023["AREA_TOTAL"] = Datos_2023[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum(axis=1)
# Agrupar por departamento - tecnología y sumar las áreas totales
cobertura_tec_2024 = Datos_2024.groupby(["DEPARTAMENTO", "TECNOLOGIA"])["AREA_TOTAL"].sum().unstack(fill_value=0)
cobertura_tec_2023 = Datos_2023.groupby(["DEPARTAMENTO", "TECNOLOGIA"])["AREA_TOTAL"].sum().unstack(fill_value=0)
# Seleccionar los departamentos con mayor y menor cobertura total para el año 2024 y 2023
# ------------2024------------
indices_2024 = cobertura_tec_2024.sum(axis=1).nlargest(5).index.union(cobertura_tec_2024.sum(axis=1).nsmallest(5).index)
cobertura_tec_2024_selec = cobertura_tec_2024.loc[indices_2024]
# ------------2023------------
indices_2023 = cobertura_tec_2023.sum(axis=1).nlargest(5).index.union(cobertura_tec_2023.sum(axis=1).nsmallest(5).index)
cobertura_tec_2023_selec = cobertura_tec_2023.loc[indices_2023]
# Heatmap para el año 2024
# cbar_kws para personalizar la barra de color y fmt (format string) para mostrar decimales
sns.heatmap(cobertura_tec_2024_selec, cmap="YlGnBu", annot=True, fmt=".1f", cbar_kws={'label': 'Área Total Cubierta (Km²)'})
plt.title("Adopción de Tecnología por Departamento (Año 2024)")
plt.xlabel("Tecnología")
plt.ylabel("Departamento")
plt.tight_layout()
plt.show()
# Heatmap para el año 2024
sns.heatmap(cobertura_tec_2023_selec, cmap="YlGnBu", annot=True, fmt=".1f", cbar_kws={'label': 'Área Total Cubierta (Km²)'})
plt.title("Adopción de Tecnología por Departamento (Año 2023)")
plt.xlabel("Tecnología")
plt.ylabel("Departamento")
plt.tight_layout()
plt.show()

# **************** 4) Tecnología vs Operador ****************
# Calcular área total de cobertura por tecnología y operador
tecno_operador = Datos_P.groupby("TECNOLOGIA")[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum()
# Calcular la suma total del área cubierta por tecnología
tecno_operador["TOTAL_AREA"] = tecno_operador.sum(axis=1)
# Seleccionar las 5 tecnologías con mayor y menor área de cobertura
mejores5_tecno_operador = tecno_operador.nlargest(5, "TOTAL_AREA")
peores5_tecno_operador = tecno_operador.nsmallest(5, "TOTAL_AREA")
# Eliminar duplicados y unir
tecno_operador_selec = pd.concat([mejores5_tecno_operador, peores5_tecno_operador]).drop_duplicates()
# Eliminar la columna TOTAL_AREA para el gráfico
tecno_operador_selec = tecno_operador_selec.drop(columns=["TOTAL_AREA"])
# Gráfico de barras agrupadas
tecno_operador_selec.plot(kind="bar", stacked=False, figsize=(10, 6))
plt.title("Área de Cobertura por Tecnología y Operador")
plt.ylabel("Área Cubierta (Km^2)")
plt.xlabel("Tecnología")
plt.xticks(rotation=45)
plt.legend(title="Operadores", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# **************** 5) Comparación de nivel de señal por tecnología y departamento ****************
# Agrupar el departamento y la tecnología según el nivel de señal
senal_tecno_dpto = Datos_P.groupby(["DEPARTAMENTO", "TECNOLOGIA"])["NIVEL_SENAL"].sum().unstack(fill_value=0)
# Seleccionar las 5 mejores y peores niveles de señal
mejores5_senal = senal_tecno_dpto.sum(axis=1).nlargest(5)
peores5_senal = senal_tecno_dpto.sum(axis=1).nsmallest(5)
# Filtrar solo las anterires
senal_tecno_dpto_selec = senal_tecno_dpto.loc[mejores5_senal.index.union(peores5_senal.index)]
# Gráfico Heatmap
sns.heatmap(senal_tecno_dpto_selec, cmap="Spectral", annot=True, fmt=".0f", cbar_kws={'label': 'Nivel de Señal'})
plt.title("Nivel de Señal por Tecnología y Departamento")
plt.xlabel("Tecnología")
plt.ylabel("Departamento")
plt.tight_layout()
plt.show()

# **************** 6) Área de cobertura total por operadores ****************
# Calcular área de cobertura total para cada opeador
cobertura_operador = Datos_P[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].sum()
# Gráfico circular
cobertura_operador.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["skyblue", "orange", "green", "pink"])
plt.title("Distribución de Área Total por Operador")
plt.ylabel("") 
plt.tight_layout()
plt.show()

"""
#### Mirar si si es necesaria
# Plot stacked bar chart -- Sorted
# Ordenar las columnas (tecnologías) por la sumatoria total ascendente
Tabla8_bivariada = Tabla8_bivariada.loc[:, Tabla8_bivariada.sum().sort_values().index]
                                        
Tabla8_bivariada.plot(kind='bar', stacked=False, figsize=(14,8))
plt.xlabel('Departamento')
plt.ylabel('Sumatoria NIVEL_SENAL')
plt.title('Sumatoria de NIVEL_SENAL por Tecnología y Departamento')
plt.legend(title='Tecnología')
plt.tight_layout()
plt.show()

####
# Crear una copia de las columnas relevantes
datos_areas = Datos_P[["ANNO", "AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]]
# Reemplazar los valores 0 con NaN para que no sean considerados en el promedio
datos_areas = datos_areas.replace(0, np.nan)
# Agrupar años y calcular el promedio ignorando valores NaN
anno_cobertura = datos_areas.groupby("ANNO")[["AREA_COB_CLARO", "AREA_COB_MOVISTAR", "AREA_COB_TIGO", "AREA_COB_WOM"]].mean()
# Seleccionar los 5 mejores y 5 peores años según la cobertura promedio total
anno_cobertura_selec = anno_cobertura.loc[anno_cobertura.mean(axis=1).nlargest(5).index.union(anno_cobertura.mean(axis=1).nsmallest(5).index)]
# Gráfico de líneas
anno_cobertura_selec.plot(kind="line", marker="o")
plt.title("Cobertura Promedio por Operador por Año (Excluyendo Valores Igual a 0)")
plt.ylabel("Cobertura Promedio (Km^2)")
plt.xlabel("Año")
plt.legend(title="Operadores")
plt.tight_layout()
plt.show()

"""