from confluent_kafka import Consumer
import pandas as pd
from tabulate import tabulate
import os
from shared_data import obtener_dataframe, quitar_evento


def agregar_evento(evento, buffer_path, columns):
    df_nuevo = pd.DataFrame([evento], columns=columns)
    if os.path.exists(buffer_path):
        df_existente = pd.read_csv(buffer_path)
        df_actualizado = pd.concat([df_existente, df_nuevo], ignore_index=True)
    else:
        df_actualizado = df_nuevo
    df_actualizado.to_csv(buffer_path, index=False)

print("⏳ Cargando eventos desde Kafka...")

try:
    while True:
        evento = quitar_evento()
        if evento is None:
            continue  # No hay más mensajes

        try:
            operacion = evento.get('operacion')
            id_ = evento.get('id')
            nombre = evento.get('nombre')
            email = evento.get('email')
            timestamp = evento.get('timestamp')

            if operacion == 'r' or operacion == 'c':
                print(f"🔍 Evento a cargar: ID={id_}, Nombre={nombre}, Email={email}")
                df_nuevo = pd.DataFrame([{
                    "id": id_,
                    "nombre": nombre,
                    "email": email
                }], columns=["id", "nombre", "email"])
                agregar_evento(evento, 'destiny.csv', ["id", "nombre", "email"])

            elif operacion == 'd':
                if os.path.exists('destiny.csv'):
                    df = pd.read_csv('destiny.csv')
                    print(f"🗑️ Evento a eliminar: ID={id_}")
                    df = df[df['id'] != id_] # Descartamos el registro con el ID especificado
                    df.to_csv('destiny.csv', index=False)
            
            elif operacion == 'u':
                if os.path.exists('destiny.csv'):
                    df = pd.read_csv('destiny.csv')
                    print(f"✏️ Evento a actualizar: ID={id_}, Nombre={nombre}, Email={email}")
                    df.loc[df['id'] == id_, ['nombre', 'email']] = [nombre, email]
                    df.to_csv('destiny.csv', index=False)


        except Exception as e:
            print(f"⚠️  Error procesando mensaje: {e}")
            print("📦 RAW:", evento.value())

except KeyboardInterrupt:
    print("\n🛑 Detenido por el usuario.")
