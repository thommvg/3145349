import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import unicodedata

df = pd.read_csv("datos.csv", encoding="utf-8-sig")

def norm(s):
    s = s.strip().replace('"', '')
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return s.replace(' ', '_').lower()

df.columns = [norm(c) for c in df.columns]
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df = df.dropna(subset=['edad', 'pais']).drop_duplicates()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='pais', y='edad')
plt.title('Distribución de edades por país')
plt.xlabel('País')
plt.ylabel('Edad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#se muestra como se distribuyen las edades de usuarios según su país usando un diagrama de bigotes. primero se cargan las librerías pandas, seaborn y matplotlib para poder leer datos, limpiar texto y graficar. Luego se abre el archivo datos.csv asegurando que se lean bien las funcines o lo que dicen los datos 
# Se define una función para limpiar los nombres de las columnas, quitando comillas, tildes y espacios, y se aplica para que queden uniformes
#despues convierte la parte de edades en numeros y datos visibles en la misma tabla y eliminan datos inecesarios para evitar errores junto a que
# se crea la tabla :)