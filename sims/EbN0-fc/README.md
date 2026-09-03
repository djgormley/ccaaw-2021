# Center-frequency characterization data

Each `fc_*.txt` file contains 300 signed frequency-control-word (FCW) outputs used for Fig. 10 of the paper. A contemporaneous MATLAB live script recovered from an author-held engineering archive (`single-term-cfe/test/tests/characterization.mlx`, created 2021-03-09 and last modified 2021-05-14 according to its package metadata) establishes this mapping and plotting method:

| File | Nominal `E_b/N_0` | Literal zeros | Plotted row mass | Conditional sample SD (MHz) |
|---|---:|---:|---:|---:|
| `fc_1.txt` | 12 dB | 0 | 1.0000 | 0 |
| `fc_2.txt` | 9 dB | 0 | 1.0000 | 0.00578 |
| `fc_3.txt` | 6 dB | 0 | 1.0000 | 0.02180 |
| `fc_4.txt` | 3 dB | 1 | 0.9967 | 0.04880 |
| `fc_5.txt` | 0 dB | 33 | 0.8900 | 0.10176 |

The script pairs FCW bins `-32768:3276:32752` with display labels `-0.50:0.05:0.50` MHz, counts only exact bin matches, and plots each count divided by 300. The figure therefore shows per-bin trial proportions, not probability density. The conditional standard deviations above use the displayed MHz grid and include only values matched by the plotting script.

Literal zero is not in the script's FCW bin vector; the grid's displayed 0-MHz point corresponds to FCW `-8`. The one omitted record at 3 dB and 33 at 0 dB leave row masses equal to the corresponding reported symbol-rate detection proportions, which is consistent with literal zero representing no returned center-frequency estimate. The generator, random seed, true center frequency, and acceptance tolerance were not retained, so this interpretation is not independently proven and the files cannot establish calibrated center-frequency accuracy.
