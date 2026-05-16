def jalankan_benchmark(self, dll_mhs_class, node_class, mhs_class):
        ukuran_uji = [20, 60, 200]
        prodi_pool = ["Teknik Elektro", "Informatika", "Mesin", "Sipil", "Kimia"]

        for n in ukuran_uji:
            list_m = dll_mhs_class()
            list_i = dll_mhs_class()

            for idx in range(n):
                mhs_mock = mhs_class(
                    nim=f"21{random.randint(100000, 999999)}",
                    nama=f"Mhs-{idx}",
                    prodi=random.choice(prodi_pool),
                    angkatan=random.choice([2021, 2022, 2023]),
                    ipk=round(random.uniform(2.0, 4.0), 2)
                )
                list_m.tambah_di_akhir(mhs_mock)
                
                node_ins = node_class(mhs_mock)
                if list_i.head is None:
                    list_i.head = list_i.tail = node_ins
                else:
                    node_ins.prev = list_i.tail
                    list_i.tail.next = node_ins
                    list_i.tail = node_ins

            t0 = time.perf_counter()
            list_m.head = self.merge_engine.sort(list_m.head)
            t_merge = (time.perf_counter() - t0) * 1000

            t1 = time.perf_counter()
            list_i.head = self.insertion_engine.sort(list_i.head)
            t_insert = (time.perf_counter() - t1) * 1000

            print(f"N: {n} -> Merge: {t_merge:.4f} ms | Insertion: {t_insert:.4f} ms")