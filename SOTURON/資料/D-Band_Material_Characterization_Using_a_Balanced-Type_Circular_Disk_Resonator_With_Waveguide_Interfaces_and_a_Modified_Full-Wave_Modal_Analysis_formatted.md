IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023 6009210

# $D$-Band Material Characterization Using a Balanced-Type Circular Disk Resonator With Waveguide Interfaces and a Modified Full-Wave Modal Analysis

**Yuto Kato**, *Member, IEEE*

**Abstract— This study presents material characterization in the $D$-band using a balanced-type circular disk resonator (BCDR) with waveguide interfaces. In the developed BCDR, ultrafine and brittle coaxial lines are covered by waveguide interfaces, which alleviates the robustness issues that occur when increasing the measurement frequency of conventional BCDRs with coaxial-line interfaces. The BCDR provides broadband complex permittivity and conductivity measurements of low-loss substrate materials over the entire $D$-band, owing to the mode-selective behavior of the resonator. Moreover, a modified modal analysis is derived to improve the accuracy of determining the permittivity from the measured resonant frequency based on the full-wave circuit analysis. A comparison between the analytical results and those of numerical simulations shows that the proposed analysis provides accurate calculations, even in cases with high-dielectric or thick samples, which typically cause inaccuracies in the conventional analysis. The developed BCDR and modified analysis are experimentally demonstrated by measuring the complex permittivity of three dielectric samples and the conductivity of two copper foil samples in the $D$-band.**

**Index Terms— Complex permittivity measurements, conductivity measurements, dielectric resonator, millimeter wave, mode-matching analysis.**

## I. INTRODUCTION

IN THE sixth-generation (6G) wireless communication, millimeter waves above 100 GHz are supposed to be used to realize high-speed and large-capacity communication with performances far exceeding those of 5G [1], [2], [3]. In general, the choice of low-loss substrate materials in the millimeter-wave bands is much more limited than in the microwave bands owing to an increased dielectric loss tangent and reduced conductivity. In particular, the effective conductivity of metallic layers on a dielectric substrate tends to become significantly smaller than the bulk metal value depending on the surface roughness, because the skin depth becomes comparable to the surface roughness [4], [5]. To efficiently develop advanced low-loss materials and sophisticated implementation processes for lower power consumption in 6G communication, accurate complex permittivity and conductivity measurements at millimeter-wave frequencies above 100 GHz are essential. The accurate evaluation of material parameters above 100 GHz is also important for the reliable design of 6G components, such as antennas, absorbers, and metasurfaces [6], [7].

Resonator methods are typically utilized for the characterization of low-loss materials [8], [9], [10], [11]. However, applying resonator methods to the millimeter-wave bands above 100 GHz has been challenging, owing to the difficulty in machining a tiny resonator. In contrast to conventional resonator methods, which utilize fundamental mode resonances, broadband material-measurement techniques have been proposed to measure the complex permittivity and conductivity of low-loss substrate materials up to over 100 GHz with a single system by utilizing higher-order $\text{TM}_{0m0}$ mode resonances of a balanced-type circular disk resonator (BCDR) [12], [13], [14], [15], [16]. The broadband measurement capability of the BCDR can be attributed to the selective excitation of $\text{TM}_{0m0}$ modes over a wideband. Selective excitation is realized by the cylindrical symmetry of the resonator and coaxial excitation mechanism.

Conventional BCDRs have coaxial-line interfaces to feed the coaxial TEM mode into the resonator. The maximum measurable frequency of the resonator is determined by the cutoff frequency of the coaxial line. Therefore, finer coaxial lines must be used in the excitation structures of the BCDR to increase the measurement frequency. However, the use of ultrafine and brittle coaxial-line interfaces causes robustness issues. Thus, implementing a BCDR with coaxial-line interfaces is impractical in the 6G frequency bands up to 300 GHz.

This study proposes a BCDR using waveguide interfaces as an excitation mechanism to extend the applicable frequency of the BCDR with a structure that alleviates the robustness issues exist in conventional BCDR structures having coaxial-line interfaces. The waveguide $\text{TE}_{10}$ mode transmitted to the waveguide interfaces is converted to the coaxial TEM mode by the coaxial-to-waveguide converters that are implemented in the excitation structures to excite a dielectric sample by the coaxial mode. A BCDR with WR-6 waveguide interfaces is developed to demonstrate the complex permittivity and conductivity measurements in the $D$-band (110–170 GHz). The proposed approach is expected to be applied at even higher frequencies, such as the 300-GHz band.

Moreover, an improved modal analysis is introduced for the BCDR to calculate the permittivity from the resonant frequency. In previous studies based on the mode-matching analysis [12], [13], [15], [17], a BCDR has been analyzed based on an approximate model in which the dielectric sample is surrounded by magnetic walls. This approximation was used because the mode-matching analysis is only suitable for simple structures. The conventional analysis can only approximately consider radial radiation through dielectric-sheet samples, and the previous study has reported that the relative permittivity is underestimated especially for high-dielectric materials [15]. This study further clarifies that the errors in the conventional analysis are amplified as the measurement frequency approaches the cutoff frequency of the radial radiation through the dielectric sheets. To address this problem, full-wave circuit modal analysis [18], [19], [20], [21], [22] is applied to analyze an exact and complex structure of the BCDR. In the circuit analysis method, the entire geometry is divided into simpler elements to express the whole structure as a connection of admittance matrices for the elements obtained via the mode-matching analysis. This is a powerful and flexible tool that can provide accurate analysis, even for complex structures with particular symmetries. By applying the circuit analysis, this study formulates, for the first time, a full-wave analysis for the BCDR based on an exact resonator structure, which is indispensable for accurate material measurements with the BCDR method in millimeter-wave bands above 100 GHz.

Incidentally, in addition to the BCDR method, the open-resonator method can provide permittivity measurements above 100 GHz [23], [24], [25]. An open resonator measures the complex permittivity tangential to a sheet sample by utilizing higher-order $\text{TEM}_{00n}$ modes over a wideband. In contrast, the BCDR method provides measurements of the complex permittivity perpendicular to a sheet sample, as well as the conductivity measurements of a metallic sample. Considering that anisotropic substrate materials require knowledge of both in-plane and perpendicular permittivities, both two methods are essential for material development for 6G communications.

This article is an extended version of [26], and it is expanded by including additional and detailed numerical simulations and experimental measurements for the developed BCDR with waveguide interfaces and by developing the modified analysis of the BCDR based on the full-wave circuit modal analysis.

The remainder of this article is organized as follows. The developed BCDR with waveguide interfaces used in this study is described in Section II. The improved modal analysis for the BCDR is introduced in Section III. The proposed modal analysis is numerically verified to clarify its accuracy compared with that of the conventional analysis in Section IV. Complex permittivity and conductivity measurements are demonstrated by using the developed BCDR with waveguide interfaces and the proposed modal analysis in Section V. Finally, the conclusions are presented in Section VI.

> **[Fig. 1の説明]:**
> (a) WR-6導波管インターフェースを備えた開発されたBCDRの写真。金属製の筐体と導波管接続部が見える。
> (b) WR-6導波管インターフェースを備えた開発されたBCDRの概略図。導波管から同軸線路への変換部、導体ディスク（厚さ $t_c$, 半径 $R$）、誘電体シート（厚さ $t$）、銅板、励振孔（半径 $a$, 長さ $M$）の構造が示されている。
> (c) 励振構造に実装された同軸-導波管変換器の概略図。WR-6導波管、ステップ構造、0.6 mm同軸線路が示されている。
> (d) BCDRに実装された励振構造のシミュレーションされたSパラメータ。反射（Reflection, dB）と透過（Transmission, dB）が周波数（100〜180 GHz）に対してプロットされている。反射は-20dB以下、透過は-1dB程度で推移している。
> (e) サンプルを装荷したBCDRのシミュレーションされた透過特性。周波数（100〜180 GHz）に対する透過（Transmission, dB）がプロットされている。3つの条件（$\epsilon_r=2, t=0.1$ mm; $\epsilon_r=2, t=0.27$ mm; $\epsilon_r=9, t=0.1$ mm）について、多数の共振ピークが観測されている。

## II. BCDR WITH WAVEGUIDE INTERFACES

A photograph and schematic of the developed BCDR for material characterization in the $D$-band are shown in Fig. 1(a) and (b), respectively. The BCDR has WR-6 waveguide interfaces and is connected to $D$-band frequency multipliers via bent waveguide lines. As shown in Fig. 1(b), the resonator comprises a thin circular conductor disk with a thickness $t_c = 0.06$ mm, diameter $2R = 15.0$ mm, and conductivity $\sigma$, sandwiched between a pair of dielectric sheet samples, each with a thickness $t$, relative permittivity $\epsilon_r$, and loss tangent $\tan \delta$ [i.e., the complex relative permittivity of the sample is $\epsilon_r(1 - j \tan \delta)$]. The dielectric sheets are sandwiched between two parallel copper plates. To realize the selective excitation for the $\text{TM}_{0m0}$ modes in a wideband up to 170 GHz, the resonator is excited and detected by 0.6-mm coaxial lines through excitation holes, of diameter $2a = 0.80$ mm and length $M = 0.5$ mm, located at the center of the resonator. The inner diameter of the outer conductor and the outer diameter of the center conductor of the coaxial lines are 0.610 and 0.203 mm, respectively. These ultrafine and brittle coaxial lines are covered inside the resonator by the waveguide interfaces, which alleviates the robustness issues. Coaxial-to-waveguide converters are implemented in the excitation structures of the BCDR to convert the waveguide $\text{TE}_{10}$ mode to the coaxial TEM mode. The relative permittivity of the dielectric sheet sample at each resonant frequency of the $\text{TM}_{0m0}$ modes is determined from the measured resonant frequency by considering the resonance condition of the BCDR with the modal analysis, which is explained in detail in Section III. The loss tangent of the dielectric sheet sample and conductivity of the conductor disk are obtained from the measured unloaded $Q$-factor.

Fig. 1(c) shows the coaxial-to-waveguide converter. The end of the WR-6 waveguide has a four-stage metallic stepped structure with the center conductor of the coaxial line inserted into it. The stepped structure is optimized for an efficient mode conversion over the entire $D$-band. Fig. 1(d) shows the simulation results of the S-parameters of the excitation structure calculated from 105 to 175 GHz using a commercial electromagnetic full-wave simulator HFSS.$^1$ In the simulations, ports 1 and 2 are set at the coaxial line and waveguide end faces, respectively. The lengths of the coaxial line and waveguide from the converter are set to 48 and 20 mm, respectively. As observed in Fig. 1(d), highly efficient coaxial-to-waveguide conversion without reflections is realized over the entire $D$-band. The reflections for both ports are less than $-20$ dB and the transmission including the insertion losses of the coaxial line and waveguide is more than $-1.2$ dB at frequencies from 110 to 170 GHz.

Fig. 1(e) shows the simulated transmissions of the BCDR loaded with dielectric sheet samples and copper disk calculated from 105 to 175 GHz. In the simulations, three sample conditions are considered for the dielectric sheets: 1) relative permittivity $\epsilon_r = 2$ and thickness $t = 0.1$ mm; 2) $\epsilon_r = 2$ and $t = 0.27$ mm; and 3) $\epsilon_r = 9$ and $t = 0.1$ mm. The loss tangent of the dielectric sheets and conductivity of the copper disk are set to $\tan \delta = 0.0004$ and $\sigma = 5.63 \times 10^7$ S/m, respectively. It is noted that the maximum frequency at which the electromagnetic field can be confined in the BCDR is limited by the cutoff frequency for the radial radiation through the dielectric sheets, as determined by the following equation [15]:

$$
f_c^{\text{rad}} = \frac{c}{4(t + t_c/2)\sqrt{\epsilon_r}} \quad (1)
$$

where $c$ is the velocity of light in free space. For the three sample conditions, $f_c^{\text{rad}}$ are calculated to be 408, 192, and 177 GHz, respectively. These values are higher than 170 GHz, which is the upper limit of the $D$-band. Considering the computational-cost constraints, the simulations are carried out at 701 points with a coarse resolution of 100 MHz. Fig. 1(e) shows that the selective excitation for the $\text{TM}_{0m0}$ modes is realized in the developed BCDR with waveguide interfaces, as in conventional BCDRs with coaxial-line interfaces [12], [13], [14], [15], [16]. In the frequency range from 105 to 175 GHz, $\text{TM}_{0,8,0}$ to $\text{TM}_{0,11,0}$ modes, $\text{TM}_{0,8,0}$ to $\text{TM}_{0,12,0}$ modes, and $\text{TM}_{0,16,0}$ to $\text{TM}_{0,25,0}$ modes are confirmed for sample conditions 1), 2), and 3), respectively.

Alignment between the conductor disk and excitation hole is essential for the mode selectivity of the $\text{TM}_{0m0}$ modes. To ensure alignment during the experiments, a donut-shaped thin film made of a cyclic olefin polymer (COP) with a thickness of 0.05 mm is used as a shim. The shim is carefully removed from the resonator to avoid moving the disk after ensuring disk alignment. We can find the misalignment from the measured transmission by detecting the resonances of the unwanted modes.

> **[Fig. 2の説明]:** BCDRの解析ジオメトリの概略図。
> (a) 提案されたモーダル解析（Proposed modal analysis）。励振孔、誘電体シート、導体ディスク、空気層、磁気壁（Mag. wall）、電気壁（Elec. wall）を含む詳細な構造が示されている。
> (b) 従来のモーダル解析（Conventional modal analysis）。励振孔が無視され、誘電体領域が磁気壁で囲まれた円筒として近似されている。半径は $R + \Delta R$ となっている。

## III. MODIFIED FULL-WAVE MODAL ANALYSIS

The analysis geometry of the BCDR considered in this study is shown in Fig. 2(a). Only half of the BCDR needs to be considered, owing to its symmetrical structure; therefore, a magnetic wall is placed on the plane of $z = t + t_c/2$. The air region in $0 \le r \le a$ and $-M \le z \le 0$, dielectric region in $r \ge 0$ and $0 \le z \le t$, and air region in $r \ge R$ and $t \le z \le t + t_c/2$ represent the excitation hole, dielectric sheet, and air gap, respectively. Here, we assume that the dielectric sheet is sufficiently large, and the dielectric region and upper air region extend infinitely in the radial direction.

The approximate analysis geometry shown in Fig. 2(b) is considered in the conventional mode-matching analysis [12], [13], [15], [17], where the dielectric region is approximated as a cylinder surrounded by a magnetic wall. The radius of the dielectric region is larger than that of the conductor disk by $\Delta R$, owing to the effect of the fringing field at the disk edge. In [15], we proposed an algorithm to estimate $\Delta R$ via the mode-matching analysis for a structure that ignored the excitation hole, and the algorithm improved the accuracy of the relative permittivity measurements using the BCDR method. However, the approximate model in Fig. 2(b) neglects the leakage from the dielectric into the air gap. As clarified later via a comparison with the full-wave simulations, this approximation has a non-negligible effect on the measurement results, particularly for measurement frequencies close to $f_c^{\text{rad}}$ with high-dielectric or thick samples.

We introduce the full-wave circuit analysis method [18], [19], [20], [21], [22] to rigorously analyze the structure shown in Fig. 2(a) by dividing the entire structure into three simple elements. The circuit segmentation of the structure shown in Fig. 2(a) is shown in Fig. 3(a), and the three elements contained in the circuit network are shown in Fig. 3(b)–(d). In the following, we first compute the admittance matrix of each element using the mode-matching analysis, in which the electromagnetic fields inside the structure are approximated on each surface of the ports using series expansions of basis functions. We then analyze the resonance condition of the entire circuit network by connecting the elements using the obtained admittance matrices.

When computing the admittance matrix, we only need to consider the $\text{TM}_{0m}$ modes because they are decoupled from all the TE modes and the $\text{TM}_{nm}$ modes ($n \ne 0$), owing to the coaxial cylindrical geometries of the elements (the elements do not have the TEM modes because of their geometries). This fact can be confirmed by calculating the coupling between the basis functions of the port fields and those of the internal fields for each mode.

> **[Fig. 3の説明]:**
> (a) BCDRの回路分割（Circuit segmentation）。要素A、B、Cがどのように接続されているかを示すブロック図。
> (b) 3ポート円筒構造（要素A）。ポート1（上部）、ポート2（側面）、ポート3（下部）を持つ円筒形の誘電体領域。
> (c) 1ポート円筒構造（要素B）。ポート1（上部）を持つ円筒形の空気領域（励振孔）。
> (d) 1ポートリング構造（要素C）。ポート1（内側面）を持つリング状の領域（空気ギャップと誘電体）。

### A. Three-Port Cylindrical Structure (Element A)

Fig. 3(b) shows the three-port cylindrical structure corresponding to element A in Fig. 3(a). The ports are defined as follows: port 1 at $0 \le r \le R$ and $z = t$, port 2 at $r = R$ and $0 \le z \le t$, and port 3 at $0 \le r \le a$ and $z = 0$. An electric wall condition is imposed at $z = 0$ and $a \le r \le R$. The structure is filled with the dielectric sheet sample.

The transverse electromagnetic fields at each port of element A can be written as a series expansion of the basis functions as follows:

$$
e^{\text{I}} = -\sum_{p=1}^{\infty} \alpha_p^{\text{I}} k_{Rp} J_1(k_{Rp}r) \hat{r} \quad (2)
$$

$$
h^{\text{I}} = -\sum_{u=1}^{\infty} \beta_u^{\text{I}} k_{Ru} J_1(k_{Ru}r) \hat{\phi} \quad (3)
$$

$$
e^{\text{II}} = \sum_{p=0}^{\infty} \alpha_p^{\text{II}} \cos\left(\frac{p\pi}{t}z\right) \hat{z} \quad (4)
$$

$$
h^{\text{II}} = \sum_{u=0}^{\infty} \beta_u^{\text{II}} \cos\left(\frac{u\pi}{t}z\right) \hat{\phi} \quad (5)
$$

$$
e^{\text{III}} = -\sum_{p=1}^{\infty} \alpha_p^{\text{III}} k_{ap} J_1(k_{ap}r) \hat{r} \quad (6)
$$

$$
h^{\text{III}} = -\sum_{u=1}^{\infty} \beta_u^{\text{III}} k_{au} J_1(k_{au}r) \hat{\phi} \quad (7)
$$

where $\alpha_p^{\text{I}}$, $\alpha_p^{\text{II}}$, and $\alpha_p^{\text{III}}$ are the expansion coefficients for the transverse electric fields at ports 1, 2, and 3, respectively, $\beta_u^{\text{I}}$, $\beta_u^{\text{II}}$, and $\beta_u^{\text{III}}$ are the expansion coefficients for the transverse magnetic fields at ports 1, 2, and 3, respectively, $\hat{r}$, $\hat{\phi}$, and $\hat{z}$ are the unit vectors in the $r$-, $\phi$-, and $z$-directions, respectively, $J_n$ is the Bessel function of the first kind of order $n$, and

$$
k_{Rn} = \frac{\chi_{0n}}{R}, \quad k_{an} = \frac{\chi_{0n}}{a} \quad (8)
$$

where $\chi_{0n}$ is the $n$th zero of $J_0$.

To calculate the $Y_{i1}$ parameters of element A, electric wall conditions are imposed on ports 2 and 3. In this case, the transverse components of the electromagnetic fields inside the structure are given by the following equations:

$$
E^{\text{in}} = -\sum_{m=1}^{\infty} A_m \frac{\gamma_{Rm}}{k_{Rm}} J_1(k_{Rm}r) \sinh(\gamma_{Rm}z) \hat{r} \quad (9)
$$

$$
H^{\text{in}} = \sum_{m=1}^{\infty} B_m \frac{j\omega\epsilon_r\epsilon_0}{k_{Rm}} J_1(k_{Rm}r) \cosh(\gamma_{Rm}z) \hat{\phi} \quad (10)
$$

where $A_m$ and $B_m$ are the expansion coefficients, $\omega$ is the angular frequency, $\epsilon_0$ is the permittivity in free space, and

$$
\gamma_{Rm}^2 = k_{Rm}^2 - \epsilon_r k_0^2 \quad (11)
$$

where $k_0 = \omega/c$ is the wavenumber in free space. Imposing the boundary condition for the transverse electric field at port 1 yields the following:

$$
E^{\text{in}}(z = t) = e^{\text{I}}. \quad (12)
$$

We then apply the orthogonality of the Bessel function and obtain

$$
A_m = \sum_{p=1}^{\infty} \frac{k_{Rp}^2}{\gamma_{Rp} \sinh(\gamma_{Rp}t)} \delta_{mp} \quad (13)
$$

where $\delta_{mp}$ denotes the Kronecker delta.

Imposing the boundary condition for the transverse magnetic fields at the ports yields the following:

$$
H^{\text{in}}(z = t) = h^{\text{I}} \quad (14)
$$
$$
H^{\text{in}}(r = R) = h^{\text{II}} \quad (15)
$$
$$
H^{\text{in}}(z = 0) = h^{\text{III}}. \quad (16)
$$

We then apply the orthogonality of the basis functions and obtain the following:

$$
\vec{\beta}^{\text{I}} = Y_{11}^{\text{A}} \vec{\alpha}^{\text{I}}, \quad \vec{\beta}^{\text{II}} = Y_{21}^{\text{A}} \vec{\alpha}^{\text{I}}, \quad \vec{\beta}^{\text{III}} = Y_{31}^{\text{A}} \vec{\alpha}^{\text{I}} \quad (17)
$$

$$
[Y_{11}^{\text{A}}]_{up} = -\frac{j\omega\epsilon_r\epsilon_0}{\gamma_{Rp} \tanh(\gamma_{Rp}t)} \delta_{up} \quad (18)
$$

$$
[Y_{21}^{\text{A}}]_{up} = \frac{2j\omega\epsilon_r\epsilon_0 J_1(\chi_{0p}) k_{Rp} t}{(\gamma_{Rp}t)^2 + (\pi u)^2} \frac{(-1)^u}{1 + \delta_{0u}} \quad (19)
$$

$$
[Y_{31}^{\text{A}}]_{up} = \frac{2j\omega\epsilon_r\epsilon_0}{\gamma_{Rp} \sinh(\gamma_{Rp}t)} \frac{J_0(k_{Rp}a)}{a J_1(\chi_{0u})} \frac{k_{Rp}^2 k_{au}}{k_{Rp}^2 - k_{au}^2}. \quad (20)
$$

To calculate the $Y_{i2}$ parameters of element A, electric wall conditions are imposed on ports 1 and 3. In this case, the transverse components of the electromagnetic fields inside the structure are given by the following equations:

$$
E^{\text{in}} = \sum_{m=0}^{\infty} A_m J_0(k_{tm}r) \cosh(\gamma_{tm}z) \hat{z} \quad (21)
$$

$$
H^{\text{in}} = \sum_{m=0}^{\infty} B_m \frac{j\omega\epsilon_r\epsilon_0}{k_{tm}} J_1(k_{tm}r) \cosh(\gamma_{tm}z) \hat{\phi} \quad (22)
$$

where

$$
\gamma_{tm} = \frac{jm\pi}{t}, \quad k_{tm}^2 = \epsilon_r k_0^2 + \gamma_{tm}^2. \quad (23)
$$

By applying the boundary conditions at the ports and the orthogonality of the basis functions as in the derivation of $Y_{i1}^{\text{A}}$, we obtain the following:

$$
\vec{\beta}^{\text{I}} = Y_{12}^{\text{A}} \vec{\alpha}^{\text{II}}, \quad \vec{\beta}^{\text{II}} = Y_{22}^{\text{A}} \vec{\alpha}^{\text{II}}, \quad \vec{\beta}^{\text{III}} = Y_{32}^{\text{A}} \vec{\alpha}^{\text{II}} \quad (24)
$$

$$
[Y_{12}^{\text{A}}]_{up} = \frac{2j\omega\epsilon_r\epsilon_0 R^2}{R^2 k_{tp}^2 - \chi_{0u}^2} \frac{(-1)^p}{\chi_{0u} J_1(\chi_{0u})} \quad (25)
$$

$$
[Y_{22}^{\text{A}}]_{up} = \frac{j\omega\epsilon_r\epsilon_0}{k_{tp}} \frac{J_1(k_{tp}R)}{J_0(k_{tp}R)} \delta_{up} \quad (26)
$$

$$
[Y_{32}^{\text{A}}]_{up} = \frac{2j\omega\epsilon_r\epsilon_0 a^2}{a^2 k_{tp}^2 - \chi_{0u}^2} \frac{J_0(k_{tp}a)}{J_0(k_{tp}R) J_1(\chi_{0u}) \chi_{0u}}. \quad (27)
$$

To calculate the $Y_{i3}$ parameters of element A, electric wall conditions are imposed on ports 1 and 2. In this case, the transverse components of the electromagnetic fields inside the structure are given by the following equations:

$$
E^{\text{in}} = -\sum_{m=1}^{\infty} A_m \frac{\gamma_{Rm}}{k_{Rm}} J_1(k_{Rm}r) \sinh[\gamma_{Rm}(z - t)] \hat{r} \quad (28)
$$

$$
H^{\text{in}} = \sum_{m=1}^{\infty} B_m \frac{j\omega\epsilon_r\epsilon_0}{k_{Rm}} J_1(k_{Rm}r) \cosh[\gamma_{Rm}(z - t)] \hat{\phi}. \quad (29)
$$

By applying the boundary conditions at the ports and the orthogonality of the basis functions as in the derivation of $Y_{i1}^{\text{A}}$, we obtain the following:

$$
\vec{\beta}^{\text{I}} = Y_{13}^{\text{A}} \vec{\alpha}^{\text{III}}, \quad \vec{\beta}^{\text{II}} = Y_{23}^{\text{A}} \vec{\alpha}^{\text{III}}, \quad \vec{\beta}^{\text{III}} = Y_{33}^{\text{A}} \vec{\alpha}^{\text{III}} \quad (30)
$$

$$
[Y_{13}^{\text{A}}]_{up} = -\frac{2j\omega\epsilon_r\epsilon_0}{\gamma_{Ru} \sinh(\gamma_{Ru}t)} \frac{J_0(k_{Ru}a) J_1(\chi_{0p})}{R^2 [J_1(\chi_{0u})]^2} \frac{\chi_{0p}}{k_{Ru}^2 - k_{ap}^2} \quad (31)
$$

$$
[Y_{23}^{\text{A}}]_{up} = \sum_{m=1}^{\infty} \frac{4j\omega\epsilon_r\epsilon_0}{1 + \delta_{0u}} \frac{at}{(\gamma_{Rm}t)^2 + (\pi u)^2} \times \frac{J_0(k_{Rm}a) J_1(\chi_{0p})}{R^2 J_1(\chi_{0m})} \frac{k_{Rm} k_{ap}}{k_{Rm}^2 - k_{ap}^2} \quad (32)
$$

$$
[Y_{33}^{\text{A}}]_{up} = \sum_{m=1}^{\infty} \frac{4j\omega\epsilon_r\epsilon_0 \chi_{0p}}{R^2 \chi_{0u} \gamma_{Rm} \tanh(\gamma_{Rm}t)} \frac{J_1(\chi_{0p}) J_0^2(k_{Rm}a)}{J_1(\chi_{0u}) J_1^2(\chi_{0m})} \times \frac{k_{Rm}^2}{(k_{Rm}^2 - k_{au}^2)(k_{Rm}^2 - k_{ap}^2)}. \quad (33)
$$

### B. One-Port Cylindrical Structure (Element B)

Fig. 3(c) shows the one-port cylindrical structure corresponding to element B in Fig. 3(a). The port is defined at $0 \le r \le a$ and $z = 0$. Electric wall conditions are imposed on the other boundaries of the cylinder. The structure is filled with air. In a similar manner to that used to obtain $Y_{11}^{\text{A}}$, we obtain $Y_{11}$ of element B as follows:

$$
[Y_{11}^{\text{B}}]_{up} = -\frac{j\omega\epsilon_a\epsilon_0}{\gamma_{ap} \tanh(\gamma_{ap}t)} \delta_{up} \quad (34)
$$

where $\epsilon_a$ is the relative permittivity of air and

$$
\gamma_{ap}^2 = k_{ap}^2 - \epsilon_r k_0^2. \quad (35)
$$

### C. One-Port Ring Structure (Element C)

Fig. 3(d) shows the one-port ring structure corresponding to element C in Fig. 3(a). The port is defined at $r = R$ and $0 \le z \le t$. The structure is filled with the dielectric sample in $0 \le z \le t$ and air in $t \le z \le t + t_c/2$. Electric wall conditions are imposed on the bottom of the dielectric region ($r \ge R, z = 0$) and lateral surface of the air region ($r = R, t \le z \le t + t_c/2$), and a magnetic wall condition is imposed on the top of the air region ($r \ge R, t \le z \le t + t_c/2$). The dielectric and air regions are assumed to extend infinitely in the $r$-direction.

The field components in the dielectric and air regions are given by the following equations:

$$
E_z^{(1)} = \sum_{m=1}^{\infty} K_0(q_m r) \left[ A_m^{(1)} e^{\gamma_m^{(1)}z} + B_m^{(1)} e^{-\gamma_m^{(1)}z} \right] \quad (36)
$$

$$
E_r^{(1)} = \sum_{m=1}^{\infty} \frac{\gamma_m^{(1)}}{q_m} K_1(q_m r) \left[ A_m^{(1)} e^{\gamma_m^{(1)}z} - B_m^{(1)} e^{-\gamma_m^{(1)}z} \right] \quad (37)
$$

$$
H_{\phi}^{(1)} = \sum_{m=1}^{\infty} -\frac{j\omega\epsilon_r\epsilon_0}{q_m} K_1(q_m r) \left[ A_m^{(1)} e^{\gamma_m^{(1)}z} + B_m^{(1)} e^{-\gamma_m^{(1)}z} \right] \quad (38)
$$

$$
E_z^{(2)} = \sum_{m=1}^{\infty} K_0(q_m r) \left[ A_m^{(2)} e^{\gamma_m^{(2)}z} + B_m^{(2)} e^{-\gamma_m^{(2)}z} \right] \quad (39)
$$

$$
E_r^{(2)} = \sum_{m=1}^{\infty} \frac{\gamma_m^{(2)}}{q_m} K_1(q_m r) \left[ A_m^{(2)} e^{\gamma_m^{(2)}z} - B_m^{(2)} e^{-\gamma_m^{(2)}z} \right] \quad (40)
$$

$$
H_{\phi}^{(2)} = \sum_{m=1}^{\infty} -\frac{j\omega\epsilon_a\epsilon_0}{q_m} K_1(q_m r) \left[ A_m^{(2)} e^{\gamma_m^{(2)}z} + B_m^{(2)} e^{-\gamma_m^{(2)}z} \right] \quad (41)
$$

where superscripts (1) and (2) denote the quantities for the dielectric and air regions, respectively, $K_n$ is the modified Bessel function of the second kind of order $n$, and

$$
q_m^2 = -\epsilon_r k_0^2 - {\gamma_m^{(1)}}^2 = -\epsilon_a k_0^2 - {\gamma_m^{(2)}}^2. \quad (42)
$$

By applying the boundary conditions at $z = 0, z = t$, and $z = t + t_c/2$ for $E_r$ and $H_{\phi}$ and the orthogonality of the basis functions, we obtain the following:

$$
[X] \begin{pmatrix} A_m^{(1)} \\ A_m^{(2)} \end{pmatrix} = 0 \quad (43)
$$

$$
[X] = \begin{pmatrix} 1 & -L_{11} + L_{12} e^{2\gamma_m^{(2)}(t+t_c/2)} \\ 1 & -L_{21} + L_{22} e^{2\gamma_m^{(2)}(t+t_c/2)} \end{pmatrix} \quad (44)
$$

$$
[L] = \begin{pmatrix} \gamma_m^{(1)} e^{\gamma_m^{(1)}t} & -\gamma_m^{(1)} e^{-\gamma_m^{(1)}t} \\ \epsilon_r\epsilon_0 e^{\gamma_m^{(1)}t} & \epsilon_r\epsilon_0 e^{-\gamma_m^{(1)}t} \end{pmatrix}^{-1} \times \begin{pmatrix} \gamma_m^{(2)} e^{\gamma_m^{(2)}t} & -\gamma_m^{(2)} e^{-\gamma_m^{(2)}t} \\ \epsilon_a\epsilon_0 e^{\gamma_m^{(2)}t} & \epsilon_a\epsilon_0 e^{-\gamma_m^{(2)}t} \end{pmatrix}. \quad (45)
$$

The characteristic equation of $\det[X] = 0$ is given from (43) and by substituting (42) into the characteristic equation, $\gamma_m^{(1)}$, $\gamma_m^{(2)}$, and $q_m$ can be obtained. It should be noted that by imposing $q_m^2 > 0$ such that the fields do not diverge at $r \to \infty$, we can obtain the cutoff frequency for the radial radiation. When the air region is assumed to be filled with the same dielectric with $\epsilon_r$, the cutoff frequency thus obtained agrees with that obtained from the conventional modal analysis of (1).

To calculate $Y_{11}$ of element C, $Y_{11}^{\text{C}}$, we introduce $P_m$ defined by the following equation. $P_m$ can be readily calculated from (42) and the boundary conditions at $z = 0, z = t$, and $z = t + t_c/2$

$$
P_m = \frac{1}{{A_m^{(1)}}^2} \left\{ \int_0^t \epsilon_r\epsilon_0 \left[ A_m^{(1)} e^{\gamma_m^{(1)}z} + B_m^{(1)} e^{-\gamma_m^{(1)}z} \right]^2 + \int_t^{t+t_c/2} \epsilon_a\epsilon_0 \left[ A_m^{(2)} e^{\gamma_m^{(2)}z} + B_m^{(2)} e^{-\gamma_m^{(2)}z} \right]^2 \right\}. \quad (46)
$$

The transverse electromagnetic fields at the port can be given by (4) and (5). By applying the boundary conditions at $r = R$ and the orthogonality of the basis functions, we obtain the following:

$$
[Y_{11}^{\text{C}}]_{up} = \sum_{m=1}^{\infty} -\frac{8 j\omega t^3 (-1)^{u+p}}{q_m(1 + \delta_{0u})} \frac{K_1(q_m R)}{P_m K_0(q_m R)} \times \frac{\left[ \epsilon_r\epsilon_0 \gamma_m^{(1)} \sinh(\gamma_m^{(1)}t) \right]^2}{\left[ (\gamma_m^{(1)}t)^2 + (\pi u)^2 \right] \left[ (\gamma_m^{(1)}t)^2 + (\pi p)^2 \right]}. \quad (47)
$$

### D. Connections of the Elements

The connections of the three elements are carried out based on the circuit theory, and the following equations are obtained:

$$
\begin{pmatrix} \vec{\beta}^{\text{I}} \\ \vec{\beta}^{\text{II}} \\ \vec{\beta}^{\text{III}} \end{pmatrix} = \begin{pmatrix} Y_{11}^{\text{A}} & Y_{12}^{\text{A}} & Y_{13}^{\text{A}} \\ Y_{21}^{\text{A}} & Y_{22}^{\text{A}} & Y_{23}^{\text{A}} \\ Y_{31}^{\text{A}} & Y_{32}^{\text{A}} & Y_{33}^{\text{A}} \end{pmatrix} \begin{pmatrix} \vec{\alpha}^{\text{I}} \\ \vec{\alpha}^{\text{II}} \\ \vec{\alpha}^{\text{III}} \end{pmatrix} \quad (48)
$$

$$
\vec{\beta}^{\text{III}} = Y_{11}^{\text{B}} \vec{\alpha}^{\text{III}} \quad (49)
$$

$$
\vec{\beta}^{\text{II}} = Y_{11}^{\text{C}} \vec{\alpha}^{\text{II}}. \quad (50)
$$

Then, the admittance and scattering matrices of the entire structure seen from port 2 of element A are derived. Finally, considering that port 2 is short-terminated, a resonance condition is derived to calculate the sample permittivity [18], [20].

The mode numbers for the ports considered in the calculations are truncated to finite values. In Sections IV and V, the mode numbers for ports 1, 2, and 3 of element A are set as $N^{\text{I}} = 300, N^{\text{II}} = 50$, and $N^{\text{III}} = 50$, respectively, unless otherwise specified. The mode numbers for the fields inside elements A and C, which correspond to the upper limit of $m$ in (32)–(33) and (47), are set as $N^{\text{I}}$ and $N^{\text{II}}$, respectively.

## IV. NUMERICAL VERIFICATION OF THE MODAL ANALYSIS

To verify the accuracy of the proposed modal analysis compared with that of the conventional one, full-wave electromagnetic simulations are carried out using the HFSS$^1$ eigenmode solver. In the simulations, similar to those in Section II, three sample conditions are considered for the dielectric sheet: 1) $\epsilon_r = 2$ and $t = 0.1$ mm; 2) $\epsilon_r = 2$ and $t = 0.27$ mm; and 3) $\epsilon_r = 9$ and $t = 0.1$ mm. For the three conditions, the resonant frequencies of the $\text{TM}_{0m0}$ modes are calculated in the range from 105 to 175 GHz. Then, the relative permittivity of the dielectric sheet is calculated from each simulated resonant frequency using the proposed and conventional modal analyses to compare with the setting values. To accurately calculate the resonant frequency at a moderate computational cost, both dielectric and conductor losses in the resonator are not considered in the simulations. In addition, considering the symmetrical structure of the BCDR and electromagnetic distributions at resonances, only a portion of the lower half of the resonator with a center angle of $30^{\circ}$ is analyzed by setting perfect magnetic conductor (PMC) boundaries, as shown in Fig. 4(a). The dielectric sheet and air gap are terminated by a perfectly matched layer (PML) boundary to consider the radial radiation.

Fig. 4(b)–(d) shows the deviations of the analytically calculated relative permittivity from each setting. The red and blue markers represent the results obtained from the simulated resonant frequencies by using the proposed and conventional modal analyses, respectively. The results for sample conditions 1), 2), and 3) are shown in Fig. 4(b)–(d), respectively. Fig. 4(b)–(d) shows that the proposed analysis provides highly accurate results for all sample conditions at all resonances with a deviation within $\pm 0.04\%$. However, the results obtained from the conventional analysis are underestimated for all three cases and slightly decrease with the frequency for samples with a large thickness [Fig. 4(c)] or high permittivity [Fig. 4(d)]. This is because the conventional analysis does not consider the effect of radial radiation from the dielectric sheet into the air gap, and the radiation becomes significant as the frequency approaches $f_c^{\text{rad}}$ ($f_c^{\text{rad}} = 408, 177$, and 192 GHz for cases 1), 2), and 3), respectively).

> **[Fig. 4の説明]:**
> (a) BCDRのフルウェーブシミュレーションの構成。PMC境界、PML境界、励振孔、誘電体シート、導体ディスク、空気ギャップが示されている。
> (b)-(d) 各設定値からの解析的に計算された比誘電率の偏差（Deviation, %）。
> (b) $\epsilon_r=2, t=0.1$ mmの場合。提案法（赤）はほぼ0%の偏差。従来法（青）は-0.2%〜-0.4%程度の偏差。
> (c) $\epsilon_r=2, t=0.27$ mmの場合。提案法（赤）はほぼ0%。従来法（青）は-0.6%〜-0.8%程度で、周波数と共に偏差が増大。
> (d) $\epsilon_r=9, t=0.1$ mmの場合。提案法（赤）はほぼ0%。従来法（青）は-0.4%〜-0.6%程度で、周波数と共に偏差が増大。

The deviations for the conventional analysis shown in Fig. 4(b)–(d) are replotted against $f/f_c^{\text{rad}}$ for the three sample conditions, as shown in Fig. 5. Fig. 5 indicates that the magnitudes of the deviations increase with $f/f_c^{\text{rad}}$ among the results with the same $\epsilon_r$. In addition, comparing the results with $\epsilon_r = 2$ and 9 shows that the deviations increase with $\epsilon_r$ for the results with similar $f/f_c^{\text{rad}}$. This result can be explained by the fact that the effect of radial radiation into the air gap on the permittivity calculation in the conventional analysis becomes pronounced when the difference between the sample permittivity and the air permittivity ($\approx 1$) increases. According to (1), we obtain the following:

$$
\frac{f}{f_c^{\text{rad}}} = \frac{4(t + t_c/2)}{\lambda_0/\sqrt{\epsilon_r}} = 2g \quad (51)
$$

where $\lambda_0$ is the wavelength in free space, and $g$ is the “electric length” for the distance between the upper and lower copper plates defined here by $g = (2t + t_c)/(\lambda_0/\sqrt{\epsilon_r})$. Fig. 5 suggests that the relative permittivity error in the conventional analysis owing to the radial radiation is governed by $g$ and $\epsilon_r$.

Incidentally, it would be possible to mitigate the error in the conventional analysis to some extent by performing BCDR measurements without removing the donut-shaped dielectric shim used for disk alignment, because the difference in the permittivity between the sample and the gap is suppressed; however, it has been reported that nonnegligible errors still remain for high-dielectric samples with large permittivity differences from the shim [15]. The proposed analysis based on the rigorous resonator-structure model that considers the radial radiation can provide sufficiently accurate results, even when the frequency is close to $f_c^{\text{rad}}$ with high-dielectric or thick samples.

> **[Fig. 5の説明]:**
> 従来解析の比誘電率の偏差を $f/f_c^{\text{rad}}$ に対してプロットしたグラフ。3つのサンプル条件の結果が示されている。$f/f_c^{\text{rad}}$ が大きくなるにつれて、偏差の絶対値が増加している。

To study the convergence of the proposed analysis on the mode numbers, the dependence of the results on $N^{\text{I}}$ (the mode number on the circular port with radius $R$) is investigated. Fig. 6 shows the deviations of the results compared to those of the case of $N^{\text{I}} = 300$ for sample conditions 1), 2), and 3). In Fig. 6, the results for the highest-order modes at frequencies below 175 GHz are presented for each sample condition ($\text{TM}_{0,11,0}, \text{TM}_{0,12,0}$, and $\text{TM}_{0,25,0}$ modes at 161, 171, and 173 GHz for conditions 1), 2), and 3), respectively). The mode numbers for the other ports are fixed at $N^{\text{II}} = N^{\text{III}} = 50$. As observed in Fig. 6, the results converge sufficiently when $N^{\text{I}}$ increases to 300. Even for the relatively slow convergence case with $\epsilon_r = 9$ [condition 3)], the deviation between the results for $N^{\text{I}} = 250$ and $N^{\text{I}} = 300$ is as small as 0.02%.

> **[Fig. 6の説明]:**
> 円形ポート（半径 $R$）に使用されるモード数 $N^{\text{I}}$ に対する提案モーダル解析の収束性。$N^{\text{I}}=300$ の場合と比較した計算された比誘電率の偏差（%）がプロットされている。$N^{\text{I}}$ が増加するにつれて偏差は0に収束し、300付近では十分収束していることがわかる。

## V. EXPERIMENTS

### A. Complex Permittivity Measurements in the D-Band

To demonstrate the developed BCDR with waveguide interfaces and the proposed modal analysis, the complex permittivity of COP, polytetrafluoroethylene (PTFE), and perfluoroalkoxy alkanes (PFA) is measured in the $D$-band. The thickness and associated uncertainty of the dielectric sheet pairs are $0.255 \pm 0.002$ mm, $0.209 \pm 0.003$ mm, and $0.257 \pm 0.006$ mm for the COP, PTFE, and PFA samples, respectively. The difference in the thickness of each sample pair is less than 0.001 mm and is included in the thickness uncertainty. Each sheet sample has a circular shape with a diameter of 50 mm. A copper disk with $t_c = 0.06$ mm and $2R = 15.0$ mm is used in the experiments.

Fig. 7(a) shows the measured transmissions of the BCDRs loaded with the three samples obtained from 105 to 175 GHz using a Keysight vector network analyzer (VNA) N5227B with VDI frequency multipliers N5262BW06. Before the measurements, the through-reflect-line (TRL) calibration is performed on the VNA at the waveguide interfaces of the resonator. As observed in Fig. 7(a), the $\text{TM}_{0m0}$ mode resonances are clearly observed for all samples with other resonant modes sufficiently suppressed, as in the simulated transmissions of Fig. 1(e). This indicates that the selective excitation for the $\text{TM}_{0m0}$ modes is realized for the developed BCDR with waveguide interfaces, as in conventional BCDRs with coaxial-line interfaces [12], [13], [14], [15], [16].

The relative permittivity calculated from the measured resonant frequency using the proposed modal analysis method is shown in Fig. 7(b). The red, blue, and green circles represent the results for the COP, PTFE, and PFA samples, respectively. It can be observed from Fig. 7(b) that the measured relative permittivity for each sample is nearly flat over the entire frequency range, which supports the validity of the measurement system and analysis method. For comparison, the relative permittivity calculated from the conventional modal analysis is shown in Fig. 7(b) with black triangle markers for the COP sample. The results are slightly smaller than those from the proposed modal analysis, and they decrease with frequency. This is consistent with the simulation results shown in Fig. 4 and experimentally demonstrates the effectiveness of the proposed modal analysis compared with that of the conventional one.

The loss tangent is obtained from the measured unloaded $Q$-factor $Q_u$ of each $\text{TM}_{0m0}$ mode of the BCDR. Assuming that the effects of the fringing fields at the disk edge and conductor losses in the excitation holes are negligible, which is an appropriate assumption considering the typical measurement uncertainty of the $Q$-factor (i.e., $\sim 2\%$), the loss tangent is obtained from the following equation [13], [15], [16]:

$$
\tan \delta = \frac{1}{Q_u} - \frac{1}{t\sqrt{\pi\mu_0 f_r \sigma}} \quad (52)
$$

where $\mu_0$ is the permeability in free space, $f_r$ is the resonant frequency, and $\sigma$ is the conductivity of the two parallel copper plates and the copper disk of the BCDR. $\sigma$ is measured beforehand using the two-dielectric resonator method [27] at 10 GHz, and the result is $\sigma = (5.63 \pm 0.18) \times 10^7$ S/m. The measurement results of the loss tangent for the three samples are shown in Fig. 7(c). As observed in Fig. 7(c), the measured loss tangent shows almost flat (COP) or linearly increasing (PTFE, PFA) frequency characteristics in the $D$-band.

In Fig. 7(b) and (c), the associated uncertainties with the coverage factor $k = 2$ are shown as error bars. The uncertainties of the relative permittivity and loss tangent, $U(\epsilon_r)$ and $U(\tan \delta)$, are evaluated by considering the uncertainty propagation for ($t, t_c, R, a, M, f_r$) and ($t, f_r, Q_u, \sigma$), respectively, on the basis of the sensitivity analysis. The uncertainties of $t_c, R, a$, and $M$ are estimated to be 0.002, 0.0025, 0.005, and 0.25 mm, respectively, and those of $f_r$ and $Q_u$ are evaluated based on the repeatability of five measurements. In addition, for $U(\epsilon_r)$, the uncertainty associated with the error of the proposed modal analysis is estimated to be 0.05% on the basis of the accuracy (see Fig. 4) and convergence in terms of mode numbers (see Fig. 6) and is included in the combined uncertainty in Fig. 7(b). $U(\epsilon_r)$ is found to be less than 0.5% for the COP and PTFE samples and less than 0.7% for the PFA sample in the entire frequency band. $U(\tan \delta)$ is less than 8% for the COP (except for the first measurement point) and PFA samples and less than 17% for the PTFE sample. The relatively high $U(\tan \delta)$ of 12.8% at the first measurement point of 108 GHz for the COP sample can be attributed to the degraded signal-to-noise ratio for a weak resonant peak [see Fig. 7(a)].

> **[Fig. 7の説明]:**
> (a) 3つのサンプルを装荷したBCDRの測定された透過特性（Transmission, dB）。周波数（100〜180 GHz）に対してプロットされている。COP（赤）、PTFE（青）、PFA（緑）の共振ピークが明確に観測されている。
> (b) 測定された比誘電率と関連する不確かさ。COP（約2.3）、PTFE（約2.1）、PFA（約2.1）の結果が示されている。COPについては従来解析の結果（黒三角）も示されており、提案法よりも低い値を示している。
> (c) 測定された誘電正接（Loss tangent）と関連する不確かさ。PFA（約$6 \times 10^{-4}$）、COP（約$4 \times 10^{-4}$）、PTFE（約$2 \times 10^{-4}$）の結果が示されている。

### B. Conductivity Measurements in the D-Band

To further demonstrate the developed BCDR with waveguide interfaces, the conductivity of copper foils used as circuit materials is measured. In general, copper foils used for circuit boards are roughened on one side to strengthen their adhesion with dielectric substrates via the anchor effect [28]. The roughening treatment is performed by plating nodular metallic particles onto a raw copper foil [29], [30]. However, as mentioned in Section I, the surface roughness tends to degrade the conductivity, particularly in the 6G frequency bands where the skin depth is in the submicrometer order [4], [5]. Therefore, it is desirable to develop a copper foil that achieves both high conductivity and strong adhesion by optimizing the composition, size, and shape of roughening particles.

Two copper foils (samples 1 and 2) are prepared for the conductivity measurements in the $D$-band. Scanning electron microscope images of the roughened surfaces of the two samples are shown in Fig. 8(a). Owing to the differences in particle size and shape, the roughened surfaces of samples 1 and 2 have different surface roughnesses with typical $R_{zjis}$ (ten-point mean roughness) values of 0.4 and 0.7 $\mu$m, respectively. The copper foils to be loaded into the BCDR are machined into circular shapes with a diameter of $2R = 15.0$ mm. Photographs of the roughened and unroughened surfaces of the copper foil sample are shown in Fig. 8(b). The thickness of each sample is $t_c = 0.012$ mm. Let $\sigma^{\text{rough}}$ and $\sigma^{\text{unrough}}$ be the conductivities of the roughened and unroughened surfaces of the copper foil sample, respectively. Assuming that $\sigma^{\text{unrough}}$ is equal to the conductivity $\sigma$ of the copper disk used in Section V-A, $\sigma^{\text{rough}}$ is obtained using the following equation [16]:

$$
\sigma^{\text{rough}} = \left[ \frac{1}{\sqrt{\sigma}} - 4t\sqrt{\pi\mu_0 f_r} \left( \frac{1}{Q_u} - \frac{1}{Q_u^{\text{rough}}} \right) \right]^{-2} \quad (53)
$$

where $Q_u^{\text{rough}}$ and $Q_u$ are the $Q$-factors of the BCDRs loaded with the copper foil sample (one side roughened) and copper disk (both sides unroughened), respectively (the resonant frequencies of the two measurements are almost the same with the measured differences below 0.2%). The COP sheets with $t = 0.255$ mm used in Section V-A are used again for the conductivity measurements.

Fig. 8(c) shows the measured conductivity of the two copper foil samples. As observed in Fig. 8(c), the conductivity of sample 1 is almost flat over the entire $D$-band. However, the conductivity of sample 2 is lower than that of sample 1 and slightly decreases with increasing frequency, which reflects the differences in the surface profiles and $R_{zjis}$ values.

In Fig. 8(c), the associated uncertainty with the coverage factor $k = 2$ is shown as error bars. The uncertainty of the conductivity $U(\sigma^{\text{rough}})$ is evaluated by considering the uncertainty propagation for $t, f_r, Q_u^{\text{rough}}, Q_u$, and $\sigma$, on the basis of the sensitivity analysis. $U(\sigma^{\text{rough}})$ is found to be in the range of 10%–20% except for the first measurement point. Similar to the case of $U(\tan \delta)$, large $U(\sigma^{\text{rough}})$ values of 48% and 45% for samples 1 and 2, respectively, at the first measurement point originate from the degraded signal-to-noise ratio at the first resonance. $U(\sigma^{\text{rough}})$ would be reduced by strengthening the resonator coupling with a decreased excitation hole length $M$.

> **[Fig. 8の説明]:**
> (a) 2つの銅箔サンプルの粗化面の走査型電子顕微鏡（SEM）画像。サンプル1とサンプル2の表面形状の違いが示されている。
> (b) 銅箔サンプル（サンプル1）の粗化面と未粗化面の写真。
> (c) 測定された導電率（Conductivity, S/m）と関連する不確かさ。周波数（100〜180 GHz）に対してプロットされている。サンプル1（赤）は約$4 \times 10^7$ S/mでほぼ一定、サンプル2（青）は約$2.5 \times 10^7$ S/mで周波数と共にわずかに減少している。

## VI. CONCLUSION

In this study, a BCDR using waveguide interfaces for an excitation mechanism has been proposed to extend the applicable frequency of the BCDR with a structure that alleviates the robustness issues exist in conventional BCDR structures having coaxial-line interfaces. To demonstrate this approach, a BCDR with WR-6 waveguide interfaces has been developed. The selective excitation for the $\text{TM}_{0m0}$ modes in the developed BCDR has been confirmed both numerically and experimentally, which enables broadband measurement capability of the developed resonator for material characterization over the entire $D$-band. Moreover, a modified analysis has been proposed for the BCDR based on the full-wave circuit modal analysis, where the entire resonator structure is divided into three simple elements characterized by admittance matrices. Full-wave simulations and experimental measurements have revealed that the proposed analysis is more accurate than the conventional analysis in determining the relative permittivity. The effectiveness of the proposed analysis becomes particularly pronounced for high-dielectric or thick samples, for which the conventional analysis becomes inaccurate owing to the radial radiation through the dielectric sample. To experimentally demonstrate the developed BCDR and proposed modal analysis, the complex permittivity of the COP, PTFE, and PFA samples and the conductivity of the two copper foil samples with different surface roughnesses have been measured in the $D$-band with uncertainty evaluations. The developed resonator system can contribute to the development of advanced substrate materials for 6G applications. Future research includes the realization of a BCDR with WR-3 waveguide interfaces that is applicable for material characterization up to 300 GHz as well as the extension of the circuit modal analysis to the nonsymmetrical case of the BCDR to investigate the effect of the differences between dielectric sheet pair on the measurements.

## ACKNOWLEDGMENT

The author would like to thank JX Nippon Mining and Metals Corporation for providing the copper foil samples used for the conductivity measurements and their surface profile data.

## REFERENCES

[1] T. S. Rappaport et al., “Wireless communications and applications above 100 GHz: Opportunities and challenges for 6G and beyond,” *IEEE Access*, vol. 7, pp. 78729–78757, 2019.
[2] I. F. Akyildiz, A. Kak, and S. Nie, “6G and beyond: The future of wireless communications systems,” *IEEE Access*, vol. 8, pp. 133995–134030, 2020.
[3] W. Saad, M. Bennis, and M. Chen, “A vision of 6G wireless systems: Applications, trends, technologies, and open research problems,” *IEEE Netw.*, vol. 34, no. 3, pp. 134–142, May 2020.
[4] G. Gold and K. Helmreich, “A physical surface roughness model and its applications,” *IEEE Trans. Microw. Theory Techn.*, vol. 65, no. 10, pp. 3720–3732, Oct. 2017.
[5] K. Lomakin, G. Gold, and K. Helmreich, “Analytical waveguide model precisely predicting loss and delay including surface roughness,” *IEEE Trans. Microw. Theory Techn.*, vol. 66, no. 6, pp. 2649–2662, Jun. 2018.
[6] A. E. Olk, P. E. M. Macchi, and D. A. Powell, “High-efficiency refracting millimeter-wave metasurfaces,” *IEEE Trans. Antennas Propag.*, vol. 68, no. 7, pp. 5453–5462, Jul. 2020.
[7] Y. Kato, K. Omori, and A. Sanada, “D-band perfect anomalous reflectors for 6G applications,” *IEEE Access*, vol. 9, pp. 157512–157521, 2021.
[8] J. Krupka, A. P. Gregory, O. C. Rochard, R. N. Clarke, B. Riddle, and J. Baker-Jarvis, “Uncertainty of complex permittivity measurements by split-post dielectric resonator technique,” *J. Eur. Ceram. Soc.*, vol. 21, no. 15, pp. 2673–2676, Jan. 2001.
[9] M. D. Janezic, E. F. Kuester, and J. B. Jarvis, “Broadband complex permittivity measurements of dielectric substrates using a split-cylinder resonator,” in *IEEE MTT-S Int. Microw. Symp. Dig.*, vol. 3, Jun. 2004, pp. 1817–1820.
[10] J. Krupka and J. Mazierska, “Contactless measurements of resistivity of semiconductor wafers employing single-post and split-post dielectric-resonator techniques,” *IEEE Trans. Instrum. Meas.*, vol. 56, no. 5, pp. 1839–1844, Oct. 2007.
[11] J. Krupka, “Measurements of the complex permittivity of low loss polymers at frequency range from 5 GHz to 50 GHz,” *IEEE Microw. Wireless Compon. Lett.*, vol. 26, no. 6, pp. 464–466, Jun. 2016.
[12] H. Kawabata and Y. Kobayashi, “The analysis of a balanced-type circular disk resonator excited by coaxial cable lines to measure the complex permittivity,” in *Proc. APMC. Asia-Pacific Microw. Conf.*, 2001, pp. 1322–1325.
[13] H. Kawabata, K.-I. Hasuike, Y. Kobayashi, and Z. Ma, “Multi-frequency measurements of complex permittivity of dielectric plates using higher-order modes of a balanced-type circular disk resonator,” in *Proc. Eur. Microw. Conf.*, Manchester, U.K., Sep. 2006, pp. 388–391.
[14] Y. Kato and M. Horibe, “Permittivity measurements and associated uncertainties up to 110 GHz in circular-disk resonator method,” in *Proc. 46th Eur. Microw. Conf. (EuMC)*, London, U.K., Oct. 2016, pp. 1139–1142.
[15] Y. Kato and M. Horibe, “Broadband permittivity measurements up to 170-GHz using balanced-type circular-disk resonator excited by 0.8-mm coaxial line,” *IEEE Trans. Instrum. Meas.*, vol. 68, no. 6, pp. 1796–1805, Jun. 2019.
[16] Y. Kato and M. Horibe, “Broadband conductivity measurement technique at millimeter-wave bands using a balanced-type circular disk resonator,” *IEEE Trans. Microw. Theory Techn.*, vol. 69, no. 1, pp. 861–873, Jan. 2021.
[17] K. Tanabe, Y. Kobayashi, and S. Tanaka, “Numerical analysis of eigenvalue solution of disk resonator (short papers),” *IEEE Trans. Microw. Theory Techn.*, vol. MTT-23, no. 6, pp. 508–511, Jun. 1975.
[18] F. L. Penaranda-Foix, J. M. Catala-Civera, A. J. Canos-Marin, and B. Garcia-Banos, “Circuital analysis of a coaxial re-entrant cavity for performing dielectric measurement,” in *IEEE MTT-S Int. Microw. Symp. Dig.*, Jun. 2009, pp. 1309–1312.
[19] F. L. Penaranda-Foix, M. D. Janezic, J. M. Catala-Civera, and A. J. Canos, “Full-wave analysis of dielectric-loaded cylindrical waveguides and cavities using a new four-port ring network,” *IEEE Trans. Microw. Theory Techn.*, vol. 60, no. 9, pp. 2730–2740, Sep. 2012.
[20] D. Marqués-Villarroya, F. L. Peñaranda-Foix, B. García-Baños, J. M. Catalá-Civera, and J. D. Gutiérrez-Cano, “Enhanced full-wave circuit analysis for modeling of a split cylinder resonator,” *IEEE Trans. Microw. Theory Techn.*, vol. 65, no. 4, pp. 1191–1202, Apr. 2017.
[21] D. Marques-Villarroya, A. J. Canós, F. L. Peñaranda-Foix, B. Garcia-Baños, and J. M. Catalá-Civera, “Full-wave modal analysis of a novel dielectrometer for accurate measurement of complex permittivity of high-loss liquids at microwave frequencies,” *IEEE Trans. Microw. Theory Techn.*, vol. 66, no. 12, pp. 5760–5770, Dec. 2018.
[22] J. R. Sánchez et al., “Characterization of nematic liquid crystal at microwave frequencies using split-cylinder resonator method,” *IEEE Trans. Microw. Theory Techn.*, vol. 67, no. 7, pp. 2812–2820, Jul. 2019.
[23] T. M. Hirvonen, P. Vainikainen, A. Lozowski, and A. V. Raisanen, “Measurement of dielectrics at 100 GHz with an open resonator connected to a network analyzer,” *IEEE Trans. Instrum. Meas.*, vol. 45, no. 4, pp. 780–786, Aug. 1996.
[24] H. Chen, H. Chen, W. Che, S. Zheng, X. Xiu, and Q. Xue, “Review and modification of permittivity measurement on open resonator for transparent material measurements at terahertz,” *IEEE Trans. Instrum. Meas.*, vol. 69, no. 11, pp. 9144–9156, Nov. 2020.
[25] B. Salski, J. Cuper, T. Karpisz, P. Kopyt, and J. Krupka, “Complex permittivity of common dielectrics in 20–110 GHz frequency range measured with a Fabry–Pérot open resonator,” *Appl. Phys. Lett.*, vol. 119, no. 5, Aug. 2021, Art. no. 052902.
[26] Y. Kato, “Material characterizations in the D-band using a balanced-type circular disk resonator with waveguide interfaces,” in *Proc. Conf. Precis. Electromagn. Meas. (CPEM)*, Wellington, New Zealand, Dec. 2022, pp. 1–2.
[27] N. Marcuvitz, *Waveguide Handbook*. New York, NY, USA: McGraw-Hill, 1951.
[28] J. E. E. Baglin, “Interface design for thin film adhesion,” in *Fundamentals of Adhesion*, L.-H. Lee, Ed. Boston, MA, USA: Springer, 1991, pp. 363–382.
[29] C.-Y. Lee et al., “Effects of nodule treatment of rolled copper on the mechanical properties of the flexible copper-clad laminate,” *Microelectron. Eng.*, vol. 84, no. 11, pp. 2653–2657, Nov. 2007.
[30] P. G. Huray, O. Oluwafemi, J. Loyer, E. Bogatin, and X. Ye, “Impact of copper surface texture on loss: A model that works,” *DesignCon*, vol. 1, pp. 462–483, Jun. 2010.

**Yuto Kato** (Member, IEEE) received the B.S. and M.S. degrees in physics from The University of Tokyo, Tokyo, Japan, in 2010 and 2012, respectively, and the Ph.D. degree from Osaka University, Toyonaka, Japan, in 2020.
Since 2012, he has been with the National Metrology Institute of Japan, National Institute of Advanced Industrial Science and Technology, Tsukuba, Japan. His current research interests include material characterizations and electromagnetic metasurfaces at microwave and millimeter-wave frequencies.
Dr. Kato is an Associate Editor of IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT.