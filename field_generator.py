# Field Generator

A lightweight procedural music generator built on a deterministic grammar of seven orders.

## Features

- zero training
- zero GPU
- optional offline operation
- one-file Python implementation
- deterministic output for a fixed description
- hard refusal checks before synthesis

## Requirements

```bash
pip install numpy scipy
```

## Run

```bash
python field_generator.py
```

Then edit the `DESCRIPTION` constant near the top of the file.

## Important

This repository is intentionally published without a license file.

## Output

The generated audio is written to `output.wav` in the project root.
