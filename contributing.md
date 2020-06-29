# Contributing
If you would like to contribute to this repository please feel free to submit a pull request or open up an issue.

## Developer tools
In order to avoid bugs and different formatting, please use the following tools when writing source code in the project.
- `black` for formatting
- `flake8` for linting
- `pydocstyle` for warning when you are missing docstrings.
- `mypy` for static type checking.

These tools (excluding `black`) will be run when a pull request is submitted and the build will fail if these tools complain.

## Running the tests
Just run:
```
pytest
```
