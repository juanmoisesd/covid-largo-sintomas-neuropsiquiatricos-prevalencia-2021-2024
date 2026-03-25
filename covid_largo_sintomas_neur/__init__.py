"""Prevalencia global de síntomas neurológicos y psiquiátricos del COVID Largo (nie
DOI:https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Prevalencia global de síntomas neurológicos y psiquiátricos "
def info():print("DOI: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QUWC1F\nGitHub: https://github.com/juanmoisesd/covid-largo-sintomas-neuropsiquiatricos-prevalencia-2021-2024")
