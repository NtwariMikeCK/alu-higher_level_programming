#!/usr/bin/python3
import marshal
import types

def main():
    with open('hidden_4.pyc', 'rb') as f:
        f.seek(16)  # Skip the header of the .pyc file
        code = marshal.load(f)
        module = types.ModuleType('hidden_4')
        exec(code, module.__dict__)

    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()
