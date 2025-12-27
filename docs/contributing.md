# Contributing

Thank you for your interest in contributing to py-ds-academy! This document provides guidelines and instructions for contributing.

## Getting Started

### Fork and Clone the Repository

1. **Fork the repository** on GitHub by clicking the "Fork" button
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/py-ds-academy.git

   cd py-ds-academy
   ```

### Set Up the Development Environment

#### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver written in Rust.

**Install uv:**

Follow the steps in [uv's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for your OS.

**Set up the project:**
```bash
# Create the venv and install dependencies (including dev and doc dependencies)
uv sync --all-groups

# Install pre-commit hooks (required before development)
pre-commit install
```

When you install with `--all-groups`, you get:

- `pytest` - Testing framework
- `ruff` - Linting and formatting
- `pre-commit` - Git hooks for code quality
- `mkdocs-material` - Documentation generation

### Verify Development Setup

```bash
# Run tests
pytest

# Run linting
ruff check .

# Try importing
python -c "from py_ds import Stack, Queue, LinkedList; print('Development setup successful!')"
```

## Development Workflow

1. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the project's coding standards

3. **Write or update tests** for your changes

4. **Ensure all tests pass:**
   ```bash
   pytest
   ```

5. **Run linting and formatting:**
   ```bash
   ruff check .  # or `ruff check --fix .` for fixable lint errors
   ruff format .
   ```

6. **Commit your changes** with clear commit messages

7. **Push to your fork** and create a Pull Request

## Coding Standards

### Type Hints

All code should include type hints:

```python
def push(self, item: int) -> None:
    """Push an item onto the stack."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def pop(self) -> int:
    """Pop and return the top item.
    
    Returns:
        The top item from the stack.
        
    Raises:
        IndexError: If the stack is empty.
    """
    ...
```

### Code Style

- Follow PEP 8 guidelines
- Use `ruff` for linting and formatting
- Maximum line length: 120 characters
- Use single quotes for strings

### Testing

- Write tests for all new functionality
- Aim for high test coverage
- Use descriptive test names
- Follow the existing test structure

## Project Structure

```
py-ds-academy/
├── src/py_ds/          # Source code
├── tests/              # Test files
├── docs/               # Documentation
└── pyproject.toml      # Project configuration
```

## Adding a New Data Structure

1. Create the implementation in `src/py_ds/datastructures/`
2. Add exports to `src/py_ds/__init__.py`
3. Write comprehensive tests in `tests/`
4. Add documentation in `docs/structures/`
5. Update `docs/structures.md` overview
6. add api reference in `docs/reference/`
7. add documentation in `docs/reference/api.md`
8. Update the README if needed

## Documentation

### Updating Documentation

When updating documentation, you may need to update multiple files:

1. **Update the relevant documentation file** in `docs/`:
   - Structure guides: `docs/structures/`
   - Reference docs: `docs/reference/`
   - Getting started: `docs/getting-started/`

2. **Update `mkdocs.yml`** if you:
   - Add a new documentation page
   - Rename or move a documentation file
   - Change the navigation structure

   The `mkdocs.yml` file controls the site navigation. Make sure your new or updated pages are included in the `nav` section with the correct path.

   Example: If you add a new file `docs/structures/new-structure.md`, add it to the navigation:
   ```yaml
   nav:
     - Data Structures:
         - Overview: structures.md
         - New Structure: structures/new-structure.md
   ```

3. **Update API reference** if you:
   - Add new classes or methods
   - Change method signatures
   - Add new modules

   API reference pages use `mkdocstrings` to auto-generate from docstrings. Ensure your docstrings are properly formatted.

### Documentation Guidelines

- Keep documentation up to date with code changes
- Add examples for new features
- Update API reference when adding new methods
- Use clear, concise language
- Test code examples to ensure they work

### Previewing Documentation

To preview your documentation changes locally:

```bash
# Serve the documentation site locally
mkdocs serve
```

Visit `http://127.0.0.1:8000` to view the site.

## Pull Request Process

1. Ensure your PR addresses a specific issue or adds a feature
2. Include tests for new functionality
3. Update documentation as needed (including `mkdocs.yml` if navigation changes)
4. Ensure all CI checks pass
5. Request review from maintainers

## Questions?

If you have questions or need help, please:

- Open an issue on GitHub
- Check existing issues and discussions
- Review the documentation

Thank you for contributing! 🎉
