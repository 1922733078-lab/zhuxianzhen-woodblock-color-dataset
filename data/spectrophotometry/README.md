# Spectrophotometric Measurement Dataset & Spectral Reflectance Ledger

This directory contains high-precision spectral reflectance measurements obtained from physical authentic Zhuxianzhen woodblock prints.

## Files

- `spectrophotometer_readings_63rows.csv`: 63 measurement rows across 20 sessions (with $L^*, a^*, b^*, X, Y, Z, C^*, h^\circ$ coordinates).
- `spectrophotometer_ledger_36channels.jsonl`: Complete 36-channel spectral reflectance records (380–730 nm in 10 nm increments).
- `图_a*b平面_全量.png`: 2D chromaticity distribution of all physical patches.
- `图_光谱_全量.png`: Spectral power distribution across all measurement sessions.
- `图_L时序_全量.png`: Time-series stability verification of luminance $L^*$.

## Instrumentation & Protocol

- **Spectrophotometer:** X-Rite i1Pro 3.
- **Illumination / Observer Condition:** D50 / 2° geometry (standard physical printing environment).
- **White Calibration:** Performed prior to each session using certified ceramic white calibration plaque.
- **Measurement Structure:**
  - 20 independent measurement sessions (`S001`–`S020`).
  - Session `S001`: White tile anchor verification (6 consecutive readings).
  - Sessions `S002`–`S020`: Triple repetitive readings on physical woodblock ink patches across 2 authentic works.
- **Repeatability:** Maximum pairwise $\Delta E_{00} \le 0.0475$ within any session (instrument error ceiling $< 0.05$).
- **Chromatic Adaptation:** Physical readings under D50/2° are mapped to digital D65/2° space using standard Bradford chromatic adaptation matrix for direct cross-domain comparison with digital training prior centers.
