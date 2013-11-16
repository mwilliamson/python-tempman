import tempfile
import shutil


def create_temp_dir():
    path = tempfile.mkdtemp()
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
