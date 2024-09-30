import pandas as pd

df = pd.read_csv('jobdataset.csv')

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

df = df[df['work_type'] == 'Intern']
df = df[df['company_size'] < 50000]

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df['experience'] = df['experience'].astype(int)
df['salary'] = df['salary'].astype(float)

q1 = df['salary'].quantile(0.25)
q3 = df['salary'].quantile(0.75)
iqr = q3 - q1
df = df[(df['salary'] >= (q1 - 1.5 * iqr)) & (df['salary'] <= (q3 + 1.5 * iqr))]

df.to_csv('jobs_dataset.csv', index=False)

print("Data cleaning complete!")
