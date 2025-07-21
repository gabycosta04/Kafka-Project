import pandas as pd
import os
from pandas.errors import EmptyDataError  # esto es para el tema en que se este modificando el archivo y no se pueda leer

BUFFER_PATH = "buffer.csv"
COLUMNAS = ["operacion", "id", "nombre", "email", "timestamp"]

def agregar_evento(evento, buffer_path=BUFFER_PATH, columns=COLUMNAS):
    df_nuevo = pd.DataFrame([evento], columns=COLUMNAS)
    if os.path.exists(BUFFER_PATH):
        df_existente = pd.read_csv(BUFFER_PATH)
        df_actualizado = pd.concat([df_existente, df_nuevo], ignore_index=True)
    else:
        df_actualizado = df_nuevo
    df_actualizado.to_csv(BUFFER_PATH, index=False)

def obtener_dataframe():
    if os.path.exists(BUFFER_PATH):
        return pd.read_csv(BUFFER_PATH)
    else:
        return pd.DataFrame(columns=COLUMNAS)

def limpiar_dataframe():
    if os.path.exists(BUFFER_PATH):
        os.remove(BUFFER_PATH)

def quitar_evento():
    if os.path.exists(BUFFER_PATH):
        try:
            df = pd.read_csv(BUFFER_PATH)
        except EmptyDataError:
            return None  # Si el archivo está vacío, no hay evento que quitar
        if not df.empty:
            evento = df.iloc[0].to_dict()
            df = df.iloc[1:].reset_index(drop=True)
            df.to_csv(BUFFER_PATH, index=False)
            return evento
    return None