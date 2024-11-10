from cassandra.cluster import Cluster

class CassandraConfig:
    def __init__(self, nodes=['127.0.0.1']):
        self.cluster = Cluster(nodes)
        self.session = None

    def connect(self, keyspace="pokemon_db"):
        self.session = self.cluster.connect()
        self.session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {keyspace}
        WITH REPLICATION = {{ 'class': 'SimpleStrategy', 'replication_factor': '1' }}
        """)
        self.session.set_keyspace(keyspace)
        return self.session

    def close(self):
        if self.session:
            self.session.shutdown()
        if self.cluster:
            self.cluster.shutdown()
