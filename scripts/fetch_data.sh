#!/bin/bash
# Fetch third-party benchmark datasets (not redistributed in this repo).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data && cd data

echo "== ETHICS (Hendrycks et al. 2021) =="
curl -sO https://people.eecs.berkeley.edu/~hendrycks/ethics.tar
tar xf ethics.tar

echo "== MoralChoice (Scherrer et al. 2023) =="
mkdir -p moralchoice && cd moralchoice
for f in low high; do
  curl -sO "https://raw.githubusercontent.com/ninodimontalcino/moralchoice/master/data/scenarios/moralchoice_${f}_ambiguity.csv"
done
cd ..

echo "== SCRUPLES Dilemmas (Lourie et al. 2021) =="
curl -sO https://storage.googleapis.com/ai2-mosaic-public/projects/scruples/v1.0/data/dilemmas.tar.gz
mkdir -p scruples && tar xzf dilemmas.tar.gz -C scruples

echo "== MMLU (Hendrycks et al. 2021) =="
curl -s -o mmlu.tar https://people.eecs.berkeley.edu/~hendrycks/data.tar
tar xf mmlu.tar

echo "done. datasets in data/"
