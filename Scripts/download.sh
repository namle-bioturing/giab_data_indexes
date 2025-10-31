#!/bin/bash

# Download benchmark files
while IFS=$'\t' read -r sample ref url; do
  [[ $sample =~ ^#.*$ || -z "$sample" ]] && continue
  dest="$sample/benchmark"
  echo "→ $dest/$(basename "$url")"
  mkdir -p "$dest"
  # wget -P "$dest" "$url"
done < benchmark.txt

# Download sequence files for short reads
while IFS=$'\t' read -r url1 _ url2 _; do
  for url in $url1 $url2; do
    [[ $url =~ ^(ftp|http) ]] || continue
    sample=$(echo "$url" | grep -oP 'HG00\d')
    path=$(echo "$url" | sed 's|.*AshkenazimTrio/[^/]*/[^/]*/[^/]*/||')
    dest="$sample/raw/$(dirname "$path")"
    echo "→ $dest/$(basename "$url")"
    mkdir -p "$dest"
    # wget -P "$dest" "$url"
  done
done < <(tail -n +2 sequence.index.AJtrio_Illumina300X_wgs_07292015_updated)
