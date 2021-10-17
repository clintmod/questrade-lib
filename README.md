# questrade-report

Generates a report of Questrade accounts

## Prerequisites

- Grab a questrade api access code
https://www.questrade.com/api/documentation/getting-started

- Put the access code in a file called `access_code.txt` next to this README.md

- Install poetry
https://python-poetry.org/docs/#installation

## Setup

Run setup if this is your first time or you change pyproject.toml

```
make setup
```

## Running the program

- To fetch the data and generate the report just run:

```
make
```

- If you just want to fetch the data run:

```
make fetch
```

- If you just want to generate the report based on the existing data:

```
make report
```
