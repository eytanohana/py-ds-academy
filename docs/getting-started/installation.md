# Installation

## Requirements

- Python 3.10 or higher
- pip (Python's package installer)

## Install from PyPI

### Using pip

The easiest way to install [py-ds-academy](https://pypi.org/project/py-ds-academy) is using pip:

```bash
pip install py-ds-academy
```

#### Using a Virtual Environment (Recommended)

Virtual environments help keep your project isolated and avoid conflicts with other packages installed on your system:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install py-ds-academy
pip install py-ds-academy
```

### Using uv

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver written in Rust. It's great for both installing packages and managing development environments.

**Install uv:**

Follow the steps in [uv's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for your OS.

**Install py-ds-academy:**

```bash
# create a new project managed by uv
uv init my-project

# enter your project directory
cd my-project

# Install the package
uv add py-ds-academy
```

## Verify Installation

```python
# Try importing
import py_ds

print(py_ds.__version__)
```

## Next Steps

- Read the [Quick Start Guide](quickstart.md) to begin using the library
- Explore the [Data Structures Overview](../structures/index.md)
- Check out the [API Reference](../reference/index.md)

## Development Installation

If you want to contribute to the project or work with the source code, see the [Contributing Guide](../contributing.md) for instructions on setting up a development environment.
