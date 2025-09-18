ARG BUILD_FROM
FROM $BUILD_FROM

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

