# Computational Drug Discovery Using Machine Learning for Toxicity Prediction

## Project Overview
This project focuses on computational drug discovery using machine learning approaches for predicting **drug-induced liver injury (DILI)**. Early identification of hepatotoxic compounds is a critical step in drug discovery because toxicity remains one of the major reasons for drug failure during development and post-marketing withdrawal. This project focuses on computational drug repurposing for **Asthma (ICD-10: J45)** using machine learning and cheminformatics approaches. Drug repurposing aims to identify existing approved drugs that may have therapeutic potential for asthma, reducing the time, cost, and risk associated with traditional de novo drug discovery.

Asthma is a chronic inflammatory respiratory disease characterised by airway inflammation, bronchial hyperresponsiveness, mucus overproduction, and airflow obstruction. Despite existing treatment options, some patients remain poorly controlled, highlighting the need for alternative therapeutic strategies.

This project applies computational drug discovery workflows to identify candidate compounds using molecular descriptors, similarity analysis, and predictive modelling.

---

## Objectives
- Develop predictive models for DILI classification.
- Evaluate model performance using classification metrics.
- Demonstrate reproducible computational drug discovery workflows.
- Apply computational drug discovery techniques for candidate screening.
- Use molecular structure data for cheminformatics analysis.
- Build predictive machine learning models for compound classification.
- Compare model performance using evaluation metrics.
- Support reproducible computational drug repurposing research.

---

## Methodology

### Data Collection
Drug and compound datasets related to asthma were collected and prepared for computational analysis.

Disease classification:
- **Disease:** Asthma
- **ICD-10 Code:** J45

---

### Molecular Processing
Chemical structures were represented using:
- **SMILES notation**

Structures were processed using:
- KNIME Analytics Platform
- RDKit cheminformatics tools

Molecular descriptors/fingerprints were generated for machine learning analysis.

---

### Machine Learning Models
Multiple classification models were implemented and compared:

- Logistic Regression
- Linear Discriminant Analysis (LDA)
- K-Nearest Neighbours (KNN)
- Decision Tree
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest

---

### Data Balancing Techniques
To address class imbalance, the following techniques were applied:
- Oversampling
- Undersampling

Model performance was evaluated across balanced datasets.

---

### Evaluation Metrics
Models were assessed using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC Curve / AUC

---

## Repository Structure

```text
drug_discovery/
└── Drug_repurposing/
    ├── data/
    │   └── dataset files
    │
    ├── Sourcecode/
    │   └── KNIME workflows / scripts
    │
    ├── Results/
    │   ├── Drug Repurposing_Report.pdf
    │   ├── modelcomparison.png
    │   └── result figures
    │
    └── README.md
