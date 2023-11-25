# Mastodon usage

Project obtained from the article "https://betterprogramming.pub/mastodon-usage-counting-toots-with-kafka-duckdb-seaborn-42215c9488ac" and "https://towardsdatascience.com/introduction-to-kafka-stream-processing-in-python-e30d34bf3a12", adapted for scholar purposes by Jorge Garcia.

[Mastodon](https://joinmastodon.org/) is a _decentralized_ social networking platform. Mastodon users are members of a _specific_ Mastodon server, and servers are capable of joining other servers to form a global (or at least federated) social network.

Tools used
- [Mastodon.py](https://mastodonpy.readthedocs.io/) - Python library for interacting with the Mastodon API
- [Apache Kafka](https://kafka.apache.org/) - distributed event streaming platform.
- [faust-streaming](https://pypi.org/project/faust-streaming/, https://faust.readthedocs.io/en/latest/) - A stream processing library, porting the ideas from Kafka Streams to Python.

## Developer app token
Signing in a Mastodon server is the first thing you should do. You can follow "https://docs.joinmastodon.org/user/signup/" for any further help. Moreover, you should get an app token ("https://docs.joinmastodon.org/client/token/") and include it in 'src/aux/mastodon/token.py'.

# Data collection

## Data streaming

We will use Kafka as distributed stream processing platform to collect data from multiple instances. To run Kafka and schema registry (to support AVRO serialisation) you should execute the following commands with privileges:

```console
 cd config/docker/
 docker-compose up -d
 ```

To stop your Docker environment, run the following command:
```
cd config/docker/
docker-compose stop
```

To stop and remove the Docker environment from your
machine, run the following command:

```
cd config/docker/
docker-compose down --rmi 'all'
```

## Setup virtual python environment
Create a [virtual python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) environment to keep dependencies separate. The _venv_ module is the preferred way to create and manage virtual environments. 

 ```console
python3 -m venv env
```

Before you can start installing or using packages in your virtual environment you’ll need to activate it.

```console
source env/bin/activate
pip install --upgrade pip
pip install -r config/requirements.txt
 ```
 
 If you work on Windows:
```console
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
cd env
.\Scripts\activate
python.exe -m pip install --upgrade pip 
cd ..\config
pip install -r requirements.txt
 ```
 
## Mastodon listener
The python `mastodon_stream` application listens for posts to the specified server (you must have got a token from that mastodon server to get access), and sends each toot to Kafka. You can run multiple Mastodon listeners, each listening to the activity of different servers.

```console
python3 src/mastodon_stream.py --baseURL https://mastodon.world
```

## Testing producer (optional)
As an optional step, you can check in another terminal that AVRO messages are being written to kafka

```console
python src/aux/kafka/kafka_m_consumer.py
```

## Launch speed and batch layers with faust agents
To launch the faust agent in another terminal you should use the following command from the src folder:

```console
cd src
faust -A mastodon_lambda worker -l info
```

Or in Windows if you have any issue with the previous:

```console
python src/mastodon_lambda.py worker
```

# Optional steps

## Cleanup of virtual environment and docker usage

If you want to switch projects or otherwise leave your virtual environment, simply run:

```console
deactivate
```

If you want to re-enter the virtual environment just follow the same instructions above about activating a virtual environment. There’s no need to re-create the virtual environment.

If you want to stop your docker infrastructure, simply run:

```console
cd config/docker/
docker-compose stop
```
