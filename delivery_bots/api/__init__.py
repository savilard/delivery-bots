import os

import sentry_sdk

sentry_sdk.init(
    os.getenv('SENTRY_URL', 'SENTRY'),
    traces_sample_rate=1.0,
)
