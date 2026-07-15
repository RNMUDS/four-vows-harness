# LaTeX build

- Source of truth: `../sections/*.md` → assembled `../draft_full.md`.
- Rebuild: from `paper/`:
  `pandoc draft_full.md -o latex/main.tex --standalone --pdf-engine=xelatex -H latex/preamble.tex -V documentclass=article -V fontsize=11pt --metadata title="..." --metadata author="..."`
  then `xelatex main.tex` (twice). xelatex is required for the CJK
  characters (四弘誓願 etc.; font: Hiragino Mincho ProN via xeCJK).
- Submission note: AI and Ethics accepts standard LaTeX at initial
  submission; switch `documentclass` to Springer `sn-jnl` (template
  "sn-article", download from Springer author pages) only for the
  accepted-version typeset. Body content is class-agnostic.
