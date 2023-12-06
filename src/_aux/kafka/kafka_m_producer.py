from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro

# Función que devuelve un AvroProducer, el cuál se conecta
# a un servidor Kafka, y permite devolver un mensaje, con un estándar
# dado (que sería Avro).
def kafka_m_producer(topic):
    # Configuración que utilizará el Producer para la conexión
    producer_config = {
        'bootstrap.servers': 'localhost:9092',
        'schema.registry.url': 'http://localhost:8081', 
        'broker.address.family': 'v4'
    }
    #TODO 1.0: Cargar datos de schema avro.
    # Esquema según el estándar Avro, que siguen los mensajes que se almacenan.
    # El archivo contiene una descripción de dicho estándar.
    schema = avro.load("./config/avro/mastodon-topic-value.avsc")
    return AvroProducer(config=producer_config, default_value_schema=schema)
