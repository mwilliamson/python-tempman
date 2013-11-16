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


@istest
def dir_argument_can_be_used_to_set_parent_directory():
    with tempman.create_temp_dir() as parent_directory:
        with tempman.create_temp_dir(dir=parent_directory.path) as directory:
            assert_equal([os.path.basename(directory.path)], os.listdir(parent_directory.path))


@istest
def using_root_to_create_temporary_directories_creates_directories_under_root_path():
    with tempman.create_temp_dir() as parent_directory:
        root = tempman.root(parent_directory.path)
        with root.create_temp_dir() as directory:
            assert_equal([os.path.basename(directory.path)], os.listdir(parent_directory.path))
