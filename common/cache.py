from django.core.cache import cache


def reset_endpoint_cache(key_prefix: str) -> None:
    cache.delete_many(keys=cache.keys(f"*.{key_prefix}.*"))  # type: ignore
