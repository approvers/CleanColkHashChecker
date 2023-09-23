import datetime


def datetime_must_be_utc(
        field_name: str, value: datetime.datetime
) -> None:
    if value.tzinfo != datetime.timezone.utc:
        raise ValueError(
            f"ValueError: '{field_name}' must be UTC. '{field_name}' is {value.tzinfo}"
        )
