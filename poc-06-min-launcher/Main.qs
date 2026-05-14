import Std.Measurement.*;

operation Main() : Result {
    use q = Qubit();
    H(q);
    return MResetZ(q);
}
