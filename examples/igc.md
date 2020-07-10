<h1 align="center">
Example of Usage <br/>
The Icelandic Gigaword Corpus (IGC)
</h1>

<!-- omit in toc -->
## Introduction

The Icelandic Corpora Toolkit is a collection of scripts to use with various Icelandic text corpora. 

Here below are some of the most common examples of usage.

<details>
<summary>List of all examples</summary>

- [1. Extracting plain text from IGC](#1-extracting-plain-text-from-igc)
</details>

## 1. Extracting plain text from IGC
The IGC is distributed as a collection of .xml files in the tei format. 
ICTK provides a script that takes these files and writes (some of) the content to an output file.

<details>
<summary>Terra User (A cloud cluster at LVL)</summary>

- The command takes as a first argument a file (or stdin, using `-`) with a single file path in each line.
- The second argument is a file to write the parsed files.

```consoles
find /data/risamalheild/2018/rmh1 -type f \( -name "*.xml" -not -name "hdr?.xml" \) | ictk read-rmh - rmh.txt --threads 16 --chunksize 400
```
This will prase all `.xml` files, excluding the header files, in the directory `/data/risamalheild/2018/rmh1` using 16 threads and processing 400 files. The output is written to `rmh.txt`.

</details>

<details>
<summary>Non-Terra User</summary>

Make sure you 

- The command takes as a first argument a file (or stdin, using `-`) with a single file path in each line.
- The second argument is the output file to write the parsed data.

```consoles
$ find rmh/ -type f \( -name "*.xml" -not -name "hdr?.xml" \) | ictk read-igc - rmh.txt --threads 2 --chunksize 400
```
This will prase all `.xml` files, excluding the header files, in the directory `rmh` using 2 threads and processing 400 files at once. The output is written to `rmh.txt`.

</details>