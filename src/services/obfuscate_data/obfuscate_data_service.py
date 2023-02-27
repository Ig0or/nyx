# Standard
from typing import Callable
import json

# Third Party
from cryptography.fernet import Fernet
from decouple import config


class ObfuscateDataService:
    __fernet_key = config("FERNET_KEY")
    __fernet_instance = Fernet(key=__fernet_key)

    @classmethod
    def __encode_str(cls, value: str) -> bytes:
        bytes_value = value.encode()

        return bytes_value

    @classmethod
    def __encode_dict(cls, value: dict) -> bytes:
        bytes_value = json.dumps(value).encode()

        return bytes_value

    @classmethod
    def __get_encode_method_from_value_type(cls, value: dict | str) -> Callable:
        encode_methods = {str: cls.__encode_str, dict: cls.__encode_dict}

        value_type = type(value)
        encode_method = encode_methods[value_type]

        return encode_method

    @classmethod
    def __encode_value(cls, value: dict | str) -> bytes:
        encode_method = cls.__get_encode_method_from_value_type(value=value)
        encoded_value = encode_method(value=value)

        return encoded_value

    @classmethod
    def obfuscate_value(cls, value: dict | str) -> bytes:
        encoded_value = cls.__encode_value(value=value)

        obfuscated_value = cls.__fernet_instance.encrypt(data=encoded_value)

        return obfuscated_value
