FROM python:3.9-bullseye
RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN adduser -D myuser
RUN adduser myuser
# RUN apk add --no-cache gcc musl-dev linux-headers
RUN apt install gcc
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install --user -r requirements.txt