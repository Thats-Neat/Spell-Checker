import sys
import os
import time

functionPath = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.append(functionPath)

from wagner.algo import wagner_fischer

def testTwo():

    ex_output = 3

    start_time = time.time()

    instance = wagner_fischer()
    output = instance.wagner("saturday", "sunday")

    end_time = time.time()

    if output == ex_output:
        print(
            f"{__file__} ({instance.wagner.__qualname__}) (Took {end_time-start_time:.5f}s) (Expected: {ex_output} -> Got: {output}) - PASS")
    else:
        print(
            f"{__file__} ({instance.__qualname__}) (Took {end_time-start_time:.5f}s) (Expected: {ex_output} -> Got: {output}) - FAILED")
