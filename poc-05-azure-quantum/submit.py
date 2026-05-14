"""Submit the Bell-state Q# program to an Azure Quantum hardware target.

Fill in RESOURCE_ID and LOCATION from the workspace overview page in the
Azure portal before running. Credentials come from `az login`.
"""

from __future__ import annotations

from pathlib import Path

import qsharp
from azure.quantum import Workspace

RESOURCE_ID = "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Quantum/Workspaces/<workspace>"
LOCATION = "westus"
TARGET = "ionq.simulator"  # swap for "ionq.qpu", "quantinuum.qpu.h1-1", etc.
SHOTS = 100


def main() -> None:
    workspace = Workspace(resource_id=RESOURCE_ID, location=LOCATION)
    qsharp.init(target_profile=qsharp.TargetProfile.Base)
    qsharp.eval(Path("bell.qs").read_text())

    program = qsharp.compile("Bell()")
    target = workspace.get_targets(TARGET)
    job = target.submit(program, name="bell-poc", shots=SHOTS)
    print(f"submitted: {job.id}  status={job.details.status}")

    job.wait_until_completed()
    print(f"results: {job.get_results()}")


if __name__ == "__main__":
    main()
