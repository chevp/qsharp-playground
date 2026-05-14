"""Run the Azure Quantum Resource Estimator against the Bell-state program.

This does not contact Azure — the estimator ships in the local `qsharp`
package. It returns a fault-tolerant cost breakdown that would otherwise
require running on a real machine to discover.
"""

from __future__ import annotations

import json
from pathlib import Path

import qsharp


def main() -> None:
    qsharp.eval(Path("bell.qs").read_text())
    estimate = qsharp.estimate("Bell()")
    summary = {
        "logical_qubits": estimate["physicalCounts"]["breakdown"]["algorithmicLogicalQubits"],
        "t_states": estimate["physicalCounts"]["breakdown"]["numTstates"],
        "physical_qubits": estimate["physicalCounts"]["physicalQubits"],
        "runtime_ns": estimate["physicalCounts"]["runtime"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
