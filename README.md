# Zhuxianzhen Woodblock Colorization Dataset & Replication Package

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FAIR Data](https://img.shields.io/badge/FAIR-Compliant-brightgreen.svg)](https://www.go-fair.org/fair-principles/)

Official open research dataset and replication package for the academic manuscript:  
**"面向朱仙镇木版年画的色彩知识约束扩散模型线稿上色与文创应用"**  
*(Color-Knowledge Constrained Diffusion Model for Zhuxianzhen Woodblock New Year Print Colorization and Creative Product Application)*  
Target Journal: **Color Research & Application (Wiley)**

---

## 📖 Overview

Traditional Zhuxianzhen woodblock New Year prints embody distinctive folk polychrome palettes, mineral-inspired pigment combinations, and bold visual contrast. However, unconstrained deep generative models frequently suffer from chromatic hallucination, out-of-gamut artifacts, and semantic disharmony. 

To overcome the **unconstrained metric paradox** (where naive algorithms minimize pixel distance at the cost of authentic cultural aesthetics), this study introduces a **color-knowledge constrained diffusion pipeline (M4)** coupled with rigorous physical colorimetry and psychophysical evaluation.

This repository provides the complete, de-identified research datasets, physical spectrophotometric ledgers, color priors, and one-click reproduction scripts supporting the published findings.

---

## 📂 Repository Structure

```text
zhuxianzhen-woodblock-color-dataset/
├── README.md                      # Main documentation and reproduction guide
├── LICENSE                        # MIT (scripts) & CC BY 4.0 (data)
├── requirements.txt               # Lightweight runtime dependencies
├── .gitignore
├── docs/
│   ├── DATA_AVAILABILITY_STATEMENT.md  # Official Data Availability Statement
│   └── ETHICS_AND_CONSENT.md           # Ethics governance & Helsinki compliance
├── data/
│   ├── psychophysics/             # Human observer 2AFC perception experiment
│   │   ├── human_visual_experiment_4800trials.csv    # Standard English CSV (4,800 trials)
│   │   ├── human_visual_experiment_4800trials_cn.csv # Chinese header CSV
│   │   ├── human_visual_experiment_4800trials.xlsx   # Spreadsheet format
│   │   └── README.md                                 # Codebook and experimental design
│   ├── spectrophotometry/         # X-Rite i1Pro 3 physical colorimetry
│   │   ├── spectrophotometer_readings_63rows.csv     # 63 readings across 20 sessions
│   │   ├── spectrophotometer_ledger_36channels.jsonl # 36-channel spectral reflectance
│   │   ├── 图_a*b平面_全量.png                        # a*b* chromaticity distribution
│   │   ├── 图_光谱_全量.png                          # Reflectance power distribution
│   │   ├── 图_L时序_全量.png                         # Luminance temporal repeatability
│   │   └── README.md                                 # Instrument protocol & Bradford setup
│   ├── color_prior/               # Parametric woodblock color palette
│   │   ├── train_color_prior.json                    # K=9 Gaussian mixture prior (D65/2°)
│   │   └── README.md                                 # Palette definitions & extraction
│   └── splits/                    # Leakage-safe artwork partitioning
│       ├── suggested_split_manifest.csv              # 460 works (370 train / 45 val / 45 test)
│       ├── all_splits_manifest.json                  # Cryptographic checksums & audit logs
│       └── README.md                                 # Cluster anti-leakage methodology
└── scripts/
    ├── reproduce_psychophysics_analysis.py           # Reproduce 2AFC stats, Z-scores, W
    └── reproduce_spectrophotometry_analysis.py       # Reproduce Bradford adaptation & DE00
```

---

## 🔬 Core Empirical Datasets

### 1. Human Observer 2AFC Visual Experiment (`data/psychophysics/`)
- **Scale:** 4,800 double-blind paired comparison trials.
- **Factorial Setup:** 20 observers $\times$ 12 representative works (6 genres) $\times$ 10 paired method comparisons $\times$ 2 perceptual dimensions.
- **Participant Cohort:** Two-tier design cohort:
  - Senior Faculty Experts ($n=8$, `E01–E08`)
  - Trainee Designers ($n=12$, `N01–N12`)
- **Key Dimensions:** *Style Authenticity* (民间风格地道性) and *Visual Harmony* (画面视觉和谐度).
- **Ethics & Privacy:** Zero personal identifiers; fully de-identified in compliance with the Declaration of Helsinki.

### 2. Physical Spectrophotometric Ledger (`data/spectrophotometry/`)
- **Instrument:** X-Rite i1Pro 3 spectrophotometer (standard D50 / 2° physical printing geometry).
- **Scope:** 63 physical readings across 20 independent measurement sessions on two genuine antique woodblock prints.
- **Repeatability:** Max pairwise $\Delta E_{00} \le 0.0475$ within any session (instrument error ceiling $< 0.05$).
- **Chromatic Adaptation:** Physical D50 readings converted to digital D65/2° frame via Bradford transform matrix for equitable cross-domain comparison.

### 3. Woodblock Color Knowledge Prior (`data/color_prior/`)
- Parametric $K=9$ canonical color centers ($L^*a^*b^*$, cov, prior weights) extracted from 370 train works under strict cluster-safe partitioning.

### 4. Leakage-Safe Manifest (`data/splits/`)
- Audit-verified partitioning of 460 authenticated woodblock works into 370 train, 45 val, and 45 test sets, preventing same-plate duplication across subsets.

---

## 🚀 Quick Start & One-Click Reproduction

### Environment Setup

The reproduction suite requires only lightweight standard scientific Python packages:

```bash
git clone https://github.com/192273078-lab/zhuxianzhen-woodblock-color-dataset.git
cd zhuxianzhen-woodblock-color-dataset
pip install -r requirements.txt
```

### Reproduce Psychophysical Statistics (Figure 9 & Section 5)

Run the self-contained analysis script:

```bash
python scripts/reproduce_psychophysics_analysis.py
```

**Expected Output Verification:**
- **Head-to-Head Win Rates (M4 vs. Competitors):**
  - M4 vs M0: **321/480 (66.9%)**, $p = 5.89 \times 10^{-14}$
  - M4 vs M1: **372/480 (77.5%)**, $p = 2.73 \times 10^{-35}$
  - M4 vs DDColor: **385/480 (80.2%)**, $p = 9.93 \times 10^{-43}$
  - M4 vs Reinhard: **372/480 (77.5%)**, $p = 2.73 \times 10^{-35}$
- **Observer-Level Clustered $t$-test (Eliminating Pseudoreplication):**
  - $t(19) = 7.94$, $p = 9.43 \times 10^{-8}$ (Mean win rate = 66.9%, SD = 0.095).
- **Thurstone Case V Z-Scores ($M1 = 0$ Baseline):**
  - Overall: M4 = **+0.648**, M0 = **+0.236**, M1 = **0.000**, DDColor = **-0.194**, Reinhard = **-0.246**
  - Style Authenticity: M4 = **+0.878**, M0 = **+0.482**
  - Visual Harmony: M4 = **+0.449**, M0 = **+0.012**
- **Inter-Observer Reliability (Kendall's $W$):**
  - Overall ($m=20$): $W = 0.8645$, $\chi^2(4) = 69.16$, $p = 3.41 \times 10^{-14}$
  - Faculty Experts ($m=8$): $W = 0.8344$, $\chi^2(4) = 26.70$, $p = 2.29 \times 10^{-5}$
  - Student Trainees ($m=12$): $W = 0.8875$, $\chi^2(4) = 42.60$, $p = 1.25 \times 10^{-8}$

### Reproduce Spectrophotometry Analysis

```bash
python scripts/reproduce_spectrophotometry_analysis.py
```

**Expected Output Verification:**
- Confirms 63 physical measurement rows across 20 sessions.
- Validates within-session max pairwise $\Delta E_{00} \le 0.0475$, verifying strict instrument precision.

---

## 📜 Citation

If you use this dataset or replication code in your research, please cite:

```bibtex
@article{xue2026zhuxianzhen,
  title={面向朱仙镇木版年画的色彩知识约束扩散模型线稿上色与文创应用 (Color-Knowledge Constrained Diffusion Model for Zhuxianzhen Woodblock New Year Print Colorization and Creative Product Application)},
  author={Xue, Zihang and collaborators},
  journal={Color Research & Application},
  year={2026},
  publisher={Wiley}
}
```

---

## ⚖️ License

- **Source Code and Analysis Scripts (`scripts/`):** Licensed under the [MIT License](LICENSE).
- **Datasets and Documentation (`data/`, `docs/`):** Licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE).
