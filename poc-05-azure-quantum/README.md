# poc-05-azure-quantum

Submit Q# programs to **Azure Quantum** — either a real hardware provider
(IonQ, Quantinuum, Rigetti) or the **Resource Estimator** target that
returns a logical-qubit / T-gate cost breakdown without executing.

## What's here

```
requirements.txt     ← qsharp + azure-quantum
bell.qs              ← same Bell op as poc-03, just retargeted
submit.py            ← Python host: connect, set target, submit, poll, print
estimate.py          ← Python host: run the Resource Estimator instead
```

## Prerequisites

- Python 3.10+
- An Azure subscription with an [Azure Quantum workspace](https://learn.microsoft.com/azure/quantum/how-to-create-workspace) provisioned

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
az login   # the azure-quantum SDK reuses the az CLI's credential cache
```

## Run — Resource Estimator (free, no hardware queue)

```sh
python estimate.py
```

Prints logical qubit counts, T-state counts, and physical-qubit estimates
for the chosen error budget. This is the **first thing to run** for any
algorithm — it tells you whether the program is even feasible on near-term
hardware before you spend a hardware credit on it.

## Run — submit to hardware (incurs Azure Quantum charges)

Edit `submit.py` to fill in `RESOURCE_ID` and `LOCATION` from your workspace
overview page, choose a target, then:

```sh
python submit.py
```

The script polls until the job completes and prints the result histogram.

## Status

**Untested against a live workspace.** The connection-string boilerplate is
correct as of `azure-quantum` 2.x but no run has been recorded here —
production use needs at minimum: cost-cap configuration, target availability
checks, and a retry strategy for the queue.

## Reference

- [Azure Quantum submission quickstart](https://learn.microsoft.com/azure/quantum/how-to-submit-jobs)
- [Azure Quantum Resource Estimator](https://learn.microsoft.com/azure/quantum/intro-to-resource-estimation)
