# Post-publication fact-check and compliance audit

Audit date: 2026-09-02

This repository contains the source for “A Spectrum Sensor for CubeSat Radios,” presented at the 2021 IEEE Cognitive Communications for Aerospace Applications Workshop (CCAAW). The [NASA record](https://ntrs.nasa.gov/citations/20210016644) and [IEEE DOI](https://doi.org/10.1109/CCAAW50069.2021.9527303) identify the immutable version of record. The revised source and `output/pdf/ccaaw_2021_audited.pdf` are explicitly labeled as a post-publication audit; they do not replace the published paper.

## Outcome

The published five-page paper used the expected IEEE conference layout and was accepted into the proceedings. Its letter-size, two-column PDF has embedded/subset fonts, no security, and no crop or registration marks. The audit nevertheless found several substantive technical errors and unsupported claims. Those have been corrected or qualified in the revised manuscript without inventing replacement results.

## Material corrections applied

| Severity | Finding | Resolution in revised manuscript |
|---|---|---|
| Critical | Equation (1) used integer indices without frequency normalization, making both printed exponential factors equal one; it also conflated a frequency-list index with physical center frequency. | Rewrote the channelizer with the archived physical candidate `f_{c,k}/f_s`, its positive sign convention, and the normalized symbol-rate bin `v/N`. |
| Critical | The printed Youden equation was not Youden's statistic, and the ROC caption reported `(P_d,J)` as `(P_fa,P_d)`. | Replaced it with `J=P_d-P_fa`; corrected the plotted point to approximately `(0.17000,0.64167)` and `J=0.47167`. |
| Critical | The script loses the mapping from an averaged ROC point back to `beta`, so `beta=1.23e-4` is not a verified optimum. | Retained it only as the historically reported design value and removed “optimal” claims. |
| High | The simulation scores symbol-rate membership only and explicitly does not test center frequency. | Limited all `P_d`/`P_fa` claims to symbol-rate candidates and removed center-frequency-accuracy claims. |
| High | The noise generator peak-normalizes each signal, calls `awgn` without measured average power, and adds noise separately before summing signals. The table labels therefore do not establish achieved `E_b/N_0`. | Relabeled the settings as nominal and required a corrected rerun before quantitative inference. |
| High | The current `sims/sca.m` settings differ from Table I, the exported `.m` file contains non-code headings, no random seed or raw ROC array is retained, and the saved AUC is negative because the script does not order `P_fa` increasingly before integration. | Marked the ROC and tables as non-reproducible from the archived files and avoided validating them. |
| High | HelioSwarm, Starling1, and the cited commercial megaconstellations were conflated as CubeSat formations with tens, hundreds, and thousands of spacecraft. | Distinguished a nine-spacecraft HelioSwarm baseline, a four-spacecraft Starling1 demonstration intended to test technology scalable to at least 100, and separate proposed commercial constellations of thousands. |
| High | The Starling presentation had the wrong authors; Starling-LunarNet was placed in low Earth rather than low lunar orbit; “in-site” was used for “in situ.” | Corrected the bibliography, orbit, wording, and concept captions. |
| Medium | Categorical claims that CubeSat radios cannot implement an SCA and that the search requires no prior knowledge were not supported. | Narrowed the claims to resource motivation and documented the assumed signal class, configured search grid, and fixed threshold. |
| Medium | Timing text selected “the test statistic with the highest `k`,” and an output paragraph pointed to the input figure. | Corrected the selection rule and figure cross-reference. |

The archived center-frequency files contain 300 samples each. Their sample standard deviations are approximately 0, 379, 1,428, 3,196, and 6,367 in the stored units, which supports a qualitative increase in dispersion across the apparent impairment sequence. The repository does not retain enough provenance to map every file unambiguously to a complete scenario, so the revised paper does not present those values as calibrated errors.

## Reference corrections

- Erik Kulu is now credited by name and the figure is dated through April 4, 2021: [Nanosats Database](https://www.nanosats.eu/).
- HelioSwarm scale and architecture were checked against the [NASA technical paper](https://ntrs.nasa.gov/citations/20190029108).
- Starling1 scale and authors were checked against the [Utah State University record](https://digitalcommons.usu.edu/smallsat/2018/all2018/299/) and the [NASA presentation record](https://ntrs.nasa.gov/citations/20180007374).
- The commercial-constellation citation was corrected using the [IEEE article DOI](https://doi.org/10.1109/MNET.2018.1800037).
- The thesis title and author name were corrected using the [OhioLINK record](https://rave.ohiolink.edu/etdc/view?acc_num=csu1622636550863441).
- Conventional cyclostationary-processing cost is now supported by the [NASA technical memorandum](https://ntrs.nasa.gov/citations/20190027051).
- Youden's original statistic is cited from the [1950 article record](https://pubmed.ncbi.nlm.nih.gov/15405679/).

## Format and venue review

The official [CCAAW 2021 call for papers](https://strs.grc.nasa.gov/ccaa21/call-for-papers/) required a 200--250 word preliminary abstract and later directed authors to an IEEE two-column Word template. The 200--250 word rule was for the preliminary submission, not explicitly the final-paper abstract. The final-paper abstract is one paragraph and is 187 words by a `detex`/whitespace count, within the current IEEE 250-word ceiling. The original standalone abstract was 174 words; its explicitly labeled post-publication revision is 201 words by the same count and therefore fits the preliminary-submission range if reused.

The source now uses standard IEEE table rules, consistent SI spacing and capitalization, corrected author/email punctuation, canonical U.S. Government copyright wording, descriptive figure captions, valid equation syntax, and PDF title/author/subject/keyword metadata plus a document language.

The audited PDF was checked against the current [IEEE Xplore PDF requirements](https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/meet-ieee-xplore-requirements/). Remaining modernization items are not historical acceptance failures: the pdfLaTeX output is untagged, graphics have no machine-readable alternative text, and several 2021 raster graphics are only about 220--280 ppi and have limited grayscale contrast. PDF tagging and alternative text can be added without the original artwork, but improving the raster resolution and contrast would require source artwork or recreated figures.

## Reproducibility work still needed

Do not treat the revised PDF as a revalidated experimental paper. A defensible rerun should:

1. Restore the live scripts as executable functions and version all configuration values.
2. Normalize average signal power, combine clean signals, and add channel noise once with measured power.
3. Define search bounds and resolution independently of ground-truth `R_s` and `f_c`.
4. Save a random seed, raw trial outcomes, ROC coordinates, and the `beta` associated with each coordinate.
5. Sort ROC coordinates before integrating AUC and report uncertainty intervals.
6. Score symbol-rate and center-frequency error separately, with a stated center-frequency tolerance.
7. Supply synthesizable HDL and implementation reports before making FPGA resource, timing, or power claims.
