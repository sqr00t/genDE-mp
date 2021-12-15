FROM python:3.9.7-slim-buster
WORKDIR /application
COPY /app .
CMD python /application/mp1.py
# to launch container with mounted volume
# do: docker run --rm -it -v VOLUMENAME:WORKDIR dockertag
# --rm: removes container on exit
# -it: interactive terminal mode
# -v: specifies volume mount