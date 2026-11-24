# Support Intent Baseline

[![CI](https://github.com/MoustafaMZaalouk/support-intent-baseline/workflows/Reproducible%20project%20checks/badge.svg)](https://github.com/MoustafaMZaalouk/support-intent-baseline/blob/main/.github/workflows/test.yml)

*Live workflow status, not a production-readiness or model-quality rating.*

Test word TF-IDF and logistic regression on an original, tiny English support-intent corpus.

A small educational project prepared with AI assistance for Moustafa Zaalouk's portfolio. This is new demonstration code, not a claim about past employment, research, clients or production deployment. It does not reuse another person's project under a different name.

## Run it

Use Python 3.10 or newer. The recorded local run used Python 3.10.12. A virtual environment is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python demo.py
python -m unittest -v
```

On Windows use `.venv\Scripts\activate` instead. The first command runs the full experiment and writes `results.json`. The second runs four checks. No API keys, paid services or internet data downloads are needed after dependency installation.

## Recorded results

These are small educational benchmarks, not evidence of real-world generalization. Perfect scores on this small evaluation are not a production accuracy claim.

![Recorded local result](results.png)

These values are generated from `results.json`, not estimated or copied. Rerun the code to check them. Minor numerical differences may occur across platforms. Full per-example or per-fold details, where applicable, are in the JSON file.

| Measure | Local result |
| --- | ---: |
| Accuracy | 1.000000 |
| Macro F1 | 1.000000 |
| Majority accuracy | 0.333333 |
| Seed | 42 |
| Test rows | 12 |
| Train rows | 30 |

`verification.txt` records the local test run. The included GitHub Actions workflow is a reproducible check, not a claim that remote CI has already passed.

## How to read the code

1. `demo.py`: data construction/loading, split, model, evaluation and output.
2. `test_demo.py`: output consistency and three experiment-specific checks.
3. `results.json`: the actual captured local results.
4. `requirements.txt`: exact versions used locally.

## Publishing and CI

The initial source is stored as a checksummed ZIP inside the workflow so GitHub can restore exact filenames and the chart without a manual multi-file upload. On its first run it unpacks this original AI-assisted source, tests it, runs the experiment and commits the initialized files as `github-actions[bot]`. Later runs test the actual checked-out source; they do not overwrite it from the bundle. This automation history is not a claim of manual authorship or review.

## Data and attribution

Original hand-written English examples embedded in demo.py. No copied support tickets or personal data.

The experiment uses NumPy, SciPy and scikit-learn rather than claiming to implement their estimators from scratch. Their licenses and dataset terms remain separate from this repository's MIT license. No upstream code, author name or license was removed.

## What this does not prove

The hand-written test examples are intentionally related to the hand-written training examples. This is an explanatory smoke benchmark, not an independent customer-support evaluation. English only; no unknown-intent rejection, privacy review or live integration.

## شرح بالمصري

الفكرة: نحول جمل الدعم لأرقام TF-IDF ونصنفها: دفع، دخول، أو عطل. الأمثلة إحنا كاتبينها وعددها قليل، فالنتيجة دي للتعليم بس مش جودة خدمة عملاء حقيقية.

لما تشرح المشروع: قول مصدر الداتا، اتقسمت إزاي، إيه الـbaseline، بنقيس بإيه، وإيه حدود النتيجة. ما تقولش إنه شغال في production أو نتيجة على داتا حقيقية لو التجربة صناعية.

## Next experiment

Replace the demonstration data with an appropriately licensed dataset, define an independent evaluation protocol before tuning, and report failures as well as successes. Keep private data and credentials out of commits.
