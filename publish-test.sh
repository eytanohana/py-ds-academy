#!/usr/bin/env bash
# ---------------------------------------------
# Publish the package to TEST PYPI
# ---------------------------------------------
# This script:
#   1. Loads credentials from .env (not committed)
#   2. Bumps the package version (patch/minor/major)
#   3. Commits + tags the new version
#   4. Rebuilds the package (clean dist/)
#   5. Uploads to TestPyPI using uv publish
# ---------------------------------------------

set -euo pipefail
# -e  : exit immediately on error
# -u  : error on undefined variables
# -o pipefail : make pipeline errors propagate

if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "Error: working tree not clean. Commit or stash changes first."
    exit 1
fi


# ---------------------------------------------
# Ensure no untracked files exist in src/
# ---------------------------------------------
if git ls-files --others --exclude-standard src/ | grep -q .; then
    echo "Error: untracked files detected in src/. Commit, delete, or ignore them."
    echo
    git ls-files --others --exclude-standard src/
    exit 1
fi


# ---------------------------------------------
# Run tests before releasing
# ---------------------------------------------
echo "Running tests..."
for v in 3.10 3.11 3.12 3.13 3.14; do
  echo "=== Testing Python $v ==="
  uv run --python "$v" pytest || exit 1
done
echo "✅ All tests passed."

# ---------------------------------------------
# Load environment variables securely
# ---------------------------------------------
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${SCRIPT_DIR}/.env"
if [ -f .env ]; then
    # set -a: automatically export all sourced variables
    # ensures UV_PUBLISH_* variables are available to uv
    set -a
    source "${ENV_FILE}"
    set +a
else
    echo "Error: .env file not found. Please create one with UV_PUBLISH_TEST_TOKEN."
    exit 1
fi

# ---------------------------------------------
# Determine bump level (default: patch)
# ---------------------------------------------
level="${1:-patch}"  # allow ./publish-test.sh or ./publish-test.sh minor
echo "Bumping package version level: ${level}"

# ---------------------------------------------
# Bump package version (updates pyproject.toml and uv.lock)
# ---------------------------------------------
uv version --bump="${level}"

# Grab the new version (without the leading v)
new_version="$(uv version --short)"
tag="v${new_version}"
echo "New version: ${new_version} (tag: ${tag})"

# ---------------------------------------------
# Commit and tag the new version
# ---------------------------------------------
git add pyproject.toml uv.lock
git commit --message "release: ${tag}"
git tag "${tag}"

# ---------------------------------------------
# Clean previous build artifacts
# ---------------------------------------------
echo "Cleaning dist/..."
rm -rf dist/

# ---------------------------------------------
# Build the package using uv's build backend
# ---------------------------------------------
echo "Building package..."
uv build

# ---------------------------------------------
# Publish to TEST PYPI
# ---------------------------------------------
echo "Publishing ${new_version} to TestPyPI..."
uv publish \
    --publish-url "https://test.pypi.org/legacy/" \
    --token "${UV_PUBLISH_TEST_TOKEN}" \
    dist/*

echo "✅ Successfully published ${new_version} to TestPyPI!"
