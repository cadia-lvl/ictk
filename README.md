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

<!-- omit in toc -->
## Table of Contents

<details>
<summary>Click to expand</summary>

- [1. Introduction](#1-introduction)
  - [1.1. Corpora](#11-corpora)
- [2. Setup](#2-setup)
- [3. Example of Usage](#3-example-of-usage)
- [4. License](#4-license)
- [5. References](#5-references)
- [6. Contributors](#6-contributors)
</details>

## 1. Introduction

The Icelandic Corpora Toolkit is a  collection of scripts to use with various Icelandic text corpora.

### 1.1. Corpora

There are two main sources of corpora available for Icelandic:

- <https://clarin.is/>
- <http://malfong.is/>

## 2. Setup


<details>
<summary>Linux and macOS</summary>

Create a virtual enviroment

```
$ pyton3 -m venv ./venv python=3.6
$ . ./venv/scripts/activate
(venv) $
```

Install required modules

```
(venv) $ pip install -e .

Try to run it

```
(venv) $ ictk --version
ICTK 1.0.0
```
</details>


<details>
<summary>Windows</summary>
Create a virtual enviroment

```
C:\Users\USER>c:\Python36\python -m venv c:\Python36\venv
C:\Users\USER>c:\Python36\venv\Scripts\activate.bat
(venv) C:\Users\USER>
```

Install required modules

```
(venv) C:\Users\USER>pip install -e .
```

Try to run it

```
(venv) C:\Users\USER>ictk --version
ICTK 1.0.0
```
</details>


## 3. Example of Usage

- [The Icelandic Gigaword Corpus (IGC)](./examples/igc.md)

## 4. License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 5. References

## 6. Contributors
<a href="https://github.com/cadia-lvl/ictk/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=cadia-lvl/ictk" />
</a>
<!-- Made with [contributors-img](https://contributors-img.web.app). -->

[Become a contributor](contributing.md)

<p align="center">
🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
</p>
