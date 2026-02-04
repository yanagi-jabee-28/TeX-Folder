"""生成: 相関解析の.xlsx（ラベル・式・散布図・回帰線・注記）とPNGを出力するスクリプト
使い方: python generate_correlation_xlsx.py
出力:
 - 相関解析課題_kaito.xlsx
 - scatter_correlation.png
"""
from pathlib import Path
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

WORKDIR = Path(__file__).resolve().parent
CSV_IN = WORKDIR / "pattern_data_clean.csv"
XLSX_OUT = WORKDIR / "相関解析課題_kaito.xlsx"
PNG_OUT = WORKDIR / "scatter_correlation.png"

# --- read
df = pd.read_csv(CSV_IN)
x = df.iloc[:, 1].astype(float).values  # めっき厚
y = df.iloc[:, 2].astype(float).values  # 幅
n = len(x)

# --- stats
x_mean = x.mean()
y_mean = y.mean()
dev_x = x - x_mean
dev_y = y - y_mean
prod = dev_x * dev_y
ss_x = np.sum(dev_x**2)
ss_y = np.sum(dev_y**2)
ss_prod = np.sum(prod)

r = ss_prod / math.sqrt(ss_x * ss_y)
t_stat = r * math.sqrt((n-2) / (1 - r**2))
p_val = 2 * stats.t.sf(abs(t_stat), df=n-2)
# Fisher z for 95% CI
z = 0.5 * np.log((1+r)/(1-r))
se_z = 1 / math.sqrt(n-3)
z_crit = stats.norm.ppf(1-0.05/2)
lo_r, hi_r = math.tanh(z - z_crit*se_z), math.tanh(z + z_crit*se_z)

# --- prepare sheet table (include computed columns)
out_df = df.copy()
out_df['めっき厚-平均'] = out_df.iloc[:, 1] - x_mean
out_df['幅-平均'] = out_df.iloc[:, 2] - y_mean
out_df['偏差積'] = out_df['めっき厚-平均'] * out_df['幅-平均']
out_df['偏差^2_厚'] = out_df['めっき厚-平均']**2
out_df['偏差^2_幅'] = out_df['幅-平均']**2

# summary rows
summary = pd.DataFrame({
    out_df.columns[0]: ['平均', '合計'],
    out_df.columns[1]: [x_mean, np.sum(out_df.iloc[:, 1])],
    out_df.columns[2]: [y_mean, np.sum(out_df.iloc[:, 2])],
    'めっき厚-平均': [np.nan, np.sum(out_df['めっき厚-平均'])],
    '幅-平均': [np.nan, np.sum(out_df['幅-平均'])],
    '偏差積': [np.nan, np.sum(out_df['偏差積'])],
    '偏差^2_厚': [np.nan, np.sum(out_df['偏差^2_厚'])],
    '偏差^2_幅': [np.nan, np.sum(out_df['偏差^2_幅'])],
})

# --- write Excel with formulas + chart
with pd.ExcelWriter(XLSX_OUT, engine='xlsxwriter') as writer:
    out_df.to_excel(writer, sheet_name='Data', index=False, startrow=0)
    summary.to_excel(writer, sheet_name='Data',
                     index=False, startrow=len(out_df)+2)

    workbook = writer.book
    worksheet = writer.sheets['Data']

    # --- put Excel formulas for derived columns (so sheet contains functions, not only values)
    # data rows are written at B2:C{last_row}
    first_row = 2
    last_row = n + 1
    # headers for derived cols (if pandas didn't write them)
    derived_headers = ['めっき厚-平均', '幅-平均', '偏差積', '偏差^2_厚', '偏差^2_幅']
    for i, hdr in enumerate(derived_headers, start=3):
        worksheet.write(0, i, hdr)

    # per-row formulas
    for r in range(first_row, last_row + 1):
        worksheet.write_formula(
            r-1, 3, f"=B{r}-AVERAGE($B$2:$B${last_row})")    # D
        worksheet.write_formula(
            r-1, 4, f"=C{r}-AVERAGE($C$2:$C${last_row})")    # E
        worksheet.write_formula(
            r-1, 5, f"=D{r}*E{r}")                              # F
        worksheet.write_formula(
            r-1, 6, f"=D{r}^2")                                # G
        worksheet.write_formula(
            r-1, 7, f"=E{r}^2")                                # H

    # summary rows (平均, 合計) using Excel functions
    summary_start = last_row + 2
    worksheet.write(summary_start-1, 0, '平均')
    worksheet.write_formula(
        summary_start-1, 1, f"=AVERAGE($B$2:$B${last_row})")
    worksheet.write_formula(
        summary_start-1, 2, f"=AVERAGE($C$2:$C${last_row})")
    worksheet.write_formula(
        summary_start-1, 3, f"=AVERAGE($D$2:$D${last_row})")
    worksheet.write_formula(
        summary_start-1, 4, f"=AVERAGE($E$2:$E${last_row})")
    worksheet.write_formula(summary_start-1, 5, f"=SUM($F$2:$F${last_row})")
    worksheet.write_formula(
        summary_start-1, 6, f"=AVERAGE($G$2:$G${last_row})")
    worksheet.write_formula(
        summary_start-1, 7, f"=AVERAGE($H$2:$H${last_row})")

    worksheet.write(summary_start, 0, '合計')
    worksheet.write_formula(summary_start, 1, f"=SUM($B$2:$B${last_row})")
    worksheet.write_formula(summary_start, 2, f"=SUM($C$2:$C${last_row})")
    worksheet.write_formula(summary_start, 3, f"=SUM($D$2:$D${last_row})")
    worksheet.write_formula(summary_start, 4, f"=SUM($E$2:$E${last_row})")
    worksheet.write_formula(summary_start, 5, f"=SUM($F$2:$F${last_row})")
    worksheet.write_formula(summary_start, 6, f"=SUM($G$2:$G${last_row})")
    worksheet.write_formula(summary_start, 7, f"=SUM($H$2:$H${last_row})")

    # formats
    hfmt = workbook.add_format({'bold': True, 'align': 'center'})
    num = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', 12)
    worksheet.set_column('B:C', 14, num)
    worksheet.set_column('D:H', 14, num)

    # write calculation block (with formulas for reproducibility)
    calc_row = len(out_df) + len(summary) + 5
    worksheet.write(calc_row, 0, '計算', hfmt)
    worksheet.write(calc_row, 1, '相関係数_r')
    # place formula for r using SUMPRODUCT-like (Excel-compatible)
    # r = SUM(F2:F17)/SQRT(SUM(G2:G17)*SUM(H2:H17)) but we have numeric columns here
    worksheet.write_formula(calc_row, 2,
                            "=SUM(F2:F17)/SQRT(SUM(G2:G17)*SUM(H2:H17))")
    worksheet.write(calc_row+1, 1, 'n')
    worksheet.write_formula(calc_row+1, 2, "=COUNT(B2:B17)")
    worksheet.write(calc_row+2, 1, 't値')
    worksheet.write_formula(calc_row+2, 2,
                            "=C{r}*SQRT((C{n}-2)/(1-C{r}^2))".format(r=calc_row+1+1, n=calc_row+2+1))
    worksheet.write(calc_row+3, 1, 'p値 (two-tailed)')
    worksheet.write_formula(
        calc_row+3, 2, "=T.DIST.2T(ABS(C{t}),C{n}-2)".format(t=calc_row+2+1, n=calc_row+1+1))
    worksheet.write(calc_row+4, 1, 't臨界(α=0.05)')
    worksheet.write_formula(
        calc_row+4, 2, "=T.INV.2T(0.05,C{n}-2)".format(n=calc_row+1+1))

    # additional Excel-derived diagnostics
    # degrees of freedom
    worksheet.write(calc_row+5, 1, 'df')
    worksheet.write_formula(calc_row+5, 2, "=C{n}-2".format(n=calc_row+1+1))
    # Fisher z-based 95% CI (Excel formulas)
    worksheet.write(calc_row+6, 1, 'Fisher_z')
    worksheet.write_formula(
        calc_row+6, 2, "=0.5*LN((1+C{r})/(1-C{r}))".format(r=calc_row+1))
    worksheet.write(calc_row+7, 1, 'se_z')
    worksheet.write_formula(calc_row+7, 2, "=1/SQRT(COUNT(B2:B17)-3)")
    worksheet.write(calc_row+8, 1, 'z_crit(0.975)')
    worksheet.write_formula(calc_row+8, 2, "=NORM.S.INV(1-0.05/2)")
    worksheet.write(calc_row+9, 1, 'r_lower (95%CI)')
    worksheet.write_formula(calc_row+9, 2, "=TANH(C{z} - C{zc}*C{s})".format(
        z=calc_row+6+1, zc=calc_row+8+1, s=calc_row+7+1))
    worksheet.write(calc_row+10, 1, 'r_upper (95%CI)')
    worksheet.write_formula(calc_row+10, 2, "=TANH(C{z} + C{zc}*C{s})".format(
        z=calc_row+6+1, zc=calc_row+8+1, s=calc_row+7+1))

    # write numeric results too (for quick view)
    res_row = calc_row
    worksheet.write(res_row, 4, '結果（Python計算）', hfmt)
    worksheet.write(res_row+1, 4, 'r', hfmt)
    worksheet.write_number(res_row+1, 5, r, num)
    worksheet.write(res_row+2, 4, 'n', hfmt)
    worksheet.write_number(res_row+2, 5, n)
    worksheet.write(res_row+3, 4, 't', hfmt)
    worksheet.write_number(res_row+3, 5, t_stat, num)
    worksheet.write(res_row+4, 4, 'p (two‑tailed)', hfmt)
    worksheet.write_number(res_row+4, 5, p_val, num)
    worksheet.write(res_row+5, 4, '95% CI for r', hfmt)
    worksheet.write(res_row+5, 5, f"[{lo_r:.2f}, {hi_r:.2f}]")

    # --- add scatter chart with trendline and annotation
    chart = workbook.add_chart(
        {'type': 'scatter', 'subtype': 'straight_with_markers'})
    chart.add_series({
        'name':       'データ',
        'categories': ['Data', 1, 1, len(out_df), 1],  # B2:B17
        'values':     ['Data', 1, 2, len(out_df), 2],  # C2:C17
        'marker':     {'type': 'circle', 'size': 6},
    })
    chart.set_x_axis({'name': 'パターンめっき厚 (μm)'})
    chart.set_y_axis({'name': 'パターン幅 (μm)'})
    chart.set_title({'name': 'パターンめっき厚 と パターン幅 の散布図'})
    chart.set_legend({'position': 'none'})
    # trendline (linear) with equation and R^2
    chart.add_series({
        'trendline': {
            'type': 'linear',
            'display_equation': True,
            'display_r2': True,
        }
    })
    # place chart
    worksheet.insert_chart('J2', chart, {'x_scale': 1.4, 'y_scale': 1.2})

# --- also create a high-quality PNG via matplotlib
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='C0')
# linear fit
slope, intercept, r_val, p_scipy, std_err = stats.linregress(x, y)
xs = np.linspace(x.min()-1, x.max()+1, 100)
plt.plot(xs, intercept + slope*xs, color='C1', linestyle='-', linewidth=1)
plt.xlabel('パターンめっき厚 (μm)')
plt.ylabel('パターン幅 (μm)')
plt.title('パターンめっき厚 vs パターン幅')
# annotation
txt = f"n={n}\nr={r:.3f}\nt={t_stat:.3f}\np(two‑tailed)={p_val:.4f}\n95%CI=[{lo_r:.2f},{hi_r:.2f}]"
plt.gca().text(0.02, 0.98, txt, transform=plt.gca().transAxes,
               verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.tight_layout()
plt.savefig(PNG_OUT, dpi=300)
print(f"Wrote: {XLSX_OUT}\nWrote: {PNG_OUT}")
