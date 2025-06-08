ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web-obfuscation:latest AS builder

COPY verification/ /dulno/verification/
COPY ticket/ /dulno/ticket/
COPY templates/ /dulno/templates/
COPY settings/ /dulno/settings/
COPY product/ /dulno/product/
COPY maintenance/ /dulno/maintenance/
COPY errors/ /dulno/errors/
COPY base/ /dulno/base/
COPY obfuscation/ /dulno/obfuscation/

ENV OBFUSCATION_HOME=/dulno

RUN node /dulno/obfuscation/obfuscate.js

FROM ${DOCKER_REGISTRY}/dulno-web-base:latest

COPY manage.py /dulno/manage.py
COPY locale/ /dulno/locale/
COPY app/ /dulno/app/
COPY --from=builder /dulno/verification/ /dulno/verification/
COPY --from=builder /dulno/ticket/ /dulno/ticket/
COPY --from=builder /dulno/templates/ /dulno/templates/
COPY --from=builder /dulno/settings/ /dulno/settings/
COPY --from=builder /dulno/product/ /dulno/product/
COPY --from=builder /dulno/maintenance/ /dulno/maintenance/
COPY --from=builder /dulno/errors/ /dulno/errors/
COPY --from=builder /dulno/base/ /dulno/base/

WORKDIR /dulno

RUN django-admin compilemessages

USER 1000

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]