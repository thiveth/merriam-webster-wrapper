from merriam import errors
import requests
from .config import Identifiers


class Client:
    def __init__(self, thesaurus=False, dictionary=True):
        self.DSECRET = Identifiers.keys[1]
        self.TSECRET = Identifiers.keys[0]
        self.thesaurus = thesaurus
        self.dictionary = dictionary

        if not self.is_online():
            print("You are not online.")
            quit(0)

    def define(self, word: str) -> str:

        if self.thesaurus:
            dr = requests.get(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/test?key={self.TSECRET}")
            if "Invalid API key. Not subscribed for this reference." in dr.text:
                raise errors.INVALID_API_KEY("Invalid API KEY PASSED.")
            else:
                try:
                    dr = requests.get(
                        f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={self.TSECRET}").json()
                    # definitions: str = '\n'.join([_ for _ in dr[0]["shortdef"]])
                    stems = ', '.join([_ for _ in dr[0]["meta"]["stems"]])
                    print(f"({word}) Thesaurus Definition(s): \n")
                    print("Stems: {0}".format(stems))
                    _ = {_["fl"]: _["shortdef"][0] for _ in dr[:]}

                    for k, v in _.items():
                        print(f"{k}: {v}")
                    print('\n' * 2)
                    return word

                except TypeError:
                    print(f"No instance of the word \"{word}\" in this thesaurus. \n")
        if self.dictionary:
            dr = requests.get(
                f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={self.DSECRET}")

            if "Invalid API key. Not subscribed for this reference." in dr.text:
                raise errors.INVALID_API_KEY("Invalid API KEY PASSED.")
            else:
                try:
                    dr = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={self.DSECRET}").json()
                    # definitions: str = '\n'.join([_ for _ in dr[0]["shortdef"]])
                    stems = ', '.join([_ for _ in dr[0]["meta"]["stems"]])
                    print(f"({word}) Dictionary Definition(s): \n")
                    print("Stems: {0}".format(stems))
                    _ = {_["fl"]: _["shortdef"][0] for _ in dr[:]}

                    for k, v in _.items():
                        print(f"{k}: {v}")
                    print('\n')

                except TypeError:
                    print(f"No instance of the word \"{word}\" in this dictionary. \n")

    def synonyms(self, word):

        if self.thesaurus:
            dr = requests.get(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/test?key={self.TSECRET}")
            if "Invalid API key. Not subscribed for this reference." in dr.text:
                raise errors.INVALID_API_KEY("Invalid API KEY PASSED.")
            else:
                dr = requests.get(
                    f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={self.TSECRET}").json()
                syns: str = '\n'.join([_ for _ in dr[0]["meta"]["syns"][0]])
                print("Synonyms:")
                print('\n', syns)


    def antonyms(self, word):
        if self.thesaurus:
            dr = requests.get(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/test?key={self.TSECRET}")
            if "Invalid API key. Not subscribed for this reference." in dr.text:
                raise errors.INVALID_API_KEY("Invalid API KEY PASSED.")
            else:
                dr = requests.get(
                    f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={self.TSECRET}").json()
                ants: str = '\n'.join([_ for _ in dr[0]["meta"]["ants"][0]])
                print("\nAntonyms:")
                print('\n', ants)

    @staticmethod
    def is_online():
        if requests.get("https://www.merriam-webster.com").status_code == 200:
            return True
        return False
