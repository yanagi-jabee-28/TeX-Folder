# 電子工学 (5E) — 課題 2 解答

**提出期限**: 2026年1月15日（木）13:00

---

**使用する物理定数**
- $k = 1.38 \times 10^{-23}\ \mathrm{J \cdot K^{-1}}$
- $e = 1.60 \times 10^{-19}\ \mathrm{C}$
- $m = 9.11 \times 10^{-31}\ \mathrm{kg}$
- $h = 6.63 \times 10^{-34}\ \mathrm{J \cdot s}$
- $c = 3.00 \times 10^{8}\ \mathrm{m/s}$

**計算における有効数字**: 3桁

---

## 課題 1

**条件**: $d=1.0\times10^{-2}\ \mathrm{m},\ V=200\ \mathrm{V},\ v_0=0$. 求: ①〜③.

### ① 陽極に達するまでの時間

**式:**

$$E = \frac{V}{d}$$

$F=eE\Rightarrow a=F/m=\dfrac{eE}{m}=\dfrac{eV}{md}$

初速度0: $d=\tfrac{1}{2}at^2\Rightarrow t=\sqrt{\dfrac{2d}{a}}=\sqrt{\dfrac{2md^2}{eV}}$

**代入:**

$$t = \sqrt{\frac{2 \times 9.11 \times 10^{-31} \times (1.0 \times 10^{-2})^2}{1.60 \times 10^{-19} \times 200}}$$

$$= \sqrt{\frac{2 \times 9.11 \times 10^{-31} \times 1.0 \times 10^{-4}}{3.20 \times 10^{-17}}}$$

$$= \sqrt{\frac{1.822 \times 10^{-34}}{3.20 \times 10^{-17}}}$$

$$= \sqrt{5.69 \times 10^{-18}}$$

$$= 2.39 \times 10^{-9}\ \mathrm{s}$$

**解**: $t = 2.39 \times 10^{-9}\ \mathrm{s}$

### ② 陽極に達したときの速度

**式:**

エネルギー保存則より，電子が電位差 $V$ で加速されたときの運動エネルギーは

$$\frac{1}{2}mv^2 = eV$$

これを $v$ について解くと

$$v = \sqrt{\frac{2eV}{m}}$$

**代入:**

$$v = \sqrt{\frac{2 \times 1.60 \times 10^{-19} \times 200}{9.11 \times 10^{-31}}}$$

$$= \sqrt{\frac{6.40 \times 10^{-17}}{9.11 \times 10^{-31}}}$$

$$= \sqrt{7.025 \times 10^{13}}$$

$$= 8.38 \times 10^{6}\ \mathrm{m/s}$$

**解**: $v = 8.38 \times 10^{6}\ \mathrm{m/s}$

### ③ 陽極に与えるエネルギー

**式:**

電子が電位差 $V$ で加速されて得る運動エネルギーは，電子が陽極に与えるエネルギーに等しい。したがって

$$\Delta K = eV$$

**代入:**

$$\Delta K = 1.60 \times 10^{-19} \times 200$$

$$= 3.20 \times 10^{-17}\ \mathrm{J}$$

また，これを電子ボルト (eV) で表すと

$$\Delta K = 200\ \mathrm{eV}$$

補足: 問②で求めた速度 $v=8.38\times10^{6}\ \mathrm{m/s}$ を用いて運動エネルギーを計算すると

$$\frac{1}{2}mv^2 = \frac{1}{2} \times 9.11 \times 10^{-31} \times (8.38 \times 10^{6})^2 = 3.20 \times 10^{-17}\ \mathrm{J},$$

となり，電位差から求めた $\Delta K$ の値と一致する（丸めによる僅差を除く）。

**解**: $\Delta K = 3.20 \times 10^{-17}\ \mathrm{J}$ （または $200\ \mathrm{eV}$） 

---

## 課題 2

**条件**: $K=100\ \mathrm{eV},\ B=0.05\ \mathrm{T},\ \theta=90^\circ$.

### ① 電子の円運動の半径

**式:**

まず，電子の速度 $v$ を求める。初期運動エネルギー $K$ が与えられているので

$$K = \frac{1}{2}mv^2$$

より

$$v = \sqrt{\frac{2K}{m}}$$

ここで，$K = 100\ \mathrm{eV}$ （$=100\times1.60\times10^{-19}\ \mathrm{J}$）。

磁界中で等速円運動する電子には，ローレンツ力が向心力として働くので

$$evB = \frac{mv^2}{r}$$

これを $r$ について解くと

$$r = \frac{mv}{eB}$$

**代入:**

$$K = 100 \times 1.60 \times 10^{-19} = 1.60 \times 10^{-17}\ \mathrm{J}$$

速度を計算:

$$v = \sqrt{\frac{2 \times 1.60 \times 10^{-17}}{9.11 \times 10^{-31}}}$$

$$= \sqrt{\frac{3.20 \times 10^{-17}}{9.11 \times 10^{-31}}}$$

$$= \sqrt{3.513 \times 10^{13}}$$

$$= 5.93 \times 10^{6}\ \mathrm{m/s}$$

円運動の半径を計算:

$$r = \frac{9.11 \times 10^{-31} \times 5.93 \times 10^{6}}{1.60 \times 10^{-19} \times 0.05}$$

$$= \frac{5.40 \times 10^{-24}}{8.00 \times 10^{-21}}$$

$$= 6.75 \times 10^{-4}\ \mathrm{m}$$

**解**: $r = 6.75 \times 10^{-4}\ \mathrm{m}$

### ② 毎秒の回転数

**式:**

円運動の角速度を $\omega$ とすると

$$\omega = \frac{v}{r} = \frac{eB}{m}$$

毎秒の回転数（周波数）$f$ は

$$f = \frac{\omega}{2\pi} = \frac{eB}{2\pi m}$$

**代入:**

$$f = \frac{1.60 \times 10^{-19} \times 0.05}{2\pi \times 9.11 \times 10^{-31}}$$

$$= \frac{8.00 \times 10^{-21}}{5.724 \times 10^{-30}}$$

$$= 1.40 \times 10^{9}\ \mathrm{s^{-1}}$$

**解**: $f = 1.40 \times 10^{9}\ \mathrm{s^{-1}}$ 

---

## 課題 3

**条件**: $D=1.0\times10^{-2}\ \mathrm{m},\ V_a=100\ \mathrm{V},\ B_z=0.1\ \mathrm{T}$. 初期: $(x,y)=(0,0),\ v_0=0$. 電界||x, B||z.

### ① $x_m$ を求める

**式:**

$E=-dV/dx=-V_a/D$. 方程式: $m\dot v_x=-eE-e v_yB$, $m\dot v_y=e v_xB$. $\omega=eB/m$ とおくと解は以下。

ここで，$\omega = \frac{eB}{m}$ とおくと

$$\frac{dv_x}{dt} = \frac{e|E|}{m} - \omega v_y$$

$$\frac{dv_y}{dt} = \omega v_x$$

これらを解くと，初期条件 $v_x(0) = v_y(0) = 0$ より

$$v_x(t) = \frac{|E|}{B}\sin(\omega t)$$

$$v_y(t) = \frac{|E|}{B}(1 - \cos(\omega t))$$

位置は速度を積分して

$$x(t) = \int_0^t v_x \, dt = \frac{|E|}{B\omega}(1 - \cos(\omega t)) = \frac{m|E|}{eB^2}(1 - \cos(\omega t))$$

$$y(t) = \int_0^t v_y \, dt = \frac{|E|}{B}\left(t - \frac{\sin(\omega t)}{\omega}\right) = \frac{|E|}{B}t - \frac{m|E|}{eB^2}\sin(\omega t)$$

$x(t)$ の最大値は $\cos(\omega t) = -1$ のとき，すなわち $\omega t = \pi$ のときに得られる

$$x_m = \frac{m|E|}{eB^2}(1 - (-1)) = \frac{2m|E|}{eB^2}$$

**代入:**

$$|E| = \frac{V_a}{D} = \frac{100}{1.0 \times 10^{-2}} = 1.00 \times 10^{4}\ \mathrm{V/m}$$

$x_m$ を計算:

$$x_m = \frac{2 \times 9.11 \times 10^{-31} \times 1.00 \times 10^{4}}{1.60 \times 10^{-19} \times (0.10)^2}$$

$$= \frac{1.822 \times 10^{-26}}{1.60 \times 10^{-21}}$$

$$= 1.14 \times 10^{-5}\ \mathrm{m}$$

**解**: $x_m = 1.14 \times 10^{-5}\ \mathrm{m}$

### ② $y_m$ を求める

**式:**

$x(t)$ が最大値 $x_m$ をとるとき $\omega t = \pi$ であるから，このときの $y$ 座標 $y_m$ は

$$y_m = \frac{|E|}{B} \cdot \frac{\pi}{\omega} - \frac{m|E|}{eB^2}\sin(\pi)$$

$\sin(\pi) = 0$ より

$$y_m = \frac{|E|}{B} \cdot \frac{\pi}{\omega} = \frac{|E|}{B} \cdot \frac{\pi m}{eB} = \frac{\pi m|E|}{eB^2}$$

これは $x_m = \frac{2m|E|}{eB^2}$ を用いて

$$y_m = \frac{\pi}{2} \cdot \frac{2m|E|}{eB^2} = \frac{\pi}{2} x_m$$

あるいは，直接計算して

$$y_m = \frac{2\pi m|E|}{eB^2}$$

**代入:**

$$y_m = \frac{2\pi \times 9.11 \times 10^{-31} \times 1.00 \times 10^{4}}{1.60 \times 10^{-19} \times (0.10)^2}$$

$$= \frac{5.73 \times 10^{-26}}{1.60 \times 10^{-21}}$$

$$= 3.58 \times 10^{-5}\ \mathrm{m}$$

または，$x_m$ の値を用いて

$$y_m = \pi \times \frac{x_m}{2} = \pi \times \frac{1.14 \times 10^{-5}}{2} = 3.58 \times 10^{-5}\ \mathrm{m}$$

**解**: $y_m = 3.58 \times 10^{-5}\ \mathrm{m}$

---

**以上**