"""
covid-largo-neuropsiquiatrico
==============================
DOI: https://doi.org/10.7910/DVN/QUWC1F
Autor: Juan Moises de la Serna (ORCID: 0000-0002-8401-8018)

Uso:
    from covid_largo_neuropsiquiatrico import cargar_datos, resumen_prevalencia
    df = cargar_datos()
"""
from .cargador import cargar_datos, listar_archivos, resumen_prevalencia, obtener_doi
__version__ = "1.0.0"
__doi__ = "10.7910/DVN/QUWC1F"
__autor__ = "Juan Moises de la Serna"
__all__ = ["cargar_datos","listar_archivos","resumen_prevalencia","obtener_doi"]
