/// # Sample
/// Bell-state preparation and measurement — the "hello world" of Q#.
/// Demonstrates entanglement: measuring one qubit collapses the other
/// to the same value, so RunBell always returns (Zero, Zero) or (One, One).

import Std.Diagnostics.*;
import Std.Measurement.*;

operation Main() : (Result, Result) {
    RunBell()
}

operation RunBell() : (Result, Result) {
    use (q0, q1) = (Qubit(), Qubit());
    H(q0);
    CNOT(q0, q1);
    let r0 = MResetZ(q0);
    let r1 = MResetZ(q1);
    return (r0, r1);
}
