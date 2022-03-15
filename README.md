# Python Boilerplate

[![Made by The Data Shed](docs/ds-badge.svg)](https://thedatashed.co.uk)

[![Security Status](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)



<p align="center">
<a href="https://pypi.python.org/pypi/python_boilerplate">
    <img src="https://img.shields.io/pypi/v/python_boilerplate.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/KingMichaelPark/python_boilerplate/actions">
    <img src="https://github.com/KingMichaelPark/python_boilerplate/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">
</a>




</p>


Python Boilerplate contains all the boilerplate you need to create a Python package.
-   Free software: MIT license

## Documentation

Is generated using `mkdocs` and will update on release as long as the pages option is turned on
for the repo, and setting the branch to build from as the root directory of `gh-pages`

- [Documentation](https://KingMichaelPark.github.io/python_boilerplate)


## Getting started

Activate your virtualenv:

```bash
source venv/bin/activate
# Run your tests
pytest
# Run on multple versions
tox
# See other commands in the make file like building docs etc...
```

### Bumping versions:

```bash
# On main
bump2version <patch | minor | major>
git push
git push --tags
```



## Features

-   TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [KingMichaelPark/cookiecutter-pypackage](https://github.com/KingMichaelPark/cookiecutter-pypackage) project template.
