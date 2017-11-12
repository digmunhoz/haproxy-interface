#! /usr/bin/python

from haproxyadmin import haproxy
import config
import json

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

def main():
    frontend()

def frontend():
    frontends = hap.frontends()
    lst = {'frontend': [] } 
    for frontend in frontends:
        lst['frontend'].append(frontend.name)
    print(json.dumps(lst))

if __name__ == '__main__':
    main()
