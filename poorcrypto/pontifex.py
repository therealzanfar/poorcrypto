# cSpell:words poorcrypto Wyant cryptonomicon schneier unkeyed

# Copyright (C) 2023, Matthew Wyant
#
# This file is part of poorcrypto
#
# poorcrypto is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# poorcrypto is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# The cipher implemented here as "Pontifex" is derived from the description
# of the method of the same name in Neal Stephenson's "Cryptonomicon" which is
# itself based on the method known as "Solitaire" developed by Bruce Schneier
# # of Counterpane Systems

import random

from poorcrypto import Cipher


class Pontifex(Cipher):
    """An implementation of the Pontifex cipher"""

    def __init__(self, key: tuple[int, ...]):
        assert len(key) == 54
        for k in key:
            assert isinstance(type(k), int)
            assert 1 <= k <= 54

        self.key = list(key)

    @classmethod
    def unkeyed(cls) -> "Pontifex":
        """Generate an unkeyed version of the cipher"""

        key = tuple(range(1, 54 + 1))
        return cls(key)

    @classmethod
    def random(cls, seed=None) -> "Pontifex":
        """Generate a random-keyed version of the cipher"""

        shuffle = random.shuffle

        if seed:
            shuffle = random.Random(seed).shuffle

        key = list(range(1, 54 + 1))
        shuffle(key)

        return cls(tuple(key))
