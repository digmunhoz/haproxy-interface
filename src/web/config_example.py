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
	INFO = '/api/v1/info',
	SERVERS = '/api/v1/servers',
	BACKENDS = '/api/v1/backends',
	FRONTENDS = '/api/v1/frontends',
	ERRORS = '/api/v1/errors',
	HARDWARE = '/api/v1/hardware',
)

connection_timeout = 3
