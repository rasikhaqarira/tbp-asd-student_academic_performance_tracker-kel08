# modules/modul_1.py
from dll import TranskripNilai

class ModulTranskrip:
    def __init__(self):
        pass 

    def tambah_entri_nilai(self, node_mhs, matkul_obj, grade_map):
        if not node_mhs:
            return 0.0
            
        target_mhs = getattr(node_mhs, 'data', getattr(node_mhs, 'mhs', None))
        
        if not hasattr(target_mhs, 'transkripsi') or target_mhs.transkripsi is None:
            target_mhs.transkripsi = TranskripNilai()
            
        target_mhs.transkripsi.tambah_nilai(matkul_obj)
        
        ipk_sekarang = target_mhs.transkripsi.hitung_ipk(grade_map)
        
        if hasattr(target_mhs, 'ipk'):
            target_mhs.ipk = ipk_sekarang
            
        return ipk_sekarang

    def hitung_ipk_mhs(self, node_mhs, grade_map):
        target_mhs = getattr(node_mhs, 'data', getattr(node_mhs, 'mhs', None))
        if target_mhs and hasattr(target_mhs, 'transkripsi') and target_mhs.transkripsi:
            return target_mhs.transkripsi.hitung_ipk(grade_map)
        return 0.0