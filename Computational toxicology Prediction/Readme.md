# Computational Toxicology Prediction Using KNIME Random Forest Workflow

## Project Overview
This project presents a computational toxicology workflow developed in **KNIME Analytics Platform** for predicting **Drug-Induced Liver Injury (DILI)** using a **Random Forest classification model**. Drug-induced liver injury is a major concern in pharmaceutical research, as hepatotoxicity is one of the leading causes of drug failure during development and post-marketing withdrawal.

The workflow applies cheminformatics methods to convert molecular structure data into machine-readable fingerprints and uses Random Forest machine learning for binary toxicity classification.

---

## Aim
The aim of this project is to develop a KNIME-based computational workflow for predicting drug-induced liver injury using molecular fingerprints and a Random Forest classification model.

---

## Workflow Description
The KNIME workflow includes the following steps:

1. **File Reader**
   - Imports the compound dataset containing molecular structure information.

2. **Molecule Type Cast**
   - Converts imported chemical structure data into RDKit-compatible molecular objects.

3. **RDKit Fingerprint Generation**
   - Generates molecular fingerprints from chemical structures for machine learning input.

4. **Number to String Conversion**
   - Converts the target classification variable into categorical format.

5. **Table Partitioning**
   - Splits the dataset into training and testing subsets.

6. **X-Partitioner**
   - Performs cross-validation for model robustness.

7. **Random Forest Learner**
   - Trains the Random Forest classification model.

8. **Random Forest Predictor**
   - Predicts toxicity outcomes on validation/test data.

9. **X-Aggregator**
   - Collects cross-validation results.

10. **Scorer**
   - Evaluates classification performance.

11. **ROC Curve**
   - Visualises model discrimination performance.

---

## Dataset
The dataset consists of chemical compounds labelled for binary liver toxicity classification:

- **Class 0:** Non-toxic compounds
- **Class 1:** Toxic compounds

Chemical structures are represented using:
- **SMILES notation**

---

## Model Used
This project uses:

**Random Forest Classifier**

Reason for selection:
- robust classification performance
- handles high-dimensional fingerprint data effectively
- suitable for binary toxicity prediction
- resistant to overfitting compared with simpler tree-based methods

---

## Evaluation Metrics
Model performance is assessed using:

- Accuracy
- Confusion Matrix
- ROC Curve
- AUC Score
- Precision
- Recall
- F1-score

---

## Repository Structure

```text
drug_discovery/
└── Computational toxicology Prediction/
    ├── Data/
    │   └── dataset files
    │
    ├── KNIME_Workflow/
    │   └── DILI_Prediction.knwf
    │
    ├── Results/
    │   └── output figures / report
    │
    └── README.md
