from math import log2
from collections import Counter


class EntropyCalculator:

    @staticmethod
    def calculate_entropy(text):
        if len(text) == 0:
            return 0

        char_freq = iter(count / len(text) for count in Counter(text).values())
        entropy = sum(-freq * log2(freq) / log2(2) for freq in char_freq)
        return entropy
