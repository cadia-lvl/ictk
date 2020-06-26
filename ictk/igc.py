import logging
from typing import List, Tuple, Iterable
from concurrent.futures import ProcessPoolExecutor
from xml.etree import ElementTree as ET

from tqdm import tqdm


log = logging.getLogger()

Token = str
Sentence = Tuple[Token, ...]
Corpus = Tuple[Sentence, ...]


def read_rmh_file(path: str) -> Corpus:
    """
    Reads a single RMH file and returns a TokCorpus.

    Adjusted code from xml_tools.py from Róbert Kjaran <robert@kjaran.com>
    """
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


def read_rmh(files: List[str], threads=1, chunksize=400) -> Iterable[Corpus]:
    """Reads RMH files and extracts the tokens, including punctuations.

    Args:
        files: The list of RMH files to process.
        threads: The number of threads to use.
        chunksize: The number of files to send to each thread.
    Returns:
        An iterable of Corpus. Corpus=Tuple[Sentence], i.e. a sequence of sentences.
    """
    with ProcessPoolExecutor(max_workers=threads) as executor:
        results = tqdm(
            executor.map(read_rmh_file, files, chunksize=chunksize), total=len(files)
        )
        yield from results
