ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/portal
RUN ln -s /obfuscation /home/dulno/portal

COPY static /home/dulno/portal/static
COPY obfuscation /home/dulno/portal/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/portal

RUN node /home/dulno/portal/obfuscation/obfuscate.js

FROM nginx

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

# FIXES CVE-2024-55549  & CVE-2025-24855
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    libxslt1.1=1.1.35-1+deb12u1 \
    && apt-get clean

COPY --from=builder /home/dulno/portal/static /home/dulno/portal/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN mkdir -p /etc/nginx/sites-enabled
RUN ln -sf /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]