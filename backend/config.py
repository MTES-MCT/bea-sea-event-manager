ENVIRONMENT_VALID_VALUES = ["demo", "production", "development"]

ENVIRONMENT = "demo"
if ENVIRONMENT not in ENVIRONMENT_VALID_VALUES:
    raise Exception(f"Invalid environment: {ENVIRONMENT}")
