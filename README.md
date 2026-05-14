# q-sharp-playground

Q# proof-of-concepts exploring **hosting and interop patterns** for the
[Microsoft Quantum Development Kit (QDK)](https://learn.microsoft.com/azure/quantum/).

## Status

**Scaffold only.** None of the POCs are built or run by CI — each exists to
document the file layout, project metadata, and minimum host code for one
specific way of running Q#. They are reference templates, not finished apps.

## Why Q# integration is non-trivial

Q# is a domain-specific language for quantum computation. It cannot meaningfully
run on its own — every useful program has a *host* that drives the quantum
operations, collects results, and (for variational/hybrid workloads) closes a
classical optimization loop around them. The QDK ships in two generations:

- **Classic QDK** (`Microsoft.Quantum.Sdk` MSBuild SDK, `IQ#` Jupyter kernel,
  `qsharp` 0.x Python package). Strongly coupled to .NET; rich C# interop.
- **Modern QDK** (`qsharp` 1.x Python package, `qsharp-project.json`,
  VS Code extension). .NET-free; standardizes on Python/Jupyter/VS Code.

The six POCs below cover the practical host targets that exist today.

## POCs

| Folder | Pattern | Trade-offs |
|---|---|---|
| [poc-01-standalone-modern-qdk](poc-01-standalone-modern-qdk/) | Modern QDK standalone project (`qsharp-project.json` + `src/*.qs`) | Lowest setup cost. No .NET, no Python. Run from VS Code or the `qsharp` CLI |
| [poc-02-csharp-host](poc-02-csharp-host/) | Classic QDK with `Microsoft.Quantum.Sdk` and a C# host calling Q# operations | Richest interop and tooling, but pulls in the entire .NET SDK and the deprecated 0.x QDK |
| [poc-03-python-host](poc-03-python-host/) | Modern `qsharp` Python package — `qsharp.eval` / `qsharp.run` from a script | The recommended host for new work. Best fit for ML/optimization wrappers |
| [poc-04-jupyter-notebook](poc-04-jupyter-notebook/) | Jupyter notebook using the modern `qsharp` package's `%%qsharp` magic | Same engine as poc-03; optimized for exploration and result visualization |
| [poc-05-azure-quantum](poc-05-azure-quantum/) | Submit Q# programs to Azure Quantum providers (IonQ, Quantinuum, Rigetti) or the Resource Estimator | Only path to real hardware. Requires an Azure subscription and workspace |
| [poc-06-min-launcher](poc-06-min-launcher/) | Smallest possible standalone Q# program — single `.qs` file, no host | Minimum reproducer for bug reports; not a viable project layout |

## Run

Each POC has its own README with toolchain prerequisites and the exact commands
to run it. Nothing in this repo builds top-down — there is no workspace file.

## Reference

- [Modern QDK overview](https://learn.microsoft.com/azure/quantum/install-overview-qdk)
- [Q# language reference](https://learn.microsoft.com/azure/quantum/user-guide/)
- [Azure Quantum providers](https://learn.microsoft.com/azure/quantum/qc-target-list)
