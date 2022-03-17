"""Environment management package for sunologic OTEL instrumentation"""

import os
from collections import namedtuple

EnvironmentVariable = namedtuple(
    "EnvironmentVariable", ["name", "default", "description"]
)

SUMOLOGIC_OTEL_VARS = [
    EnvironmentVariable(
        "OTEL_PROPAGATORS",
        "tracecontext,baggage,b3,b3multi,jaeger,xray,ottrace",
        "Propagators to be used",
    ),
    EnvironmentVariable(
        "OTEL_TRACES_EXPORTER", "otlp_proto_http", "Traces exporter protocol"
    ),
    EnvironmentVariable(
        "OTEL_SERVICE_NAME",
        "",
        "This will appear as a tracing service name in Sumo Logic",
    ),
    EnvironmentVariable(
        "OTEL_EXPORTER_OTLP_ENDPOINT",
        "",
        "The endpoint where telemetry data will be sent. For example "
        "OTEL_EXPORTER_OTLP_ENDPOINT=http://collection-sumologic-otelcol.sumologic:55681",
    ),
    EnvironmentVariable(
        "OTEL_RESOURCE_ATTRIBUTES",
        "",
        "Resource attributes, for example the application name",
    ),
]


def generate():
    """Generates new default env conffig of OTEL"""

    for env_var in SUMOLOGIC_OTEL_VARS:
        if env_var.name not in os.environ:
            os.environ[env_var.name] = env_var.default


def dump():
    """Dumps OTEL env config"""

    # Print most important env vars first.
    for env_var in SUMOLOGIC_OTEL_VARS:
        if env_var.name in os.environ:
            print(f"# {env_var.description}")
            print(f"{env_var.name}={os.environ[env_var.name]}")

    # Print remaining OTEL env vars.
    dumped = set(env_var.name for env_var in SUMOLOGIC_OTEL_VARS)
    otel_env = (x for x in os.environ if x.startswith("OTEL_"))
    remaining_otel_env = (x for x in otel_env if x not in dumped)

    for env_var_name in remaining_otel_env:
        print(f"{env_var_name}={os.environ[env_var_name]}")
