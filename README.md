# A Spectrum Sensor for CubeSat Radios

This repository preserves the source and supporting material for the 2021 IEEE Cognitive Communications for Aerospace Applications Workshop paper. The [IEEE DOI](https://doi.org/10.1109/CCAAW50069.2021.9527303) and [NASA record](https://ntrs.nasa.gov/citations/20210016644) identify the immutable version of record.

The source has since received a post-publication factual and formatting audit. The canonical corrected reading copy is [`output/pdf/ccaaw_2021_audited.pdf`](output/pdf/ccaaw_2021_audited.pdf). See [`ERRATA.md`](ERRATA.md) for the concise correction list and [`FACT_CHECK.md`](FACT_CHECK.md) for the evidence and remaining limitations. The older `main/ccaaw_2021.pdf` and `output/pdf/ccaaw_2021.pdf` files are retained historical builds, not the corrected reading copy. Likewise, `ccaaw2021_presentation.pptx` is the uncorrected 2021 presentation and repeats claims superseded by the errata. The original MATLAB files are provenance snapshots rather than a current runnable package; the audit documents their missing inputs and version-dependent behavior.

## Build

Run these commands from the repository root with a current TeX distribution containing `IEEEtran`, `latexmk`, and BibTeX:

```sh
mkdir -p tmp/pdfs
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -jobname=ccaaw_2021_audited -outdir=tmp/pdfs main.tex
cp tmp/pdfs/ccaaw_2021_audited.pdf output/pdf/ccaaw_2021_audited.pdf

latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=tmp/pdfs main/ccaaw_2021_abstract.tex
cp tmp/pdfs/ccaaw_2021_abstract.pdf main/ccaaw_2021_abstract.pdf
```

Regenerate the corrected center-frequency figure with Python 3.9 or later and Matplotlib:

```sh
python3 sims/EbN0-fc/plot_characterization.py
```

For a release check, confirm that both PDFs use US Letter pages, contain embedded fonts, have no security or attachments, and render without clipping or overlap. The corrected manuscript intentionally remains labeled as a post-publication reading copy rather than the IEEE version of record.
