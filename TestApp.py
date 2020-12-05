import pytest
from main import  StartProcess
def Checktitle():
    assert str(StartProcess()) == "startprocess - A Code Genrator", "Should be startprocess - A Code Genrator"

if __name__ == "__main__":
    Checktitle()
    print("Everything passed")