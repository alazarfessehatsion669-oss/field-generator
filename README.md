# Field Generator

Free music generation. Zero training. Zero GPU. Zero cost. No owner.

## What this is

Field Generator turns a plain-text description into deterministic audio using a procedural grammar instead of a trained model.

It does not require:
- training data
- GPU compute
- cloud services
- a subscription
- a model owner

It runs anywhere Python 3 can run, with `numpy` and `scipy` installed.

## Why it exists

The current music-AI industry assumes that creative generation requires:
- massive datasets
- expensive GPUs
- paid APIs
- model licensing
- default genres

Field Generator proves a different path: a fixed grammar of seven morphological orders, applied deterministically, with explicit refusals.

## Quick start

```bash
pip install numpy scipy
python field_generator.py
```

Then edit the `DESCRIPTION` constant near the top of `field_generator.py` and run it again.

## Example

```python
DESCRIPTION = """
Ancient royal dark fantasy. Two voices, gold and purple.
Hands that almost touch. Slow, ceremonial. Deep, heavy, ancient.
Never Cinderella.
"""
```

Running the script creates `output.wav` in the project directory.

## The grammar

Music is treated as a substrate shaped by frequency into seven stable orders:

| Order | Name | Meaning |
|------|------|---------|
| CB1 | Identity | sustained base tone |
| CB2 | Extension | forward melodic motion |
| CB3 | Hook | brief ornament |
| CB4 | Bass Open | low-end foundation |
| CB5 | Loop | repeating figure |
| CB6 | Compression | tension and narrowing |
| CB7 | Closure | cadence and resolution |

The system compiles the incoming description into a sequence of these order tokens, applies refusal checks, then renders the deterministic result to audio.

## Refusals

A refusal list is enforced on the input text. If a blocked word appears, the run is rejected before synthesis begins.

```python
DEFAULT_REFUSALS = [
    "waltz", "disney", "princess", "cinderella", "pop",
    "ballroom", "happy", "upbeat", "bright", "cheerful",
]
```

## Project structure

- `field_generator.py` — complete generator
- `README.md` — overview and quick start
- `PRINCIPLES.md` — philosophy and design constraints
- `ARCHITECTURE.md` — pipeline and decoder design
- `WHY.md` — why this exists
- `CODE.md` — code map and usage notes
- `RELEASE.md` — publishing instructions
- `tests/` — smoke tests

## No ownership claim

This repository is intentionally published without a license file.

That means the code is provided as-is, without a formal copyright license grant. It is a deliberate anti-owner stance. If you want a clearer public-domain alternative, add a dedicated license file in your own fork before publishing.

## Read next

- `PRINCIPLES.md`
- `ARCHITECTURE.md`
- `WHY.md`

The light fades. The tone remains.
