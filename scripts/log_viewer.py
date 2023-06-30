"""Loads events from a structured log file into a SimpleNamespace object"""
from argparse import ArgumentParser
import json

from types import SimpleNamespace


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    events = []

    with open(args.file, "r") as f:
        lines = f.readlines()
        for line in lines:
            event = json.loads(line, object_hook=lambda item: SimpleNamespace(**item))
            events.append(event)
