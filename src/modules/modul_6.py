# modules/modul_6.py

class ModulAnalisisRingkasan:
    """Modul Tambahan untuk Ringkasan Data Dashboard Mahasiswa"""
    def __init__(self):
        pass

    def ringkasan_dashboard(self, bst_obj):
        all_nodes = bst_obj.inorder()
        if not all_nodes:
            print("\n[Dashboard] Belum ada data mahasiswa di database.")
            return

        total_mhs = len(all_nodes)
        tertinggi = all_nodes[0].mhs
        terendah = all_nodes[0].mhs
        total_ipk = 0

        for node in all_nodes:
            mhs = node.mhs
            total_ipk += mhs.ipk
            if mhs.ipk > tertinggi.ipk: tertinggi = mhs
            if mhs.ipk < terendah.ipk: terendah = mhs

        rata_rata = total_ipk / total_mhs

        print("\n" + "="*40)
        print("      DASHBOARD STATISTIK AKADEMIK      ")
        print("="*40)
        print(f"Total Mahasiswa Terdaftar : {total_mhs}")
        print(f"Rata-rata IPK Universitas : {rata_rata:.2f}")
        print(f"IPK Tertinggi            : {tertinggi.ipk} ({tertinggi.nama} - {tertinggi.nim})")
        print(f"IPK Terendah             : {terendah.ipk} ({terendah.nama} - {terendah.nim})")
        print("="*40)