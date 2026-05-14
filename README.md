# tbp-asd-student_academic_performance_tracker-kel08
import numpy as np, time, random
from dataclasses import dataclass
form typing import Optinal, List, Dict, Tuple

np.random.seed(31)
random.seed(31)
PRODI = ['Teknik Elektro', 'Informasimatika', 'Mesin', 'Sipil', 'Kimia']
GRADE_MAP = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'D': 1.0, 'E': 0.0}

