# Human Psychophysical Observer 2AFC Dataset

This directory contains the complete de-identified raw trial logs for the 2AFC visual perception experiment.

## Files

- `human_visual_experiment_4800trials.csv`: Standardized UTF-8 CSV with English column headers.
- `human_visual_experiment_4800trials_cn.csv`: Standardized UTF-8 CSV with original Chinese column headers.
- `human_visual_experiment_4800trials.xlsx`: Spreadsheet format containing the complete trial workbook.

## Dataset Specification

- **Total Trials:** 4,800 paired comparisons.
- **Design:** Full factorial design = 20 observers $\times$ 12 representative woodblock prints $\times$ 10 paired method combinations $\times$ 2 evaluation dimensions.
- **Observers ($n=20$):**
  - `E01–E08`: Senior Faculty Expert group ($n=8$).
  - `N01–N12`: Trainee Designer / Student group ($n=12$).
- **Dimensions:**
  - `Style Authenticity` (民间风格地道性): Evaluation of adherence to traditional folk woodblock aesthetics and pigment conventions.
  - `Visual Harmony` (画面视觉和谐度): Evaluation of global color composition, balance, and visual appeal.
- **Compared Methods ($K=5$):**
  - `M4`: Color-knowledge constrained diffusion model (Ours).
  - `M0`: Unconstrained base diffusion model.
  - `M1`: ControlNet line-art conditioned baseline.
  - `DDColor`: Exemplar/reference-based deep colorization baseline.
  - `Reinhard`: Classic global color transfer baseline.

## Codebook / Data Dictionary

| Column Name | Type | Description | Allowed Values |
|---|---|---|---|
| `trial_id` | Integer | Global sequential trial index | 1 to 4800 |
| `observer_id` | String | De-identified participant code | `E01`–`E08`, `N01`–`N12` |
| `observer_cohort` | String | Participant professional background | `Faculty`, `Student` |
| `evaluation_dimension` | String | Perceptual evaluation dimension | `Style Authenticity`, `Visual Harmony` |
| `artwork_id` | String | Catalog ID of the 12 representative prints | e.g., `IMG20260430102902`, etc. |
| `left_method` | String | Method displayed on the left | `M4`, `M0`, `M1`, `DDColor`, `Reinhard` |
| `right_method` | String | Method displayed on the right | `M4`, `M0`, `M1`, `DDColor`, `Reinhard` |
| `selected_position` | String | Spatial button pressed by the observer | `Left`, `Right` |
| `winner_method` | String | Method chosen by the observer | `M4`, `M0`, `M1`, `DDColor`, `Reinhard` |
| `loser_method` | String | Method not chosen | `M4`, `M0`, `M1`, `DDColor`, `Reinhard` |
