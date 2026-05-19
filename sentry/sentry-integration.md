# Sentry Integration

Sentry is used for application-level error tracking.

## What it monitors

- Python exceptions
- 500 errors
- Failed API requests
- Stack traces
- Release-based errors

## Test Error

Visit:

/error

Expected result:

Sentry captures the exception and shows stack trace.

## Value

Grafana shows system health.
Sentry shows application code errors.
Together they improve MTTR.
