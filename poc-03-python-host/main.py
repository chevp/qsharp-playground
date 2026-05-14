"""Run a Q# Bell-state experiment from Python via the modern qsharp package."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import qsharp

SHOTS = 1000


def main() -> None:
    qsharp.eval(Path("bell.qs").read_text())
    results = qsharp.run("Bell()", shots=SHOTS)
    histogram = Counter(tuple(map(str, r)) for r in results)
    print(f"shots={SHOTS}  histogram={dict(histogram)}")


if __name__ == "__main__":
    main()
