FROM python:3.9.7-slim-buster
WORKDIR /application
COPY /app .
RUN pip install -r requirements.txt
CMD python /application/main.py
# to launch container with mounted volume
# do: docker run --rm --network="host" -it -v VOLUMENAME:WORKDIR dockertag
# first run: docker run --rm --network="host" -it -v app:/application miniproj-oop:db ls /application

## double-dash arguments first, then single-dash
# --rm: removes container on exit
# --network="host": sets docker run to use network="host" (localhost ip)
# -it: interactive terminal mode
# -v: specifies volume mount

# docker ps -all -> list all and recently run containers
# docker images -> list all images
# docker rm containername -> stops & removes containername
# docker rmi imagename:imagetag -> removes imagename:imagetag
# docker build . -t test:v1 -> builds image in file