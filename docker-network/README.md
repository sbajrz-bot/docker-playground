# docker-nginx-hello-world
Single page docker nginx 


NGINX webserver that serves a simple page containing its hostname, IP address and port as wells as the request URI and the local time of the webserver.

The images are uploaded to Docker Hub -- https://hub.docker.com/r/dockerbogo/docker-nginx-hello-world/.

How to run:
```
$ docker run -p 8080:80 -d dockerbogo/docker-nginx-hello-world
```

Now, assuming we found out the IP address and the port that mapped to port 80 on the container, in a browser we can make a request to the webserver and get the page below: 

![hello_world](./hello_world.png)


Reference: [Docker & Kubernetes](http://bogotobogo.com/DevOps/Docker/Docker_Kubernetes.php)

docker run -d --name login nginx:latest
docker exec -it login /bin/bash
apt update
apt-get install iputils-ping -y
Ping -V
docker network ls
docker network rm test
docker network create secure-network
docker run -d --name container3  --network=secure-network nginx:latest
docker exec -it container3 /bin/bash
ping -V

docker run -d --name host-demo  --network=network nginx:latest
docker inspect host-demo 

Ipaddress=""
container1 - 172.17.0.16
container2 - 172.17.0.15


