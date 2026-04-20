FROM ghcr.io/home-assistant/base:latest
LABEL \
    org.opencontainers.image.title="SolarSynkV3" \
    org.opencontainers.image.description="Home Assistant add-on for syncing solar/inverter data from SynSynk.net" \
    org.opencontainers.image.source="https://github.com/martinville/solarsynkv3" \
    io.hass.version="3.0.32" \
    io.hass.arch="amd64" \
    io.hass.type="app" \
    io.hass.name="SolarSynkV3" \
    io.hass.description="Home Assistant add-on for syncing solar/inverter data from SynSynk.net" \
    io.hass.url="https://github.com/martinville/solarsynkv3/tree/main"
ARG \
    BUILD_VERSION="3.0.32" \
    BUILD_ARCH="amd64"

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip py3-requests py3-cryptography

WORKDIR /data

# Copy data for add-on
COPY run.sh /
COPY main.py /
COPY getapi.py /
COPY gettoken.py /
COPY postapi.py /
COPY settingsmanager.py /
COPY src/ /src/

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
