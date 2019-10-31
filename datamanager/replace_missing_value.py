def replace_missing_values1(df,qualifies_columns, continuous_columns):
    dict_mean = {feat: df.select(f.mean(feat)).collect()[0][0] 
                 for feat in continuous_columns}
    return df.select([f.when(df[feature].isNotNull(), df[feature])\
                      .otherwise('-1').alias(feature) for feature in qualifies_columns]\
                     +[f.when(df[feature].isNotNull(), df[feature])\
                       .otherwise(dict_mean[feature]).alias(feature) 
                       for feature in continuous_columns])

# Another fonctions
def replace_missing_values2(df,qualifies_columns, continuous_columns):
    
    return df.select([f.when(df[feature].isNotNull(), df[feature])\
                      .otherwise('-1').alias(feature) for feature in qualifies_columns]\
                     +[f.when(df[feature].isNotNull(), df[feature])\
                       .otherwise(df.select(f.mean(df[feature])).collect()[0][0])\
                       .alias(feature) for feature in continuous_columns])
