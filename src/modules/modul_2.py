# modules/modul_2.py
from data_structures.bst import BSTMahasiswa

class ModulDatabase:
    def __init__(self, database_obj=None):
        self.db = database_obj if database_obj else BSTMahasiswa()

    def simpan_mahasiswa(self, mahasiswa_obj):
        self.db.insert(mahasiswa_obj)

    def cari_mahasiswa(self, nim):
        return self.db.search(nim)

    def cari_by_nim(self, nim):
        return self.cari_mahasiswa(nim)

    def ambil_semua_data(self):
        if hasattr(self.db, 'get_inorder_list'):
            return self.db.get_inorder_list()
        return self.db.inorder()

    def perbarui_ipk_mhs(self, nim, grade_map=None):
        # Disesuaikan dengan bst.py yang baru (tidak perlu melempar grade_map lagi)
        return self.db.update_ipk(nim)

    def filter_berdasarkan_rentang_ipk(self, low, high):
        return self.db.range_ipk(low, high)