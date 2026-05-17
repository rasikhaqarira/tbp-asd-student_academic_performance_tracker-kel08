"""
Modul CLI - Command Line Interface
====================================
Perintah: CARI_MHS, INPUT_NILAI, UNDO_NILAI, TRANSKRIPSI,
          IPK, RANKING_IPK, FILTER_IPK, PRASYARAT_CEK,
          URUTAN_MATKUL, KELUAR
"""

from dll import NilaiMatkul, GRADE_MAP
from stack_undo import UndoRecord


def _hr(char='─', w=60): return char * w
def _ok(m): print(f"  [OK] {m}")
def _err(m): print(f"  [!]  {m}")
def _info(m): print(f"  »  {m}")
def _header(t):
    print(_hr('═'))
    print(f"  {t}")
    print(_hr('═'))


def _tampil_menu() -> None:
    """Tampilkan menu utama CLI."""
    print("\n" + _hr('='))
    print("   ACADEMIC PERFORMANCE TRACKER")
    print(_hr('='))
    print("  [1]  CARI_MHS      <nim>")
    print("  [2]  INPUT_NILAI   <nim> <kode> <sks> <grade> <sem>")
    print("  [3]  UNDO_NILAI    <nim>")
    print("  [4]  TRANSKRIPSI   <nim>")
    print("  [5]  IPK           <nim>")
    print("  [6]  RANKING_IPK")
    print("  [7]  FILTER_IPK    <min> <max>")
    print("  [8]  PRASYARAT_CEK <nim> <kode>")
    print("  [9]  URUTAN_MATKUL")
    print("  [0]  KELUAR")
    print(_hr('='))


def cmd_cari_mhs(bst, args):
    if len(args) < 1: return _err("Penggunaan: CARI_MHS <nim>")
    node = bst.search(args[0])
    if not node: return _err(f"NIM {args[0]} tidak ditemukan.")
    m = node.mhs
    _header(f"Data Mahasiswa – {m.nim}")
    _info(f"Nama     : {m.nama}")
    _info(f"Prodi    : {m.prodi}")
    _info(f"Angkatan : {m.angkatan}")
    _info(f"IPK      : {m.ipk:.2f}")


def cmd_input_nilai(bst, undo_stack, args):
    if len(args) < 5:
        return _err("Penggunaan: INPUT_NILAI <nim> <kode> <sks> <grade> <sem>")
    nim, kode, sks_s, grade, sem_s = args
    try:
        sks, sem = int(sks_s), int(sem_s)
    except ValueError:
        return _err("sks dan semester harus angka bulat.")
    node = bst.search(nim)
    if not node: return _err(f"NIM {nim} tidak ditemukan.")
    if grade not in GRADE_MAP:
        return _err(f"Grade '{grade}' tidak valid. Pilihan: {list(GRADE_MAP)}")
    node.transkripsi.tambah_nilai(NilaiMatkul(kode, kode, sks, grade, sem))
    ipk = bst.update_ipk(nim)
    undo_stack.push(UndoRecord(nim=nim, kode_mk=kode))
    _ok(f"Nilai {kode} (grade {grade}, {sks} sks, sem {sem}) ditambahkan.")
    _ok(f"IPK terbaru: {ipk:.2f}")


def cmd_undo_nilai(bst, undo_stack, args):
    if len(args) < 1: return _err("Penggunaan: UNDO_NILAI <nim>")
    nim = args[0]
    if undo_stack.is_empty(): return _err("Tidak ada operasi yang bisa di-undo.")
    rec = undo_stack.peek()
    if rec.nim != nim:
        return _err(f"Operasi terakhir bukan milik NIM {nim} (milik {rec.nim}).")
    undo_stack.pop()
    node = bst.search(nim)
    hapus = node.transkripsi.hapus_terakhir()
    if not hapus: return _err("Transkrip sudah kosong.")
    bst.update_ipk(nim)
    _ok(f"Nilai {hapus.kode_mk} (grade {hapus.grade}) di-undo dari {nim}.")
    _ok(f"IPK terbaru: {node.mhs.ipk:.2f}")


def cmd_transkripsi(bst, args):
    if len(args) < 1: return _err("Penggunaan: TRANSKRIPSI <nim>")
    node = bst.search(args[0])
    if not node: return _err(f"NIM {args[0]} tidak ditemukan.")
    semua = node.transkripsi.semua_nilai()
    _header(f"Transkrip – {args[0]} ({node.mhs.nama})")
    if not semua: return _info("(kosong)")
    print(f"  {'Kode':<12} {'MK':<20} {'SKS':>4} {'Grade':>6} {'Sem':>4}")
    print(_hr())
    for nm in semua:
        print(f"  {nm.kode_mk:<12} {nm.nama_mk:<20} {nm.sks:>4} {nm.grade:>6} {nm.semester:>4}")
    print(_hr())
    _info(f"IPK: {node.transkripsi.hitung_ipk():.2f}")


def cmd_ipk(bst, args):
    if len(args) < 1: return _err("Penggunaan: IPK <nim>")
    node = bst.search(args[0])
    if not node: return _err(f"NIM {args[0]} tidak ditemukan.")
    _ok(f"IPK {args[0]} ({node.mhs.nama}): {node.mhs.ipk:.2f}")


def _merge_sort_ipk(data):
    if len(data) <= 1: return data
    mid = len(data) // 2
    L, R = _merge_sort_ipk(data[:mid]), _merge_sort_ipk(data[mid:])
    hasil, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i].ipk >= R[j].ipk:
            hasil.append(L[i]); i += 1
        else:
            hasil.append(R[j]); j += 1
    return hasil + L[i:] + R[j:]


def cmd_ranking_ipk(bst):
    semua = bst.inorder()
    if not semua: return _err("Data kosong.")
    terurut = _merge_sort_ipk(semua)
    _header("Ranking IPK")
    print(f"  {'No':>3}  {'NIM':<12} {'Nama':<20} {'Prodi':<20} {'IPK':>5}")
    print(_hr())
    for i, m in enumerate(terurut, 1):
        print(f"  {i:>3}  {m.nim:<12} {m.nama:<20} {m.prodi:<20} {m.ipk:>5.2f}")


def cmd_filter_ipk(bst, args):
    if len(args) < 2: return _err("Penggunaan: FILTER_IPK <min> <max>")
    try:
        low, high = float(args[0]), float(args[1])
    except ValueError:
        return _err("min dan max harus angka.")
    hasil = bst.range_ipk(low, high)
    _header(f"Filter IPK [{low:.2f} – {high:.2f}]")
    if not hasil: return _info("Tidak ada mahasiswa dalam rentang tersebut.")
    for m in hasil:
        _info(f"{m.nim}  {m.nama:<20}  IPK: {m.ipk:.2f}")
    _info(f"Total: {len(hasil)} mahasiswa")


def cmd_prasyarat_cek(bst, graph, args):
    if len(args) < 2: return _err("Penggunaan: PRASYARAT_CEK <nim> <kode_mk>")
    nim, kode_mk = args
    node = bst.search(nim)
    if not node: return _err(f"NIM {nim} tidak ditemukan.")
    if kode_mk not in graph.adj: return _err(f"MK '{kode_mk}' tidak terdaftar.")
    if graph.prasyarat_terpenuhi(node, kode_mk):
        _ok(f"{nim} memenuhi semua prasyarat untuk {kode_mk}.")
    else:
        _err(f"{nim} BELUM memenuhi semua prasyarat untuk {kode_mk}.")


def cmd_urutan_matkul(graph):
    urutan = graph.topological_sort()
    _header("Urutan Pengambilan Matakuliah")
    if urutan is None:
        return _err("Terdeteksi siklus pada graph prasyarat!")
    for i, kode in enumerate(urutan, 1):
        _info(f"{i:>3}. {kode}  –  {graph.matkul.get(kode, kode)}")


def run_cli(bst, undo_stack, graph) -> None:
    """Loop utama CLI."""
    _tampil_menu()

    while True:
        try:
            raw = input("\n>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nKeluar.")
            break

        if not raw:
            _tampil_menu()
            continue

        # Izinkan input nomor menu
        menu_map = {
            '1': 'CARI_MHS', '2': 'INPUT_NILAI', '3': 'UNDO_NILAI',
            '4': 'TRANSKRIPSI', '5': 'IPK', '6': 'RANKING_IPK',
            '7': 'FILTER_IPK', '8': 'PRASYARAT_CEK', '9': 'URUTAN_MATKUL',
            '0': 'KELUAR',
        }
        parts = raw.split()
        if parts[0] in menu_map:
            parts[0] = menu_map[parts[0]]

        perintah = parts[0].upper()
        args = parts[1:]

        if perintah == "KELUAR":
            print("  Sampai jumpa!")
            break
        elif perintah == "CARI_MHS":
            cmd_cari_mhs(bst, args)
        elif perintah == "INPUT_NILAI":
            cmd_input_nilai(bst, undo_stack, args)
        elif perintah == "UNDO_NILAI":
            cmd_undo_nilai(bst, undo_stack, args)
        elif perintah == "TRANSKRIPSI":
            cmd_transkripsi(bst, args)
        elif perintah == "IPK":
            cmd_ipk(bst, args)
        elif perintah == "RANKING_IPK":
            cmd_ranking_ipk(bst)
        elif perintah == "FILTER_IPK":
            cmd_filter_ipk(bst, args)
        elif perintah == "PRASYARAT_CEK":
            cmd_prasyarat_cek(bst, graph, args)
        elif perintah == "URUTAN_MATKUL":
            cmd_urutan_matkul(graph)
        else:
            _err(f"Perintah '{perintah}' tidak dikenal.")

        _tampil_menu()