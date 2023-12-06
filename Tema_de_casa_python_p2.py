import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fișierul CSV
df = pd.read_csv("data.csv")

# Afișarea primelor X valori pentru toate coloanele
X = 7
print("Primele {7} valori:".format(X))
print(df.head(X))

# Afișarea ultimelor Y valori pentru coloanele Durata și Puls
Y = 9
print("\nUltimele {9} valori pentru coloanele Durata și Puls:".format(Y))
print(df[['Durata', 'Puls']].tail(Y))

# Plotează toate valorile pentru coloanele Durata și Puls
plt.figure(figsize=(10, 6))
plt.plot(df['Durata'], label='Durata')
plt.plot(df['Puls'], label='Puls')
plt.title('Graficul Duratei și Pulsului')
plt.xlabel('Index')
plt.ylabel('Valoare')
plt.legend()
plt.show()
