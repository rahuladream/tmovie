


# For Mac
```
$ brew install rabbitmq
$ export PATH=$PATH:/usr/local/sbin
```
# Start server (Mac)
```
$ sudo rabbitmq-server -detached #-detached flag indicates the server to run in the background
```
# To stop server
```
sudo rabbitmqctl stop

#Add user settings (optional)
$ sudo rabbitmq-server -detached
$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
```


# For Ubuntu
```
$ apt-get install -y erlang
$ apt-get install rabbitmq-server

# Then enable and start the RabbitMQ service:
$ systemctl enable rabbitmq-server
$ systemctl start rabbitmq-server
```

# Check rabbitmq server status
```
$ systemctl status rabbitmq-server​
```



# Celery beat server start
```
celery -A tmovie worker -l info -B
```