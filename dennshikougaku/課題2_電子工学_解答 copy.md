# 電子工学 (5E) — 課題 2 解答

**提出期限**: 2026年1月15日（木）13:00

---

**使用する物理定数（与えられた値）**
- $k=1.38\times10^{-23}\ \mathrm{J\,K^{-1}}$
- $e=1.60\times10^{-19}\ \mathrm{C}$
- $m=9.11\times10^{-31}\ \mathrm{kg}$
- $h=6.63\times10^{-34}\ \mathrm{J\,s}$
- $c=3.00\times10^{8}\ \mathrm{m/s}$

(有効数字は最終答を3桁で表記)

---

## 問1

条件: 電極間距離 $d=1.0\times10^{-2}\ \mathrm{m}$，電圧差 $\Delta V=200\ \mathrm{V}$，初速度 $0$.

1) 電界 $E$

$$E=-\frac{\mathrm{d}V}{\mathrm{d}x}=-\frac{\Delta V}{d}=-\frac{200}{1.0\times10^{-2}}=-2.00\times10^{4}\ \mathrm{V/m}.$$ 

2) 加速度 $a$

電荷 $q=-e$ により $F=qE$，加速度の大きさ

$$a=\frac{|qE|}{m}=\frac{e|E|}{m}. $$

数値代入:

$$a=\frac{1.60\times10^{-19}\times2.00\times10^{4}}{9.11\times10^{-31}}=3.515\times10^{15}\ \mathrm{m/s^{2}}\approx3.52\times10^{15}\ \mathrm{m/s^{2}}.$$ 

3) 陽極までの時間 $t$

初速度 $0$，移動距離 $d$ より

$$t=\sqrt{\frac{2d}{a}}.$$

数値代入:

$$t=\sqrt{\frac{2\times1.0\times10^{-2}}{3.515\times10^{15}}}=\sqrt{5.689\times10^{-18}}=2.39\times10^{-9}\ \mathrm{s}.$$ 

4) 陽極到達時の速度 $v$

$$v=\sqrt{2ad}=\sqrt{\frac{2e\Delta V}{m}}.$$

数値代入:

$$v=\sqrt{\frac{2\times1.60\times10^{-19}\times200}{9.11\times10^{-31}}}=8.38\times10^{6}\ \mathrm{m/s}.$$ 

5) 陽極に与えるエネルギー $\Delta K$

$$\Delta K=e\Delta V=1.60\times10^{-19}\times200=3.20\times10^{-17}\ \mathrm{J}=200\ \mathrm{eV}.$$ 

---

## 問2

条件: 初期エネルギー $100\ \mathrm{eV}$，磁束密度 $B=0.05\ \mathrm{T}$，入射は磁場に直交.

1) 速度 $v$

$$\mathrm{KE}=100\ \mathrm{eV}=100\times1.60\times10^{-19}=1.60\times10^{-17}\ \mathrm{J},$$

$$v=\sqrt{\frac{2\mathrm{KE}}{m}}=\sqrt{\frac{2\times1.60\times10^{-17}}{9.11\times10^{-31}}}=5.93\times10^{6}\ \mathrm{m/s}.$$ 

2) 円運動の半径 $r$

$$r=\frac{mv}{eB}.$$

数値代入:

$$r=\frac{9.11\times10^{-31}\times5.93\times10^{6}}{1.60\times10^{-19}\times0.05}=6.75\times10^{-4}\ \mathrm{m}.$$ 

3) 毎秒の回転数 $f$

$$\omega=\frac{eB}{m},\quad f=\frac{\omega}{2\pi}=\frac{eB}{2\pi m}.$$

数値代入:

$$f=\frac{1.60\times10^{-19}\times0.05}{2\pi\times9.11\times10^{-31}}=1.40\times10^{9}\ \mathrm{s^{-1}}.$$ 

---

## 問3

条件: $D=1.0\times10^{-2}\ \mathrm{m}$, $V_a=100\ \mathrm{V}$, $V(x)=V_a x/D$, $B_z=0.1\ \mathrm{T}$, 初期位置 $(x,y)=(0,0)$, 初速度 $0$.

1) 電界 $E$

$$E=-\frac{\mathrm{d}V}{\mathrm{d}x}=-\frac{V_a}{D}=-\frac{100}{1.0\times10^{-2}}=-1.00\times10^{4}\ \mathrm{V/m}.$$ 

2) 運動方程式

$q=-e$，$m$，$B=(0,0,B)$ とおくと

$$m\frac{\mathrm{d}v_x}{\mathrm{d}t}=qE+qv_yB,\quad m\frac{\mathrm{d}v_y}{\mathrm{d}t}=-qv_xB.$$ 

$q=-e$ を代入し，$\omega\equiv eB/m$ とすると

$$\frac{\mathrm{d}v_x}{\mathrm{d}t}=\frac{eE}{m}-\omega v_y,\quad \frac{\mathrm{d}v_y}{\mathrm{d}t}=\omega v_x.$$ 

これらを組合せると

$$\frac{\mathrm{d}^2 v_x}{\mathrm{d}t^2}=-\omega^2 v_x.$$ 

初期条件 $v_x(0)=v_y(0)=0$ より解は

$$v_x(t)=\frac{E}{B}\sin(\omega t),\quad v_y(t)=\frac{E}{B}\bigl(1-\cos(\omega t)\bigr).$$ 

位置は積分して

$$x(t)=\int_0^t v_x\,\mathrm{d}t=\frac{E}{B}\frac{1-\cos(\omega t)}{\omega}=\frac{mE}{eB^2}\bigl(1-\cos(\omega t)\bigr),$$

$$y(t)=\int_0^t v_y\,\mathrm{d}t=\frac{E}{B}\Bigl(t-\frac{\sin(\omega t)}{\omega}\Bigr)=\frac{E}{B}t-\frac{mE}{eB^2}\sin(\omega t).$$ 

3) 最大値 $x_m$ と対応する $y_m$

$x(t)$ の最大は $\cos(\omega t)=-1$（$t=\pi/\omega$）で

$$x_m=2\frac{mE}{eB^2},\quad y_m=\frac{E}{B}\frac{2\pi}{\omega}=2\pi\frac{mE}{eB^2}.$$

4) 数値代入

$$E=\frac{V_a}{D}=\frac{100}{1.0\times10^{-2}}=1.00\times10^{4}\ \mathrm{V/m},$$

$$S\equiv\frac{mE}{eB^2}=\frac{9.11\times10^{-31}\times1.00\times10^{4}}{1.60\times10^{-19}\times(0.10)^2}=5.69\times10^{-6}\ \mathrm{m},$$

$$x_m=2S=1.14\times10^{-5}\ \mathrm{m},\quad y_m=2\pi S=3.58\times10^{-5}\ \mathrm{m}.$$ 

（答） $x_m=1.14\times10^{-5}\ \mathrm{m},\ y_m=3.58\times10^{-5}\ \mathrm{m}$.

---

## 検算

検算に用いたスクリプト: `verify_calc.py`（ワークスペースに保存）。スクリプトで再計算した値と，最終的に本文で採用した有効数字3桁での表示を示す。

計算結果（スクリプトでの高精度出力 → 採用値（有効数字3桁））:

- 問1
  - $a$ = 3.512623e15 → $3.52\times10^{15}\ \mathrm{m/s^2}$
  - $t$ = 2.386158e-9 → $2.39\times10^{-9}\ \mathrm{s}$
  - $v$ = 8.381675e6 → $8.38\times10^{6}\ \mathrm{m/s}$
  - $\Delta K$ = 3.200000e-17 J → $3.20\times10^{-17}\ \mathrm{J}$

- 問2
  - $v$ = 5.926739e6 → $5.93\times10^{6}\ \mathrm{m/s}$
  - $r$ = 6.749074e-4 → $6.75\times10^{-4}\ \mathrm{m}$
  - $f$ = 1.397628e9 → $1.40\times10^{9}\ \mathrm{s^{-1}}$

- 問3
  - $x_m$ = 1.138750e-5 → $1.14\times10^{-5}\ \mathrm{m}$
  - $y_m$ = 3.577488e-5 → $3.58\times10^{-5}\ \mathrm{m}$

注: スクリプトと本文の差は丸め（有効数字3桁）によるものであり，物理的には一致しています。

以上。

---

## 付録 — 手書きメモ（文字起こし）

以下は資料画像（手書きノート）の文字起こし（原文に忠実）です。

1. 問1 (V = 200, D = 1×10^{-2})

(1)
$$t=D\sqrt{\frac{2m}{eV_a}}=\sqrt{\frac{2mD^2}{eV_a}}$$
数値代入:
$$t=1\times10^{-2}\sqrt{\frac{2\times9.11\times10^{-31}}{1.6\times10^{-19}\times200}}=2.39\times10^{-9}\ \mathrm{s}$$

(2)
$$v=\sqrt{\frac{2eV}{m}}=\sqrt{\frac{2\times1.6\times10^{-19}\times200}{9.11\times10^{-31}}}=8.38\times10^{6}\ \mathrm{m/s}$$

(3)
運動エネルギー:
$$\frac{1}{2}mv^2=\frac{1}{2}\times9.11\times10^{-31}\times(8.38\times10^{6})^2=3.20\times10^{-17}\ \mathrm{J}$$

2. 問2 (初期エネルギー = 100 eV, B_z = 0.05 T)

(1)
円運動半径:
$$r=\frac{mv}{eB_z}\ (\sin\theta=1\text{ for }\theta=\pi/2)$$
数値代入:
$$r=\frac{9.11\times10^{-31}\times\sqrt{2\times100\times1.6\times10^{-19}/9.11\times10^{-31}}}{1.6\times10^{-19}\times0.05}=6.75\times10^{-4}\ \mathrm{m}$$

(2)
回転数（周波数）:
$$f=\frac{eB_z}{2\pi m}\approx1.40\times10^{9}\ \mathrm{Hz}$$

3. 問3 — 手書き原稿（逐語文字起こし）

(1) $x_m$ のとき $\omega_c t=\pi$ より

手書き:

"x_m = A / \omega_c^2 (1 - \cos\omega_c t) = e m^2 V_a / e^2 m D B^2 (1 - \cos\pi)"

手書きの途中計算:

"m V_a / (D e B^2) = 9.11\times10^{-31} \times 100 / (1\times10^{-2} \times 1.6\times10^{-19} \times 0.1^2) = 5.69\times10^{-6}\ [m]"

(2) $y_m$ のとき $\omega_c t=2\pi$

手書き:

"y_m = A / \omega_c^2 (\omega_c t - \sin\omega_c t) = e m^2 V_a / e^2 m D B^2 (2\pi - \sin 2\pi)"

手書きの途中計算:

"= m V_a / (e D B^2) \times 2\pi = 9.11\times10^{-31} \times 100 / (1.6\times10^{-19} \times 1\times10^{-2} \times 0.1^2) \times 2\pi = 3.58\times10^{-5}\ [m]"

注: 手書きは $y_m$ を $\omega_c t=2\pi$ として評価して $2\pi S\ (=3.58\times10^{-5}\ \mathrm{m})$ を示している。本稿でも $y_m$ を $2\pi S\ (=3.58\times10^{-5}\ \mathrm{m})$ として採用した。