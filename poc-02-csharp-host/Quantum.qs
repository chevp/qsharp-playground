namespace QSharpPlayground.CSharpHost {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    /// Prepares a Bell pair and returns the two measurement outcomes.
    operation Bell() : (Result, Result) {
        use (q0, q1) = (Qubit(), Qubit());
        H(q0);
        CNOT(q0, q1);
        let r0 = MResetZ(q0);
        let r1 = MResetZ(q1);
        return (r0, r1);
    }
}
