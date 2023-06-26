"""train.py aims to be a comprehensive and opinionated utility script for training PyTorch models.

Basic operation:

1. Parse the program arguments.
2. Resolve the configuration of the script.
3. Setup and start logging.
4. Setup the experiment information and directory.
5. Load the dataset.
6. Setup the model for training.
7. Call ``train()``.

Caveats:

- The ``--log-level`` argument only filters the messages logged to ``stdout``.
- If there is already an experiment in the $DATA_ROOT with the same label,
  the experiment label will be modified unless ``--from-checkpoint`` is specified.

For more information run ``python train.py --help``.
"""

from argparse import ArgumentParser, Namespace
from configparser import ConfigParser

from datetime import datetime

import os

import json
from types import SimpleNamespace

DATA_ROOT = os.path.join(os.getcwd(), "data")


def get_args() -> Namespace:
    """Setup the argument parser and parse the args."""
    parser = ArgumentParser(description="A utility script for training PyTorch models")
    parser.add_argument("--exp-label", default=None, help="Label for the experiment")
    parser.add_argument(
        "--data-root", default=DATA_ROOT, help="Path to the root of the $DATA directory"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Set the logging level.",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
    )
    parser.add_argument("--gpu", default=None, help="Specify a CUDA device to use")
    parser.add_argument(
        "--from-checkpoint",
        default=None,
        help="Start training from a given checkpoint.",
    )

    return parser.parse_args()


def configure(args):
    """Resolve the configuration from args and config files
    :returns: a configuration
    """

    # Do some magic to encode the arguments dict into a nested SimpleNamespace
    # vars(args) converts the argparse.Namespace into a dict
    # object_hook calls the SimpleNamespace constructor on every object
    # WARNING! objects must be serializable for this to work
    return json.loads(
        json.dumps(vars(args)), object_hook=lambda item: SimpleNamespace(**item)
    )


def train(cuda_device=None, experiment_label=None, epochs=100, dataset=None):
    """Trains a model for a given number of epochs and configuration"""
    pass


if __name__ == "__main__":
    # setup and parse the script args
    args = get_args()
    log_msg = {
        "timestamp": datetime.now().astimezone().isoformat(),
        "message": "arguments supplied to the script.",
        "args": vars(args),
    }

    print(json.dumps(log_msg))

    config = configure(args)
    log_msg = {
        "timestamp": datetime.now().astimezone().isoformat(),
        "message": "final configuration information.",
        "config": vars(config),
    }
    print(json.dumps(log_msg))
    # load any applicable config files

    # merge the args and config

    pass
