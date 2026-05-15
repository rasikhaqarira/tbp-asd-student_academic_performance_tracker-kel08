from src.data_structures.bst import BSTMahasiswa

class ModulDatabase:
    def __init__(self, database_obj=None):
        self.db = database_obj if database_obj else BSTMahasiswa()

    def simpan_mahasiswa(self, mahasiswa_obj):
        self.db.insert(mahasiswa_obj)

    def cari_mahasiswa(self, nim):
        return self.db.search(nim)

    # ALIAS khusus untuk memenuhi panggilan dari test_bst.py
    def cari_by_nim(self, nim):
        return self.cari_mahasiswa(nim)

    def ambil_semua_data(self):
        # Memastikan memanggil fungsi inorder yang ada di bst.py
        if hasattr(self.db, 'get_inorder_list'):
            return self.db.get_inorder_list()
        return self.db.inorder()