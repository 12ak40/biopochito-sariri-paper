import pandas as pd
import numpy as np
from scipy import stats

# Cargar datos
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
        df[f'{prefijo}_TOTAL_{sec}'] = sub.sum(axis=1, skipna=True)
    return df

df = totales(df, 'PRE')
df = totales(df, 'POST')

constructos = {
    'Knowledge':              ('D', 'D'),
    'Environmental Attitude': ('C', 'C'),
    'Curiosity':              ('A', 'A'),
    'MIL Self-Efficacy':      ('B', 'B'),
}

print("=== REPORTE RIGUROSO WILCOXON (Para el revisor) ===\n")

for nombre, (pre_sec, post_sec) in constructos.items():
    pre = df[f'PRE_TOTAL_{pre_sec}']
    post = df[f'POST_TOTAL_{post_sec}']
    diff = post - pre
    
    # 1. Medianas e IQR
    pre_median = pre.median()
    pre_iqr = pre.quantile(0.75) - pre.quantile(0.25)
    post_median = post.median()
    post_iqr = post.quantile(0.75) - post.quantile(0.25)
    
    # 2. Direcciones de las diferencias
    pos_diff = (diff > 0).sum()
    neg_diff = (diff < 0).sum()
    zero_diff = (diff == 0).sum()
    
    # 3. Wilcoxon exacto (W+ y W-)
    diff_nonzero = diff[diff != 0]
    ranks = stats.rankdata(np.abs(diff_nonzero))
    W_plus = ranks[diff_nonzero > 0].sum()
    W_minus = ranks[diff_nonzero < 0].sum()
    
    # Prueba de Wilcoxon (SciPy)
    res = stats.wilcoxon(post, pre, alternative='two-sided', zero_method='wilcox')
    
    # 4. Tamaño del efecto CON SIGNO
    # r = (W+ - W-) / (W+ + W-)
    r_signed = (W_plus - W_minus) / (W_plus + W_minus)
    
    # 5. Intervalo de confianza del 95% para la mediana de las diferencias (Bootstrap)
    boot_medians = []
    np.random.seed(42)
    for _ in range(2000):
        sample = np.random.choice(diff, size=len(diff), replace=True)
        boot_medians.append(np.median(sample))
    ci_lower = np.percentile(boot_medians, 2.5)
    ci_upper = np.percentile(boot_medians, 97.5)
    
    print(f"--- {nombre} ---")
    print(f"  Pre:  Median = {pre_median:.1f}, IQR = {pre_iqr:.1f}")
    print(f"  Post: Median = {post_median:.1f}, IQR = {post_iqr:.1f}")
    print(f"  Differences: Positive = {pos_diff}, Negative = {neg_diff}, Zero = {zero_diff}")
    print(f"  W+ = {W_plus:.1f}, W- = {W_minus:.1f} (Wilcoxon Statistic W = {res.statistic:.1f})")
    print(f"  p-value = {res.pvalue:.4f}")
    print(f"  Effect size (r) = {r_signed:+.2f}") # Con signo
    print(f"  Median Diff 95% CI = [{ci_lower:.1f}, {ci_upper:.1f}]\n")
