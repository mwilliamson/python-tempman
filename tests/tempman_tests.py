import os
import time
from datetime import timedelta

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


@istest
def directories_older_than_integer_timeout_are_deleted_when_cleaning_up():
    _directories_older_than_timeout_are_deleted_when_cleaning_up(60)


@istest
def directories_older_than_float_timeout_are_deleted_when_cleaning_up():
    _directories_older_than_timeout_are_deleted_when_cleaning_up(60.0)


@istest
def timeout_can_be_specified_using_timedelta():
    _directories_older_than_timeout_are_deleted_when_cleaning_up(timedelta(minutes=1))


def _directories_older_than_timeout_are_deleted_when_cleaning_up(one_minute):
    with tempman.create_temp_dir() as parent_directory:
        root = tempman.root(parent_directory.path, timeout=one_minute)
        now = time.time()
        
        old_dir = os.path.join(parent_directory.path, "one")
        os.mkdir(old_dir)
        os.utime(old_dir, (now - 70, now - 70))
        
        newer_dir = os.path.join(parent_directory.path, "two")
        os.mkdir(newer_dir)
        os.utime(newer_dir, (now - 10, now - 10))
        
        root.cleanup()
        
        assert_equal(["two"], os.listdir(parent_directory.path))


@istest
def cleanup_occurs_when_creating_directory_under_root():
    with tempman.create_temp_dir() as parent_directory:
        root = tempman.root(parent_directory.path, timeout=60)
        now = time.time()
        
        old_dir = os.path.join(parent_directory.path, "one")
        os.mkdir(old_dir)
        os.utime(old_dir, (now - 70, now - 70))
        
        with root.create_temp_dir() as directory:
            pass
            
        assert_equal([], os.listdir(parent_directory.path))
