# Fonction pour trouver les valeurs manquantes dans chaque colonnes
def find_feature_missing_values(df):
    from pyspark.sql.functions import col,sum
    return df.select(*(sum(col(c).isNull().cast("int")).alias(c) for c in df.columns)).toPandas().iloc[:,0:10]
    
