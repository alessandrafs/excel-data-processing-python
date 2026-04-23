import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Process data
df['total'] = df['quantity'] * df['price']

# Save result
df.to_csv('output.csv', index=False)

print("Data processed successfully!")
