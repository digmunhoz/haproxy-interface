server_listen = dict (
    ADDRESS = '0.0.0.0',
    PORT = '5000',
)

api_server = dict (
    ADDRESS = 'haproxy',
    PORT = '5001',
)

# Use external address because the request will be made by your browsers
ajax_api = dict (
    ADDRESS = 'localhost',
    PORT = '5001',	
)

api_endpoint = dict (
	INFO = '/api/info',
	SERVERS = '/api/servers',
	BACKENDS = '/api/backends',
	FRONTENDS = '/api/frontends',
	ERRORS = '/api/errors',
	HARDWARE = '/api/hardware',
)

connection_timeout = 3
