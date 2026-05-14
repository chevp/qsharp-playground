# poc-06-min-launcher

The smallest possible standalone Q# program — one file, no project manifest,
no host. Mirrors the role of `poc-06-min-launcher` in [rust-playground][rp]:
a minimum reproducer template for bug reports against the QDK toolchain.

[rp]: https://github.com/chevp/rust-playground/tree/main/poc-06-min-launcher

## What's here

```
Main.qs              ← single-file Q# program — measures one qubit in the |+⟩ state
```

## Run

VS Code Q# extension: open `Main.qs` and click *Run Q# file*.

From a Python shell (modern QDK):

```sh
python -c "import qsharp; qsharp.eval(open('Main.qs').read()); print(qsharp.run('Main()', shots=20))"
```

## Why this is *not* a viable project layout

- No `qsharp.json` ⇒ no project lints, no dependencies, no namespace isolation.
- Cannot be imported by another Q# file.
- Cannot be packaged for Azure Quantum submission without first promoting it.

Use this layout only for one-off reproducers. For anything else, copy
[poc-01](../poc-01-standalone-modern-qdk/).
