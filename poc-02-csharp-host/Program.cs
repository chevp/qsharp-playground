// C# host that drives the Q# Bell-state operation defined in Quantum.qs.
//
// The Microsoft.Quantum.Sdk build target generates a C# class `Bell` from
// the Q# `operation Bell()` declaration. We instantiate the simulator (which
// implements IOperationFactory) and dispatch the operation against it.

using System;
using System.Threading.Tasks;
using Microsoft.Quantum.Simulation.Core;
using Microsoft.Quantum.Simulation.Simulators;
using QSharpPlayground.CSharpHost;

internal static class Program
{
    private static async Task<int> Main()
    {
        const int shots = 100;
        var matches = 0;

        using var sim = new QuantumSimulator();
        for (var i = 0; i < shots; i++)
        {
            var (r0, r1) = await Bell.Run(sim);
            if (r0 == r1) matches++;
        }

        Console.WriteLine($"Bell agreement: {matches}/{shots} (expected 100/100)");
        return matches == shots ? 0 : 1;
    }
}
