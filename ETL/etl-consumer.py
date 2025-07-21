from confluent_kafka import Consumer
import pandas as pd
import json
from datetime import datetime
from tabulate import tabulate

TOPIC = "pgserver1.public.clientes"
group_id = f"python-consumer-{datetime.now().strftime('%Y%m%d%H%M%S')}"

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': group_id,
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe([TOPIC]) #aca tenemos los mensajes a consumir, donde nos suscribimos a un topic especifico

eventos = []

print("⏳ Cargando eventos desde Kafka...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue  # No hay más mensajes
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        try:
            data = json.loads(msg.value().decode('utf-8'))
            payload = data.get("payload", {})

            op = payload.get("op")
            ts_ms = payload.get("ts_ms")

            registro = payload.get("after") or payload.get("before") or {}
            

            eventos.append({
                "operacion": op,
                "id": registro.get("id"),
                "nombre": registro.get("nombre"),
                "email": registro.get("email"),
                "timestamp": datetime.fromtimestamp(ts_ms / 1000.0) if ts_ms else None
            })

            df = pd.DataFrame(eventos)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            print(tabulate(df.tail(1), headers='keys', tablefmt='fancy_grid', showindex=False))


        except Exception as e:
            print(f"⚠️  Error procesando mensaje: {e}")
            print("📦 RAW:", msg.value())

except KeyboardInterrupt:
    print("\n🛑 Detenido por el usuario.")

finally:
    consumer.close()
