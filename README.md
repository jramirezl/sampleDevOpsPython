# sampleDevOpsPython

### Python


- pip3 install <lib_name>
- pip3 freeze > requirements.txt // transportar dependiencias

#### Flask

add env variables: 
- export FLASK_APP=application.py 
- export FLASK_ENV=development


### Docker
docker

- docker build -t <account_docker_registry>/<image_name>:< version > .
- docker run -it --rm -p 5000:5000 --name <docker_container_name> <account_docker_registry>/<image_name>:< version >
    
