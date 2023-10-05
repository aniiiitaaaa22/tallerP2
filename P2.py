import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Paso 1: Crear una matriz Numpy aleatoria de 3 dimensiones con un tamaño de 11520000
shape = (120, 160, 600)  # Establecemos las dimensiones
matriz_numpy = np.random.rand(*shape)  # Creamos una matriz aleatoria

# Paso 2: Crear una copia de la matriz creada en el ítem anterior
copia_matriz_numpy = matriz_numpy.copy()

# Paso 3: Mostrar todos los atributos propios de la matriz (dimensiones, tamaño, etc.)
print("Atributos de la matriz original:")
print("Forma (shape):", matriz_numpy.shape)
print("Número de dimensiones:", matriz_numpy.ndim)
print("Tamaño (size):", matriz_numpy.size)
print("Tipo de datos:", matriz_numpy.dtype)

# Paso 4: Modificar su forma y pasarla a 2D
matriz_numpy_2d = matriz_numpy.reshape(-1, shape[2])  # Convertir a una matriz 2D

# Función para graficar una señal
def graficar_senal(matriz, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False, cuadricula=False):
    plt.figure()
    plt.plot(matriz)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    if leyenda:
        plt.legend(["Señal"])
    
    if cuadricula:
        plt.grid()
    
    plt.show()

# Función para graficar un histograma
def graficar_histograma(matriz, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False, cuadricula=False):
    plt.figure()
    plt.hist(matriz, bins=30)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    if leyenda:
        plt.legend(["Histograma"])
    
    if cuadricula:
        plt.grid()
    
    plt.show()

# Función para graficar stems
def graficar_stems(matriz, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False, cuadricula=False):
    plt.figure()
    plt.stem(matriz)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    if leyenda:
        plt.legend(["Stems"])
    
    if cuadricula:
        plt.grid()
    
    plt.show()

# Función para graficar barras
def graficar_barras(matriz, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False, cuadricula=False):
    plt.figure()
    plt.bar(range(len(matriz)), matriz)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    if leyenda:
        plt.legend(["Barras"])
    
    if cuadricula:
        plt.grid()
    
    plt.show()

# Función para graficar un gráfico de pastel
def graficar_pie(matriz, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False):
    plt.figure()
    plt.pie(matriz, labels=range(len(matriz)))
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    if leyenda:
        plt.legend(["Pie Chart"])
    
    plt.show()

# Pedir al usuario los parámetros para la graficación
titulo = input("Ingrese el título del gráfico: ")
etiqueta_x = input("Ingrese la etiqueta del eje x: ")
etiqueta_y = input("Ingrese la etiqueta del eje y: ")
leyenda = input("¿Activar leyenda? (Sí/No): ").lower() == "si"
cuadricula = input("¿Activar cuadrícula? (Sí/No): ").lower() == "si"

# Pedir al usuario el tipo de gráfico a crear
print("Seleccione el tipo de gráfico:")
print("1. Señal")
print("2. Histograma")
print("3. Stems")
print("4. Barras")
print("5. Gráfico de Pastel")
opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    graficar_senal(matriz_numpy_2d, titulo, etiqueta_x, etiqueta_y, leyenda, cuadricula)
elif opcion == 2:
    graficar_histograma(matriz_numpy_2d, titulo, etiqueta_x, etiqueta_y, leyenda, cuadricula)
elif opcion == 3:
    graficar_stems(matriz_numpy_2d, titulo, etiqueta_x, etiqueta_y, leyenda, cuadricula)
elif opcion == 4:
    graficar_barras(matriz_numpy_2d, titulo, etiqueta_x, etiqueta_y, leyenda, cuadricula)
elif opcion == 5:
    graficar_pie(matriz_numpy_2d[0], titulo, etiqueta_x, etiqueta_y, leyenda)
else:
    print("Opción no válida.")

# Paso 5: Crear una función que convierta la matriz a un DataFrame de Pandas
def matriz_a_dataframe(matriz):
    # Crear un DataFrame de Pandas
    df = pd.DataFrame(matriz)
    return df

# Llamar a la función para convertir la matriz 2D a un DataFrame
dataframe_resultante = matriz_a_dataframe(matriz_numpy_2d)

# Mostrar las primeras filas del DataFrame
print("\nDataFrame resultante:")
print(dataframe_resultante.head())

# Función para cargar archivos .mat
def cargar_matriz(mat_file):
    data = loadmat(mat_file)
    return data

# Función para cargar archivos .csv
def cargar_csv(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Función para realizar operaciones a lo largo de un eje utilizando NumPy
def operacion_a_lo_largo_de_eje(arr, operacion, eje=0):
    if operacion == 'suma':
        return np.sum(arr, axis=eje)
    elif operacion == 'resta':
        return np.subtract(arr, np.mean(arr, axis=eje, keepdims=True))
    elif operacion == 'multiplicacion':
        return np.prod(arr, axis=eje)
    elif operacion == 'division':
        return np.divide(arr, np.mean(arr, axis=eje, keepdims=True))
    elif operacion == 'logaritmo':
        return np.log(arr)
    elif operacion == 'promedio':
        return np.mean(arr, axis=eje)
    elif operacion == 'desviacion_estandar':
        return np.std(arr, axis=eje)
    else:
        return None

# Función para cargar un archivo .csv y permitir al usuario seleccionar columnas
def cargar_csv_y_seleccionar_columnas(csv_file):
    # Cargar el archivo CSV en un DataFrame
    dataframe = pd.read_csv(csv_file)
    
    # Mostrar las columnas disponibles para que el usuario elija
    print("Columnas disponibles:")
    for idx, columna in enumerate(dataframe.columns):
        print(f"{idx}: {columna}")
    
    # Pedir al usuario que seleccione las columnas
    seleccionadas = input("Ingrese el número de las columnas separadas por comas (ejemplo: 0,1): ")
    columnas_seleccionadas = [int(idx) for idx in seleccionadas.split(',')]
    
    return dataframe, columnas_seleccionadas

# Función para realizar operaciones a lo largo de columnas seleccionadas
def operacion_a_lo_largo_de_columnas(dataframe, columnas, operacion):
    if operacion == 'suma':
        resultado = dataframe.iloc[:, columnas].sum()
    elif operacion == 'resta':
        resultado = dataframe.iloc[:, columnas].subtract(dataframe.iloc[:, columnas].mean())
    elif operacion == 'multiplicacion':
        resultado = dataframe.iloc[:, columnas].prod()
    elif operacion == 'division':
        resultado = dataframe.iloc[:, columnas].div(dataframe.iloc[:, columnas].mean())
    elif operacion == 'logaritmo':
        resultado = dataframe.iloc[:, columnas].apply(lambda x: x.apply(lambda y: np.log(y) if y > 0 else np.nan))
    elif operacion == 'promedio':
        resultado = dataframe.iloc[:, columnas].mean()
    elif operacion == 'desviacion_estandar':
        resultado = dataframe.iloc[:, columnas].std()
    else:
        resultado = None
    return resultado
