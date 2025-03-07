---
title: ekai has written 7% of its own code (outdated, now 70%)
excerpt: This article is quite out dated. ekai is currently writing about 70% of the new code in each release.
highlight_image: /assets/self-assembly.jpg
nav_exclude: true
---
{% if page.date %}
<p class="post-date">{{ page.date | date: "%B %d, %Y" }}</p>
{% endif %}

# ekai has written 7% of its own code (outdated, now 70%)

[![self assembly](/assets/self-assembly.jpg)](https://ekai.chat/assets/self-assembly.jpg)

{: .note }
This article is quite old and outdated. 
ekai is currently writing about 70% of the new code
in each release.
See
[ekai's release history](/HISTORY.html) for the latest statistics.

The
[ekai git repo](https://github.com/ekai-AI/ekai)
currently contains about 4K commits and 14K lines of code.

ekai made 15% of the commits, inserting 4.8K and deleting 1.5K lines of code.

About 7% of the code now in the repo is attributable to an ekai commit
using `git blame`.
This number is probably a significant undercount, because periodic reformatting
by `black` is likely obscuring ekai's authorship of many lines.

Here's the breakdown of the code ekai wrote in the current code base
according to `git blame`.

| File | Lines | Percent |
|---|---:|---:|
|ekai/args.py| 6 of 449 | 1.3% |
|ekai/coders/base_coder.py| 37 of 1354 | 2.7% |
|ekai/coders/editblock_coder.py| 14 of 507 | 2.8% |
|ekai/coders/editblock_func_coder.py| 6 of 141 | 4.3% |
|ekai/coders/udiff_coder.py| 2 of 421 | 0.5% |
|ekai/coders/wholefile_coder.py| 5 of 146 | 3.4% |
|ekai/coders/wholefile_func_coder.py| 4 of 134 | 3.0% |
|ekai/commands.py| 67 of 703 | 9.5% |
|ekai/diffs.py| 15 of 129 | 11.6% |
|ekai/gui.py| 2 of 533 | 0.4% |
|ekai/history.py| 19 of 124 | 15.3% |
|ekai/io.py| 55 of 368 | 14.9% |
|ekai/linter.py| 30 of 240 | 12.5% |
|ekai/main.py| 30 of 466 | 6.4% |
|ekai/mdstream.py| 3 of 122 | 2.5% |
|ekai/models.py| 22 of 549 | 4.0% |
|ekai/repo.py| 19 of 266 | 7.1% |
|ekai/repomap.py| 17 of 518 | 3.3% |
|ekai/scrape.py| 12 of 199 | 6.0% |
|ekai/versioncheck.py| 10 of 37 | 27.0% |
|ekai/voice.py| 9 of 104 | 8.7% |
|benchmark/benchmark.py| 33 of 730 | 4.5% |
|benchmark/over_time.py| 32 of 60 | 53.3% |
|benchmark/swe_bench_lite.py| 40 of 71 | 56.3% |
|scripts/blame.py| 55 of 212 | 25.9% |
|scripts/versionbump.py| 96 of 123 | 78.0% |
|setup.py| 11 of 47 | 23.4% |
|tests/test_coder.py| 48 of 612 | 7.8% |
|tests/test_commands.py| 135 of 588 | 23.0% |
|tests/test_editblock.py| 23 of 403 | 5.7% |
|tests/test_io.py| 30 of 65 | 46.2% |
|tests/test_main.py| 13 of 239 | 5.4% |
|tests/test_models.py| 6 of 28 | 21.4% |
|tests/test_repo.py| 2 of 296 | 0.7% |
|tests/test_repomap.py| 70 of 217 | 32.3% |
|tests/test_udiff.py| 7 of 119 | 5.9% |
|tests/test_wholefile.py| 37 of 321 | 11.5% |
| **Total** | **1022 of 14219** | 7.2% |


