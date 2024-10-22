<h1 align="center">
The Icelandic Corpora Toolkit
</h1>

<p align="center"><i>
  A collection of scripts to use with various Icelandic text corpora. <br/>
  Center for Analysis and Design of Intelligent Agents, Language and Voice Lab <br/>
  Reykjavik University - School of Computer Science, Menntavegur 1, IS-101 Reykjavik, Iceland
</i></p>

<img src="https://user-images.githubusercontent.com/9976294/85869930-e65f6400-b7bb-11ea-8c53-196d1ec83189.png" alt="Cover Image" align="center"/>

<!-- Logo using: -->
<!-- <div>Icons made by <a href="https://www.flaticon.com/authors/photo3idea-studio" title="photo3idea_studio">photo3idea_studio</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div> -->

## Table of Contents
<!-- ⛔️ MD-MAGIC-EXAMPLE:START (TOC:collapse=true&collapseText=Click to expand) -->
<details>
<summary>Click to expand</summary>

* [Introduction](#introduction)
* [Corpora](#corpora)
* [Setup](#setup)
* [Example of Usage](#example-of-usage)
* [Contributors](#contributors)
* [License](#license)
* [References](#references)

</details>
<!-- ⛔️ MD-MAGIC-EXAMPLE:END -->

## Introduction

The Icelandic Corpora Toolkit is a  collection of scripts to use with various Icelandic text corpora.

## Setup
Install via pip (from master branch)
```
pip install git+https://github.com/cadia-lvl/ictk.git@master
```

## Example of Usage
The tool can be used as a terminal line client or as a Python library.

### Reading the IGC
The IGC is distributed as a collection of .xml files in the tei format. We provide a tool to parse these files and write (some of) the content to a file. If you need additional fields, please submit an issue.

#### Python
From `examples.py`
```Python
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

```
#### Terminal client
- The command takes as a first argument a file (or stdin, using `-`) with a multiple filepaths.
- The second argument is a file to write the parsed files.
```
find /data/risamalheild/2018/rmh1 -type f \( -name "*.xml" -not -name "*Hdr.xml" \) | \
  ictk read-igc - igc.txt --threads 2 --chunksize 400
```
This will prase all `.xml` files, excluding the header files, in the directory `/data/risamalheild/2018/rmh1` using 2 threads and processing 400 files at once. The output is written to `igc.txt`.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Corpora

There are two main sources of corpora available for Icelandic:

* <https://clarin.is/>
* <http://malfong.is/>


## References

<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>

## Contributors
<a href="https://github.com/cadia-lvl/ictk/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=cadia-lvl/ictk" />
</a>
<!-- Made with [contributors-img](https://contributors-img.web.app). -->

## [Contributing](contributing.md)
