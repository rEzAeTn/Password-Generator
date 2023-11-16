from abc import ABC, abstractmethod
from typing import List, Optional
import random
import string
import nltk

nltk.download('words')

class PasswordGenerator(ABC):
    """
    Abstract base class for password generators.
    """

    @abstractmethod
    def password_generator(self) -> str:
        """
        Abstract method to generate a password.
        """
        pass


class PinCodesGenerator(PasswordGenerator):
    """
    Class to generate pin codes.

    :param length: The length of the pin code. Default is 8.
    :type length: int
    """

    def __init__(self, length: int = 8):
        self.length = length

    def password_generator(self) -> str:
        """
        Generate a pin code.

        :return: The generated pin code.
        :rtype: str
        """
        pin_codes: str = ''.join([random.choice(string.digits) for _ in range(self.length)])
        return pin_codes


class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generate random passwords.

    :param length: The length of the password. Default is 8.
    :type length: int
    :param include_lowercase: Whether to include lowercase letters. Default is True.
    :type include_lowercase: bool
    :param include_uppercase: Whether to include uppercase letters. Default is True.
    :type include_uppercase: bool
    :param include_punc: Whether to include punctuation. Default is True.
    :type include_punc: bool
    :param include_number: Whether to include numbers. Default is True.
    :type include_number: bool
    """

    def __init__(
        self,
        length: int = 8,
        include_lowercase: bool = True,
        include_uppercase: bool = True,
        include_punc: bool = True,
        include_number: bool = True
    ):
        self.length = length
        self.characters = ''

        if include_lowercase:
            self.characters += string.ascii_lowercase
        if include_uppercase:
            self.characters += string.ascii_uppercase
        if include_punc:
            self.characters += string.punctuation
        if include_number:
            self.characters += string.digits

    def password_generator(self) -> str:
        """
        Generate a random password.

        :return: The generated password.
        :rtype: str
        """
        random_password: str = ''.join([random.choice(self.characters) for _ in range(self.length)])
        return random_password


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate memorable passwords.

    :param number_of_words: The number of words in the password. Default is 8.
    :type number_of_words: int
    :param separator: The separator between words. Default is '-'.
    :type separator: str
    :param capitalized: Whether to capitalize words. Default is False.
    :type capitalized: bool
    :param vocabulary: The vocabulary to use. Default is nltk.corpus.words.words().
    :type vocabulary: Optional[List[str]]
    """

    def __init__(
        self,
        number_of_words: int = 8,
        separator: str = '-',
        capitalized: bool = False,
        vocabulary: Optional[List[str]] = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalized = capitalized
        self.vocabulary = vocabulary

    def password_generator(self) -> str:
        """
        Generate a memorable password.

        :return: The generated password.
        :rtype: str
        """
        memorable_password: list = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalized:
            memorable_password = [word.upper() if random.choice([True, False]) else word.lower() for word in memorable_password]
        return self.separator.join(memorable_password)


if __name__ == '__main__':

    obj = PinCodesGenerator(length=8)
    password = obj.password_generator()
    print(f'PIN Code: {password}')

    obj = RandomPasswordGenerator(
    length=15,
    include_lowercase=False,
    include_uppercase=True,
    include_punc=True,
     include_number=True
)
    password = obj.password_generator()
    print(f'Random Password: {password}')

    obj = MemorablePasswordGenerator(
    number_of_words=4,
    separator='-',
    capitalized=True,
    vocabulary=None,
)
    password = obj.password_generator()
    print(f'Memorable Password: {password}')
