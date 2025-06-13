# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Valideer is a lightweight Python data validation and adaptation library that provides:
- **Validation**: Check if values conform to defined schemas
- **Adaptation**: Convert valid input to appropriate output formats  
- **Declarative schemas**: Mini-language for defining validation rules
- **Extensibility**: Custom validators and adaptors

## Development Commands

```bash
# Run tests
python setup.py test

# Run tests with coverage via tox
tox

# Install in development mode
python setup.py install

# Run tests with coverage (CI approach)
coverage run --source=valideer setup.py test
coverage report
```

## Code Architecture

### Core Components

- **`valideer/base.py`** - Core validation framework containing:
  - `Validator` base class and validation infrastructure
  - `ValidationError` and `SchemaError` exception classes
  - Function decorators: `@accepts`, `@returns`, `@adapts`
  - Schema parsing and error formatting

- **`valideer/validators.py`** - Built-in validator implementations:
  - Primitive validators: `Boolean`, `Integer`, `Number`, `String`
  - Collection validators: `Mapping`, `Sequence`, `Set`
  - Temporal validators: `Date`, `Time`, `Datetime`
  - Composite validators: `AnyOf`, `AllOf`, `ChainOf`, `Nullable`, `Range`

- **`valideer/compat.py`** - Python 3 compatibility utilities

### Key Patterns

- **Validator Registration**: Validators auto-register using `Validator.__init_subclass__`
- **Schema Parsing**: String schemas are parsed into validator instances via `parse()`
- **Error Context**: Validation errors include path context showing where validation failed
- **Adaptation Pattern**: Validators can both validate and transform data

### Testing

- **Framework**: Python unittest (single test file with 171 tests)
- **Coverage**: Comprehensive test coverage across all validators
- **Test Structure**: One large test file organized by validator type

## Dependencies

- **Runtime**: `decorator` package for function decoration
- **Development**: `coverage` for test coverage reporting
- **Python Version**: 3.10 (recently migrated)