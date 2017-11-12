haproxy_socket = dict(
    DIR = '/tmp',
    FILE = 'stats',
)

server_listen = dict (
    ADDRESS = '0.0.0.0',
    PORT = '5000',
)

api_server = dict (
    ADDRESS = 'haproxy',
    PORT = '5001',
)

connection_timeout = 3
