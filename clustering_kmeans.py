import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Percorso del file CSV
file_path = 'data/clienti_sintetico.csv'

try:
    # Carica il dataset
    cliente_df = pd.read_csv(file_path)

    # Selezione delle feature per il clustering
    features_per_clustering = ['Spesa_Totale', 'Numero_Ordini', 'Frequenza_Visite']
    X = cliente_df[features_per_clustering]

    # Standardizzazione delle feature (assicuriamoci che sia fatta qui o che il file pre-processa_dati.py sia eseguito prima)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Scelta del numero di cluster (k) - per ora scegliamo 3 come esempio
    n_clusters = 3

    # Inizializzazione e applicazione dell'algoritmo k-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10) # n_init per evitare problemi di convergenza
    cliente_df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Visualizzazione dei risultati (prime righe con l'assegnazione dei cluster)
    print("Prime righe del dataset con l'assegnazione dei cluster:")
    print(cliente_df.head())

    # Visualizzazione dei centri dei cluster
    print("\nCentri dei cluster:")
    print(pd.DataFrame(kmeans.cluster_centers_, columns=features_per_clustering))

except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato. Assicurati che il percorso sia corretto.")
except ImportError as e:
    print(f"Errore di importazione: {e}. Assicurati che la libreria sia installata.")
except Exception as e:
    print(f"Si è verificato un errore durante l'esecuzione del clustering k-means: {e}")
