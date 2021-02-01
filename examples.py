"""Example usage of the Python library."""
from ictk import igc

# A single file reading
igc_file = "tests/igc_test_file.txt"
parsed = igc.get_corpus_from_file(igc_file)
for line in parsed:
    print(line)
    # ('Fyrirlestraröð', 'Framfara', 'stendur', 'fyrir', 'fyrirlestri', 'um', 'ástæður', 'ofþjálfunar', ',', 'einkenni', 'og', 'meðferð', '.')
    # ...

# Multi-file, multi-threaded reading two per thread.
corpora = igc.get_corpus([igc_file] * 10, threads=2, chunksize=2)
# Each corpus is a single file.
for corpus in corpora:
    for line in corpus:
        print(line)
        # ('Fyrirlestraröð', 'Framfara', 'stendur', 'fyrir', 'fyrirlestri', 'um', 'ástæður', 'ofþjálfunar', ',', 'einkenni', 'og', 'meðferð', '.')
        # ...
