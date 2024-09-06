import pandas as pd

# CMS IP Dataset
url = 'https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv'
df = pd.read_csv(url, delimiter='|')

# Medical Codexes Fields
codex_columns = ['ADMTG_DGNS_CD', 'PRNCPAL_DGNS_CD', 'ICD_DGNS_CD1', 'ICD_DGNS_CD2', 
                 'ICD_DGNS_CD3', 'ICD_DGNS_CD4', 'ICD_DGNS_CD5', 'ICD_DGNS_CD6',
                 'ICD_DGNS_CD7', 'ICD_DGNS_CD8', 'ICD_DGNS_CD9', 'ICD_DGNS_CD10',
                 'ICD_PRCDR_CD1', 'ICD_PRCDR_CD2', 'ICD_PRCDR_CD3', 'ICD_PRCDR_CD4', 
                 'ICD_PRCDR_CD5', 'CLM_DRG_CD', 'HCPCS_CD']

# DataFrame with medical codex columns only
codex_df = df[codex_columns]

# Drop rows with missing medical codex values
codex_df_clean = codex_df.dropna()

# Show cleaned updata
print("Data after dropping rows with missing values:")
print(codex_df_clean.head())

#Frequency analysis
for column in codex_columns:
    print(f"\nFrequency for {column} after dropping missing values:")
    print(codex_df_clean[column].value_counts().head(10))  # Top 10  frequent values
