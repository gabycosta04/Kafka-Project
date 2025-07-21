from confluent_kafka import Consumer
import json

TOPIC = "pgserver1.public.clientes"

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group2',
    'auto.offset.reset': 'earliest'  # Cambiá a 'latest' si no querés procesar todo el historial
}

consumer = Consumer(conf)
consumer.subscribe([TOPIC])

print(f"🟢 Escuchando eventos del topic '{TOPIC}'...\n")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        try:
            data = json.loads(msg.value().decode('utf-8'))
            payload = data.get('payload', {})

            before = json.dumps(payload.get('before'), indent=2)
            after = json.dumps(payload.get('after'), indent=2)
            source = json.dumps(payload.get('source'), indent=2)

            print("🔹 EVENTO ---------------------------")
            print(f"🟥 BEFORE:\n{before}")
            print(f"🟩 AFTER:\n{after}")
            print(f"🛰️  SOURCE:\n{source}\n")

        except Exception as e:
            print(f"⚠️  Error procesando mensaje: {e}")
            print("Contenido bruto:", msg.value())

except KeyboardInterrupt:
    print("\n🛑 Detenido por el usuario")

finally:
    consumer.close()
