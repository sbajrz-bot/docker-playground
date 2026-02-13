# docker-hello-world
Single page docker image 

# Build the image
docker build -t helloworld .

# Docker tag
docker tag helloworld devopstrainingust/helloworld:V1.0

# List docker images

 Docker images
                                                                                                                           i Info →   U  In Use
IMAGE                                                                                          ID             DISK USAGE   CONTENT SIZE   EXTRA

## devopstrainingust/helloworld:V1.0                                                              f46694b237dd        840MB          224MB    U
docker/desktop-kubernetes:kubernetes-v1.34.1-cni-v1.7.1-critools-v1.33.0-cri-dockerd-v0.3.20-1-debian
                                                                                               
# Push image to Dockerhub

 docker login

 docker push devopstrainingust/helloworld:V1.0

 # Remove image and pull from docker registry
  docker rmi devopstrainingust/helloworld:V1.0
  docker pull devopstrainingust/helloworld:V1.0

