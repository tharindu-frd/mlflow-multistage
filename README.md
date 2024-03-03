```bash
conda create --prefix ./env python=3.7 -y
conda activate ./env
conda env export > conda.yaml

```

## After creating main.py

```bash

mlflow run .
mlflow ui

```
