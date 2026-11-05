import pandas as pd

df = pd.read_csv("01_data/raw/datos.txt", sep="\t")
df.columns = df.columns.str.strip()

# Calculate totals
def totales(df, prefijo):
    for sec, cols in {
        'A': [f'{prefijo}_A{i}' for i in range(1,6)],
        'B': [f'{prefijo}_B{i}' for i in range(1,9)],
        'C': [f'{prefijo}_C{i}' for i in range(1,6)],
        'D': [f'{prefijo}_D{i}' for i in range(1,9)],
    }.items():
        df[f'{prefijo}_TOTAL_{sec}'] = df[cols].apply(pd.to_numeric, errors='coerce').sum(axis=1, skipna=True)
    return df

df = totales(df, 'PRE')
df = totales(df, 'POST')

# Assign age groups based on the 14/18/20 split you provided
# Assuming SARIRI-001 to 014 (Group 1), 015 to 032 (Group 2), 033 to 052 (Group 3)
def assign_group(code):
    num = int(code.split('-')[1])
    if num <= 14: return 'G1 (8-10y)'
    elif num <= 32: return 'G2 (11-14y)'
    else: return 'G3 (15-17y)'

df['Age_Group'] = df['Codigo'].apply(assign_group)

print("=== DESCRIPTIVE STATISTICS BY AGE GROUP ===")
for group in ['G1 (8-10y)', 'G2 (11-14y)', 'G3 (15-17y)']:
    sub = df[df['Age_Group'] == group]
    print(f"\n--- {group} (N={len(sub)}) ---")
    for construct, sec in [('Knowledge', 'D'), ('Attitude', 'C'), ('Curiosity', 'A'), ('MIL', 'B')]:
        pre_med = sub[f'PRE_TOTAL_{sec}'].median()
        post_med = sub[f'POST_TOTAL_{sec}'].median()
        print(f"  {construct:12}: Pre Median = {pre_med:4.1f}, Post Median = {post_med:4.1f}")
