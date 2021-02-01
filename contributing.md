# Contributing
If you would like to contribute to this repository please feel free to submit a pull request or open up an issue.

## Setting up
We use [poetry](https://python-poetry.org/) to manage dependencies. Simply create a new virtual environment and install the project by calling `poetry install`. To activate the environment call `poetry shell` and execute commands.

## Developer tools
In order to avoid bugs and different formatting, please use the following tools when writing source code in the project.
- `black` for formatting
- `pydocstyle` for warning when you are missing docstrings.

These tools (excluding `black`) will be run when a pull request is submitted and the build will fail if these tools complain.

## Running the tests
Just run (inside the virtual environment):
```
pytest
```
