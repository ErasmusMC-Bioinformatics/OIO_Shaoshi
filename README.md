# OIO_Shaoshi

The directory **Deciphering_TME** is for the reproducibility of the paper **Deciphering Tumour Microenvironment of Liver Cancer through Deconvolution of Bulk RNA-seq Data with Single-cell Atlas**

Prepocessed data can be downloaded

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7315791.svg)](https://doi.org/10.5281/zenodo.7315791)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7467268.svg)](https://doi.org/10.5281/zenodo.7467268)

## Preprocessing

The script

**/Deciphering_TME/Preprocess/SCAN_Normalizaiton.r**

shows how to retrieve expression matrix of a study from GEO database. The function **SCAN** in R package **SCAN.UPC** provides a one-step process to download the raw data (CEL files) and corrects the GC-content related bias.

The script

**/Deciphering_TME/Preprocess/BioMart.r**

shows an example to transfer gene symbol with the R package **BiomArt**.

The script

**/Deciphering_TME/Preprocess/Remove.Duplication.RNA-seq.py**

shows an example to remove duplication of gene symbol in the expression matrix. For RNA-seq matrix, duplicated features are recommended to collapse with **Summation** strategy, while those for microarray studies are recommended to use **MaxMean** strategy.

The script

**/Deciphering_TME/Preprocess/ScRNA-seq_H5AD.ipynb**

shows how to pack the expression matrix of scRNA-seq atlas into H5AD file.


## Pseudobulk Generation

The script

**/Deciphering_TME/Preprocess/Pseudobulk_Generator.py**

shows how to generate pseudobulk RNA-seq expression matrix for validation experiments. 

## Estimation of Cell Abundance Through Support Vector Regression

The script in the directory

**SVR_Estimation**

show the work flow to estimate the abundance of a specific cell type in bulk RNA-seq samples with support vector regression and single-cell RNA-seq atlas.

## Figure Plot

All the scripts in the directory

**/Deciphering_TME/Figures**

show the generation of figures in the main text and supplements.

