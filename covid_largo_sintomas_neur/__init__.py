"""Prevalencia global de síntomas neurológicos y psiquiátricos del COVID Largo (niebla mental, ansiedad
DOI: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F | GitHub: https://github.com/juanmoisesd/covid-largo-sintomas-neuropsiquiatricos-prevalencia-2021-2024"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Prevalencia global de síntomas neurológicos y psiquiátricos del COVID Largo (nie. Zenodo. https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F'
def info(): print(f"Dataset: Prevalencia global de síntomas neurológicos y psiquiátricos del COVID Largo (nie\nDOI: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F\nGitHub: https://github.com/juanmoisesd/covid-largo-sintomas-neuropsiquiatricos-prevalencia-2021-2024")