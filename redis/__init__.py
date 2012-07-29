from redis.client import Redis, StrictRedis
from redis.connection import (
    ConnectionPool,
    Connection,
    UnixDomainSocketConnection
    )
from redis.exceptions import (
    AuthenticationError,
    ConnectionError,
    DataError,
    InvalidResponse,
    PubSubError,
    RedisError,
    ResponseError,
    WatchError,
    )


__version__ = '2.4.12'
VERSION = tuple(map(int, __version__.split('.')))
__version__ += '-scripting'
VERSION = VERSION + ('scripting',)

__all__ = [
    'Redis', 'StrictRedis', 'ConnectionPool',
    'Connection', 'UnixDomainSocketConnection',
    'RedisError', 'ConnectionError', 'ResponseError', 'AuthenticationError',
    'InvalidResponse', 'DataError', 'PubSubError', 'WatchError',
    ]
