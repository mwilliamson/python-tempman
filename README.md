# Tempman: Create and clean up temporary directories

## Example

```python
import tempman

with tempman.create_temp_dir() as directory:
    assert os.path.exists(directory.path)
    assert os.path.isdir(directory.path)

assert not os.path.exists(directory.path)
```

## API

### `tempdir.create_temp_dir(dir=None)`

Creates a temporary directory and returns an instance of `TemporaryDirectory`.
The directory will be deleted when the instance of `TemporaryDirectory` is closed.

If `dir` is set,
the temporary directory is created as a sub-directory of `dir`.

### `TemporaryDirectory`

Has the following attributes:

* `path` - path to the temporary directory
* `close()` - delete the temporary directory, including any files and sub-directories

`TemporaryDirectory` is a context manager,
so using `with` will also delete the temporary directory.

### `tempdir.root(dir)`

Creates a factory for temporary directories,
all of which will be under the directory `dir`.
Returns `Root`.

### `Root`

Has the following attributes:

* `create_temp_dir()`: creates a temporary directory in the same way as `tempman.create_temp_dir()`,
  except that the parent directory is always the directory of the `Root`.

## Installation

```
pip install tempman
```
