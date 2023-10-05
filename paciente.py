#paciente.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Paciente:
    def __init__(self, nombre, cedula, genero, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.genero = genero
        self.edad = edad
        self.examenes_eeg = None
        self.examenes_ecg = None

    def cargar_examenes_eeg(self, datos_eeg):
        self.examenes_eeg = pd.DataFrame(datos_eeg)

    def cargar_examenes_ecg(self, datos_ecg):
        self.examenes_ecg = pd.DataFrame(datos_ecg)

    def graficar_eeg(self, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False, cuadricula=False):
        if self.examenes_eeg is not None:
            # Realizar operaciones a lo largo de un eje (por ejemplo, promedio)
            promedio_eeg = self.examenes_eeg.mean(axis=1)
            
            plt.ion()  # Habilitar el modo interactivo de matplotlib
            plt.figure()
            plt.plot(promedio_eeg)
            plt.title(titulo)
            plt.xlabel(etiqueta_x)
            plt.ylabel(etiqueta_y)
            
            if leyenda:
                plt.legend(["Promedio EEG"])
            
            if cuadricula:
                plt.grid()
            
            plt.show()
        else:
            print("No se han cargado exámenes EEG.")

    def graficar_ecg(self, titulo="", etiqueta_x="", etiqueta_y="", leyenda=False, cuadricula=False):
        if self.examenes_ecg is not None:
            # Realizar operaciones a lo largo de un eje (por ejemplo, promedio)
            promedio_ecg = self.examenes_ecg.mean(axis=1)
            
            plt.ion()  # Habilitar el modo interactivo de matplotlib
            plt.figure()
            plt.plot(promedio_ecg)
            plt.title(titulo)
            plt.xlabel(etiqueta_x)
            plt.ylabel(etiqueta_y)
            
            if leyenda:
                plt.legend(["Promedio ECG"])
            
            if cuadricula:
                plt.grid()
            
            plt.show()
        else:
            print("No se han cargado exámenes ECG.")

    def calcular_estadisticos_eeg(self):
        if self.examenes_eeg is not None:
            # Calcular estadísticas descriptivas de los exámenes EEG
            estadisticos_eeg = self.examenes_eeg.describe()
            return estadisticos_eeg
        else:
            print("No se han cargado exámenes EEG.")
            return None

    def calcular_estadisticos_ecg(self):
        if self.examenes_ecg is not None:
            # Calcular estadísticas descriptivas de los exámenes ECG
            estadisticos_ecg = self.examenes_ecg.describe()
            return estadisticos_ecg
        else:
            print("No se han cargado exámenes ECG.")
            return None
