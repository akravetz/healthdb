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
WORKDIR /
ENTRYPOINT ["/venv/bin/python3", "-m", "src.app"]
