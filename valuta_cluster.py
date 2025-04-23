import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Percorso del file CSV
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

    # Scelta del numero di cluster (k) - manteniamo 3 per ora
    n_clusters = 3

    # Inizializzazione e applicazione dell'algoritmo k-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)

    # Calcolo del coefficiente di silhouette
    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    print(f"Coefficiente di Silhouette medio per {n_clusters} cluster: {silhouette_avg:.2f}")

except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato. Assicurati che il percorso sia corretto.")
except ImportError as e:
    print(f"Errore di importazione: {e}. Assicurati che la libreria sia installata.")
except Exception as e:
    print(f"Si è verificato un errore durante la valutazione del cluster: {e}") 
