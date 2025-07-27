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
```

![Arquitectura de datos](img/Arquitectura_de_datos.png)

## ⚙️ Tecnologías utilizadas
- Docker: Orquestación de contenedores
  - 📦 Descargar Docker Desktop (Windows/Mac):https://www.docker.com/products/docker-desktop/
  - Para comprobar la version de docker y que este instalado:
```bash
     docker --version
     docker compose version
```
- MySQL: Base de datos origen
- Debezium: Conector que permite la captura de datos en tiempo real (CDC)
- Apache Kafka: Cola de eventos distribuida
- Kafka Connect: Framework para conectar Debezium a Kafka
- Python (utilizando las libs: confluent-kafka, pandas, tabulate): consumidor de eventos provenientes del Kafka y almacenamiento en CSV
- Shell y jq: Para debug y parseo de eventos por medio de la terminal