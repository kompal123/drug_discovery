# Drug Repurposing for Pulmonary Arterial Hypertension (PAH)

## Project Overview
This project explores a computational drug repurposing approach for **Pulmonary Arterial Hypertension (PAH)** using network medicine and cheminformatics methodologies. The objective is to identify approved non-PAH drugs with potential therapeutic relevance by analysing molecular similarity, drug interactions, and biological network proximity.

Pulmonary Arterial Hypertension is a progressive and life-threatening cardiovascular disease characterised by vascular remodelling, elevated pulmonary arterial pressure, and eventual right heart failure. Since traditional drug development is time-consuming and expensive, drug repurposing offers a faster and cost-effective strategy by identifying new applications for already approved drugs.

This project follows a network-based drug repositioning framework inspired by computational systems pharmacology approaches.

---

## Objectives
- Identify candidate drugs for PAH repurposing.
- Analyse drug–drug interaction relationships.
- Compare molecular structures using chemical fingerprints.
- Map drug targets and disease proteins onto the human interactome.
- Prioritise candidate drugs based on biological network proximity.
- Present reproducible computational drug discovery workflows.

---

## Methodology

### 1. Drug Selection
A set of approved PAH drugs was selected as the initial reference group.

### 2. Drug Interaction Analysis
Drug interaction data were obtained from **DrugBank** to identify drugs interacting with approved PAH therapies.

### 3. Chemical Similarity Screening
Chemical structures were compared using molecular fingerprint approaches:

- **Morgan fingerprints**
- Structural similarity metrics

This filtering step reduced the candidate pool to structurally relevant compounds.

### 4. Network Medicine Analysis
Drug targets and PAH disease-associated proteins were mapped onto the human protein interaction network (**human interactome**) to evaluate biological proximity.

### 5. Candidate Prioritisation
Drugs with statistically significant proximity to the PAH disease module were identified as promising repurposing candidates.

---

## Repository Structure

```text
drug_discovery/
└── Drug_repurposing/
    ├── Results/
    │   ├── Drug Repurposing_Report.pdf
    │   ├── modelcomparison.png
    │
    ├── Sourcecode/
    │   └── (analysis scripts / workflow files)
    │
    ├── data/
    │   └── (input datasets)
    │
    └── README.md
