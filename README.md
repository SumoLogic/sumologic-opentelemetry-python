# Sumo Logic OpenTelemetry Python

An all-in-one package for python projects used to enable OpenTelemetry auto-instrumentation.

Includes all supported propagators and auto-instrumentation plugins.

- [Sumo Logic OpenTelemetry Python](#sumo-logic-opentelemetry-python)
  - [Installation](#installation)
  - [Installation without instrumented packages](#installation-without-instrumented-packages)
  - [Instrumented packages](#instrumented-packages)
    - [Instrumented packages](#instrumented-packages-1)
    - [Propagators](#propagators)
    - [Other requirements](#other-requirements)
  - [Application execution](#application-execution)
  - [Environment variables config](#environment-variables-config)
    - [Propagators](#propagators-1)
    - [Exporter](#exporter)
    - [Service name](#service-name)
    - [Endpoint](#endpoint)
  - [Resource attributes](#resource-attributes)

## Installation

Following command will installation the package with all instrumented packages.

```bash
pip install sumologic-opentelemetry[all]
```

## Installation without instrumented packages

```bash
pip install sumologic-opentelemetry
```

Instrumented packages needs to be installed per application.
Command bellow executed in the root directory of your Python application will install corresponding instrumented packages used by the application.

```bash
opentelemetry-bootstrap --action=install
```

## Instrumented packages

This package installs all officially supported auto-instrumentation packages as well as commonly used propagators and exporters:

### Instrumented packages

Following list of instrumented packages is optional, but recommended for easy installation:

- [opentelemetry-instrumentation-aws-lambda](https://pypi.org/project/opentelemetry-instrumentation-aws-lambda/)
- [opentelemetry-instrumentation-dbapi](https://pypi.org/project/opentelemetry-instrumentation-dbapi)
- [opentelemetry-instrumentation-logging](https://pypi.org/project/opentelemetry-instrumentation-logging)
- [opentelemetry-instrumentation-sqlite3](https://pypi.org/project/opentelemetry-instrumentation-sqlite3)
- [opentelemetry-instrumentation-urllib](https://pypi.org/project/opentelemetry-instrumentation-urllib)
- [opentelemetry-instrumentation-wsgi](https://pypi.org/project/opentelemetry-instrumentation-wsgi)
- [opentelemetry-instrumentation-aiohttp-client](https://pypi.org/project/opentelemetry-instrumentation-aiohttp-client)
- [opentelemetry-instrumentation-aiopg](https://pypi.org/project/opentelemetry-instrumentation-aiopg)
- [opentelemetry-instrumentation-asgi](https://pypi.org/project/opentelemetry-instrumentation-asgi)
- [opentelemetry-instrumentation-asyncpg](https://pypi.org/project/opentelemetry-instrumentation-asyncpg)
- [opentelemetry-instrumentation-boto](https://pypi.org/project/opentelemetry-instrumentation-boto)
- [opentelemetry-instrumentation-botocore](https://pypi.org/project/opentelemetry-instrumentation-botocore)
- [opentelemetry-instrumentation-celery](https://pypi.org/project/opentelemetry-instrumentation-celery)
- [opentelemetry-instrumentation-django](https://pypi.org/project/opentelemetry-instrumentation-django)
- [opentelemetry-instrumentation-elasticsearch](https://pypi.org/project/opentelemetry-instrumentation-elasticsearch)
- [opentelemetry-instrumentation-falcon](https://pypi.org/project/opentelemetry-instrumentation-falcon)
- [opentelemetry-instrumentation-fastapi](https://pypi.org/project/opentelemetry-instrumentation-fastapi)
- [opentelemetry-instrumentation-flask](https://pypi.org/project/opentelemetry-instrumentation-flask)
- [opentelemetry-instrumentation-grpc](https://pypi.org/project/opentelemetry-instrumentation-grpc)
- [opentelemetry-instrumentation-httpx](https://pypi.org/project/opentelemetry-instrumentation-httpx)
- [opentelemetry-instrumentation-jinja2](https://pypi.org/project/opentelemetry-instrumentation-jinja2)
- [opentelemetry-instrumentation-kafka-python](https://pypi.org/project/opentelemetry-instrumentation-kafka-python)
- [opentelemetry-instrumentation-mysql](https://pypi.org/project/opentelemetry-instrumentation-mysql)
- [opentelemetry-instrumentation-pika](https://pypi.org/project/opentelemetry-instrumentation-pika)
- [opentelemetry-instrumentation-psycopg2](https://pypi.org/project/opentelemetry-instrumentation-psycopg2)
- [opentelemetry-instrumentation-pymemcache](https://pypi.org/project/opentelemetry-instrumentation-pymemcache)
- [opentelemetry-instrumentation-pymongo](https://pypi.org/project/opentelemetry-instrumentation-pymongo)
- [opentelemetry-instrumentation-pymysql](https://pypi.org/project/opentelemetry-instrumentation-pymysql)
- [opentelemetry-instrumentation-pyramid](https://pypi.org/project/opentelemetry-instrumentation-pyramid)
- [opentelemetry-instrumentation-redis](https://pypi.org/project/opentelemetry-instrumentation-redis)
- [opentelemetry-instrumentation-requests](https://pypi.org/project/opentelemetry-instrumentation-requests)
- [opentelemetry-instrumentation-sklearn](https://pypi.org/project/opentelemetry-instrumentation-sklearn)
- [opentelemetry-instrumentation-sqlalchemy](https://pypi.org/project/opentelemetry-instrumentation-sqlalchemy)
- [opentelemetry-instrumentation-starlette](https://pypi.org/project/opentelemetry-instrumentation-starlette)
- [opentelemetry-instrumentation-tornado](https://pypi.org/project/opentelemetry-instrumentation-tornado)
- [opentelemetry-instrumentation-urllib3](https://pypi.org/project/opentelemetry-instrumentation-urllib3)

### Propagators

Following propagators are installed as a dependency.

- [opentelemetry-exporter-otlp-proto-http](https://pypi.org/project/opentelemetry-exporter-otlp-proto-http/)
- [opentelemetry-propagator-jaeger](https://pypi.org/project/opentelemetry-propagator-jaeger/)
- [opentelemetry-propagator-b3](https://pypi.org/project/opentelemetry-propagator-b3/)
- [opentelemetry-propagator-aws-xray](https://pypi.org/project/opentelemetry-propagator-aws-xray/)
- [opentelemetry-propagator-ot-trace](https://pypi.org/project/opentelemetry-propagator-ot-trace/)

### Other requirements

- [opentelemetry-distro](https://pypi.org/project/opentelemetry-distro/)
- [opentelemetry-instrumentation](https://pypi.org/project/opentelemetry-instrumentation/)

## Application execution

Execute the following command. The command will also print the opentelemetry config used.

```
sumologic-opentelemetry-instrument python3 SCRIPT_NAME.py
```

## Environment variables config

The wrapper command checks for the following basic OpenTelemetry env variables that are required for the collected data to be useful within Sumo Logic:

- `OTEL_PROPAGATORS`
- `OTEL_TRACES_EXPORTER`
- `OTEL_SERVICE_NAME`
- `OTEL_EXPORTER_OTLP_ENDPOINT`
- `OTEL_RESOURCE_ATTRIBUTES`

### Propagators

By default, all propgators are enabled (`OTEL_PROPAGATORS=tracecontext,baggage,b3,b3multi,jaeger,xray,ottrace`).

### Exporter

By default, exported is set to OTLP HTTP (`OTEL_TRACES_EXPORTER=otlp_proto_http`).

### Service name

By default, service name will not be set `OTEL_SERVICE_NAME=`.
Overwrite the env var with a string value representing service business logic, such as "FinanceServiceCall".
This will appear as a tracing service name in Sumo Logic.

### Endpoint

By default, endpoint is not set (`OTEL_EXPORTER_OTLP_ENDPOINT=`). Represents the endpoint where telemetry data will be sent.
Change to appropriate endpoint, for example `OTEL_EXPORTER_OTLP_ENDPOINT=http://collection-sumologic-otelcol.sumologic:55681`

## Resource attributes

By default, resource attributes are not set (`OTEL_RESOURCE_ATTRIBUTES=`).
Is used to configure the application name (i.e. `OTEL_RESOURCE_ATTRIBUTES=application=APPLICATION_NAME`).
The application name will appear as a tracing application name in Sumo Logic.
Additional attributes can be added here as comma separated key=value pairs.
