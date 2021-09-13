import sentry_sdk
sentry_sdk.init(
    "https://6701c09fd39548baa6654f471bcefd1f@o994707.ingest.sentry.io/5953356",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
