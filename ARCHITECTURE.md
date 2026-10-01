# Architecture

## The complete pipeline

```text
Field description (plain text)
↓
field compiler (keyword → orders)
↓
refusal layer (hard constraints)
↓
order sequencer (timestamped tokens)
↓
seven-order decoder (principled synthesis)
↓
renderer (tuple → WAV)
↓
audio output
```

Every layer is named. Every boundary is explicit. No hidden state. No learned weights.

---

## The seven orders

Each order is a morphological operation on the substrate.

| Order | Waveform behavior |
|------|-------------------|
| CB1_identity | constant amplitude, root tone |
| CB2_extension | sine wave, forward motion |
| CB3_hook | sine plus short envelope, ornament |
| CB4_bass_open | low-frequency sine at reduced amplitude |
| CB5_loop | repeating sine, ostinato |
| CB6_compression | sine plus contractive envelope, tension |
| CB7_closure | sine plus rising envelope, resolution |

These seven operations generate the musical form.

---

## The decoder

The decoder takes order tokens and renders them into a deterministic mono signal.

```python
def decode_orders(orders, sample_rate=44100, total_samples=None):
    if total_samples is None:
        total_samples = max(token["start_sample"] + token["duration_samples"] for token in orders)

    signal = np.zeros(total_samples, dtype=np.float32)
    weights = np.zeros(total_samples, dtype=np.float32)

    for token in orders:
        order_name = token["name"]
        rendered = _render_order(order_name, token, sample_rate)
        start = token["start_sample"]
        stop = min(start + len(rendered), total_samples)

        signal[start:stop] += rendered[: stop - start]
        weights[start:stop] += 1.0

    signal = np.divide(signal, weights, out=np.zeros_like(signal), where=weights > 0)
    signal = np.clip(signal, -1.0, 1.0)
    return signal
```

What refuses:
- no hidden state
- no learned parameters
- unknown orders raise errors

What carries:
- orders
- sample rate
- optional total length

What is derived:
- a tuple or NumPy array of floating-point samples

What is next:
- the renderer converts the samples to WAV

---

## The overlap principle

When multiple orders overlap in time, the decoder averages their contributions:

```python
signal[start:stop] += rendered[: stop - start]
weights[start:stop] += 1.0
signal = np.divide(signal, weights, out=np.zeros_like(signal), where=weights > 0)
```

The result is a shared field, not an unbounded sum. This is the substrate principle in code.

---

## Refusal layer

Refusals are hard constraints. They are not suggestions.

```python
DEFAULT_REFUSALS = [
    "waltz", "disney", "princess", "cinderella", "pop",
    "ballroom", "happy", "upbeat", "bright", "cheerful",
]
```

The system rejects blocked words before synthesis begins.

---

## The full code

The complete system is in `field_generator.py`.

It is a single file. It is self-contained. It runs on any Python 3 environment with `numpy` and `scipy`.

---

## The two-line close

Return: Seven order channels. One decoder. One field. One output.

Next: Read `WHY.md` for why this exists.
