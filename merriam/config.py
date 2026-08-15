import os

from dotenv import load_dotenv

load_dotenv()

THESAURUS_API_KEY = os.getenv("MERRIAM_THESAURUS_API_KEY")
DICTIONARY_API_KEY = os.getenv("MERRIAM_DICTIONARY_API_KEY")


def _check_key(name: str, value: str | None) -> None:
    if not value:
        print(
            f"Warning: {name} is not set. "
            f"Add it to your .env file or export it as an environment variable."
        )


_check_key("MERRIAM_THESAURUS_API_KEY", THESAURUS_API_KEY)
_check_key("MERRIAM_DICTIONARY_API_KEY", DICTIONARY_API_KEY)


class Identifiers:
    """Kept for backward compatibility with the rest of the package.
    keys[0] = thesaurus key, keys[1] = dictionary key (same order as before).
    """
    keys: tuple = (THESAURUS_API_KEY, DICTIONARY_API_KEY)
