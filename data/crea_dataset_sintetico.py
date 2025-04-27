import pandas as pd

# Creiamo un dizionario con i dati dei clienti
data = {
    'Cliente': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12'],
    'Spesa_Totale': [150, 20, 500, 30, 600, 100, 250, 40, 700, 80, 350, 90],
    'Numero_Ordini': [3, 1, 10, 2, 12, 2, 5, 3, 15, 1, 7, 4],
    'Frequenza_Visite': [4, 2, 5, 1, 4, 3, 4, 2, 5, 1, 3, 2]
}

# Creiamo un DataFrame Pandas dal dizionario
df = pd.DataFrame(data)

# Stampiamo il DataFrame per visualizzarlo
print(df)

# Salviamo il DataFrame in un file CSV nella cartella 'data'
df.to_csv('data/clienti_sintetico.csv', index=False)

print("\nDataset sintetico salvato in 'data/clienti_sintetico.csv'")
