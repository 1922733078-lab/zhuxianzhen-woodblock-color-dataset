# Reproduction scope and statistical conventions

This public archive contains the released observer trial records, measurement ledger, nine-color image-referred prior and split manifests. It does not currently contain the full artwork image corpus, model weights or a complete generative inference package. The two analysis scripts reproduce the endpoints described below, not every manuscript table.

## Psychophysics

The 4,800 decisions are repeated observations from 20 observers, 12 artworks, 10 method pairs and two dimensions. Pooled one-sided binomial probabilities are printed as descriptive calculations; they do not account for within-observer dependence. The primary M4-versus-M0 observer-level t-test is two-sided: t(19)=7.93668, p=1.88553e-7, with 321/480 pooled wins. These are distinct test conventions, not conflicting datasets.

Kendall concordance uses average ranks for tied observer win totals and corrects its denominator for ties. The corrected overall W is 0.868844 (chi-square=69.5075, approximate p=2.88371e-14); faculty W is 0.844937; student W is 0.8875. Earlier code omitted tie correction and returned 0.8645/0.8344/0.8875. These differences reflect a calculation correction; raw decisions are unchanged. With five methods, chi-square probabilities should be identified as approximations rather than exact calibration.

## Spectrophotometry

The CSV contains 63 reading rows in 20 sessions, not 63 independent patches. The maximum within-session CIEDE2000 difference is 0.04754939, which rounds to 0.0475 but is not literally <=0.0475. The validation threshold is <0.05, evaluated by an actual conditional check. The script now executes Bradford adaptation on recorded XYZ values and reports session means in the D65/2-degree frame.

The released ledger does not supply a verified session-to-artwork-name-to-pigment-group mapping for the manuscript's ten-row physical comparison. No such mapping is guessed by the script. Adaptation and repeatability do not prove pigment chemistry, antiquity, original unfaded color or agreement with every prior center.

## Color prior and splits

The prior is digitized-image-referred color appearance with assumed sRGB encoding. Its JSON contains centers and weights, not Gaussian covariance matrices. The manifests provide partition identities and checksums; they are not copies of the artwork images. Historical local source paths are provenance strings, not publicly downloadable image locations.

## Manuscript synchronization

The original submission version contains numerical and mapping discrepancies requiring reconciliation against its final experimental records, notably the ten-row physical table and the M3/component-ablation claims. Those discrepancies are not repaired by creating placeholders or relabeling unrelated experimental runs. Use this archive only for endpoints reproducible from its actual released inputs. Paper-level claims should be checked against the exact manuscript version and its independently verified source files.
