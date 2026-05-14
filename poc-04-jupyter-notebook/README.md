# poc-04-jupyter-notebook

Jupyter notebook hosting Q# via the modern `qsharp` package's `%%qsharp`
cell magic. Same engine as [poc-03](../poc-03-python-host/) — different
ergonomics, optimized for exploration and plotting.

## What's here

```
requirements.txt     ← qsharp + jupyter + matplotlib
bell.ipynb           ← notebook: register magic, define Q# op, run, plot histogram
```

## Prerequisites

- Python 3.10+

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab bell.ipynb
```

## How it differs from poc-03

- Q# source lives in `%%qsharp` cells instead of `.qs` files — re-evaluating
  a cell hot-patches the operation, which is the main reason notebooks are
  preferred for iterative work.
- `qsharp_widgets` provides interactive histogram and circuit-diagram widgets;
  the script in poc-03 prints text only.
- No `qsharp.eval(open(...))` boilerplate.

## Why this is not just "poc-03 in a notebook"

The notebook host swaps `qsharp.run` for `%%qsharp` and `qsharp.eval`-style
state. In particular, you do *not* re-`import qsharp` per cell — the kernel
holds a single Q# compilation context across the whole notebook.

## Reference

- [`qsharp` Jupyter integration](https://learn.microsoft.com/azure/quantum/install-overview-qdk#use-q-in-jupyter-notebooks)
- [`qsharp-widgets`](https://pypi.org/project/qsharp-widgets/)
