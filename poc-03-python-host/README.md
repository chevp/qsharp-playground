# poc-03-python-host

Python script that hosts Q# via the **modern `qsharp` package** —
the recommended path for new work as of QDK 1.x.

## What's here

```
requirements.txt     ← pinned qsharp + numpy
bell.qs              ← Q# operation source
main.py              ← Python host: loads bell.qs, runs 1000 shots, prints histogram
```

## Prerequisites

- Python 3.10+

```sh
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```sh
python main.py
```

Expected output (modulo simulator randomness):

```
{('Zero', 'Zero'): ~500, ('One', 'One'): ~500}
```

## How interop works

The modern QDK has no codegen step. The host loads Q# source as text via
`qsharp.eval(...)` (or `qsharp.init(project_root=...)` for project layouts),
then invokes named operations with `qsharp.run("Op.Name()", shots=N)`.

```python
import qsharp
qsharp.eval(open("bell.qs").read())
results = qsharp.run("Bell()", shots=1000)
```

Compared to poc-02's C# host: lighter setup, no .NET, but classical data
shuttling is string-based (Q# expression text) rather than typed method calls.

## Reference

- [Modern QDK Python package](https://pypi.org/project/qsharp/)
- [`qsharp.run` API](https://learn.microsoft.com/python/qsharp-core/qsharp)
