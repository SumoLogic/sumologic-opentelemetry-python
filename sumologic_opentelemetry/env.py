import os

# from dataclasses import dataclass
from collections import namedtuple

EnvironmentVariable = namedtuple('EnvironmentVariable', ['name', 'default', 'description'])

SUMOLOGIC_OTEL_VARS = [
    EnvironmentVariable(
        'OTEL_PROPAGATORS',
        'tracecontext,baggage,b3,b3multi,jaeger,xray,ottrace',
        'Propagators to be used'
    ),
    EnvironmentVariable(
        'OTEL_TRACES_EXPORTER',
        'otlp_proto_http',
        'Traces exporter protocol'
    ),
    EnvironmentVariable(
        'OTEL_SERVICE_NAME',
        '',
        'This will appear as a tracing service name in Sumo Logic'
    ),
    EnvironmentVariable(
        'OTEL_EXPORTER_OTLP_ENDPOINT',
        '',
        'The endpoint where telemetry data will be sent. For example OTEL_EXPORTER_OTLP_ENDPOINT=http://collection-sumologic-otelcol.sumologic:55681'
    ),
    EnvironmentVariable(
        'OTEL_RESOURCE_ATTRIBUTES',
        '',
        'Resource attributes, for example the application name'
    ),
]

def generate():
    for env_var in SUMOLOGIC_OTEL_VARS:
        if env_var.name not in os.environ:
            os.environ[env_var.name] = env_var.default


def dump():
    for env_var in SUMOLOGIC_OTEL_VARS:
        print(f'# {env_var.description}')
        print(f'{env_var.name}={os.environ[env_var.name]}')


