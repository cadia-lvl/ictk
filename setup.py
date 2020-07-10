import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    print("ICTK requires Python >= 3.6")
    sys.exit(1)

setup(
    name='ictk',
    version='0.0.1',
    author="Language and Voice Lab",
    author_email="lvl@ru.is",
    description="A collection of scripts to use with various Icelandic text corpora.",
    long_description="ICTK is a collection of scripts to use with various Icelandic text corpora.",
    url="https://github.com/cadia-lvl/ictk",
	include_package_data=True,
    install_requires=[
        'click',
		'tqdm'
    ],
    entry_points='''
        [console_scripts]
        ictk=ictk.main:cli
    ''',
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Natural Language :: Icelandic",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords=["ictk", "lvl", "nlp", "corpus", "corpora", "icelandic"],
    python_requires='>=3.6',
)