from paciente import Paciente
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat1


def menu():
    print("\nMenú:")
    print("1. Crear paciente")
    print("2. Cargar exámenes EEG")
    print("3. Cargar exámenes ECG")
    print("4. Graficar EEG")
    print("5. Graficar ECG")
    print("6. Calcular estadísticas EEG")
    print("7. Calcular estadísticas ECG")
    print("8. Salir")

def main():
    paciente_actual = None

    while True:
        menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            cedula = input("Cédula del paciente: ")
            genero = input("Género del paciente: ")
            edad = int(input("Edad del paciente: "))
            paciente_actual = Paciente(nombre, cedula, genero, edad)
            print(f"Paciente {nombre} creado.")

        elif opcion == "2":
            if paciente_actual is not None:
                # Cargar exámenes EEG desde archivo CSV
                archivo_eeg = input("Ingrese la ruta del archivo CSV para los exámenes EEG: ")
                try:
                    datos_eeg = pd.read_csv(archivo_eeg)
                    paciente_actual.cargar_examenes_eeg(datos_eeg)
                    print("Exámenes EEG cargados desde archivo CSV.")
                except FileNotFoundError:
                    print(f"El archivo {archivo_eeg} no se encuentra en la ruta especificada.")
            else:
                print("Primero debe crear un paciente.")

        elif opcion == "3":
            if paciente_actual is not None:
                # Cargar exámenes ECG desde archivo CSV
                archivo_ecg = input("Ingrese la ruta del archivo CSV para los exámenes ECG: ")
                try:
                    datos_ecg = pd.read_csv(archivo_ecg)
                    paciente_actual.cargar_examenes_ecg(datos_ecg)
                    print("Exámenes ECG cargados desde archivo CSV.")
                except FileNotFoundError:
                    print(f"El archivo {archivo_ecg} no se encuentra en la ruta especificada.")
            else:
                print("Primero debe crear un paciente.")

        elif opcion == "4":
            if paciente_actual is not None:
                paciente_actual.graficar_eeg("Promedio EEG", "Tiempo", "Amplitud", True, True)
            else:
                print("Primero debe crear un paciente.")

        elif opcion == "5":
            if paciente_actual is not None:
                paciente_actual.graficar_ecg("Promedio ECG", "Tiempo", "Amplitud", True, True)
            else:
                print("Primero debe crear un paciente.")

        elif opcion == "6":
            if paciente_actual is not None:
                estadisticos_eeg = paciente_actual.calcular_estadisticos_eeg()
                print("Estadísticas EEG:")
                print(estadisticos_eeg)
            else:
                print("Primero debe crear un paciente.")

        elif opcion == "7":
            if paciente_actual is not None:
                estadisticos_ecg = paciente_actual.calcular_estadisticos_ecg()
                print("Estadísticas ECG:")
                print(estadisticos_ecg)
            else:
                print("Primero debe crear un paciente.")

        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")

if __name__ == "__main__":
    main()
