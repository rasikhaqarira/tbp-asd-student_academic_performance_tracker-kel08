from src.data_structures.dll import TranskripNilai

class ModulTranskrip:
    def __init__(self):
        self.transkrip = TranskripNilai()

    def tambah_entri_nilai(self, node_mhs, matkul_obj, grade_map):
        # 1. Tambah nilai ke Linked List
        self.transkrip.tambah_nilai(matkul_obj)
        
        # 2. Hitung IPK terbaru
        ipk_sekarang = self.transkrip.hitung_ipk(grade_map)
        
        # 3. Update IPK di objek mahasiswa (Cek 'data' atau 'mhs')
        if node_mhs:
            # Cek apakah pakenya .data atau .mhs
            target = getattr(node_mhs, 'data', getattr(node_mhs, 'mhs', None))
            if target and hasattr(target, 'ipk'):
                target.ipk = ipk_sekarang
            
        return ipk_sekarang

    def hitung_ipk(self, grade_map):
        return self.transkrip.hitung_ipk(grade_map)

