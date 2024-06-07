### `README.md`
# Template Poetry App

A simple application demonstrating sorting algorithms implemented in Python, using Poetry for dependency management and Tox for testing across multiple environments.

## Project Structure

```
template_poetry_app
├── pyproject.toml
├── README.md
├── src
│   ├── assets
│   │   └── assets.txt
│   ├── configs
│   │   └── config.ini
│   ├── data
│   │   └── data.csv
│   ├── logs
│   ├── template_poetry_app
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── bubble_sort.py
│   │   ├── merge_sort.py
│   │   ├── logger_setup.py
│   │   └── template_poetry_app.py
└── tests
    ├── __init__.py
    └── test_sorting_algorithms.py
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Poetry
- Tox

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/template_poetry_app.git
    cd template_poetry_app
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

### Configuration

The project uses a configuration file located at `src/configs/config.ini`. This file contains settings for the sorting algorithm and logger:

```ini
[settings]
sorting_algorithm = bubble_sort

[logger]
name = my_logger
logfile = app.log
logfile_path = ../logs
log_level = DEBUG
enable_console = true
```

### Running the Application

You can run the application using Poetry:

```bash
poetry run template_poetry_app
```

### Formatting Code

The project uses `black` for code formatting. To format the code, run:

```bash
poetry run flake8 ./src/template_poetry_app
poetry run pyre
poetry run black ./src/template_poetry_app
```

### Running Tests

The project uses `pytest` for testing and `tox` for running tests across multiple environments.

To run tests with `pytest`, use:

```bash
poetry run pytest
```

To run tests with `tox`, use:

```bash
poetry run tox
-OR-
tox
```

### Running Specific Test Environments with Tox

By default, `tox` will run tests in multiple environments specified in the `tox.ini` file. You can run tests in a specific environment by specifying it:

```bash
poetry run tox -e py312
```
