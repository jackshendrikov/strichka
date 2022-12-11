from typing import AnyStr

import re


def slugify_value(value: AnyStr) -> str:
    """
    Convert spaces to underscore. Remove characters that aren't
    alphanumerics, underscores, or underscores. Convert to lowercase. Also strip
    leading and trailing whitespace.
    """
    value = re.sub(r"[^\w\s_]", "", value).strip().lower()  # type: ignore
    return re.sub(r"[_\s]+", "_", value)
