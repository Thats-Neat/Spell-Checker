import sys
import os

functionPath = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.append(functionPath)

from wagner.algo import wagner_fischer

def testOne():
    instance = wagner_fischer()

    test = instance.wagner("float", "boats")

    print(test)
