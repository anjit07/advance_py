import numpy as np
from app.data_repository.data_loader import load_csv

def compute_statistics(file_path):
    df = load_csv(file_path)
    scores = df['score'].to_numpy()
    return {
        "mean": np.mean(scores),
        "std": np.std(scores),
        "min": np.min(scores),
        "max": np.max(scores),
    }
