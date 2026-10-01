import hashlib
from pathlib import Path

import numpy as np
from scipy.io import wavfile

from field_generator import DESCRIPTION, generate, check_refusals


def test_refusal_list_blocks_terms():
    for term in ["cinderella", "pop", "happy", "princess"]:
        try:
            check_refusals(term)
            assert False, f"Expected refusal on {term}"
        except ValueError:
            pass


def test_generate_creates_valid_wav(tmp_path):
    output = tmp_path / "output.wav"
    result = generate(DESCRIPTION, str(output))

    assert result == str(output)
    assert output.exists()

    rate, data = wavfile.read(str(output))
    assert rate == 44100
    assert data.size > 0
    assert np.isfinite(data).all()
    assert data.dtype.kind in {"i", "f"}


def test_determinism_same_description_same_output(tmp_path):
    out1 = tmp_path / "one.wav"
    out2 = tmp_path / "two.wav"

    generate(DESCRIPTION, str(out1))
    generate(DESCRIPTION, str(out2))

    a = hashlib.sha256(out1.read_bytes()).hexdigest()
    b = hashlib.sha256(out2.read_bytes()).hexdigest()
    assert a == b


def test_generate_rejects_blocked_input(tmp_path):
    blocked = "A bright cheerful princess ballad"
    try:
        generate(blocked, str(tmp_path / "bad.wav"))
        assert False, "Expected ValueError for blocked description"
    except ValueError:
        pass
