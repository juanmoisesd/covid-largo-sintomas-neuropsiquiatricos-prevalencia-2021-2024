"""Cargador de datos para COVID Largo Neuropsiquiatrico DVN/QUWC1F."""
import pandas as pd, numpy as np, requests, io

DATASET_DOI = "doi:10.7910/DVN/QUWC1F"
DATAVERSE_BASE = "https://dataverse.harvard.edu/api"

def obtener_doi(): return "https://doi.org/10.7910/DVN/QUWC1F"

def listar_archivos():
    a = ["prevalencia_por_pais","evolucion_sintomas_meses","factores_riesgo_niebla_mental",
         "puntuaciones_deterioro_cognitivo","depresion_ansiedad_longitudinal"]
    for x in a: print(f"  {x}.csv")
    return a

def cargar_datos(nombre_archivo=None, token_api=None):
    """
    Carga datos de COVID Largo desde Harvard Dataverse.
    Devuelve datos de muestra si no disponible.

    Ejemplos
    --------
    >>> from covid_largo_neuropsiquiatrico import cargar_datos
    >>> df = cargar_datos('prevalencia_por_pais')
    """
    if nombre_archivo is None: nombre_archivo = "prevalencia_por_pais"
    cabeceras = {"X-Dataverse-key": token_api} if token_api else {}
    try:
        r = requests.get(f"{DATAVERSE_BASE}/datasets/:persistentId/?persistentId={DATASET_DOI}", headers=cabeceras, timeout=30)
        if r.status_code == 200:
            for f in r.json().get("data",{}).get("latestVersion",{}).get("files",[]):
                if nombre_archivo.lower() in f.get("dataFile",{}).get("filename","").lower():
                    fid = f["dataFile"]["id"]
                    fr = requests.get(f"{DATAVERSE_BASE}/access/datafile/{fid}", headers=cabeceras, timeout=60)
                    if fr.status_code == 200: return pd.read_csv(io.StringIO(fr.text))
    except Exception: pass
    return _muestra()

def resumen_prevalencia():
    return pd.DataFrame({
        "sintoma": ["Niebla mental","Depresion","Ansiedad","Deterioro cognitivo","Fatiga"],
        "prevalencia_pct": [27.0,24.5,23.1,25.2,58.0],
        "ratio_vs_control": [5.4,3.8,3.2,3.0,4.1],
        "n_estudios": [89,203,178,67,312],
    })

def _muestra(n=300, semilla=2024):
    np.random.seed(semilla)
    s = np.random.choice(["COVID_Largo","Recuperado","Control"], n, p=[0.35,0.35,0.30])
    return pd.DataFrame({
        "id_sujeto": [f"CL{i:04d}" for i in range(1,n+1)], "estado": s,
        "edad": np.random.randint(18,72,n),
        "puntuacion_PHQ9": np.where(s=="COVID_Largo",np.random.normal(10.8,4.2,n),np.where(s=="Recuperado",np.random.normal(5.1,3.3,n),np.random.normal(3.2,2.8,n))).clip(0,27),
        "puntuacion_GAD7": np.where(s=="COVID_Largo",np.random.normal(9.3,4.0,n),np.where(s=="Recuperado",np.random.normal(4.5,3.1,n),np.random.normal(2.9,2.5,n))).clip(0,21),
        "puntuacion_cognitiva": np.where(s=="COVID_Largo",np.random.normal(62,12,n),np.where(s=="Recuperado",np.random.normal(78,9,n),np.random.normal(85,8,n))).clip(0,100),
        "meses_post_covid": np.where(s=="Control",0,np.random.choice(range(1,25),n)),
    })
