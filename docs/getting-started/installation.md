# Installation

## Requirements

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Using uv (Recommended)

[uv](https://docs.astral.sh/uv/) is a fast Python package installer and resolver written in Rust.

### Install uv

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install py-ds-academy

```bash
# Clone the repository
git clone https://github.com/eytanohana/py-ds-academy.git
cd py-ds-academy

# Create virtual environment
uv venv

# Install dependencies
uv sync
```

## Using pip

```bash
# Clone the repository
git clone https://github.com/eytanohana/py-ds-academy.git
cd py-ds-academy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

## Verify Installation

```bash
# Run tests
uv run pytest  # or: pytest

# Try importing
uv run python -c "from py_ds import Stack, Queue, MinHeap; print('Installation successful!')"
```

## Development Setup

For development, install with dev dependencies:

```bash
# Using uv
uv sync --group dev

# Using pip
pip install -e ".[dev]"
```

This includes:
- `pytest` - Testing framework
- `ruff` - Linting and formatting
- `pre-commit` - Git hooks
- `mkdocs-material` - Documentation

## Next Steps

- Read the [Quick Start Guide](quickstart.md) to begin using the library
- Explore the [Data Structures Overview](../structures.md)
- Check out the [API Reference](../reference/api.md)
