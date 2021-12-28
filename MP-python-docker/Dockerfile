FROM python:3.9.7-slim-buster
WORKDIR /application
COPY /app .
CMD python /application/mp1.py
# to launch container with mounted volume
# do: docker run --rm -it -v VOLUMENAME:WORKDIR dockertag
# --rm: removes container on exit
# -it: interactive terminal mode
# -v: specifies volume mount

# docker ps -all -> list all and recently run containers
# docker images -> list all images
# docker rm containername -> stops & removes containername
# docker rmi imagename:imagetag -> removes imagename:imagetag
# docker build . -t test:v1 -> builds image in file