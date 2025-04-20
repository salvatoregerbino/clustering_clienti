import pandas as pd

# Specifica il percorso del file CSV
file_path = 'data/clienti_sintetico.csv'

try:
    # Carica il dataset in un DataFrame Pandas
    cliente_df = pd.read_csv(file_path)

    # Stampa le prime righe del DataFrame per dare un'occhiata ai dati
    print("Prime 5 righe del dataset caricato:")
    print(cliente_df.head())

    # Stampa alcune informazioni sul DataFrame (numero di righe, colonne, tipi di dati)
    print("\nInformazioni sul dataset:")
    print(cliente_df.info())

    # Ora la variabile 'cliente_df' contiene il nostro dataset come DataFrame Pandas.
    # Potremo utilizzare questa variabile negli script successivi per la pre-elaborazione e il clustering.

except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato. Assicurati che il percorso sia corretto.")
except Exception as e:
    print(f"Si è verificato un errore durante il caricamento del file: {e}")
