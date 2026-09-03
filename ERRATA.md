# Errata: “A Spectrum Sensor for CubeSat Radios”

Date issued: 2026-09-02

Applies to: 2021 IEEE CCAAW paper, DOI [10.1109/CCAAW50069.2021.9527303](https://doi.org/10.1109/CCAAW50069.2021.9527303)

This errata records post-publication corrections supported by the paper's archived source, code, and cited primary sources. It does not change the IEEE version of record. A corrected, explicitly labeled reading copy is available at `output/pdf/ccaaw_2021_audited.pdf`; the full evidence trail is in `FACT_CHECK.md`.

## Corrections

1. **Equation (1), frequency variables and normalization.** The published equation used integer indices in both complex exponentials without frequency normalization, making those factors identically one. It also conflated a center-frequency candidate-list index with physical center frequency. In notation faithful to the archived implementation, the corrected form is

   \[
   \widehat S_X^v[k]=\frac{1}{N}\sum_{n=0}^{N-1}
   \left|\left(X[n]e^{+j2\pi f_{c,k}n/f_s}\right)\ast h[n]\right|^2
   e^{-j2\pi vn/N}.
   \]

   Here `v=round(R_s N/f_s)` is the zero-based Goertzel/DFT bin and `f_{c,k}` is the `k`th physical center-frequency candidate. The archived one-based Goertzel call uses `v+1`; `k` remains an index into the configured frequency list. The positive channelizer sign matches the archived transmitter's negative carrier convention.

2. **ROC point and Youden's statistic.** Equation (3) was not Youden's statistic, and the caption mislabeled `(P_d,J)` as `(P_fa,P_d)`. The correct statistic is `J=P_d-P_fa`. The archived red point is approximately `(P_fa,P_d)=(0.17000,0.64167)`, yielding `J=0.47167`.

3. **Threshold is not verified as optimal.** After grouping repeated false-alarm values, `sims/sca_roc.m` indexes the original `beta` array with an index from the shorter grouped array. Therefore the reported `beta=1.23e-4` is not reliably associated with the red ROC point. It should be read only as the historically reported design value pending a rerun.

4. **No 95% confidence interval was calculated.** The script assigns `CL=0.95` but never uses it. The figure contains 300 trials per threshold and no confidence interval.

5. **Detection metrics cover symbol rate only.** `sims/sca.m` explicitly checks symbol-rate membership and does not score center-frequency correctness. The reported `P_d` and `P_fa` therefore cannot support the paper's claims of accurate center-frequency detection. In addition, `P_fa` is a false-positive fraction over unoccupied symbol-rate candidates, not a whole-system false-alarm probability.

6. **`E_b/N_0` values are nominal settings.** The transmitter peak-normalizes each waveform, calls `awgn` without measured average power, and adds noise independently before summing the two signals. The listed values do not establish achieved received `E_b/N_0`; quantitative conclusions require a corrected rerun.

7. **The numerical study is not reproducible from the archive.** The surviving `sims/sca.m` is an incomplete live-script export, its parameters differ from Table I, the ROC observations and random seed are absent, and its AUC calculation does not order `P_fa` increasingly before integration. The published point estimates are preserved for provenance but are not revalidated.

8. **Mission scale and terminology.** HelioSwarm's cited baseline contains nine spacecraft, not tens. Starling1 is a four-spacecraft demonstration of technology intended to scale to at least 100 spacecraft, not itself a hundred-spacecraft formation. The systems numbering in the thousands in Giambene et al. are proposed communications megaconstellations, not CubeSat formation-flying missions. The four Starling graphics are notional swarm-enabled concepts.

9. **Starling details and citation.** Starling-LunarNet is in low lunar orbit, not low Earth orbit; “in-site” is corrected to “in situ.” The NASA presentation is correctly attributed to Howard N. Cannon, Hugo S. Sanchez, and Dawn M. McIntosh, replacing the erroneous author list.

10. **Scope of claims.** The revised text no longer says CubeSat radios categorically cannot implement an SCA, the search has no prior channel knowledge, the center frequency was accurately detected, or the design's FPGA performance was demonstrated. The repository contains diagrams and simulations, but no synthesizable HDL or implementation reports.

11. **Minor corrections.** The bibliography now uses the exact thesis title and author metadata, Erik Kulu is credited by name, QAM support is limited to the power-of-two orders accepted by the archived transmitter, the center-frequency detector is described as retaining the largest statistic rather than “the highest `k`,” and the output discussion points to the output timing figure.

## What remains unresolved

The original numerical results cannot be corrected honestly without rerunning the simulation. A replacement study should normalize average signal power, add one noise process after signal combination, define the search grid independently of ground truth, retain seeds and raw outcomes, preserve the `beta` associated with each ROC point, sort coordinates before AUC integration, report uncertainty, and score symbol-rate and center-frequency errors separately.
