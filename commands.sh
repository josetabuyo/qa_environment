## command to create the virtualenv
python3 -m venv .venv
pip3 install -r requirements.txt


#######################
#### GENERAL SETUP ####
# Install docker with https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/

### Docker

# List containers
docker container ls

# ** Possible error:
# "Cannot connect to the Docker daemon at unix:///Users/josetabuyo/.docker/run/docker.sock. Is the docker daemon running?"
# ** Solution:
# Turn Docker on! (using desktop app or deamon by shell)





#######################
##### WEB SERVICE #####


# Remove the previous intance
docker rm -f qa-web-service-pod

# ** Possible error:
# "Error: No such container: qa-web-service-pod"
# ** Solution:
# This could be the first time, just ignore it

# Build Dockerfile (can take some time on first time)
docker build --platform linux/amd64 -t qa-web-service -f Dockerfile.web .


# Instantiate
docker run --platform linux/amd64 --add-host localhost:127.0.0.1 --name qa-web-service-pod -p 8089:8089 qa-web-service

# ** Possible error:
# Here the compilation occurss,
# so, we can see Syntax Error's or any other expected issue for this step
# ** Solution:
# Fix al the compilation problems
# do 'Remove the previous intance' command and 'Build Dockerfile' again 

# ** Possible error:
# docker: Error response from daemon: Conflict. The container name "/qa-web-service-pod" is already in use by container "de729eee303c2a0d622509ec817b3a0e027d7ad658ea43ce65cb207da1709b1b". You have to remove (or rename) that container to be able to reuse that name.
# See 'docker run --help'.
# ** Solution:
# Remove the previous intance


# ** Possible warning:
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# ** Solution:
# Let's ignore it for the moment


## useful alias for iterations
alias refresh_qa_web_service="docker rm -f qa-web-service-pod && docker build --platform linux/amd64 -t qa-web-service -f Dockerfile.web . && docker run --platform linux/amd64 --add-host localhost:127.0.0.1 --name qa-web-service-pod -p 8089:8089 qa-web-service"


######################
##### REGRESSION #####

# Remove docker container
docker rm -f qa-regression-pod
# Build the container
docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg .
# Run the container
docker run --platform linux/amd64 --add-host localhost:127.0.0.1 --name qa-regression-pod qa-regression

## useful alias for iterations
alias refresh_qa_regression="docker rm -f qa-regression-pod && docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg . && docker run --platform linux/amd64 --add-host localhost:127.0.0.1 --name qa-regression-pod qa-regression"


