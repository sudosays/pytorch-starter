# Pytorch ML Research Template

This is a starting point for doing ML research projects.

A lot of it is inspired by [this blog post](https://julienbeaulieu.github.io/2020/03/16/building-a-flexible-configuration-system-for-deep-learning-models/).

What you will need:

## Assumptions

* Data such as datasets or test results are stored in Pandas DataFrame files.  
* Analysis is done in Jupyter notebooks.   
* Configurations and metadata are stored in TOML files (JSON and INI also
possible).  

### Potential datasets used

https://www.kaggle.com/datasets/uciml/iris

## Setup

Create a virtual environment and activate it:

``` sh
virtualenv venv

source ./venv/bin/activate # use activate.fish for fish shell users
```

Install the requirements:

``` sh
pip install -r requirements.txt
```

## Workflow demo

Run the data preprocessing and segmentation:

``` sh
python preprocess.py --split=0.8 --separate-sets
```

## Overview of Files

TODO: Use `tree` to generate file structure below.

``` text
README.md
requirements.txt
analysis/
├── data-analysis-demo.ipynb
└── datavis-reference.ipynb
data/
├── datasets/
│   ├── external/
│   └── prepared-dataset/
│       ├── info.toml
│       ├── test.pkl
│       └── train.pkl
└── experiments/
    └── experiment-sample/
        ├── models/
        │   └── model-sample/
        │       ├── best-model.pth
        │       ├── config.toml
        │       ├── checkpoints/
        │       │   └── model-checkpoint-epoch-1.pth
        │       └── logs/
        └── results/
scripts/
├── preprocess.py
├── test.py
└── train.py
src/
├── config/
│   ├── config.py
│   └── default-config.toml
└── models/
    └── simple.py
```

### Data Layout and Organisation

The `$DATA` folder is self contained so that it can be synchronised and archived all in one go. 

#### Archiving and Synchronising the `$DATA` Folder


Using Rsync:
TODO

Creating a Tar archive:
TODO
