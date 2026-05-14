# poc-01-standalone-modern-qdk

Standalone Q# project using the **modern QDK** layout — no .NET, no Python.
Driven by `qsharp-project.json` and the VS Code Q# extension (or the
`qsharp` CLI from the modern Python package).

## What's here

```
qsharp.json          ← modern QDK project manifest (replaces .csproj)
src/
  Main.qs            ← entry point — Bell-state preparation and measurement
```

## Prerequisites

- VS Code with the official **Azure Quantum Development Kit** extension, OR
- Python 3.10+ with `pip install qsharp` (provides a CLI entry point too)

## Run

From VS Code: open `src/Main.qs`, click *Run Q# file* in the gutter.

From the CLI (via the Python package):

```sh
python -c "import qsharp; qsharp.eval(open('src/Main.qs').read()); print(qsharp.run('Main.RunBell()', shots=100))"
```

## What this POC is *not*

It does not show interop. Anything beyond running pure Q# (passing classical
data in/out, optimizing over results, plotting) belongs in poc-03 or poc-04.

## Reference

- [Modern QDK project structure](https://learn.microsoft.com/azure/quantum/how-to-modify-qsharp-projects)
