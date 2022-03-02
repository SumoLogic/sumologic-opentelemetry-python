# Sumo Logic OpenTelemetry Python


An all-in-one package for python projects used to enable OpenTelemetry auto-instrumentation.

It contains all supported detectors, propagators and auto-instrumentation plugins.

## Usage

```
pip install sumologic-opentelemetry
```


## Instrumented packages

This package enables some officially supported [auto-instrumentation packages](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/v0.26b1/instrumentation) as well as comonly used propagators and exporters:

```
opentelemetry-distro
opentelemetry-instrumentation
opentelemetry-exporter-otlp-proto-http
opentelemetry-propagator-jaeger
opentelemetry-propagator-b3
opentelemetry-propagator-aws-xray
opentelemetry-propagator-ot-trace
```

## Manual instrumentation

TODO

Example:

```python
TODO
```

# Application execution
When everything is configured it is very simple to run an instrumented application.

```
opentelemetry-instrument python3 SCRIPT_NAME.py
```
