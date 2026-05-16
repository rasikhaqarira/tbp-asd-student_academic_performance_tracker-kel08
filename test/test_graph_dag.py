import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from src.data_structures.graph_dag import GraphPrereq 
from src.modules.modul_4 import ModulKurikulum 

def test_topo_sort():
    print("\n--- Testing Modul 4: Graph Topological Sort ---")
    g = GraphPrereq()
    mod4 = ModulKurikulum(g)
    
    g.add_edge("Matdis", "ASD")
    g.add_edge("ASD", "Strukdat")
    
    urutan = mod4.cek_urutan_matkul()
    assert urutan == ["Matdis", "ASD", "Strukdat"]
    print(f"Urutan Matkul: {' -> '.join(urutan)} | Status: PASSED")

if _name_ == "_main_":
    test_topo_sort()