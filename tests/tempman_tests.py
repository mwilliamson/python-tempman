import os

from nose.tools import istest, assert_equal

import tempman


@istest
def temporary_directory_is_initially_empty():
    with tempman.create_temp_dir() as directory:
        assert_equal([], os.listdir(directory.path))


@istest
def temporary_directory_is_deleted_on_exit():
    with tempman.create_temp_dir() as directory:
        pass
        
    assert not os.path.exists(directory.path)


@istest
def temporary_directory_is_deleted_on_close():
    directory = tempman.create_temp_dir()
    directory.close()
    assert not os.path.exists(directory.path)
