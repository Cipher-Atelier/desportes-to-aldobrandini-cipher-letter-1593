# Critical working edition — 13 October 2026

[Literal French transcript](transcript-fr.md) · [Complete Russian translation](translation-ru.md) · [Line records](line-records.json) · [Open loci](open-loci.json) · [Additional uncertainties](additional-uncertainties.json)

This is an own literal working transcript of all 85 physical lines (r00–r51/v00–v32), with header and footer, and an own Russian translation of the historical letter using proposed readings. It is not a complete exact decipherment. Code labels, monograms, polyphonic choices and gaps remain unresolved. The translation openly marks reconstructions; proposed names and expansions owe substantial contributions to Paolo Rosson’s preceding reading and Satoshi Tomokiyo’s known-key study. Physical segmentation follows Rosson. No fresh visual verification of all 4,612 indexed signs is claimed.

Paolo Rosson’s reading and paired-copy method are pre-existing work: [pinned repository c7d3688324b0153663d0a3cce722fbe56e721730](https://github.com/pangoleen/desportes-1593/blob/c7d3688324b0153663d0a3cce722fbe56e721730/reading/f186.md). See [Tomokiyo’s known-key study](https://cryptiana.web.fc2.com/code/mayenne.htm). No discovery-priority, external human expert-review or fully blind claim is made. No blanket licence is asserted.

Primary sources: [recto f347](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f347), [verso f348](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f348). Acquisition and 129 crop recipes are metadata only. Coordinates are source pixels (exclusive right/bottom); approximate sign centres are not certified ink boundaries. Scans, crops, full modern researchers’ text/key pages, private correspondence and the local PDF containing Rosson’s full candidate column are omitted. That PDF remains local/Library only.

## Russian review summary

Все 85 строк представлены, но точная полная дешифровка не установлена. L02: четыре/пять единиц, отдельный штрих или компонент E, H/B и F/A остаются открытыми. Старый «B» из L05 по окну [800,4810,940,4910] исправлен: это E/E/M; прежнее предпочтение H на таком ложном контроле не используется. V17: deux получает ограниченное более сильное оптическое предпочтение по собственным O02 d’eux и O03 конечному s; вся фраза не установлена однозначно. O09 lasseurance принято; O07 mouuemens остаётся вопросом. M8: F/S против G/T; r49/L15: FONT/SONT неразрешимо одним знаком. V28: ME→NE — конъектура. V30: восемь единиц допускают IOUEROIT/IOURROIT, дополнительные NE для JOURNEROIT не обеспечены. Зарегистрированный контроль не дал независимо допустимых решающих значений для цели.

## Reproduce bounded checks

Python 3.10+: `python3 check_package.py`. It checks public hashes, 85 IDs, 76 run memberships, 97 open spans, 68 additional uncertainties and the generated literal reader. Pixel checks explicitly report SKIPPED unless `--pixels LOCAL_EDITION_PATH` supplies original local tiles and crops; that optional mode needs Pillow. It checks hashes and crop reconstruction, not optical reading correctness.

`python3 build_reader.py` regenerates the literal French file from curated records. `python3 test_candidates.py EXTERNAL_CANDIDATES.json` tests a supplied mapping of physical row ID to string, using retained repository classes and Tomokiyo’s credited key. Put clear-script segments in `{braces}` to exclude them from the cipher projection; `non lu` marks untestable text. Unknown units may consume 0–40 letters. M8 position37 retains F/S/G/T disagreement. Results are conditional compatibility; boundaries, segmentation and spelling can cause disagreement. No full Rosson transcript is bundled. The old status summary is not independently reproducible without external text and is not a correctness score.

[Local verification](local-verification.json) records 63 tiles, 129 reconstructed crops, 85 lines, 76 runs and 87 unchanged files in local unpublished snapshot a313377aa1da2b74e6b1125fd4516d6d0cb0f9e4. Public remote baseline is 20e8169. Those are historical local checks, distinct from fresh portable metadata checks. [Registered criteria](registered-control-criteria.md) and [result](registered-control-result.json) concern one fragment of [f345](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f345)/[f352](https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f352); outcome INCONCLUSIVE_FOR_TARGET, zero admitted target-deciding values.

## Narrow follow-up — 13 October 2026

[New O01 deux/choses and e-only control comparison](../followup-v16-20261013/result.md) supplies a clearer DEUX context but no unique target e/u/x or final s assignment. Exact v16 reading remains unresolved; prior tests were not repeated.
