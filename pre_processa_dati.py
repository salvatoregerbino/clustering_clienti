import pandas as pd
from sklearn.preprocessing import StandardScaler

# Percorso del file CSV (lo stesso dello script carica_dati.py)
file_path = 'data/clienti_sintetico.csv'

try:
    # Carica il dataset
    cliente_df = pd.read_csv(file_path)

    # Selezione delle feature per il clustering
    features_per_clustering = ['Spesa_Totale', 'Numero_Ordini', 'Frequenza_Visite']
    X = cliente_df[features_per_clustering]

    # Standardizzazione delle feature
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Creazione di un nuovo DataFrame con le feature standardizzate
    cliente_df_scaled = pd.DataFrame(X_scaled, columns=features_per_clustering)

    # Aggiungiamo l'identificatore del cliente al DataFrame scalato (utile per riferimento)
    cliente_df_scaled['Cliente'] = cliente_df['Cliente']

    # Stampa le prime righe del DataFrame scalato
    print("Prime 5 righe del dataset con feature standardizzate:")
    print(cliente_df_scaled.head())

    # Stampa alcune informazioni sul DataFrame scalato
    print("\nInformazioni sul dataset con feature standardizzate:")
    print(cliente_df_scaled.info())

    # La variabile 'cliente_df_scaled' ora contiene le feature pronte per il clustering

except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato. Assicurati che il percorso sia corretto.")
except ImportError as e:
    print(f"Errore di importazione: {e}. Assicurati che la libreria sia installata.")
except Exception as e:
    print(f"Si è verificato un errore durante la pre-elaborazione dei dati: {e}")
