A Python project template

# Basic usage

1. Clone/download this repository.

2. Install [`pipx`](https://pypa.github.io/pipx/) and [`poetry`](https://python-poetry.org)

    ```
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    pipx install peotry
    # add poetry to PATH
    ```

3. Next, customize [`pyproject.toml`](pyproject.toml) and install with poetry:

    ```
    poetry install
    ```

    Make sure to select the poetry env as kernel in VSCode: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  -> `Select Interpreter`

   | Note: Update dependencies in `pyproject.toml` after `poetry update`. Also update versions in `pre-commit-config.yaml`.

## Config.ini

Create a new `config.ini` based on the [config.ini.template](config.ini.template).

## Use pre-commits for clean code

[`pre-commit`](https://pre-commit.com/) is installed as part of the dev dependencies. Run `pre commit` from cli to execute pre-commits hook to sort, format and lint the code.
