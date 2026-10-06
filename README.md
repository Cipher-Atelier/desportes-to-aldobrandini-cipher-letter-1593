# Desportes to Aldobrandini: cipher letter (22 July 1593)

A letter attributed to Baudouin Desportes, written in Paris on 22 July 1593 and addressed to Pietro Aldobrandini. Ordinary handwriting alternates with encrypted passages.

## What has been found?

A partial French working edition discusses political choices around Henri IV’s forthcoming conversion. It applies Satoshi Tomokiyo’s published key and credits Paolo Rosson’s prior reading. Many signs permit two possible letters, so a compatible choice is not automatically the correct reading.

A small example from the recorded result:

```text
IL FAUDROIT BEAUCOUP D EFFECTZ
```

This excerpt begins a passage about needing real action. The article supplies interpretation and translation; the working edition retains gaps and uncertain letter choices.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [French working text with gaps](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_reading_FR.txt) to inspect the saved text or test result itself.
3. Read the [research account](desportes-1593/article.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://archivesetmanuscrits.bnf.fr/ark:/12148/cc504266/cd0e20251); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

Partial edition using Tomokiyo’s known key, with Rosson’s prior reading credited. Replay checks 4,612 indexed regions, 4,108 compatible assignments and 4,295 expanded letters; polyphonic choice remains interpretive.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
