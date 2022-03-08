import os
import unittest
from io import StringIO
from unittest.mock import patch

import sumologic_opentelemetry.env


def capture_stdout(function, *args, **kwargs):
    @patch("sys.stdout", new_callable=StringIO)
    def invoke(mock_stdout):
        ret = function(*args, **kwargs)
        stdout = mock_stdout.getvalue()
        return ret, stdout

    return invoke()


class EnvTestCase(unittest.TestCase):
    def test_dump_prints_defaults(self):
        expected_env_values = [
            ("OTEL_PROPAGATORS", "tracecontext,baggage,b3,b3multi,jaeger,xray,ottrace"),
            ("OTEL_TRACES_EXPORTER", "otlp_proto_http"),
        ]
        sumologic_opentelemetry.env.generate()
        _, stdout = capture_stdout(sumologic_opentelemetry.env.dump)
        self.assert_env_vars_in_stdout(stdout, expected_env_values)

    def test_dump_prints_non_defaults(self):
        expected_env_values = [("OTEL_LOG_LEVEL", "info")]
        os.environ["OTEL_LOG_LEVEL"] = "info"
        _, stdout = capture_stdout(sumologic_opentelemetry.env.dump)
        self.assert_env_vars_in_stdout(stdout, expected_env_values)

    def assert_env_vars_in_stdout(self, stdout, expected):
        for key, value in expected:
            self.assertRegex(
                stdout,
                r"{key}\w*=\w*{value}\w*".format(key=key, value=value),
                f"{key}={value} not found in stdout",
            )

    def test_generate_defaults(self):
        sumologic_opentelemetry.env.generate()
        self.assertIn("OTEL_PROPAGATORS", os.environ)
        self.assertIn("OTEL_TRACES_EXPORTER", os.environ)

    def test_generate_skips_existing(self):
        os.environ["OTEL_PROPAGATORS"] = "non-default-value"
        sumologic_opentelemetry.env.generate()
        self.assertEqual(os.environ["OTEL_PROPAGATORS"], "non-default-value")
