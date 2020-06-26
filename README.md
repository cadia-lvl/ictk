<h1 align="center">
The Icelandic Corpora Toolkit
</h1>

<p align="center"><i>
  A collection of scripts to use with various Icelandic text corpora. <br/>
  Center for Analysis and Design of Intelligent Agents, Language and Voice Lab <br/>
  Reykjavik University - School of Computer Science, Menntavegur 1, IS-101 Reykjavik, Iceland
</i></p>

<img src="https://user-images.githubusercontent.com/9976294/85858541-54e7f600-b7ab-11ea-9347-c400d0b7a6e9.png" alt="Cover Image" align="center"/>

## Table of Contents
<!-- ⛔️ MD-MAGIC-EXAMPLE:START (TOC:collapse=true&collapseText=Click to expand) -->
<details>
<summary>Click to expand</summary>

* [Introduction](#introduction)
* [Corpora](#corpora)
* [Example of Usage](#example-of-usage)
* [Contributors](#contributors)
* [License](#license)
* [References](#references)

</details>
<!-- ⛔️ MD-MAGIC-EXAMPLE:END -->

## Introduction

The Icelandic Corpora Toolkit is a  collection of scripts to use with various Icelandic text corpora.

## Corpora

There are two main sources of corpora available for Icelandic:

* <https://clarin.is/>
* <http://malfong.is/>


## Example of Usage

### Reading the IGC
The IGC is distributed as a collection of .xml files in the tei format. We provide a tool to parse these files and write (some of) the content to a file.

- The command takes as a first argument a file (or stdin, using `-`) with a single filepath in each line.
- The second argument is a file to write the parsed files.
```
find /data/risamalheild/2018/rmh1 -type f \( -name "*.xml" -not -name "hdr?.xml" \) | \
  ./main.py read-rmh - rmh.txt --threads 2 --chunksize 400
```
This will prase all `.xml` files, excluding the header files, in the directory `/data/risamalheild/2018/rmh1` using 2 threads and processing 400 files at once. The output is written to `rmh.txt`.

## Contributors
<a href="https://github.com/cadia-lvl/ictk/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=cadia-lvl/ictk" />
</a>
<!-- Made with [contributors-img](https://contributors-img.web.app). -->

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Contributing
If you would like to contribute to this repository please feel free to submit a pull request or open up an issue.

#### Developer tools
In order to avoid bugs and different formatting, please use the following tools when writing source code in the project.
- `black` for formatting
- `flake8` for linting
- `pydocstyle` for warning when you are missing docstrings.
- `mypy` for static type checking.

These tools (excluding `black`) will be run when a pull request is submitted and the build will fail if these tools complain.

#### Running the tests
Just run:
```
pytest
```

## References

<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>