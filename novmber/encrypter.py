#  _   _  _____     ____  __ ____ _____ ____
# | \ | |/ _ \ \   / /  \/  | __ )___ /|  _ \
# |  \| | | | \ \ / /| |\/| |  _ \ |_ \| |_) |
# | |\  | |_| |\ V / | |  | | |_) |__) |  _ <
# |_| \_|\___/  \_/  |_|  |_|____/____/|_| \_\
#
# MIT License
#
# Copyright (c) 2024 Daniel Lima
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
from pathlib import Path
import rsa

logger = logging.getLogger(__name__)


class Encrypter:

    key_pair: tuple[rsa.PublicKey, rsa.PrivateKey]

    def gen_keys(self) -> None:
        logger.info("Creating key pair.")
        self.key_pair = rsa.newkeys(4096, poolsize=8)

    def encrypt(self, bytes_to_encrypt: bytes) -> bytes:
        return rsa.encrypt(bytes_to_encrypt, self.key_pair[0])

    # def decrypt(self, encrypted_bytes: bytes, private_key: rsa.PrivateKey) -> bytes:
    #     return rsa.decrypt(encrypted_bytes, private_key)

    def get_file_bytes(self, file: Path) -> bytes:
        with file.open("rb") as f:
            file_content = f.read()

        return file_content

    # def __enter__(self) -> None:
    #    pass
    #
    # def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
    #    pass
