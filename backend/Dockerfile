FROM python:3.9-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes gcc libpython3-dev g++ libffi-dev bcrypt && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip

# Build the virtualenv as a separate step: Only re-execute this step when requirements.txt changes
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Copy the virtualenv into a distroless image
FROM python:3.9-slim
COPY --from=build-venv /venv /venv
# install gosu, which allows us to drop root privileges to the current user
ENV GOSU_URL https://github.com/tianon/gosu/releases/download/1.4/gosu

RUN apt-get update && \
  apt-get install -yq --no-install-recommends libnuma-dev libmagic1 libxt6 ca-certificates curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* 

# download gosu and check the sha checksum
RUN curl -o /usr/local/bin/gosu -SL "$GOSU_URL-$(dpkg --print-architecture)" && \
  chmod +x /usr/local/bin/gosu && \
  [ "$(sha256sum -b /usr/local/bin/gosu)" = '3414313774edf750a3a0e46ea4fc554f5b8701ce9d4cb915916f5dddcd2202fa */usr/local/bin/gosu' ]

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/venv/bin/python3", "-m", "src.app"]
