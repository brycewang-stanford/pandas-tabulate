# Contributing to pandas-tabulate

Thank you for your interest in contributing to pandas-tabulate! This document provides guidelines for contributing to the project.

## Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/pandas-tabulate.git
   cd pandas-tabulate
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Code Style

We use Black for code formatting and flake8 for linting:

```bash
black pandas_tabulate/ tests/
flake8 pandas_tabulate/ tests/
```

## Submitting Changes

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and add tests
3. Ensure tests pass and code is formatted
4. Commit your changes with a descriptive message
5. Push to your fork and submit a pull request

## Types of Contributions

- Bug fixes
- New statistical tests
- Performance improvements
- Documentation improvements
- Example additions

## Questions?

Open an issue on GitHub for questions or discussions.
