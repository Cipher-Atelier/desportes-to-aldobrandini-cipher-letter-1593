# Verify desportes-1593

[Repository overview](../README.md) · [Read the result and check one example by hand](../READING_GUIDE.md)

## What this check does

The supported command first checks the published file fingerprints in `SHA256SUMS.txt`, then repeats this investigation’s saved calculation. A fingerprint (SHA-256) identifies exact file bytes; it is not a scientific correctness score.

The replay checks recorded-class/allowed-letter compatibility, the saved working-text hash and two retained second arrays. It does not perform a new image transcription or resolve every polyphonic choice.

It uses Python’s standard library, makes no network requests, and needs no downloaded scans or extra packages for this default check. It does not fit a new key or edit the research evidence.

## Download and open the folder

1. On [this repository’s main page](https://github.com/Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593), choose **Code → Download ZIP**, following [GitHub’s download instructions](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).
2. Extract the whole ZIP. Keep its folders and files together; do not download only `check_all.py`.
3. Open a terminal in the extracted top-level folder: it contains `README.md`, `SHA256SUMS.txt` and the `verification` folder. For example, after navigating to its parent directory:

```sh
cd desportes-to-aldobrandini-cipher-letter-1593-main
```

If you already use Git, cloning the full repository is an alternative:

```sh
git clone https://github.com/Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593.git
cd desportes-to-aldobrandini-cipher-letter-1593
```

## Run the supported check

Use **Python 3.10 or later**. On macOS/Linux, check the installed version and run:

```sh
python3 --version
python3 verification/check_all.py
```

On Windows, if the Python launcher is installed, use:

```powershell
py -3 --version
py -3 verification/check_all.py
```

If your Python command is `python` rather than `python3` or `py -3`, use that command after confirming it is Python 3.10+. If Python is absent, obtain it from [python.org](https://www.python.org/downloads/) or your operating system’s supported installation method.

Run ordinary Python, with no `-O`/`-OO` options and no `PYTHONOPTIMIZE` setting that enables optimization: the checker relies on assertions.

## What a successful run looks like

The command exits successfully and prints a JSON report with top-level `"status": "passed"`. It also reports how many fingerprinted files were checked. That file count can change when documentation is updated.

The following are the expected status/topic/replay fields; the actual report also includes `files_checked` and scope limits:

```json
{
  "status": "passed",
  "topic": "desportes-1593",
  "replay": {
    "desportes-1593": {
      "status": "PASS",
      "scope": "mechanical replay only",
      "indexed_regions": 4612,
      "assigned_positions": 4108,
      "expanded_letters": 4295,
      "second_arrays_matched": [
        "L05",
        "L10"
      ],
      "working_text_sha256": "fd1708f32a534c3afd8010ee72048fbff9a05e4548b89df5366c06534cab5af0",
      "limit": "Compatibility is not a unique reading or historical accuracy; PAR addendum not merged into frozen text."
    }
  }
}
```

In ordinary words: **4,612 indexed regions, 4,108 compatible assignments, 4,295 expanded letters; separately transcribed class arrays match for rows L05 and L10.**

## What passing does not establish

The replay checks 4,612 indexed regions, 4,108 compatible assignments and 4,295 expanded letters. These are bookkeeping/compatibility counts, not independent correctness scores, unique choices or a newly recovered key.

Passing verifies that these published inputs and saved rules give the recorded result. It does not certify source-image transcription, historical truth, a unique interpretation, author identity, discovery priority or external expert review. To inspect those questions, follow [the manual example and source-checking route](../READING_GUIDE.md#check-one-example-by-hand).

## If it fails

| Symptom | What to do |
| --- | --- |
| Python command not found, or version below 3.10 | Install/use Python 3.10+; confirm its version first |
| Cannot open `verification/check_all.py` | Move into the extracted repository’s top-level folder |
| Missing file | Extract the complete ZIP again; retain the directory structure |
| `Hash mismatch: ...` | Compare with an untouched download of the same version; edits change the fingerprint |
| Optimization warning | Run without `-O`/`-OO` and disable any `PYTHONOPTIMIZE` setting |
| Assertion, replay mismatch or another error on an untouched package | Save the complete error, Python version and repository commit/download reference; report it in a [research issue](https://github.com/Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593/issues/new?template=research.yml) |

Do not change the evidence, expected results or fingerprints just to make a failing check pass. If reporting reproduction, record the commit SHA shown on GitHub; a later `main` download may contain documentation updates. A [commit-specific archive](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives#source-code-archive-urls) pins the file version.

## Preserved publication scope

Partial edition using Tomokiyo’s known key, with Rosson’s prior reading credited. Replay checks 4,612 indexed regions, 4,108 compatible assignments and 4,295 expanded letters; polyphonic choice remains interpretive.

Partial edition with Tomokiyo key; Rosson prior reading credited. Polyphonic choice and source glyphs remain interpretive. Later PAR evidence is not merged into this frozen working edition. Raw scans need separate rights review.

From the repository root run `python3 verification/check_all.py` with Python 3.10 or later, without optimization. It verifies the repository checksum inventory and invokes only [readings/replay.py](readings/replay.py). The check uses the standard library and makes no network requests. Obtain source images separately under their provider terms for visual review. Source credit is not image redistribution permission.

See the [research record](../desportes-1593/article.md) and [machine-readable scope](TOPIC_SCOPE_INDEX.json). Successful arithmetic or exact output replay does not prove historical truth, unique interpretation or priority.
