# Zhuxianzhen Woodblock Color Knowledge Prior

This directory provides the parametric representation of traditional woodblock printing color palettes extracted from authentic historical works.

## Files

- `train_color_prior.json`: Machine-readable JSON dictionary containing the $K=9$ canonical color centers, covariance matrices, and prior probabilities under D65/2° standard illumination.

## Specification

- **Source Corpus:** 370 authentic Zhuxianzhen woodblock print artworks from the training partition (after cluster-safe leakage filtering).
- **Extraction Protocol:** Work-equalized Gaussian Mixture Clustering in CIE $L^*a^*b^*$ color space.
- **Canonical Palette Centers ($K=9$):**
  1. 朱红 (Cinnabar Red)
  2. 明黄 (Bright Yellow)
  3. 青绿 (Malachite Green)
  4. 紫 (Purple)
  5. 青 (Indigo Blue)
  6. 橙红 (Orange Red)
  7. 赭金 (Ochre Gold)
  8. 暖米灰 (Warm Beige Grey)
  9. 暖深灰 (Warm Dark Grey)
- **Illuminant / Observer Standard:** CIE D65 / 2°.
