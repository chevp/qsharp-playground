import Std.Measurement.*;

operation Bell() : (Result, Result) {
    use (q0, q1) = (Qubit(), Qubit());
    H(q0);
    CNOT(q0, q1);
    return (MResetZ(q0), MResetZ(q1));
}
