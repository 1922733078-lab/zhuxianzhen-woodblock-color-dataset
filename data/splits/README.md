# Leakage-Safe Dataset Partitioning Manifest

This directory provides the official sample partitioning mapping for the 460 curated Zhuxianzhen woodblock print artworks.

## Files

- `suggested_split_manifest.csv`: Tabular mapping of all 460 images into training, validation, and test subsets.
- `all_splits_manifest.json`: Structured manifest containing cryptographic checksums (SHA-256) and audit metadata.

## Partitioning Strategy & Anti-Leakage Controls

In traditional woodblock printing, multiple printings can originate from identical or slightly modified wooden blocks (same-plate variations). Random splitting risks catastrophic data leakage where identical line-art or composition appears in both training and test sets.

- **Total Curated Works:** 460 authenticated woodblock print scans.
- **Precautionary Clustering:** Works are clustered based on perceptual feature similarity, same-plate identification, and multi-scale visual hashes.
- **Split Distribution:**
  - **Training Set:** 370 works (used for LoRA fine-tuning and color prior extraction).
  - **Validation Set:** 45 works.
  - **Test Set:** 45 works (unseen line-art plates used for zero-shot colorization evaluation).
- **Integrity Guarantee:** Zero cross-split plate leakage or subject overlap.
