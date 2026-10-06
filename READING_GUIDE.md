# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A letter attributed to Baudouin Desportes, written in Paris on 22 July 1593 and addressed to Pietro Aldobrandini. Ordinary handwriting alternates with encrypted passages.

Start with the [source catalogue or manuscript](https://archivesetmanuscrits.bnf.fr/ark:/12148/cc504266/cd0e20251). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

A partial French working edition discusses political choices around Henri IV’s forthcoming conversion. It applies Satoshi Tomokiyo’s published key and credits Paolo Rosson’s prior reading. Many signs permit two possible letters, so a compatible choice is not automatically the correct reading.

Open [French working text with gaps](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_reading_FR.txt) and the [research account](desportes-1593/article.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
IL FAUDROIT BEAUCOUP D EFFECTZ
```

This excerpt begins a passage about needing real action. The article supplies interpretation and translation; the working edition retains gaps and uncertain letter choices.

The replay checks 4,612 indexed regions, 4,108 compatible assignments and 4,295 expanded letters. These are bookkeeping/compatibility counts, not independent correctness scores, unique choices or a newly recovered key.

## Check one example by hand

1. Open the [sign alignment](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/sign_alignment.csv) and find folio `186r`, row `P01`, indices 1–3.

| Index | Recorded class | Allowed letters | Adopted letter |
| --- | --- | --- | --- |
| 1 | `D` | `DQ` | `D` |
| 2 | `E` | `ER` | `E` |
| 3 | `F` | `FS` | `S` |

2. These adopted choices give `DES`. Each choice belongs to the allowed pair, but that fact alone cannot choose between `D/Q`, `E/R` or `F/S`. This is what *polyphonic* means here: one cipher class can represent more than one letter.
3. Compare the recorded source class with [Gallica image 347, recto](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f347), and compare the allowed pair with [the published key](https://cryptiana.web.fc2.com/code/polyphonic1593.htm). Image 348 contains the verso. The CSV stores source-row bounding boxes; those identify context, not proof that every character is correctly classified.
4. Read the resulting passage in the [working French text](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_reading_FR.txt). Spaces, punctuation and restored wording are editorial. Keep unresolved brackets intact.

The dated note above the historical article explains that the checking files are now available even though the preserved earlier article described their absence. Later PAR evidence and comparisons are kept separate from the frozen working edition.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](desportes-1593/article.md) | Historical context, method, interpretation, credits and limits |
| [French working text with gaps](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_reading_FR.txt) | The saved text or bounded test result |
| [Sign-by-sign choices](verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/sign_alignment.csv) | The recorded input/assignments used in the example |
| [Tomokiyo’s published key](https://cryptiana.web.fc2.com/code/polyphonic1593.htm) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
