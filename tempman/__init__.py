import tempfile
import shutil
import time
import os


def create_temp_dir(dir=None):
    path = tempfile.mkdtemp(dir=dir)
    return TemporaryDirectory(path)


class TemporaryDirectory(object):
    def __init__(self, path):
        self.path = path
        
    def close(self):
        shutil.rmtree(self.path)
    
    def __enter__(self):
        return self
        
    def __exit__(self, *args):
        self.close()


def root(dir, timeout=None):
    return Root(path=dir, timeout=timeout)
    
    
class Root(object):
    def __init__(self, path, timeout):
        self._path = path
        self._timeout = timeout
        
    def create_temp_dir(self):
        self._cleanup()
        
        return create_temp_dir(dir=self._path)

    def _cleanup(self):
        if self._timeout is not None:
            self._delete_directories_older_than_timeout()
            
    def _delete_directories_older_than_timeout(self):
        now = time.time()
        limit = now - self._timeout

        names = os.listdir(self._path)
        for name in names:
            path = os.path.join(self._path, name)
            stat = os.stat(path)
            
            if max(stat.st_atime, stat.st_mtime) < limit:
                shutil.rmtree(path)
