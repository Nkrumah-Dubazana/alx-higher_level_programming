#!/usr/bin/python3
"""Prints the alphabet in lowercase, not follwed by a new line."""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end = "")
