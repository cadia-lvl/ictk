#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection of tests for ``ictk/igc.py``.

ICTK: A collection of scripts to use with various Icelandic text corpora.
Copyright (C) 2020 Mál- og raddtæknistofa Gervigreindarseturs HR - Language and Voice Lab
"""

from ictk import igc


def test_igc_parsing():
    """Test whether a single IGC file is parsed correctly."""
    result = igc.get_corpus_from_file("./tests/igc_test_file.txt")
    # fmt: off
    assert result == (
        ("Fyrirlestraröð", "Framfara", "stendur", "fyrir", "fyrirlestri", "um", "ástæður", "ofþjálfunar", ",", "einkenni", "og", "meðferð", "."),
        ("Hættir", "fólki", "af", "ákveðinni", "persónugerð", "við", "ofþjálfun", "meira", "en", "öðrum", "?"),
        ("Hvaða", "áhrif", "hafa", "næring", ",", "svefn", "og", "hvíld", "?"),
        ("Stund", "og", "staður", ":"),
        ("Fimmtudaginn", "22.", "nóvember", "2012", "kl.", "19:30", "–", "21:00", "."),
        ("Íþróttamiðstöðin", "Laugardal", ",", "salur", "D."),
        ("Fyrirlesarar", ":"),
        ("Þórarinn", "Sveinsson", ",", "Dr.", "í", "lífeðlisfræði", ",", "dósent", "við", "HÍ"),
        ("Fríða", "Rún", "Þórðardóttir", ",", "MSc", "í", "næringarfræði", ",", "íþróttanæringarfræðingur"),
        ("Hafrún", "Kristjánsdóttir", ",", "Ma.", "í", "sálfræði", ",", "dósent", "við", "HR"),
        ("Aðgangseyrir", "er", "1000", "kr", "og", "rennur", "óskiptur", "til", "Framfara", ",", "hollvinafélags", "millivegalengda", "-", "og", "langhlaupara", "."),
    )
    # fmt: on
