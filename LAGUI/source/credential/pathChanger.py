def imp(path):
    import sys
    import os

    parrentdir = os.path.dirname(
        os.path.dirname(os.path.relpath(__file__)))
    sys.path.append(parrentdir+path)
