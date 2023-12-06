import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fișierul CSV
df = pd.read_csv("data.csv")

# Afișarea primelor X valori pentru toate coloanele
X = 7
print(f"Primele {X} valori:".format(X))
print(df.head(X))

plt.figure(figsize=(10, 5))
plt.plot(df.index[:X], df['Durata'][:X], label='Durata', marker='|',ms= 20, color = 'b')
plt.plot(df.index[:X], df['Puls'][:X], label='Puls', marker='|',ms = 20, color = 'r')
plt.title(f'Primele {X} valori pentru Durata si Puls')
plt.xlabel('Puls')
plt.ylabel('Durata')
plt.legend()
plt.show()


# Afișarea ultimelor Y valori pentru coloanele Durata și Puls
Y = 9
print(f"\nUltimele {Y} valori pentru coloanele Durata și Puls:".format(Y))
print(df[['Durata', 'Puls']].tail(Y))

plt.figure(figsize=(10, 5))
plt.plot(df.index[-Y:], df['Durata'].tail(Y), label='Durata', marker='|',ms=20, color = 'b')
plt.plot(df.index[-Y:], df['Puls'].tail(Y), label='Puls', marker='|',ms=20, color = 'r')
plt.title(f'Ultimele {Y} valori pentru Durata si Puls')
plt.xlabel('Puls')
plt.ylabel('Durata')
plt.legend()
plt.show()

# Plotează toate valorile pentru coloanele Durata și Puls
plt.figure(figsize=(10, 6))
plt.plot(df['Durata'], label='Durata')
plt.plot(df['Puls'], label='Puls')
plt.title('Graficul Duratei și Pulsului')
plt.xlabel('Index')
plt.ylabel('Valoare')
plt.legend()
plt.show()

