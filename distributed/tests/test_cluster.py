from distributed.cluster import Cluster
from distributed.core import connect_sync, read_sync, write_sync


def test_cluster():
    with Cluster('127.0.0.1', ['127.0.0.1', '127.0.0.1']) as c:
        stream = connect_sync('127.0.0.1', 8787)
        result = []
        while len(result) != 2:
            write_sync(stream, {'op': 'ncores'})
            result = read_sync(stream)

        c.add_worker('127.0.0.1')

        while len(result) != 3:
            write_sync(stream, {'op': 'ncores'})
            result = read_sync(stream)
