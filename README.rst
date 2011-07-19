A simple django app that responds to heartbeat polls.  

In a cluster of load-balanced web servers, this allows you to take a server out of service gracefully, by letting your load balancer know that the server is going down before shutting down.

To implement, add 'heartbeat' to INSTALLED_APPS in your Django settings file.

A control file is used for signalling.  Use the following setting in your Django settings file to specify the path for the control file:

  HEARTBEAT_FILENAME = '/etc/heartbeat'

If this file exists and contains a 0, heartbeat will respond with a 503 to let a load balancer know to stop sending new requests to the server because the server is going down for maintenance.  

To set, use eg: 
  $ echo 0 > etc/heartbeat

Or you can use the Django management commands:
  $ bin/django heartbeat down
  $ bin/django heartbeat up

Used with HAProxy, your HAProxy config file might contain this:

    backend site
        balance roundrobin
        option httpchk HEAD /heartbeat/status/ HTTP/1.0
        option httpclose
        server web-appserver-A-1 10.0.2.2:80 check inter 5000
        server web-appserver-A-2 10.0.2.3:80 check inter 5000
        server web-appserver-A-3 10.0.2.4:80 check inter 5000
        server web-appserver-B-1 10.0.5.2:80 check inter 5000
        server web-appserver-B-2 10.0.5.3:80 check inter 5000
        server web-appserver-B-3 10.0.5.4:80 check inter 5000


