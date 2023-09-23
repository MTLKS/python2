import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load the dataset located at `path` into a pandas DataFrame."""
    try:
        df = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", df.shape)
        return df
    except Exception as e:
        print(e.__class__.__name__ + ":", e)
        return None
