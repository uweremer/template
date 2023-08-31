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

    Note: to remove a poetry env, tpye: `rm -rf $(poetry config virtualenvs.path)/*`


## Config.ini

Create a new `config.ini` based on the [config.ini.template](config.ini.template).


## Use pre-commits for clean code

[`pre-commit`](https://pre-commit.com/) is installed as part of the dev dependencies. Run `pre commit` from cli to execute pre-commits hook to sort, format and lint the code.


## Database usage

If you want to use PostgreSQL as database, fire up a docker environment e.g. as provided in the `compose.yaml`:

```sh
sudo service docker start
sudo docker-compose -f compose.yaml --env-file config.ini up -d
```

Don't forget to provide the credentials within the `config.ini`.

## Convenience startup for development

If everything is prepared as suggested above , use the script [`start.sh`](start.sh) to:
- start docker service
- stop and clean up all containers
- clean the (otherwise) persistent database volume
- initialize containers

```sh
chmod +x start.sh
./start.sh
```
