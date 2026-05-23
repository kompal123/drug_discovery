import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdFMCS
from multiprocessing import Pool
from itertools import product
from tqdm import tqdm
import os


def load_data(path):
    df = pd.read_csv(path)

    df.columns = df.columns.str.strip().str.upper()

    df = df.rename(columns={
        "NAME": "Name",
        "DRUG NAME": "Name",
        "COMPOUND NAME": "Name",
        "TITLE": "Name",
        "SMILES": "SMILES",
        "SMILE": "SMILES",
        "CANONICAL SMILES": "SMILES"
    })

    df = df.dropna(subset=["Name", "SMILES"])

    return df


def MCSS(q1, q2):
    m1 = Chem.MolFromSmiles(str(q1))
    m2 = Chem.MolFromSmiles(str(q2))

    if m1 is None or m2 is None:
        return None

    a = m1.GetNumAtoms()
    b = m2.GetNumAtoms()

    r = rdFMCS.FindMCS(
        [m1, m2],
        ringMatchesRingOnly=True,
        timeout=2
    )

    c = r.numAtoms

    if c < 0:
        c = 0

    sm = r.smartsString

    sim = c / (a + b - c) if (a + b - c) > 0 else 0

    return {
        "A#": a,
        "B#": b,
        "MCS": sm,
        "MCSAtomCount": c,
        "MCSS": sim
    }


def process_pair(pair):
    row1, row2 = pair

    result = MCSS(row1["SMILES"], row2["SMILES"])

    if result is None:
        return None

    return {
        "NameA": row1["Name"],
        "NameB": row2["Name"],
        "CmpdA": row1["SMILES"],
        "CmpdB": row2["SMILES"],
        **result
    }


def compare_parallel(df1, df2, output_csv, heatmap_file, workers=32):
    records1 = df1.to_dict("records")
    records2 = df2.to_dict("records")

    total = len(records1) * len(records2)

    print(f"\nRunning {output_csv}")
    print(f"Total comparisons: {total}")
    print(f"Workers: {workers}")

    pair_generator = product(records1, records2)

    results = []

    with Pool(processes=workers) as pool:
        for res in tqdm(
            pool.imap_unordered(
                process_pair,
                pair_generator,
                chunksize=500
            ),
            total=total
        ):
            if res:
                results.append(res)

    result_df = pd.DataFrame(results)

    result_df.to_csv(output_csv, index=False)

    pivot = result_df.pivot(
        index="NameA",
        columns="NameB",
        values="MCSS"
    ).fillna(0)

    cluster = sns.clustermap(
        pivot,
        cmap="magma",
        figsize=(12, 12)
    )

    cluster.savefig(heatmap_file, dpi=300)
    plt.close()

    return result_df


if __name__ == "__main__":
    drug_df = load_data("data_drug.csv")
    np_df = load_data("data_np.csv")

    print("Drug molecules:", len(drug_df))
    print("NP molecules:", len(np_df))

    WORKERS = 32

    drug_vs_drug = compare_parallel(
        drug_df,
        drug_df,
        "drug_vs_drug.csv",
        "drug_vs_drug_heatmap.png",
        WORKERS
    )

    np_vs_np = compare_parallel(
        np_df,
        np_df,
        "np_vs_np.csv",
        "np_vs_np_heatmap.png",
        WORKERS
    )

    drug_vs_np = compare_parallel(
        drug_df,
        np_df,
        "drug_vs_np.csv",
        "drug_vs_np_heatmap.png",
        WORKERS
    )

    print(
        drug_vs_np.sort_values(
            "MCSS",
            ascending=False
        ).head(10)
    )