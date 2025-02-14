import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv("data/Iris.csv") 

df_features = df.drop(['Species'], axis=1)
print(df_features)
df_labels = df['Species']
print(df_labels)

min_max_scaler = MinMaxScaler()
df_normalized_values = min_max_scaler.fit_transform(df_features)

df_normalized = pd.DataFrame(df_normalized_values, columns=df_features.columns)
df_normalized['Species'] = df_labels

df_normalized.to_csv("./processed_data/iris_normalized.csv", index=False)

std_scaler = StandardScaler()
df_standardized_values = std_scaler.fit_transform(df_features)

df_standardized = pd.DataFrame(df_standardized_values, columns=df_features.columns)
df_standardized['Species'] = df_labels

df_standardized.to_csv("./processed_data/iris_standardized.csv", index=False)

