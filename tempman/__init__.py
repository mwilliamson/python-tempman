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
