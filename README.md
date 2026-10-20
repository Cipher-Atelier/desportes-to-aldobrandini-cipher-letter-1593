# Desportes to Aldobrandini: cipher letter (22 July 1593)

A letter attributed to Baudouin Desportes, written in Paris on 22 July 1593 and addressed to Pietro Aldobrandini. Ordinary handwriting alternates with encrypted passages.

[Cipher Atelier](https://github.com/Cipher-Atelier) · [Research index](https://github.com/Cipher-Atelier/research-index) · [Reading guide](READING_GUIDE.md) · [Verification](verification/README.md)

## Current status — 11 October 2026

The proposed text discusses political choices around Henri IV’s forthcoming conversion. This partial French working edition applies Satoshi Tomokiyo’s published polyphonic key and credits Paolo Rosson’s earlier reading. Replay checks 4,612 indexed regions, 4,108 compatible assignments and 4,295 expanded letters. Those counts measure compatibility and coverage; choosing an allowed letter does not establish its historical correctness.

| Evidence layer | Open this |
| --- | --- |
| Original | [Recto](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f347) · [verso](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f348) |
| Recorded signs and key | [Sign alignment](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/sign_alignment.csv) · [structured transcription](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_transcription.json) · [Tomokiyo’s original key study](https://cryptiana.web.fc2.com/code/mayenne.htm) |
| Literal / working French | [Working text](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_reading_FR.txt) · [ambiguity map](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/ambiguity_map.csv) |
| Interpretation / selected English translation | [Article passage](desportes-1593/article.md#why-promises-were-no-longer-enough) |

The working text uses capitals for deciphered passages and mixed case for ordinary handwriting. Spacing and punctuation are editorial; brackets retain gaps without necessarily specifying their length. On folio 186r, P01 indices 1–3, classes D/E/F permit D/Q, E/R, F/S; choosing D/E/S gives `DES`. [Check that example](READING_GUIDE.md#check-one-example-by-hand).

**Unresolved / missing:** polyphonic choices, gaps and personal identifications remain. A complete English translated edition and the historically mentioned continuous Russian translation are not included in this public package. P01/M3 are editorial locators; X labels are block-local. Later PAR commentary and Rosson restorations remain separate from the frozen edition.

## Start here

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [French working text with gaps](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_reading_FR.txt) to inspect the saved text or test result itself.
3. Read the [research account](desportes-1593/article.md) for historical context, methods, earlier work and unresolved questions.

## Reproduce the checks

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://archivesetmanuscrits.bnf.fr/ark:/12148/cc504266/cd0e20251); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

The [Evidence checks workflow](.github/workflows/verify.yml) runs this offline baseline on Python 3.10 and 3.13, without installing dependencies, and checks changed-file whitespace.

## Research scope and limitations

Partial edition using Tomokiyo’s known key, with Rosson’s prior reading credited. Replay checks 4,612 indexed regions, 4,108 compatible assignments and 4,295 expanded letters; polyphonic choice remains interpretive.

## Contribute

This is part of [Cipher Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.

## Sources and rights

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.
