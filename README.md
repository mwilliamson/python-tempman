# Tempman: Create and clean up temporary directories

## API

### `tempdir.create_temp_dir()`

Creates a temporary directory and returns an instance of `TemporaryDirectory`.
The directory will be deleted when the instance of `TemporaryDirectory` is closed.

### `TemporaryDirectory`

Has the following attributes:

* `path` - path to the temporary directory
* `close()` - delete the temporary directory, including any files and sub-directories

`TemporaryDirectory` is a context manager,
so using `with` will also delete the temporary directory.

## Example

```python
import tempman

with tempman.create_temp_dir() as directory:
    assert os.path.exists(directory.path)
    assert os.path.isdir(directory.path)

assert not os.path.exists(directory.path)
```

## Installation

```
pip install tempman
```
