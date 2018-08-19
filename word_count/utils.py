import re


def count_word_frequency(word, source):
    """Counts a word's frequency in an string"""
    pattern = r'\b{}\b'.format(word)
    matches = re.findall(pattern, source, re.IGNORECASE)
    return len(matches) if matches else 0
