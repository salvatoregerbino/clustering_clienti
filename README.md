# Progetto di Clustering di Clienti

Questo progetto ha l'obiettivo di segmentare i clienti di un'azienda in gruppi (cluster) in base al loro comportamento d'acquisto. L'analisi di questi cluster può fornire informazioni preziose per strategie di marketing mirate, personalizzazione dell'offerta e miglioramento della relazione con i clienti.

## Riepilogo delle Attività Svolte

* [X] Inizializzazione del repository Git locale.
* [X] Creazione del repository remoto su GitHub.
* [X] Connessione del repository locale a quello remoto.
* [X] Creazione del file `.gitignore`.
* [X] Primo push del progetto su GitHub.
* [X] [Installazione della libreria Pandas](https://pandas.pydata.org/install/)
  <details>
    <summary>Istruzioni per l'installazione</summary>
    Per installare la libreria Pandas, esegui questo comando nel tuo terminale o prompt dei comandi:
    ```bash
    pip install pandas
    ```
  </details>
* [X] Creazione dello script `crea_dataset_sintetico.py` per generare dati di esempio.
* [X] Esecuzione dello script `crea_dataset_sintetico.py` e creazione del file `data/clienti_sintetico.csv`.
* [X] Creazione dello script `carica_dati.py` per caricare il dataset CSV in un DataFrame Pandas.
* [X] Esecuzione dello script `carica_dati.py` e caricamento del dataset.
* [X] Creazione del file `README.md` per la documentazione del progetto.
* [X] Creazione dello script `pre_processa_dati.py` per standardizzare le feature.
* [X] Esecuzione dello script `pre_processa_dati.py` e standardizzazione delle feature.
* [X] Creazione dello script `clustering_kmeans.py` per implementare l'algoritmo k-means.(https://www.diariodiunanalista.it/posts/introduzione-al-clustering-non-supervisionato-con-k-means/ & https://www.ibm.com/it-it/think/topics/k-means-clustering).
* [X] Esecuzione dello script `clustering_kmeans.py` e assegnazione dei cluster.
* [X] Creazione dello script `valuta_cluster.py` per calcolare il coefficiente di silhouette.
* [X] Esecuzione dello script `valuta_cluster.py` e calcolo del coefficiente di silhouette.
* [X] Creazione dello script `visualizza_cluster.py` per visualizzare i risultati del clustering.
* [X] Esecuzione dello script `visualizza_cluster.py` e visualizzazione dei cluster in 3D.
![Visualizzazione dei Cluster 3D](images/cluster_visualization_3d.jpeg)
* [X] Creazione dello script `metodo_gomito.py` per determinare il numero ottimale di cluster.
![Grafico del Metodo del Gomito](images/metodo_gomito_grafico.jpeg)
* [X] Esecuzione dello script `metodo_gomito.py` e analisi del grafico del metodo del gomito (che suggerisce k=3).
      
## Struttura del Progetto
<details>
  <summary>Mostra la struttura del progetto</summary>
  clustering_clienti/
├── data/
│   └── clienti_sintetico.csv
├── images/
│   └── cluster_visualization_3d.png
│   └── metodo_gomito_grafico.jpeg
├── carica_dati.py
├── crea_dataset_sintetico.py
├── clustering_kmeans.py
├── metodo_gomito.py
├── pre_processa_dati.py
├── valuta_cluster.py
├── visualizza_cluster.py
└── README.md
</details>
* `data/`: Contiene il dataset sintetico dei clienti.
* `images/`: Contiene le immagini dei grafici generati.
* `*.py`: Script Python per le varie fasi del progetto (generazione dati, caricamento, pre-elaborazione, clustering, valutazione, visualizzazione).
* `README.md`: Il file di documentazione principale del progetto.
## Task Attuali

* [ ] (Potenziale) Esplorazione di diversi numeri di cluster (k).
* [ ] (Potenziale) Utilizzo di altre metriche di valutazione del cluster.
* [ ] (Potenziale) Analisi delle caratteristiche dei cluster.

## Prossimi Passi

* (Potenziale) Approfondimento dell'analisi dei cluster identificati.
* (Potenziale) Integrazione dei risultati in strategie di business.






