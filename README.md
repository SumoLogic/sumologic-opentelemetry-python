# Sumo Logic OpenTelemetry Python


An all-in-one package for python projects used to enable OpenTelemetry auto-instrumentation.

It contains all supported detectors, propagators and auto-instrumentation plugins.

## Instalation

```
pip install sumologic-opentelemetry
```


## Instrumented packages

This package installs all officially supported auto-instrumentation packages() as well as comonly used propagators and exporters:

### Instrumented packages
```
opentelemetry-instrumentation-aws-lambda
opentelemetry-instrumentation-dbapi
opentelemetry-instrumentation-logging
opentelemetry-instrumentation-sqlite3
opentelemetry-instrumentation-urllib
opentelemetry-instrumentation-wsgi
opentelemetry-instrumentation-aiohttp-client
opentelemetry-instrumentation-aiopg
opentelemetry-instrumentation-asgi
opentelemetry-instrumentation-asyncpg
opentelemetry-instrumentation-boto
opentelemetry-instrumentation-botocore
opentelemetry-instrumentation-celery
opentelemetry-instrumentation-django
opentelemetry-instrumentation-elasticsearch
opentelemetry-instrumentation-falcon
opentelemetry-instrumentation-fastapi
opentelemetry-instrumentation-flask
opentelemetry-instrumentation-grpc
opentelemetry-instrumentation-httpx
opentelemetry-instrumentation-jinja2
opentelemetry-instrumentation-kafka-python
opentelemetry-instrumentation-mysql
opentelemetry-instrumentation-pika
opentelemetry-instrumentation-psycopg2
opentelemetry-instrumentation-pymemcache
opentelemetry-instrumentation-pymongo
opentelemetry-instrumentation-pymysql
opentelemetry-instrumentation-pyramid
opentelemetry-instrumentation-redis
opentelemetry-instrumentation-requests
opentelemetry-instrumentation-sklearn
opentelemetry-instrumentation-sqlalchemy
opentelemetry-instrumentation-starlette
opentelemetry-instrumentation-tornado
opentelemetry-instrumentation-urllib3
```

### Included propagators
```
opentelemetry-distro
opentelemetry-instrumentation
opentelemetry-exporter-otlp-proto-http
opentelemetry-propagator-jaeger
opentelemetry-propagator-b3
opentelemetry-propagator-aws-xray
opentelemetry-propagator-ot-trace
```

## Application execution
 Execute the following command. The command will also print the opnteleemtry config used.

```
sumologic-opentelemetry-instrument python3 SCRIPT_NAME.py
```

## Environment variables config
The wrapper command checks for the basic opentelemetry env variables - OTEL_PROPAGATORS, OTEL_TRACES_EXPORTER, OTEL_SERVICE_NAME, OTEL_EXPORTER_OTLP_ENDPOINT, OTEL_RESOURCE_ATTRIBUTES - that are required for the collected data to be usefull withinn Sumo Logic.
If those are set, the wrapper will not attempt to overwrite them.

### Propagators
By default all propgators are enables (`OTEL_PROPAGATORS=tracecontext,baggage,b3,b3multi,jaeger,xray,ottrace`)

### Exporter.
By default exported is set to OTLP HTTP (`OTEL_TRACES_EXPORTER=otlp_proto_http`)

### Service name
By default service name will not be set `OTEL_SERVICE_NAME=`. Overwrite the env var with a string value representing service business logic, such as "FinanceServiceCall". This will appear as a tracing service name in Sumo Logic.


### Endpoint
By default endpoint is not set (`OTEL_EXPORTER_OTLP_ENDPOINT=`). Represents the endpoint where telemetry data will be sent. Change to appropriate endpoint, for example `OTEL_EXPORTER_OTLP_ENDPOINT=http://collection-sumologic-otelcol.sumologic:55681`

# Resource attributes
By default not set (`OTEL_RESOURCE_ATTRIBUTES=`). Is used to configure the application name (i.e. `OTEL_RESOURCE_ATTRIBUTES=application=APPLICATION_NAME`). The application name will appear as a tracing application name in Sumo Logic. Additional attributes can be added here as comma separated key=value pairs.
