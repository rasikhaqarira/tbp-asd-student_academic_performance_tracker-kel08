# modules/modul_3.py
from data_structures.stack_undo import Stack

class ModulUndo:
    def __init__(self, stack_obj=None):
        self.history = stack_obj if stack_obj else Stack()

    def catat_log(self, nim):
        self.history.push(nim)

    def batalkan_aksi(self, bst_obj, grade_map):
        nim = self.history.pop()
        if not nim:
            return False, None
        
        node_mhs = bst_obj.search(nim)
        if node_mhs and node_mhs.transkripsi:
            node_mhs.transkripsi.hapus_terakhir()
            
            if hasattr(node_mhs.mhs, 'ipk'):
                node_mhs.mhs.ipk = node_mhs.transkripsi.hitung_ipk(grade_map)
            
            return True, nim
        
        return False, nim