#! /usr/bin/env python

from pathlib import Path
import argparse
import yaml
# import sys
from srcfiles.system import ConSys


def run_config(path: Path, verbose=False):
    """
    runs the entire pipeline of the project. Only needs a path to
    a .yaml config file

    """
    assert path.suffix == '.yaml'

    with open(path, 'r') as file:
        config = yaml.safe_load(file)

    print(f'running config with relative path {path}')
    system = ConSys(config, verbose=verbose)

    system.train()

    system.eval()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a specific config file")
    parser.add_argument(
        'path',
        metavar='path',
        type=str,
        help="the path to config file"
    )
    parser.add_argument("-v", "--verbose", action='store_true')
    args = parser.parse_args()
    args.path = Path(args.path)

    run_config(args.path, args.verbose)
