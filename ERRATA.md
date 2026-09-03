# Errata: “A Spectrum Sensor for CubeSat Radios”

Date issued: 2026-09-03

Applies to: 2021 IEEE CCAAW paper, DOI [10.1109/CCAAW50069.2021.9527303](https://doi.org/10.1109/CCAAW50069.2021.9527303)

This errata document records post-publication corrections supported by the paper's archived source, code, cited primary sources, and a separately retained engineering archive. It does not change the IEEE version of record. A [corrected, explicitly labeled reading copy](output/pdf/ccaaw_2021_audited.pdf) is available; the full evidence trail is in [`FACT_CHECK.md`](FACT_CHECK.md).

## Corrections

1. **Equation (1), frequency variables and normalization.** The published equation used integer indices in both complex exponentials without frequency normalization, making those factors identically one. It also conflated a center-frequency candidate-list index with physical center frequency. In notation faithful to the archived implementation, the corrected form is

   \[
   \widehat S_X^v[k]=\frac{1}{N}\sum_{n=0}^{N-1}
   \left|\left(X[n]e^{+j2\pi f_{c,k}n/f_s}\right)\ast h[n]\right|^2
   e^{-j2\pi vn/N}.
   \]

   Here `v=round(R_s N/f_s)` is the zero-based Goertzel/DFT bin and `f_{c,k}` is the `k`th configured downconversion-frequency parameter in hertz. The archived one-based Goertzel call uses `v+1`; `k` remains an index into the configured frequency list. Because the transmitter uses a negative carrier exponential and the receiver uses the opposite sign, this parameter is not necessarily the signed spectral location under the standard Fourier convention.

2. **ROC point and Youden's statistic.** Equation (3) was not Youden's statistic, and the caption mislabeled `(P_d,J)` as `(P_fa,P_d)`. The correct statistic is `J=P_d-P_fa`. The archived red point is approximately `(P_fa,P_d)=(0.17000,0.64167)`, yielding `J=0.47167`.

3. **Threshold is not verified as optimal.** After grouping repeated false-alarm values, `sims/sca_roc.m` indexes the original `beta` array with an index from the shorter grouped array. Therefore the reported `beta=1.23e-4` is not reliably associated with the red ROC point. It should be read only as the historically reported design value pending a rerun.

4. **No 95% confidence interval was calculated.** The script assigns `CL=0.95` but never uses it. The figure contains 300 trials per threshold and no confidence interval.

5. **Detection metrics cover symbol rate only.** `sims/sca.m` explicitly checks symbol-rate membership and does not score center-frequency correctness. The reported `P_d` and `P_fa` therefore cannot support the paper's claims of accurate center-frequency detection. In addition, `P_fa` is a false-positive fraction over unoccupied symbol-rate candidates, not a whole-system false-alarm probability.

6. **`E_b/N_0` values are nominal settings.** The transmitter peak-normalizes each waveform, calls `awgn` without measured average power, and adds noise independently before summing the two signals. The listed values do not establish achieved received `E_b/N_0`; quantitative conclusions require a corrected rerun.

7. **Center-frequency figure mapping and scale.** A recovered 2021 plotting script maps `fc_1.txt` through `fc_5.txt` to nominal 12, 9, 6, 3, and 0 dB and plots exact-bin counts divided by 300. The published ordinate labeled “Probability Density” is actually per-bin trial proportion. Its bin grid excludes one literal zero at 3 dB and 33 at 0 dB, leaving row totals of 0.9967 and 0.89. Their equality to the corresponding reported `P_d` values is consistent with, but does not prove without a retained generator or driver linked to these files, zero encoding no detection. The revised figure uses marker area for trial proportion and displays the unmatched zeros separately, preserving all 300 records in each row.

8. **The numerical study is not reproducible from the archive.** The surviving `sims/sca.m` is an incomplete live-script export, its parameters differ from Table I, the ROC observations and random seed are absent, and its AUC calculation does not order `P_fa` increasingly before integration. Moreover, under the retained scoring formula, the four-decimal `P_fa` values are incompatible with the surviving script's 900 unoccupied-candidate trials. Fitting all nine rounded values requires at least 30 unoccupied candidates per run, confirming that the table-producing search configuration is absent without identifying its exact grid. The published point estimates are preserved for provenance but are not revalidated.

9. **Mission scale and terminology.** HelioSwarm's cited baseline contains nine spacecraft, not tens. Starling1 is a four-spacecraft demonstration of technology intended to scale to at least 100 spacecraft, not itself a hundred-spacecraft formation. The systems numbering in the thousands in Giambene et al. are proposed communications megaconstellations, not CubeSat formation-flying missions. The four Starling graphics are notional swarm-enabled concepts.

10. **Starling details and citation.** Starling-LunarNet is in low lunar orbit, not low Earth orbit; “in-site” is corrected to “in situ.” The NASA presentation is correctly attributed to Howard N. Cannon, Hugo S. Sanchez, and Dawn M. McIntosh, replacing the erroneous author list.

11. **Hardware evidence and claim scope.** A separately retained, mixed-date archive contains substantial RTL, an early engineering-review workbook, component-level resource records, behavioral traces, and a February 2022 hardware-manager capture. It does not contain an exact, reproducible 2021 top-level revision, a complete build and constraints, full-sensor implementation reports, or power measurements, and its components identify conflicting target devices. This supports design activity but not full-sensor resource, timing, power, or end-to-end hardware-performance claims. The revised text also no longer says CubeSat radios categorically cannot implement an SCA, the search has no prior channel knowledge, or the center frequency was accurately detected.

12. **Hardware topology changed after publication.** The paper says `beta` is fixed before synthesis and places the threshold comparison in each center-frequency detector. The later retained RTL exposes `Beta` as a runtime top-level input, produces a quantized fixed-point threshold from accumulated sample power, applies the comparison in a symbol-rate preprocessor, and gives the center-frequency detector no threshold input. A priority-based distributor added in 2022 also differs from the paper's FIFO scheduler. The revised manuscript distinguishes the published topology from this later snapshot.

13. **Result-FIFO behavior is unverified and contradicted by later RTL.** The paper says a full output FIFO discards the oldest result in favor of a new one. The later retained `SimpleFifo.vhd` instead rejects a write while full unless a read occurs in the same cycle, preserving queued entries. Source for the earlier timing diagram was not retained, so the stated overwrite-on-full behavior cannot be confirmed.

14. **Minor corrections.** The bibliography now uses the exact thesis title and author metadata, Erik Kulu is credited by name, QAM support is limited to the power-of-two orders accepted by the archived transmitter, the center-frequency detector is described as retaining the largest statistic rather than “the highest `k`,” and the output discussion points to the output timing figure.

15. **The reported signals are not co-channel.** Table I places the two signals at distinct center frequencies of 0.1 and 0.2 MHz. Their occupied spectra overlap under the stated symbol rates and roll-off, so the revised manuscript describes them as spectrally overlapping rather than co-channel.

## What remains unresolved

The original numerical results cannot be corrected honestly without rerunning the simulation. A replacement study should normalize average signal power, add one noise process after signal combination, define the search grid independently of ground truth, retain seeds and raw outcomes, preserve the `beta` associated with each ROC point, sort coordinates before AUC integration, report uncertainty, and score symbol-rate and center-frequency errors separately.

Hardware validation still requires an exact, buildable RTL revision with its device configuration and constraints, reproducible tests, implementation resource and timing reports, and power measurements. The later retained archive cannot by itself establish which topology or FIFO policy was used for the 2021 paper.
