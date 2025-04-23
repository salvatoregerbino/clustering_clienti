import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

    # Standardizzazione delle feature 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Scelta del numero di cluster (manteniamo 3)
    n_clusters = 3

    # Applica nuovamente k-means per ottenere le etichette dei cluster
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cliente_df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Creazione del grafico a dispersione 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot dei punti dati, colorati in base al cluster
    scatter = ax.scatter(cliente_df['Spesa_Totale'], cliente_df['Numero_Ordini'], cliente_df['Frequenza_Visite'],
                       c=cliente_df['Cluster'], cmap='viridis', marker='o', s=50)

    # Etichette degli assi
    ax.set_xlabel('Spesa Totale')
    ax.set_ylabel('Numero Ordini')
    ax.set_zlabel('Frequenza Visite')

    # Titolo del grafico
    ax.set_title('Visualizzazione dei Cluster dei Clienti')

    # Legenda dei colori (corrispondenti ai cluster)
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)

    # Mostra il grafico
    plt.show()

except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato. Assicurati che il percorso sia corretto.")
except ImportError as e:
    print(f"Errore di importazione: {e}. Assicurati che la libreria sia installata.")
except Exception as e:
    print(f"Si è verificato un errore durante la visualizzazione: {e}")
