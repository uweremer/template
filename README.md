# template
Template repo for python projects


# Basic usage

Install [`pipx`](https://pypa.github.io/pipx/) and [`poetry`](https://python-poetry.org)

 ```
 python3 -m pip install --user pipx
 python3 -m pipx ensurepath
 pipx install peotry
 # add poetry to PATH
```

Next, customize [`pyproject.toml`](pyproject.toml) and install with poetry:

```
poetry install
```

Make sure to select the poetry env as kernel in VSCode: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  -> `Select Interpreter`