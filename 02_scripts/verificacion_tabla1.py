import pandas as pd
from scipy import stats
import numpy as np
import os

df = pd.read_csv("01_data/raw/datos.txt", sep="\t")
df.columns = df.columns.str.strip()

def totales(df, prefijo):
    for sec, cols in {
        'A': [f'{prefijo}_A{i}' for i in range(1,6)],
        'B': [f'{prefijo}_B{i}' for i in range(1,9)],
        'C': [f'{prefijo}_C{i}' for i in range(1,6)],
        'D': [f'{prefijo}_D{i}' for i in range(1,9)],
    }.items():
        sub = df[cols].apply(pd.to_numeric, errors='coerce')
        df[f'{prefijo}_TOTAL_{sec}_skipna'] = sub.sum(axis=1, skipna=True)
        df[f'{prefijo}_TOTAL_{sec}_strict'] = sub.sum(axis=1, skipna=False)
    return df

df = totales(df, 'PRE')
df = totales(df, 'POST')

constructos = {
    'Curiosity':              ('A', 'A'),
    'MIL Self-Efficacy':      ('B', 'B'),
    'Environmental Attitude': ('C', 'C'),
    'Knowledge':              ('D', 'D'),
}

alpha_bonf = 0.05 / len(constructos)
print(f"Bonferroni threshold: {alpha_bonf:.4f}\n")
print(f"{'Construct':<24}{'N':>4}{'PreM':>8}{'PostM':>8}{'Diff':>8}{'W':>9}{'p':>10}{'r':>8}{'zeros':>7}{'ties':>6}{'Bonf':>6}")
print("-"*110)

rows = []
for nombre, (pre_sec, post_sec) in constructos.items():
    pre_col  = f'PRE_TOTAL_{pre_sec}_skipna'
    post_col = f'POST_TOTAL_{post_sec}_skipna'
    pair = df[[pre_col, post_col]].dropna()
    a = pair[pre_col].values.astype(float)
    b = pair[post_col].values.astype(float)
    d = b - a
    n = len(pair)
    zeros = int((d == 0).sum())
    dd = d[d != 0]
    ties = n - len(np.unique(np.abs(dd))) if len(dd) else 0

    shapiro_p = stats.shapiro(d).pvalue if n >= 3 else np.nan
    res = stats.wilcoxon(a, b, alternative='two-sided', zero_method='wilcox', correction=False)

    ranks = stats.rankdata(np.abs(dd))
    Wp = ranks[dd > 0].sum()
    Wm = ranks[dd < 0].sum()
    r = (Wp - Wm) / (Wp + Wm) if (Wp + Wm) else np.nan

    pre_m, pre_sd = a.mean(), a.std(ddof=1)
    post_m, post_sd = b.mean(), b.std(ddof=1)
    diff_m = (b - a).mean()
    sig = res.pvalue < alpha_bonf

    print(f"{nombre:<24}{n:>4}{pre_m:>8.2f}{post_m:>8.2f}{diff_m:>+8.2f}{res.statistic:>9.1f}{res.pvalue:>10.4f}{r:>8.3f}{zeros:>7}{ties:>6}{'YES' if sig else 'NO':>6}")
    rows.append({
        'Construct': nombre, 'N': n, 'Pre_M': round(pre_m,2), 'Pre_SD': round(pre_sd,2),
        'Post_M': round(post_m,2), 'Post_SD': round(post_sd,2), 'Mean_Diff': round(diff_m,2),
        'Wilcoxon_W': round(res.statistic,2), 'p_value': round(res.pvalue,4),
        'Effect_Size_r': round(abs(r),3), 'zeros': zeros, 'ties': ties,
        'Bonferroni_significant': sig, 'Shapiro_p': round(shapiro_p,4) if not np.isnan(shapiro_p) else None
    })

out = pd.DataFrame(rows)
os.makedirs('01_data/processed', exist_ok=True)
out.to_csv('01_data/processed/Statistical_Results_VERIFIED.csv', index=False)
print("\nGuardado: 01_data/processed/Statistical_Results_VERIFIED.csv")
print(out.to_string(index=False))
