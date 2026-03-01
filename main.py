import requests
from bs4 import BeautifulSoup

# Paso A: Conectarnos a la web
url = "https://realpython.github.io/fake-jobs/"
respuesta = requests.get(url)

# Paso B: "Masticar" el HTML para que Python lo entienda
sopa = BeautifulSoup(respuesta.content, "html.parser")

# Paso C: Buscar el contenedor de los resultados
contenedor = sopa.find(id="ResultsContainer")
tarjetas = contenedor.find_all("div", class_="card-content")

# Paso D: Mostrar los datos en la terminal
print(f"Buscando empleos en {url}...\n")

for t in tarjetas:
    titulo = t.find("h2", class_="title").text.strip()
    empresa = t.find("h3", class_="company").text.strip()
    link = t.find_all("a")[1]["href"] # El segundo enlace suele ser el de "Apply"
    
    print(f"💼 PUESTO: {titulo}")
    print(f"🏢 EMPRESA: {empresa}")
    print(f"🔗 LINK: {link}")
    print("-" * 30)