# Natural Products in Drug Design

## Project Overview

This project explores the application of computational structural bioinformatics and cheminformatics in natural product-based drug discovery. The primary objective was to analyse structural similarity between approved drug molecules and natural product compounds using Maximum Common Substructure (MCS) analysis to identify potential scaffold relationships and drug repurposing opportunities.

Natural products remain an important source of therapeutic compounds due to their chemical diversity and biological relevance. By comparing their molecular structures with approved drugs, this project demonstrates how computational screening can support early-stage drug discovery.

---

## Objectives

- Perform structural similarity analysis among approved drug molecules
- Perform structural similarity analysis among natural product compounds
- Compare approved drugs against natural products
- Identify structurally similar compounds for potential drug repurposing
- Generate similarity heatmaps for visual analysis
- Demonstrate high-performance computational analysis using parallel processing

---

## Project Structure

```bash
Natural Products in Drug Design/
│
├── Data/
│   ├── data_drug.csv              # Approved drug dataset
│   └── data_np.csv                # Natural product dataset
│
├── Results/
│   ├── drug_vs_drug.csv
│   ├── np_vs_np.csv
│   ├── drug_vs_np.csv
│   ├── drug_vs_drug_heatmap.png
│   ├── np_vs_np_heatmap.png
│   ├── drug_vs_np_heatmap.png
│
├── Sourcecode/
│   └── NP.py                      # Main Python analysis script
│
└── README.md
