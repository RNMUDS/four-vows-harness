# 投稿手順書（arXiv → AI and Ethics）

## 1. arXiv（先に実施）

アップロード物: `paper/arxiv/arxiv-upload.zip`（main.tex + preamble.tex。
フォントは TeX Live 同梱の原ノ味に自動フォールバックし、arXiv 環境での
コンパイル検証済み）

1. https://arxiv.org/submit → Start New Submission
2. License: 「arXiv.org perpetual, non-exclusive license」を推奨
   （Springer 投稿と両立。CC-BY を選ぶと出版社版との整合に注意が必要）
3. Category: **cs.CY** (Computers and Society) を primary、
   cross-list に **cs.CL** と **cs.AI**
4. ファイル: arxiv-upload.zip をアップロード → プロセッサに
   **XeLaTeX** を選択（2025年4月以降の Submission 1.5 で選択可能）
5. メタデータ:
   - Title: Vows, Not Posters: Value Content, Reflective Procedure,
     and What Moral Benchmarks Actually Measure — Evidence from a Four
     Great Vows Harness for Open-Weight Language Models
   - Abstract: paper/sections/00_abstract.md の本文をプレーンテキスト化
     して貼り付け（マークダウン記法と改行を除去）
   - Comments 欄: "27,352 judgments; code and data:
     https://github.com/RNMUDS/four-vows-harness"
6. プレビュー確認 → Submit（公開は通常1〜2営業日後）

## 2. AI and Ethics（arXiv ID 取得後すぐでOK）

1. https://link.springer.com/journal/43681 → Submit manuscript
   （Editorial Manager / Snapp）
2. Article type: Original Research
3. アップロード: paper/latex/main.pdf（審査用PDF）または
   arxiv/main.tex 一式。初回投稿はPDFで十分
4. Cover letter: paper/cover_letter.md を貼り付け
5. Funding: 上廣の結果に応じて 10_statements.md の該当行を確定して
   投稿画面にも同じ内容を入力
6. 推薦査読者を求められた場合の候補分野: AI ethics evaluation /
   machine ethics / Buddhist ethics and technology / LLM benchmark
   critique（具体名はご判断で）

## 3. 投稿後

- arXiv ID が出たら README.md と Declarations のプレプリント文言を更新
- リビジョン要求に備えた温存カード: 完全無価値ループ実験（bare_loop
  条件は実装済み・未実行）、Delphi 等の関連研究段落
