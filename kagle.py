import kagglehub
import pandas as pd
import sqlite3

#dataset do Kaggle
dataset_path = kagglehub.dataset_download("maiastudent/fake-clients-100")
print("Dataset baixado em:", dataset_path)


csv_file = f"{dataset_path}/fake_clients_100.csv"
df = pd.read_csv(csv_file)
print("CSV carregado. Primeiras linhas:")
print(df.head())


conn = sqlite3.connect("clientes.db") 

df.to_sql("clients", conn, index=False, if_exists="replace")
print("Tabela 'clients' criada no SQLite com sucesso!")
