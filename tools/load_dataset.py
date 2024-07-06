import pandas as pd
import joblib

def load_dataset(path):
    return pd.read_excel(path, usecols=["ratings_int", "restaurant", "city", "preprocessed_text"])

def load_from_serialized(path):
    return joblib.load(path)


