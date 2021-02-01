"""Useful tools and abstractions for working with BÍN."""
from collections import defaultdict
from typing import Sequence


class BIN:
    """Ensculptures the BÍN csv file using the SHsnid.

    The fields are:
        The look up word (when using a dictionary).
        The ID.
        Part of speech or noun gender.
        The section of BÍN it is found in.
        Inflection form.
        Grammatical analysis (i.e. tag).

    The tags and part of speech are not the same as with the official PoS (markamengi) for Icelandic.
    """

    def __init__(self, lines: Sequence[str]) -> None:
        """Parse the lines."""
        self.entries = 0
        self._from_form = defaultdict(set)
        self._from_lemma = defaultdict(set)
        for line in lines:
            self.entries += 1
            lemma, id, gen_pos, section, form, tag = line.strip().split(";")
            self._from_form[form].add((lemma, id, gen_pos, section, tag))
            self._from_lemma[lemma].add((form, id, gen_pos, section, tag))

    @staticmethod
    def from_file(path: str):
        """Initialize BIN from a file."""
        with open(path) as f:
            return BIN(tuple(f))
