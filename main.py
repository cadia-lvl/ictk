#!/usr/bin/env python
"""The package console entry point."""
import logging

import click

from ictk import igc

log = logging.getLogger()


@click.group()
def cli():
    """Entrypoint of the click client. Other commands are attached to this group."""
    pass


@cli.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.option("--threads", type=int, default=1, help="Number of threads to use.")
@click.option(
    "--chunksize", type=int, default=400, help="Number of files to process per thread."
)
def read_rmh(input, output, threads, chunksize):
    """Parse a list of xml files using the tei format tailored for RMH, extracts all sentences and writes to a file.

    Each RMH file contains some metadata which is ignored.
    Each RMH contains many paragraps, which contain many sentences, which contain many tokens.
    Paragraphs are flattened to sentences.

    See read_rmh --help for a full list of arguments and options.

    Args:
        files: The list of files to process.
        output: The file to write the results to. Use "-" for STDOUT.
    """
    files = [line.strip() for line in input]
    log.info(f"Processing RMH. Number of files={len(files)}")
    for corpus in igc.read_rmh(files, threads=threads, chunksize=chunksize):
        for sentence in corpus:
            output.write(" ".join(sentence) + "\n")
    log.info("Done.")


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    cli()
