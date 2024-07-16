#!/usr/bin/python3


"""This is for creating a new python read function"""
def read_file(filename):
    """start by defining the function"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
