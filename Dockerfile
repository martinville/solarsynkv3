ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip py3-requests

WORKDIR /data


# Copy data for add-on
COPY run.sh /
COPY src/main.py /
COPY src/getapi.py /
COPY src/gettoken.py /
COPY src/postapi.py /
COPY src/settingsmanager.py /



RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
