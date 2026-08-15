
class Errors(Exception):
    """ Base class for all other exceptions """
    pass


class INVALID_API_KEY(Errors):
    """ Class which deals with Invalid API Key Errors """
    pass


class NO_CALLS(Errors):
    """ Class that deals with no calls """
    pass


class WORD_NOT_FOUND(Errors):
    """ Raised when a searched word is not found """
    pass
