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

### `tempdir.root(dir, timeout=None)`

Creates a factory for temporary directories,
all of which will be under the directory `dir`.
Returns `Root`.

If `timeout` is set,
any sub-directories with an age greater than `timeout` seconds will be deleted on cleanup.
Cleanup occurs during `root.create_temp_dir()`,
and can also be triggered manually by calling `root.cleanup()`.
The age of a sub-directory is determined by the modification or access time,
whichever is later.

### `Root`

Has the following attributes:

* `create_temp_dir()`: creates a temporary directory in the same way as `tempman.create_temp_dir()`,
  except that the parent directory is always the directory of the `Root`.
  Also calls `cleanup()`.
  
* `cleanup()`: if `timeout` is set, delete old sub-directories as described above.

## Installation

```
pip install tempman
```
