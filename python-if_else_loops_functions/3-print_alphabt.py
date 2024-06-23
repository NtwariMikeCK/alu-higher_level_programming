#!/usr/bin/python3
print("".join("{:c}".format(c) for c in range(ord('a'), ord('z') + 1) if c not in [ord('q'), ord('e')]), end="")

