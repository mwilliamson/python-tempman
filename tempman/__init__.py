import tempfile
import shutil


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


def root(dir):
    return Root(path=dir)
    
    
class Root(object):
    def __init__(self, path):
        self._path = path
        
    def create_temp_dir(self):
        return create_temp_dir(dir=self._path)
