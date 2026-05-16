import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.pure_queue import PureQueue

def test_singly_linked_list_queue(
    queue = PureQueue()
    
    queue.enqueue("Data_A")
    queue.enqueue("Data_B")
    
    assert queue.is_empty() == False
    
    param1 = queue.dequeue()
    assert param1 == "Data_A"
    
    param2 = queue.dequeue()
    assert param2 == "Data_B"
    
    assert queue.is_empty() == True
    print(f"FIFO Queue Check: {param1} -> {param2} | Status: PASSED")

if __name__ == "__main__":
    test_singly_linked_list_queue()