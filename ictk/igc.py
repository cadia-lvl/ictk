#!/usr/bin/env python
"""
    ICTK: A collection of scripts to use with various Icelandic text corpora
    The Icelandic Gigaword Corpus (IGC) module
    Copyright (C) 2020 Mál- og raddtæknistofa Gervigreindarseturs HR - Language and Voice Lab
"""

import logging
from typing import List, Tuple, Iterable
from concurrent.futures import ProcessPoolExecutor
from xml.etree import ElementTree as ET

from tqdm import tqdm


log = logging.getLogger()

Token = str
Sentence = Tuple[Token, ...]
Corpus = Tuple[Sentence, ...]


def get_corpus(files: List[str], threads=1, chunksize=400) -> Iterable[Corpus]:
    """Read IGC files and extracts the tokens, including punctuations.

    Args:
        files: The list of IGC files to process.
        threads: The number of threads to use.
        chunksize: The number of files to send to each thread.
    Returns:
        An iterable of Corpus. Corpus=Tuple[Sentence], i.e. a sequence of sentences.
    """
    with ProcessPoolExecutor(max_workers=threads) as executor:
        results = tqdm(
            executor.map(get_corpus_from_file, files, chunksize=chunksize), total=len(files)
        )
        yield from results


def get_corpus_from_file(path: str) -> Corpus:
    """Read a single IGC file and returns a Corpus.
    
    Args:
        path: The file path to a single IGC file
    Returns:
        A Corpus. Corpus=Tuple[Sentence]
    """
    # Adjusted code from xml_tools.py from Róbert Kjaran <robert@kjaran.com>

    log.debug(f"Processing file={path}")
    NS = {"a": "http://www.tei-c.org/ns/1.0"}
    root = ET.parse(str(path)).getroot()
    # We gather all the paragraphs from the body, avoiding the divs
    return tuple(
        tuple(
            (
                token_node.text
                for token_node in sentence_node.findall("./*")
                if token_node.text is not None
            )
        )
        for paragraph_node in root.findall(".//a:body//a:p", NS)
        for sentence_node in paragraph_node.findall(".//a:s", NS)
    )
