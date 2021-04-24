def imp(path):
    import sys
    import os

    parrentdir = os.path.dirname(
        os.path.dirname(os.path.relpath(__file__)))

    print(parrentdir)
    sys.path.append(parrentdir+path)
    print(sys.path)
