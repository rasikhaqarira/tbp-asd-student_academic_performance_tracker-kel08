from src.data_structures.graph_dag import GraphPrereq

class ModulKurikulum:
    def __init__(self, graph_obj=None):
        self.graph = graph_obj if graph_obj else GraphPrereq()

    def cek_urutan_matkul(self):
        return self.graph.topological_sort()

    def prasyarat_terpenuhi(self, bst_mhs, nim, kode_mk, grade_map):
        node_mhs = bst_mhs.search(nim)
        if not node_mhs:
            return False, "Mahasiswa tidak ditemukan"

        mhs = node_mhs.data if hasattr(node_mhs, 'data') else node_mhs

        prasyarat_list = []
        for asal, tujuan_list in self.graph.adj.items():
            if kode_mk in tujuan_list:
                prasyarat_list.append(asal)

        if not prasyarat_list:
            return True, "Bisa diambil (Tidak ada prasyarat)"

        nilai_mhs = {}
       transkripsi_obj = getattr(mhs, 'transkripsi', None)
        curr_nilai = transkripsi_obj.head if transkripsi_obj and hasattr(transkripsi_obj, 'head') else None

        while curr_nilai:
            nilai_mhs[curr_nilai.data.kode] = curr_nilai.data.nilai_huruf
            curr_nilai = curr_nilai.next

        grade_lulus = {"A", "A-", "B+", "B", "B-", "C+", "C"}

        for mk_prasyarat in prasyarat_list:
            if mk_prasyarat not in nilai_mhs:
                return False, f"Belum mengambil matkul prasyarat: {mk_prasyarat}"
            
            grade_didapat = nilai_mhs[mk_prasyarat]
            if grade_didapat not in grade_lulus:
                return False, f"Nilai {mk_prasyarat} adalah {grade_didapat} (Kurang dari C)"

        return True, "Semua prasyarat terpenuhi"
