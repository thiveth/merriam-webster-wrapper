# Merriam-Webster API Wrapper

A lightweight Python wrapper around the Merriam-Webster Dictionary and Thesaurus APIs. Look up definitions, synonyms, and antonyms with a simple `Client` interface.

## Features

- Dictionary definitions
- Thesaurus definitions, synonyms, and antonyms
- Simple, minimal API surface

## Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/thiveth/merriam-webster-wrapper.git
   cd merriam-webster-wrapper
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Get API keys**

   Register for free Dictionary and Thesaurus API keys at [dictionaryapi.com](https://dictionaryapi.com/register/index).

4. **Set up your environment file**

   Copy the example file and fill in your real keys:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env`:

   ```
   MERRIAM_THESAURUS_API_KEY=your-thesaurus-key-here
   MERRIAM_DICTIONARY_API_KEY=your-dictionary-key-here
   ```

   `.env` is git-ignored and will never be committed — keep your real keys there, not in code.

## Usage

```python
import merriam

search = merriam.Client(dictionary=False, thesaurus=True)
search.define("den")
```

```python
# Look up synonyms and antonyms
search = merriam.Client(thesaurus=True)
search.synonyms("happy")
search.antonyms("happy")
```

## Project Structure

```
merriam-webster-wrapper/
├── merriam/
│   ├── __init__.py
│   ├── client.py       # Core Client class
│   ├── config.py        # Loads API keys from environment variables
│   └── errors.py         # Custom exception classes
├── .env.example          # Template for your local .env file
├── .gitignore
├── main.py               # Example usage
└── requirements.txt
```

## Notes

- Requires an internet connection — the client checks connectivity on init.
- Never commit your `.env` file. If a key is ever exposed, rotate it immediately at dictionaryapi.com.

## License

MIT
