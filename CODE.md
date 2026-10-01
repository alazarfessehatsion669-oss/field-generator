# The code

The complete project is in `field_generator.py`.

## Setup

```bash
pip install numpy scipy
```

Run:

```bash
python field_generator.py
```

## Edit the description

Change the `DESCRIPTION` constant near the top of the file:

```python
DESCRIPTION = """
Ancient royal dark fantasy. Two voices, gold and purple.
Hands that almost touch. Slow, ceremonial. Deep, heavy, ancient.
Never Cinderella.
"""
```

## Output

The script writes `output.wav` in the same directory. In notebooks or terminal execute contexts, it can also play inline if the environment supports audio playback.

## What the generator does

1. normalizes the description text
2. checks it against the refusal list
3. tokenizes meaning into seven order labels
4. assigns start times and durations
5. renders each order as a deterministic signal
6. overlaps and averages the signals
7. writes the resulting output as WAV

## Runtime notes

This is designed to be portable and lightweight. It uses `numpy` arrays and `scipy.io.wavfile.write()`, not a model checkpoint or GPU process.

## The complete code

See `field_generator.py` in this repository.

It is one file. It is self-contained. It is deterministic. It is meant to be open.

---

## The two-line close

Return: One file. One command. One output.

Next: Copy it. Run it. Change it. Ship it.
