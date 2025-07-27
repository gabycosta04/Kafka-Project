# 🔄 Data Streaming with Kafka: MySQL → Debezium → Kafka → Python → CSV

Este proyecto implementa un pipeline de datos en tiempo real utilizando tecnologías modernas de captura de cambios (CDC) para extraer y almacenar datos actualizados desde una base de datos MySQL hacia archivos CSV (enviados y transformados en Python) para posterior análisis o integración.

---

## 📌 Objetivo

Diseñar un flujo de procesamiento en tiempo real que:
- Detecte cambios en una tabla de MySQL (inserts, updates, deletes)
- Capture esos eventos utilizando el conector de Debezium
- Transmita los eventos a través del topico definido en Apache Kafka
- Consuma los datos con Python
- Almacene los resultados en un archivo `CSV` con formato estructurado

---

## 🧱 Arquitectura general

```plaintext
   +--------+       +-------------+       +--------+       +--------+       +-----------+
   | MySQL  | <---> | Debezium    | <---> | Kafka  | <---> | Python | --->  | CSV final |
   +--------+       +-------------+       +--------+       +--------+       +-----------+
     Fuente         CDC Connector        Mensajería       Consumidor        Almacenamiento

   +--------+       +-------------+       +--------+       +--------+       +-----------+
   | MySQL  | <---> | Debezium    | <---> | Kafka  | <---> | Python | --->  | CSV final |
   +--------+       +-------------+       +--------+       +--------+       +-----------+
     Fuente         CDC Connector        Mensajería       Consumidor        Almacenamiento
```

![Arquitectura del pipeline](img/Arquitectura_de_datos.png)
