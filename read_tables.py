import pandas as pd

simpson = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Episodios_de_Los_Simpson#Temporadas")
print(simpson[1])