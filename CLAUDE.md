# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Valideer is a lightweight Python data validation and adaptation library that provides:
- **Validation**: Check if values conform to defined schemas
- **Adaptation**: Convert valid input to appropriate output formats  
- **Declarative schemas**: Mini-language for defining validation rules
- **Extensibility**: Custom validators and adaptors

This is a **happybits fork** of the original podio/valideer with expanded Python version support.

## Development Commands

```bash
# Run tests (modern approach)
python -m unittest discover -s valideer/tests

# Run tests with coverage
coverage run --source=valideer -m unittest discover -s valideer/tests
coverage report

# Run tests across multiple Python versions
tox

# Install for development
pip install -e .

# Install from requirements (for dependent projects)
pip install git+https://github.com/happybits/valideer.git@main
```

## Installation in Other Projects

Add to `requirements.txt`:
```txt
git+https://github.com/happybits/valideer.git@main
```

Or pin to specific commit for reproducible builds:
```txt
git+https://github.com/happybits/valideer.git@42086f5
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

- **Framework**: Python unittest (single test file with 186 tests)
- **Coverage**: Comprehensive test coverage across all validators
- **Test Structure**: One large test file organized by validator type

## Dependencies

- **Runtime**: `decorator` package for function decoration
- **Development**: `coverage` for test coverage reporting
- **Python Versions**: 3.9, 3.10, 3.11, 3.12 (multi-version support)

## Migration Notes

This fork extends Python support from 3.10-only to 3.9-3.12. Key changes:
- Updated CI/CD to test across all supported Python versions
- Modernized test execution (unittest discover vs deprecated setup.py test)
- Updated repository URLs from podio/valideer to happybits/valideer
- Zero core library changes - migration achieved through configuration only