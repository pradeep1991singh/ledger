import os

from ledger.stores import store_utils
from ledger.stores.file_store import FileStore


class TextFileStore(FileStore):

    def __init__(self,
                 dbDir,
                 dbName,
                 isLineNoKey: bool=False,
                 storeContentHash: bool=True,
                 ensureDurability: bool=True):
        super().__init__(dbDir, dbName, isLineNoKey,
                         storeContentHash, ensureDurability)
        self._initDB(dbDir, dbName)

    def _initDB(self, dbDir, dbName):
        super()._initDB(dbDir, dbName)
        self.dbPath = os.path.join(os.path.expanduser(dbDir), dbName)
        self.dbFile = open(self.dbPath, mode="a+")

    def _getLines(self):
        self.dbFile.seek(0)
        return store_utils.cleanLines(self.dbFile)
