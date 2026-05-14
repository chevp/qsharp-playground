# poc-02-csharp-host

C# .NET application hosting Q# operations through the **classic QDK** —
the `Microsoft.Quantum.Sdk` MSBuild SDK auto-generates C# stubs for every
Q# `operation`, which the host invokes against the QuantumSimulator.

## What's here

```
Host.csproj          ← Microsoft.Quantum.Sdk project (classic QDK 0.x)
Program.cs           ← C# host: builds a simulator, calls Bell.Run, prints results
Quantum.qs           ← Q# operations exposed to the host
```

## Status

**Classic QDK is in maintenance.** Microsoft now points new users at the modern
QDK ([poc-01](../poc-01-standalone-modern-qdk/), [poc-03](../poc-03-python-host/)),
which has no C# host story. This POC stays here because:

- existing .NET codebases with quantum sub-modules use this pattern, and
- the C# ↔ Q# interop is genuinely cleaner than the modern Python path when
  the host already lives in .NET.

## Prerequisites

- .NET SDK 6.0 (the last LTS supported by the classic QDK)
- `dotnet new -i Microsoft.Quantum.ProjectTemplates`

## Run

```sh
dotnet run --project Host.csproj
```

## How interop works

`Microsoft.Quantum.Sdk` post-processes the build to emit, for every Q#
`operation Foo(...)`, a sibling C# class `Foo` with `.Run(IOperationFactory)`.
The host instantiates `QuantumSimulator` (which implements `IOperationFactory`)
and calls `.Run(...).Result` to execute on it.

```csharp
using var sim = new QuantumSimulator();
var (r0, r1) = await Bell.Run(sim);
```

The `Bell` symbol comes from the auto-generated C#; there is no manual binding
step. This is the main ergonomic advantage over the modern QDK's Python host.

## Reference

- [Classic QDK C# host quickstart](https://learn.microsoft.com/previous-versions/azure/quantum/install-csharp-qdk)
