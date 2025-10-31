# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains data index files for NIST's Genome in a Bottle (GIAB) project. The indexes catalog sequencing and alignment data files for reference human genome samples used in benchmarking variant calling and sequencing technologies.

## Repository Structure

The repository is organized into three main directories, each representing a different reference sample set:

- **AshkenazimTrio/**: Ashkenazi Jewish trio - Son (HG002/NA24385), Father (HG003/NA24149), Mother (HG004/NA24143)
- **ChineseTrio/**: Chinese trio - Son (HG005/NA24631), Father (HG006/NA24694), Mother (HG007/NA24695)
- **NA12878/**: Individual sample (HG001/NA12878) - widely used CEPH reference

Root directory also contains metadata Excel files documenting the sequencing platforms and datasets.

## Index File Format

All index files are tab-separated value (TSV) files with headers. There are two types:

### Sequence Index Files
- Naming pattern: `sequence.index.{Sample}_{Platform}_{Details}_{Date}`
- Contain raw sequencing data file locations (FASTQ, FASTA, HDF5, BNX, etc.)
- Common columns: file URL, MD5 checksum, optional NIST_SAMPLE_NAME

### Alignment Index Files
- Naming pattern: `alignment.index.{Sample}_{Platform}_{Aligner}_{Reference}_{Date}`
- Contain aligned sequencing data (BAM files, BioNano cmap/xmap, etc.)
- Common columns: BAM URL, BAM_MD5, BAI URL, BAI_MD5

### Sample-Specific Files
- Files ending with `.HG00X` (e.g., `.HG002`) contain data for that specific individual only
- Files without a sample suffix contain data for all individuals in that trio/set

## Common Tasks

### Updating Index Files
When adding or modifying index entries:
1. Maintain tab-separated format with proper headers
2. Include MD5 checksums for all data files
3. Use FTP URLs pointing to https://ftp.ncbi.nlm.nih.gov/ReferenceSamples/giab/
4. Follow existing naming conventions for consistency
5. Create both a combined "All" file and individual `.HG00X` files when appropriate

### Index File Conventions
- Use tabs (not spaces) as delimiters
- Keep headers consistent with existing files of the same type
- Reference genome builds: GRCh37 (hg19) and/or GRCh38 (hg38)
- Date format in filenames: MMDDYYYY (e.g., 10082018)

### Verifying Index Files
- Check that URLs are accessible
- Verify MD5 checksums match the actual data files
- Ensure proper mapping between sequence/alignment pairs for the same dataset
- Confirm sample IDs (HG00X) are consistent across files

## Sequencing Platforms Cataloged

The repository indexes data from diverse sequencing technologies including:
- Illumina (WGS, exome, mate-pair, various read lengths)
- PacBio (CLR, CCS with various insert sizes)
- Oxford Nanopore (2D, ultralong)
- 10X Genomics (GemCode, Chromium)
- BGI (BGISEQ500, MGISEQ, stLFR)
- Complete Genomics
- BioNano optical mapping
- Ion Torrent/Proton
- SOLiD

## Reference Genome Builds

Alignments are provided against:
- **GRCh37** (hg19) - most common
- **GRCh38** (hg38) - newer reference
- Some datasets aligned to both builds
