# Git Team Workflow Demo

A minimal Python calculator for practicing branches, pull requests, code review,
follow-up commits, and merge commits with two GitHub accounts.

## Run

```sh
python calculator.py 8 2 add
```

Supported operations: `add`, `subtract`, `multiply`, `divide`.

## Roles

- Owner and reviewer: `shixing-wx`
- Contributor: `jlmyc`

One person operates both accounts for this exercise.

Division example: `python calculator.py 8 2 divide`.

## Error handling

A zero divisor (including -0.0) reports `Cannot divide by zero` and exits with
status 2, without a traceback.

## Tests

```sh
python -m unittest -v
```
