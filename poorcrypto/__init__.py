# cSpell:words Wyant poorcrypto ciphertext

"""Poor Man's Crypto, or Poor Quality Crypto: simple cryptographic utilities"""

__author__ = """Matthew Wyant"""
__email__ = "me@matthewwyant.com"
__copyright__ = "Copyright 2023, Matthew Wyant"
__credits__ = [__author__]
__license__ = "GPL-3.0-plus"
__version__ = "0.1.0"
__version_info__ = (0, 1, 0)
__maintainer__ = __author__
__status__ = "Prototype"

from abc import ABC, abstractmethod
from typing import Any, TypeVar

CT = TypeVar("CT")


class Cipher(ABC):
    """A method of encryption"""

    @abstractmethod
    def __init__(self, key: Any):
        """Initialize a cipher method with a given key"""

    @abstractmethod
    def encrypt(self, plaintext: CT) -> CT:
        """Encrypt a message"""

    @abstractmethod
    def decrypt(self, ciphertext: CT) -> CT:
        """Decrypt a message"""
