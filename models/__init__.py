"""
creating a unique FileStorage instance
for the application.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

# calling reload() method on this var (task5).
storage.reload()
