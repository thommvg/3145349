import pandas as pd
import matplotlib.pyplot as plt
import unicodedata

# Cargar los datos
df = pd.read_csv("fin.csv", encoding="utf-8-sig")

# Normalizar nombres de columnas
def norm(s):
    s = s.strip().replace('"', '')
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return s.replace(' ', '_').lower()

df.columns = [norm(c) for c in df.columns]

# Convertir a numérico y limpiar datos
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df["tiempo_sesion"] = pd.to_numeric(df["tiempo_sesion"], errors="coerce")
df = df.dropna(subset=["edad", "tiempo_sesion"]).drop_duplicates()

# Crear scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(
    df["edad"], 
    df["tiempo_sesion"], 
    c=range(len(df)),       # colores distintos para cada punto
    cmap="viridis", 
    s=80, 
    edgecolors="black"
)

plt.title("Relación entre Edad y Tiempo de Sesión")
plt.xlabel("Edad")
plt.ylabel("Tiempo de sesión (minutos)")
plt.grid(linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

#este código carga los datos de un archivo csv usando pandas y después usa Seaborn para crear un gráfico de dispersión (scatterplot) mostrando la relación entre la edad y el tiempo de cada persona. cada punto en el gráfico representa un registro para que sea más visual, Seaborn automáticamente les da diferentes colores. Al final, plt.show() abre la ventana con la gráfica ya lista para analizar,
# en resumidas cuentas, primero leemos los datos, luego le decimos a Seaborn qué columnas graficar, y finalmente mostramos la gráfica para poder interpretarla visualmente