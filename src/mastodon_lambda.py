from collections import defaultdict
from datetime import datetime
import faust
from faust import Schema, Stream
from faust_avro_serializer import FaustAvroSerializer
from schema_registry.client import SchemaRegistryClient
from aux.faust.models import Message, Toot


MODEL_BATCH_IN_SECONDS = 100.0

KAFKA_BOOTSTRAP_SERVER = 'kafka://localhost:9092'
SCHEMA_REGISTRY_URL = 'http://localhost:8081'
APP_NAME = 'lambda-' + str(datetime.timestamp(datetime.now()))
FROM_TOPIC = 'mastodon-topic'

app = faust.App(APP_NAME, broker=KAFKA_BOOTSTRAP_SERVER)

schema_client = SchemaRegistryClient(SCHEMA_REGISTRY_URL)
serializer = FaustAvroSerializer(schema_client, FROM_TOPIC, False)
schema_with_avro = Schema(key_serializer=str, value_serializer=serializer)
topic = app.topic(FROM_TOPIC, schema=schema_with_avro)
channel = app.channel()

#TODO 2.0: Definir modelos

# speed layer
#TODO 2.0: Generar capa de velocidad            


# batch layer
#TODO 3.0: Generar capa de batch


# service layer
#TODO 4.0: Generar capa de servicio.


if __name__=='__main__':
    app.main()
