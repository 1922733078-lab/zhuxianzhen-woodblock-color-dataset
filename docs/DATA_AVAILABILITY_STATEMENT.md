# Data Availability Statement

**Paper Title:** 面向朱仙镇木版年画的色彩知识约束扩散模型线稿上色与文创应用 (Color-Knowledge Constrained Diffusion Model for Zhuxianzhen Woodblock New Year Print Colorization and Creative Product Application)  
**Target Journal:** *Color Research & Application* (Wiley)  
**Primary Archive:** [GitHub: 1922733078-lab/zhuxianzhen-woodblock-color-dataset](https://github.com/1922733078-lab/zhuxianzhen-woodblock-color-dataset)  
**Permanent Digital Object Identifier (DOI):** To be registered upon final acceptance via Zenodo / OSF.

---

## 1. Scope of Public Data & FAIR Compliance

In strict adherence to the **FAIR Principles** (Findable, Accessible, Interoperable, and Reusable) and Wiley *Color Research & Application* guidelines, all core empirical datasets, instrument measurement logs, human psychophysical trial records, color knowledge priors, and replication scripts supporting the findings of this study are openly accessible in this repository without commercial restrictions.

### Inventory of Archived Assets:

1. **Human Psychophysical 2AFC Experiment Dataset (`data/psychophysics/`):**
   - 4,800 individual blind two-alternative forced-choice (2AFC) trial decisions collected from 20 accredited observers (8 senior faculty experts `E01–E08` and 12 trainee designers `N01–N12`) across 12 representative woodblock print artworks and two evaluation dimensions (Style Authenticity and Visual Harmony).
   - Strict de-identification conforming to the Declaration of Helsinki (zero personal names, phone numbers, or institutional IDs).
   - Available in both standardized CSV (`human_visual_experiment_4800trials.csv`) and spreadsheet XLSX formats (`human_visual_experiment_4800trials.xlsx`).

2. **Physical Spectrophotometric Measurement Ledger (`data/spectrophotometry/`):**
   - 63 high-precision spectral measurement rows acquired from two authentic historical Zhuxianzhen woodblock prints across 20 independent measurement sessions using an X-Rite i1Pro 3 spectrophotometer (380–730 nm, 10 nm interval, 36 channels, D50/2° geometry).
   - Full chromatic coordinates (CIE $L^*a^*b^*$, $XYZ$, $C^*$, $h^\circ$) and reflectance spectral power distributions.
   - Bradford chromatic adaptation code mapping physical readings to the digital D65/2° target frame.

3. **Color Knowledge Prior (`data/color_prior/`):**
   - Empirical $K=9$ woodblock color prior distribution parameters (`train_color_prior.json`) extracted from the 370-work training subset under strict leakage-safe cluster partitioning.

4. **Leakage-Safe Partitioning Manifest (`data/splits/`):**
   - Complete partition mapping of all 460 authenticated woodblock print works into training ($n=370$), validation ($n=45$), and test ($n=45$) subsets (`suggested_split_manifest.csv` and `all_splits_manifest.json`), preventing cross-split identical-block contamination.

5. **Replication Scripts (`scripts/`):**
   - Self-contained Python scripts for instant verification of head-to-head win rates, observer-level clustered $t$-tests ($t(19) = 7.94, p = 9.43 \times 10^{-8}$), Thurstone Case V interval scales ($M4 = +0.648$), and Kendall's $W$ concordance ($W = 0.8645$).

---

## 2. Ethics and Anonymization

All human psychophysical observer studies were conducted in compliance with the Declaration of Helsinki and local institutional ethics review boards. All participants gave prior written informed consent. As guaranteed to participants, all raw individual identifiers were replaced by anonymous study codes prior to archival.

For inquiries or extended non-commercial research access to raw uncompressed ultra-high-resolution woodblock scans, contact the corresponding author.
