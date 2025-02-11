import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Citirea datelor
daune_db = pd.read_csv('Daune_DB.csv')
preturi_2021 = pd.read_csv('Preturi_2021_H4.csv')
preturi_2022 = pd.read_csv('Preturi_2022_H4.csv')

# 1. Analiza creșterii prețurilor între 2021 și 2022 pentru H4
def analiza_crestere_preturi():
    # Curățare și pregătire date (taiem spatiile dinainte si dupa texte)
    preturi_2021['Interventie'] = preturi_2021['Interventie'].str.strip()
    
    # Găsim intervențiile comune între cei doi ani
    interventii_comune = []
    
    for idx, row in preturi_2021.iterrows():
        interventie_2021 = row['Interventie'].lower()
        pret_2021 = row['Pret']
        
        # Căutăm intervenția similară în 2022
        for idx2, row2 in preturi_2022.iterrows():
            if isinstance(row2.get('Interventie'), str):
                interventie_2022 = row2['Interventie'].lower()
                if interventie_2021 in interventie_2022 or interventie_2022 in interventie_2021:
                    pret_2022 = row2['Pret']
                    crestere_procent = ((pret_2022 - pret_2021) / pret_2021) * 100
                    
                    interventii_comune.append({
                        'Interventie': row['Interventie'],
                        'Pret_2021': pret_2021,
                        'Pret_2022': pret_2022,
                        'Crestere_Procent': crestere_procent
                    })
                    break
    
    df_cresteri = pd.DataFrame(interventii_comune)
    return df_cresteri.sort_values('Crestere_Procent', ascending=False)

# 2. Analiza frecvenței procedurilor
def analiza_frecventa_proceduri():
    # Grupăm după procedură și numărăm frecvența
    frecventa = daune_db['PROCEDURE'].value_counts()
    
    # Convertim în DataFrame pentru manipulare mai ușoară
    df_frecventa = pd.DataFrame({
        'Procedura': frecventa.index,
        'Frecventa': frecventa.values
    })
    
    return df_frecventa.sort_values('Frecventa', ascending=False)

# Executăm analizele
df_cresteri = analiza_crestere_preturi()
df_frecventa = analiza_frecventa_proceduri()

# Afișăm rezultatele
print("\nTop 10 creșteri de preț între 2021 și 2022:")
print(df_cresteri.head(10)[['Interventie', 'Crestere_Procent']].to_string())

# print("\nTop 10 cele mai frecvente proceduri:")
print(df_frecventa.head(10).to_string())

# Vizualizare pentru creșterile de preț
plt.figure(figsize=(12, 6))
sns.barplot(data=df_cresteri.head(10), x='Interventie', y='Crestere_Procent')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Creșteri de Preț (2021-2022)')
plt.tight_layout()
plt.show()

# Vizualizare pentru frecvența procedurilor
plt.figure(figsize=(12, 6))
sns.barplot(data=df_frecventa.head(10), x='Procedura', y='Frecventa')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Cele Mai Frecvente Proceduri')
plt.tight_layout()
plt.show()