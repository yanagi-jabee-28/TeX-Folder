1796 IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 68, NO. 6, JUNE 2019

# Broadband Permittivity Measurements up to 170-GHz Using Balanced-Type Circular-Disk Resonator Excited by 0.8-mm Coaxial Line

**Yuto Kato**, *Member, IEEE*, and **Masahiro Horibe**, *Senior Member, IEEE*

---

**Abstract— This paper describes the broadband permittivity measurements up to 170 GHz of plate samples by using a balanced-type circular-disk resonator (BCDR) excited by a 0.8-mm coaxial line. Because only the $\text{TM}_{0m0}$ modes are selectively excited in the BCDR and their resonant frequencies largely change by changing the size of the circular disk that constitutes the resonator, the BCDR method provides permittivity measurements at an almost arbitrary frequency across a wideband. We have increased the maximum measurable frequency of the BCDR method to 170 GHz by developing a BCDR excited by a 0.8-mm coaxial line and by improving the analysis method. We demonstrated that highly stable and rather simple permittivity measurements up to 170 GHz can be realized by the BCDR method by confirming that the measured complex permittivities of a low-loss material from 11.3 to 167 GHz at 59 frequency points obtained with five circular disks of different radii are consistent within the uncertainties.**

**Index Terms— Millimeter-wave, mode-matching analysis, permittivity measurements, resonator method, uncertainty.**

---

## I. INTRODUCTION

THE accurate measurement of complex permittivity is essential to the design of microwave circuits and devices. The knowledge of the permittivity of low-loss materials is of utmost importance to engineers designing transmission lines. Permittivity measurements at millimeter frequencies are becoming increasingly important with the growing demand for millimeter-wave applications, including automotive radars and next-generation wireless communications (WiGig). In addition, it is necessary to know the broadband material properties for the design of digital signal transmissions.

For permittivity measurements in the millimeter-wave band, free-space transmission/reflection methods using antennas can be used for high-loss materials [1]–[3], but they have insufficient sensitivity in determining the loss tangent of low-loss materials. On the other hand, resonant methods can provide accurate permittivity measurements of low-loss materials [4]–[6], but there are some problems with applying them at millimeter frequencies. First, as the frequency of the fundamental mode of the resonator increases, the dimensions of the resonator and the sample inserted into it become smaller in inverse proportion to the frequency; thus, the resonator and sample cannot be machined with sufficient accuracy when the frequency of the fundamental mode reaches the millimeter- and submillimeter-wave bands. Second, when the higher order modes of the resonator are used for permittivity measurements, the interference effect or mode identification error caused by overlaps with other unwanted modes can cause a large error in the measurement results. Open resonator methods [7]–[9] are superior to typical closed resonator methods in the millimeter-wave band because they can evaluate planar samples without requiring a specific diameter or cross-sectional shape, and their resonant spectra are less dense than those of typical closed resonators. However, it should be pointed out that open resonators have disadvantages over closed resonators in that they are larger in size and sensitive to vibrations and ambient environmental changes such as temperature. Furthermore, although their modes are sparser than those of typical closed resonators of similar size, open resonator methods still suffer from the interference problem, in which higher order resonant $\text{TEM}_{lmn}$ modes can overlap with the fundamental $\text{TEM}_{00n}$-mode that is used for the measurements.

To overcome these issues, a multifrequency measurement method for the complex permittivity of low-loss materials has been proposed that utilizes the higher order modes of a balanced-type circular-disk resonator (BCDR) [10]–[15]. The BCDR method has two noteworthy features. First, it can provide broadband permittivity measurements from less than 20 GHz up to over 100 GHz with a single resonator because only the $\text{TM}_{0m0}$ modes are selectively excited in the resonator. Second, the resonant frequency of each mode in the BCDR can be drastically changed by altering the size of a single expendable part of the resonator, namely, the circular disk. These features indicate that the broadband permittivity measurements at almost arbitrary frequency points can be performed by using this method with a single resonator and expendable parts. We have experimentally demonstrated the frequency variability of the BCDR method up to 70 GHz by measuring the relative permittivity ($\epsilon_r$) and loss tangent ($\tan \delta$) of the same low-loss dielectric sample by the BCDR method with multiple circular disks of different radii [15].

Manuscript received July 10, 2018; revised October 10, 2018; accepted November 17, 2018. Date of publication January 11, 2019; date of current version May 10, 2019. The Associate Editor coordinating the review process was Djamel Allal. *(Corresponding author: Yuto Kato.)*
The authors are with the National Metrology Institute of Japan, National Institute of Advanced Industrial Science and Technology, Tsukuba 305-8563, Japan (e-mail: y-katou@aist.go.jp).
Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TIM.2018.2886864

0018-9456 © 2019 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

---

In the future, the operating frequencies of communication and radar technologies are expected to further increase up to $D$-band frequencies (110–170 GHz) to realize an increased data rate. A 120-GHz band wireless transmission system has been studied for next-generation ultrahigh-definition television broadcasting [16]. Recently, a CMOS 140-GHz radar on-chip system with integrated antennas using standard 28-nm technology has been developed for radar-based sensor applications [17]. In order to promote the development of these emerging technologies and counter spurious radiation in existing millimeter-wave applications, it is necessary to develop an accurate permittivity measurement technique up to the $D$-band.

The maximum measurable frequency of the BCDR method is limited by the following three cutoff frequencies: 1) cutoff frequency of the coaxial lines used to excite the resonator $f_c^{\text{Coax}}$; 2) that of the excitation holes $f_c^{\text{Hole}}$; and 3) that for the radial radiation through the dielectric samples $f_c^{\text{Rad}}$. $f_c^{\text{Hole}}$ can be designed to be much higher than the other two frequencies, and for low-dielectric and thin samples, $f_c^{\text{Coax}}$ determines the maximum measurable frequency of the BCDR method. For example, $f_c^{\text{Rad}}$ is 230 GHz for a sample of $\epsilon_r = 2$ and thickness $t = 0.2$ mm [see (1)], whereas $f_c^{\text{Coax}}$ is 133 GHz for a 1-mm coaxial airline. We developed the BCDR excited by a 1-mm coaxial line and demonstrated permittivity measurements up to 110 GHz [13], but this does not cover the entire $D$-band.

In this paper, we present a BCDR excited by a 0.8-mm coaxial line that can measure the complex permittivity up to 170 GHz. By changing the excitation line from a 1-mm coaxial line ($f_c^{\text{Coax}} = 133$ GHz) to a 0.8-mm coaxial line ($f_c^{\text{Coax}} = 166$ GHz), the BCDR method is now able for the first time to perform permittivity measurements in the entire $D$-band. In addition, we have developed an improved analytical formulation for determining the permittivity from the resonant frequency, where the effective radius of the circular disk is rigorously calculated by mode-matching analysis. We have clarified that this new analysis method is indispensable for accurate permittivity measurements with the BCDR method in the millimeter-wave band.

The remainder of this paper is organized as follows. The BCDR method and measurement system used in this paper are explained in Section II. The improved analysis for the BCDR method is introduced in Section III. The measurement results and uncertainty evaluation are discussed in Section IV, where we demonstrate the usefulness of the proposed analysis and verify the frequency variability of the BCDR method up to 170 GHz by measuring the same low-loss dielectric sample using the BCDR with five circular disks of different radii. The validity of the proposed analysis method is verified by full-wave electromagnetic simulations in Section V, where we investigate the effect of the shim used in the experiments to ensure the alignment of the circular disk in the resonator. The BCDR method is used to measure a pair of dielectric plate samples with the same thickness and dielectric properties. The effect of differences in the sample pair is considered in Section VI. Finally, conclusions are presented in Section VII.

> **[Figure 1]:** (a) and (b) Photographs and (d) schematic of the BCDR used in this paper. (c) Five circular disks with different radii ($2R = 9$, 12, 15, 18, and 21 mm).
> *   **(a):** Shows the BCDR excited by a 0.8-mm coaxial line. Components visible: Alignment shim, Conductor disk, Sample pair.
> *   **(b):** Shows the measurement setup with waveguides connected.
> *   **(c):** Shows five copper circular disks of varying sizes.
> *   **(d):** Schematic diagram showing the cross-section. A circular conductor disk (thickness $t_c$, diameter $2R$) is sandwiched between two dielectric plates (thickness $t$). These are sandwiched between two conductor plates. Excitation holes (diameter $2a$) are at the center, fed by 0.8-mm coaxial lines.

## II. MEASUREMENT SYSTEM

### A. BCDR

Photographs and schematics of the BCDR are shown in Fig. 1. A thin circular conductor disk with the thickness $t_c = 0.06$ mm is sandwiched between a pair of dielectric plate samples to be measured. The dielectric samples are sandwiched between two parallel conductor plates. The resonator is excited and detected by 0.8-mm coaxial lines through excitation holes of diameter $2a = 0.93$ mm and length $M = 1.5$ mm located at the center of the resonator. Only the $\text{TM}_{0m0}$ modes are selectively excited because they have an electric field at the center of the resonator. The complex permittivity at each resonant frequency is determined from the measured values of the resonant frequency and unloaded $Q$-factor for the $\text{TM}_{0m0}$ modes by considering the resonant condition of the BCDR, which will be explained in detail in Section III.

We prepare five circular disks of different sizes with the diameters $2R = 9$, 12, 15, 18, and 21 mm, as shown in Fig. 1(c). The resonant frequencies of the BCDR can be drastically changed simply by switching in disks with different diameters. Fig. 2 shows the relationship between the resonant frequency $f_{0m0}$ for the $\text{TM}_{0m0}$ modes and the relative permittivity $\epsilon_r$ of a sample with the thickness $t = 0.2$ mm for the BCDR used in this paper ($2a = 0.93$ mm and $M = 1.5$ mm) with the five circular disks. It can be seen from Fig. 2 that the resonant frequencies of the BCDR and the resonant frequency interval between adjacent modes largely depend on the diameter of the circular disk. Therefore, the relative permittivity and loss tangent can be measured at various frequency points by using multiple circular disks of different radii. Note that the dashed lines in Fig. 2 signify the cutoff frequencies $f_c^{\text{Rad}}$ at which the radiation of the electric field in the radial direction through the sample becomes prominent, as given in [10]

$$
f_c^{\text{Rad}} = \frac{c}{4(t + t_c/2)\sqrt{\epsilon_r}} \quad (1)
$$

> **[Figure 2]:** Relationship between the resonant frequencies and relative permittivity $\epsilon_r$ of a sample with the thickness $t$ of 0.2 mm for the BCDR used in this paper ($2a = 0.93$ mm and $M = 1.5$ mm) with five circular disks of $2R = 9$, 12, 15, 18, and 21 mm and $t_c = 0.06$ mm.
> The graph plots Permittivity (y-axis, range 2-6) vs Frequency (x-axis, range 0-160 GHz).
> Curves represent different modes for each disk diameter.
> Dashed lines indicate the cutoff frequency $f_c^{\text{Rad}}$.
> Smaller disks ($2R=9$ mm) cover higher frequencies, while larger disks ($2R=21$ mm) cover lower frequencies with denser mode spacing.

where $c$ is the velocity of light in free space. $f_c^{\text{Rad}}$ is higher than 170 GHz for samples with $t = 0.2$ mm and $\epsilon_r < 3.67$.

The alignment between the circular disk and excitation holes is critical for measuring the complex permittivity with high accuracy. To ensure this alignment, we use a donut-shaped thin film made of the cyclic olefin polymer (COP) with the thickness of 0.05 mm as a shim [not shown in Fig. 1(d) for clarity]. We can find the misalignment by detecting resonances of unwanted modes because the misalignment not only shifts the resonant frequencies of the $\text{TM}_{0m0}$ modes but also excites other unwanted modes. In the measurement results shown in Section IV-A, the resonances for unwanted modes are much smaller than those for adjacent $\text{TM}_{0m0}$ modes, i.e., by 10 dB or more.

### B. Samples Under Test and S-Parameter Measurement Systems

In this paper, we measure one low-loss sample and one middle-loss sample: COP (ZF16, Zeon) with $t = 0.251$ mm and a glass-reinforced hydrocarbon/ceramic material with $t = 0.2542$ mm (RO4350B, Rogers), respectively.

$S_{21}$ of the BCDR for the two samples is measured from 5 to 70 GHz with Keysight vector network analyzer (VNA) N5227A at a 100-Hz IF bandwidth, where the resonator and VNA are connected by 1.85-mm coaxial cables and adapters. After we measure the entire band at 6501 frequency points, we perform high-resolution measurements near each resonant frequency at the interval of 1 MHz by using the segment mode of N5227A in order to accurately obtain the resonant parameters [18].

> **[Figure 3]:** Schematics of the analysis geometries of the BCDR used for (a) considering the effect of the excitation hole and (b) determining the effective radius of the circular disk.
> *   **(a):** Shows a cross-section of half the resonator (due to symmetry). Region I is the dielectric sample between the conductor plate and the center plane. Region II is the excitation hole (air). Boundary conditions: Magnetic wall at $r = R + \Delta R$, Electric or Magnetic wall at $z = -M$.
> *   **(b):** Shows the geometry for determining $\Delta R$. Region I (dielectric) is $0 \le z \le t$. Region III (dielectric) is $t \le z \le t + t_c/2$. The excitation hole is ignored ($a \ll R$).

The low-loss COP sample is measured from above 70 GHz up to 170 GHz. For S-parameter measurements higher than 70 GHz, we use the Keysight VNA N5222A with OML frequency multipliers and waveguide to 0.8-mm coaxial adapters to connect them to the resonator [see Fig. 1(b)]. $W$-band and $D$-band waveguide measurement systems are used from 70 to 110 GHz and from 110 to 170 GHz, respectively. The frequency interval and IF bandwidth of both measurements are 10 MHz and 500 Hz, respectively.

## III. IMPROVED ANALYSIS FOR THE BCDR METHOD

The analysis geometry of the BCDR with the excitation hole is shown in Fig. 3(a). Region I represents the dielectric sample, and region II represents the excitation hole (air). Because of the symmetrical structure of the BCDR, we only need to consider half of it. By assuming the magnetic wall condition at the boundary of region I at $r = R + \Delta R$ and the electric or magnetic wall condition at the top of the coaxial line at $z = -M$ in region II, the resonant condition can be derived from mode-matching analysis and is represented by the following characteristic equation [10], [11]:

$$
\text{det}H(\epsilon_r, f_{0m0}, t, R + \Delta R, a, M) = 0 \quad (2)
$$

where the matrix components are given in [10]. It was found from the calculation that the terminal conditions of the boundary of region II have negligibly small effect on the resonant condition [10] and we assume the electric wall condition in the subsequent analyses.

The relative permittivity $\epsilon_r$ is derived from the measured resonant frequency and dimensional parameters by solving (2). The loss tangent $\tan \delta$ is obtained from the unloaded $Q$-factor of the BCDR resonator $Q_u$ by using the following equation:

$$
\tan \delta = \left( \frac{1}{Q_u} - \frac{1}{Q_c} \right) \left( 1 + \frac{W_1}{W_2} \right) \quad (3)
$$

where $Q_c$ is the $Q$-factor due to the conductor loss. $W_1$ and $W_2$ are the electric energies stored in the dielectric region (region I) and excitation hole region (region II), respectively. $W_1$ and $W_2$ can be calculated from mode-matching analysis [19], and $Q_c$ can be approximated by [10]

$$
Q_c = \frac{t}{\delta_s} = t\sqrt{\pi f_{0m0} \mu_0 \sigma} \quad (4)
$$

where $\delta_s$ is the skin depth of the conductor in the conductor wall, $\sigma$ is the conductivity, and $\mu_0$ is the permeability of free space.

The boundary of region I is located at $r = R + \Delta R$, which is larger than the radius of the circular disk $R$ by $\Delta R$ because of the effect of the fringing field at the disk edge. In previous studies on the BCDR method, the following approximate expression for $\Delta R$, derived based on the electrostatic theory, was utilized [12], [20]

$$
\Delta R = \frac{t}{\pi} \left[ \frac{2b}{t} \ln \left( \frac{b}{t} + 1 \right) - \left( \frac{b}{t} - 1 \right) \ln \left\{ \left( \frac{b}{t} \right)^2 - 1 \right\} \right] \quad (5)
$$

where $b = t + t_c/2$. As clarified later, this formula is only valid for lower order modes, and the relative permittivity derived from (2) and (5) deviates from that of the sample $\epsilon_r$ for higher order modes.

To make it possible to determine the relative permittivity with high accuracy by the BCDR method with higher order $\text{TM}_{0m0}$ modes, we derive a new analytical formulation that rigorously calculates $\Delta R$ by using mode-matching analysis. To determine $\Delta R$, we consider the analysis geometry shown in Fig. 3(b), where the excitation hole is ignored because $a \ll R$. Note that we assume all of regions I and III are filled with the dielectric material to be measured ($\epsilon_r, \tan \delta$), whereas an actual sample has a finite size ($>5R$ in this paper) and $t < z < t + t_c/2$ in region III is actually not occupied by a sample but by a donut-shaped shim and air. This assumption may not be acceptable for high-permittivity samples and is verified by the full-wave electromagnetic simulations described in Section V.

From the symmetry of the BCDR and the assumption that the electric field at the center of the resonator is nonzero, the electric Hertz vectors in regions I and III have only $z$-components of the form

$$
\Phi_{\text{I}} = \sum_{p=1}^{\infty} A_p J_0(k_{\text{I}p}r) \cos[\beta_{\text{I}p}(z - t)] \quad (6)
$$

$$
\Phi_{\text{III}} = \sum_{q=1}^{\infty} B_q K_0(\alpha_{\text{III}q}r) \cos(\beta_{\text{III}q} z) \quad (7)
$$

where $A_p$ and $B_q$ are the expansion coefficients, $J_n$ is the Bessel function of the first kind of order $n$, $K_n$ is the modified Bessel function of the second kind of order $n$, and

$$
k_{\text{I}p}^2 = \epsilon_r k_0^2 - \beta_{\text{I}p}^2, \quad \alpha_{\text{III}q}^2 = -\epsilon_r k_0^2 + \beta_{\text{III}q}^2 \quad (8)
$$

where $k_0 = 2\pi f_{0m0}/c$.

The field components in regions I ($E_r^{\text{I}}, E_z^{\text{I}}, H_\theta^{\text{I}}$) and III ($E_r^{\text{III}}, E_z^{\text{III}}, H_\theta^{\text{III}}$) are calculated from the electric Hertz vectors. From the electric and magnetic wall conditions on the boundaries of regions I and III, respectively, $E_r^{\text{I}}(r, z = 0) = 0$ and $H_\theta^{\text{III}}(r, z = t + t_c/2) = 0$; thus

$$
\beta_{\text{I}p} = \frac{\pi}{t}(p - 1), \quad p = 1, 2, \cdots \quad (9)
$$

$$
\beta_{\text{III}q} = \frac{\pi}{t + t_c/2} \left( q - \frac{1}{2} \right), \quad q = 1, 2, \dots \quad (10)
$$

Imposing the boundary condition that $E_z$ and $H_\theta$ be continuous at $r = R$ gives

$$
E_z(z) = E_z^{\text{I}}(r = R, z) = E_z^{\text{III}}(r = R, z) \quad (11)
$$

$$
H_\theta(z) = H_\theta^{\text{I}}(r = R, z) = H_\theta^{\text{III}}(r = R, z). \quad (12)
$$

By applying the orthogonality of the cosine functions, we obtain the following integral equation:

$$
\frac{J_1(k_{\text{I}p}R)}{k_{\text{I}p} J_0(k_{\text{I}p}R)} \int_0^t E_z(z) \cos(\beta_{\text{I}p}z) dz = \sum_{q=1}^{\infty} \frac{K_1(\alpha_{\text{III}q}R)}{\alpha_{\text{III}q} K_0(\alpha_{\text{III}q}R)} \frac{2}{t + t_c/2} P_{pq} \times \int_0^t E_z(z) \cos(\beta_{\text{III}q}z) dz \quad (13)
$$

where

$$
P_{pq} = \frac{(-1)^p \beta_{\text{III}q}}{\beta_{\text{III}q}^2 - \beta_{\text{I}p}^2} \sin(\beta_{\text{III}q}t). \quad (14)
$$

To solve (13) with the Ritz–Galerkin method, $E_z(z)$ is expressed by the following sum of a series:

$$
E_z(z) = \begin{cases} \displaystyle \sum_{l=1}^{\infty} E_l \cos(\beta_{\text{I}l}z), & (0 \le z \le t) \\ 0, & (t \le z \le t + t_c/2). \end{cases} \quad (15)
$$

By substituting (15) into (13), we obtain $[G_{lp}][E_l] = [0]$, where the matrix elements $G_{lp}$ are given by

$$
G_{lp} = \delta_{lp}(1 + \delta_{p1}) \frac{t J_1(k_{\text{I}p}R)}{2k_{\text{I}p} J_0(k_{\text{I}p}R)} + \sum_{q=1}^{\infty} \frac{K_1(\alpha_{\text{III}q}R)}{\alpha_{\text{III}q} K_0(\alpha_{\text{III}q}R)} \frac{2}{t + t_c/2} P_{pq} P_{lq} \quad (16)
$$

where $\delta_{lp}$ is the Kronecker delta. Thus, the resonant condition is given by the following characteristic equation:

$$
\text{det}G(\epsilon_r, f_{0m0}, t, t_c, R) = 0. \quad (17)
$$

We let $\epsilon_r^G(f_{0m0}, t, t_c, R)$ be the relative permittivity obtained by solving (17). Note that $\epsilon_r^G$ deviates from the relative permittivity of the sample $\epsilon_r$ because of the effect of the excitation hole. We define the effective radius of the circular disk $R^G$ enlarged by the fringing field by the following formula [19]:

$$
R^G = R + \Delta R = \frac{2\pi f_{0m0} \sqrt{\epsilon_r^G}}{c x_{0m}} \quad (18)
$$

where $x_{0m}$ is the $m$th root of $J_0'(x) = 0$. The relative permittivity $\epsilon_r$ is determined by substituting $\Delta R$ obtained from (18) into (2).

## IV. MEASUREMENT RESULTS AND UNCERTAINTY EVALUATION

### A. Measurement Results of Resonant Traces

Fig. 4 shows $S_{21}$ of the BCDR with circular disks of $2R = 9$, 12, 15, 18, and 21 mm for the COP sample from 5 to 170 GHz and for the RO4350B sample from 5 to 70 GHz. $f_{0m0}$ is indicated by downward arrows. We can confirm from Fig. 4 that $\text{TM}_{0m0}$ mode resonances are clearly observed and other resonances are sufficiently suppressed for all circular disks up to 170 and 70 GHz for the COP and RO4350B samples, respectively.

> **[Figure 4]:** Measured $S_{21}$ of the BCDR with circular disks of $2R = 9$, 12, 15, 18, and 21 mm for the (a) COP sample from 5 to 170 GHz and (b) RO4350B sample from 5 to 70 GHz. The resonant frequencies for the $\text{TM}_{0m0}$ modes are indicated by downward arrows.
> *   **(a):** COP sample. The graph shows multiple resonant peaks across the 5-170 GHz range. Different colors correspond to different disk diameters. The noise floor is around -80 to -100 dB.
> *   **(b):** RO4350B sample. Similar graph for 5-70 GHz.

> **[Figure 5]:** Measurement results of the relative permittivity with the BCDR method according to three different analyses. (a) COP. (b) RO4350B.
> *   **(a):** COP Permittivity vs Frequency (0-160 GHz).
>     *   Blue circles: Eq. (2) with Eq. (18) (Proposed). Flat around 2.33.
>     *   Red triangles: Eq. (2) with Eq. (5) (Conventional). Increases with frequency.
>     *   Green squares: Eq. (17) (No hole consideration). Lower values.
> *   **(b):** RO4350B Permittivity vs Frequency (0-60 GHz).
>     *   Similar trends. Proposed method yields flat permittivity around 3.4.

### B. Comparison of Analyses

To demonstrate that the proposed analysis derived in Section III is superior to the conventional analysis, we calculate the relative permittivity of the COP and RO4350B samples from the measurement results of $f_{0m0}$ for the BCDR with the circular disk of $2R = 18$ mm according to the following three analyses.
1) Equation (2) with (18) (proposed analysis considering the excitation hole).
2) Equation (2) with (5) (conventional analysis considering the excitation hole).
3) Equation (17) (analysis without considering the excitation hole).

The results are summarized in Fig. 5. We can see from the figure that the relative permittivity obtained from (17) ($= \epsilon_r^G$) is lower than those corresponding to the other two analyses, especially for higher order modes. This suggests that the relative permittivity is underestimated when the excitation hole is not considered. The comparison of the results obtained from (2) with different $\Delta R$ of each sample show that they are nearly equal at lower frequencies (i.e., lower order modes). At higher frequencies (i.e., over 70 GHz for the COP sample and over 50 GHz for the RO4350B sample), the relative permittivity derived with $\Delta R$ from (5) increases with the frequency, whereas the derived relative permittivity with $\Delta R$ from (18) is almost flat or slightly decreases over the entire frequency range for both samples. Because the relative permittivity generally decreases as the frequency increases at microwave and millimeter-wave frequencies [21], we can conclude that the relative permittivity can be obtained with higher accuracy by using the proposed analysis in the millimeter-wave range. Note that the difference in $\Delta R$ [ (18) or (5)] has little effect on the calculation of the loss tangent with (3).

### C. Uncertainty Evaluation

The uncertainties of the relative permittivity and loss tangent are evaluated by considering the uncertainty propagations of the measured quantities: the resonant frequency $f_{0m0}$, $Q$-factor $Q_u$, sample thickness $t$, radius $R$ and thickness $t_c$ of the circular disk, radius $a$ and length $M$ of the excitation hole, and conductivity of the conductor wall of the resonator $\sigma$. We also consider the effect of the finiteness of the number of terms used in the mode-matching analysis when solving (2) (relative convergence error). The uncertainty evaluation of each quantity is discussed in the following.

1) *Resonant Frequency and Q-Factor:* The uncertainty sources for the resonant frequency and $Q$-factor are divided into three factors: uncertainty propagation of the uncertainty of $S_{21}$, measurement repeatability, and source resulting from the interval between discrete frequency points in measurements (frequency resolution). The uncertainty propagation of $u(S_{21})$ is evaluated using Monte Carlo calculations [18].

2) *Dimensional Parameters:* The nominal thickness and associated uncertainty are $t = 0.251 \pm 0.002$ mm for the COP sample and $t = 0.2542 \pm 0.0008$ mm for the RO4350B sample. The difference in thickness of the sample pair is less than 0.001 mm and is included in the thickness uncertainty.
We let the uncertainties of $R, t_c, a$, and $M$ be 0.0025, 0.002, 0.01, and 0.5 mm, respectively.

3) *Conductivity of the Conductor Wall:* The conductivity is measured with the two-dielectric resonator method [22] at 10 GHz, and the result is $\sigma = (5.63 \pm 0.18) \times 10^7$ S/m.

4) *Relative Convergence Error:* Mode-matching analysis becomes rigorous if an infinite number of terms is used in the series expansion. However, the actual calculations are performed with a finite number of terms $N$. We set $N = 100$ ($H$ is a $100 \times 100$ square matrix) to solve (2). As $N$ is increased, both $\epsilon_r$ and $\tan \delta$ change slightly, and we evaluate the relative convergence errors by the derivations of $\epsilon_r$ and $\tan \delta$ for $N = 100$ from those for $N = 50$.
We ignore the relative convergence error when solving (17) because it only affects $\Delta R$, and we conservatively set $u(R)$ as 0.0025 mm instead of rigorously evaluating the uncertainty of $\Delta R$.

### D. Measurement Results of the Complex Permittivity for Five Circular Disks

Fig. 6 shows the measurement results of $\epsilon_r$ and $\tan \delta$ for the COP and RO4350B samples obtained from the BCDR measurements with circular disks of $2R = 9$, 12, 15, 18, and 21 mm by using the proposed analysis introduced in Section III. $\epsilon_r$ and $\tan \delta$ are measured at 59 frequency points from 11.3 to 167 GHz for the COP sample and at 28 frequency points from 9.35 to 67.7 GHz for the RO4350B sample. We plot the measured values with two-sided 95% confidence intervals. We can confirm from the figure that the measurement results obtained using each circular disk are consistent with each other within the uncertainties for the two samples for all resonant modes, which strongly suggests the validity of the measurement system and analysis method. In addition, $\epsilon_r$ of the two samples is nearly flat over the entire frequency range, which also supports the adequacy of the measurement results.

> **[Figure 6]:** Relative permittivity, loss tangent, and their uncertainties (95% confidence interval) of the (a) COP and (b) RO4350B samples obtained from the BCDR measurements with circular disks of $2R = 9$, 12, 15, 18, and 21 mm.
> *   **(a) COP:**
>     *   Permittivity: Constant around 2.33 from 10 to 170 GHz.
>     *   Loss tangent: Increases from approx $3 \times 10^{-4}$ to $6 \times 10^{-4}$.
>     *   SCR method results (black crosses) at ~24 GHz match BCDR results.
> *   **(b) RO4350B:**
>     *   Permittivity: Constant around 3.4 from 10 to 70 GHz.
>     *   Loss tangent: Increases from approx $3 \times 10^{-3}$ to $4.5 \times 10^{-3}$.

**TABLE I**
UNCERTAINTY BUDGET OF $\epsilon_r$ AND $\tan \delta$ FOR THE COP SAMPLE AT 167 GHz MEASURED BY USING THE 10TH MODE RESONANCE OF THE BCDR WITH A CIRCULAR DISK OF $2R = 12$ mm. (NOMINAL VALUES: $\epsilon_r = 2.325, \tan \delta = 6.3 \times 10^{-4}$)

| Source of uncertainty | $u(f_{0m0})$ | $u(Q_u)$ | $u(t)$ | $u(t_c)$ | $u(R)$ | $u(a)$ | $u(M)$ | $u(\sigma)$ | $u(N)$ | Combined uncertainty |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Uncertainty of $\epsilon_r$ | $5.3 \times 10^{-4}$ | $-$ | $2.5 \times 10^{-3}$ | $1.6 \times 10^{-3}$ | $1.9 \times 10^{-3}$ | $3.2 \times 10^{-3}$ | $2.1 \times 10^{-5}$ | $-$ | $1.8 \times 10^{-3}$ | $5.1 \times 10^{-3}$ |
| | | | | | | | | | Expanded uncertainty ($k=2$) | $1.0 \times 10^{-2}$ |
| Uncertainty of $\tan \delta$ | $3.6 \times 10^{-8}$ | $9.6 \times 10^{-5}$ | $3.9 \times 10^{-6}$ | $1.3 \times 10^{-8}$ | $5.7 \times 10^{-9}$ | $1.3 \times 10^{-6}$ | $2.9 \times 10^{-8}$ | $1.1 \times 10^{-5}$ | $7.7 \times 10^{-7}$ | $9.7 \times 10^{-5}$ |
| | | | | | | | | | Expanded uncertainty ($k=2$) | $1.9 \times 10^{-4}$ |

To verify the measurement results of the COP sample, we measure the same sample with the split-cylinder resonator (SCR) method [18], [23], [24]. Note that the BCDR and SCR methods measure the complex permittivity normal and tangential to the plate sample, respectively. The COP sample is expected to be isotropic, whereas the RO4350B sample should have large anisotropy depending on the orientation of the glass fibers. Therefore, we compare the measurement results of the BCDR and SCR methods for the COP sample only. The resonant frequency for the $\text{TE}_{011}$ mode without a sample in the resonator is 23.89 GHz for the SCR used in this paper. The results are shown in Fig. 6(a) as black crosses. The results obtained by the two methods are confirmed to be consistent within the uncertainties.

Tables I and II present the uncertainty budgets of $\epsilon_r$ and $\tan \delta$ for the COP and RO4350B samples, respectively, at the highest measured frequency. These are 167 GHz for the COP sample, which is measured by using the 10th mode resonance of the BCDR with the circular disk of $2R = 12$ mm, and 67.7 GHz for the RO4350B sample, which is measured by using the sixth mode resonance of the BCDR with the circular disk of $2R = 15$ mm. The largest uncertainty source for the uncertainty of $\epsilon_r$ is the uncertainty of $a$ for both samples.

**TABLE II**
UNCERTAINTY BUDGET OF $\epsilon_r$ AND $\tan \delta$ FOR THE RO4350B SAMPLE AT 67.7 GHz MEASURED BY USING THE SIXTH MODE RESONANCE OF THE BCDR WITH A CIRCULAR DISK OF $2R = 15$ mm. (NOMINAL VALUES: $\epsilon_r = 3.404, \tan \delta = 4.3 \times 10^{-3}$)

| Source of uncertainty | $u(f_{0m0})$ | $u(Q_u)$ | $u(t)$ | $u(t_c)$ | $u(R)$ | $u(a)$ | $u(M)$ | $u(\sigma)$ | $u(N)$ | Combined uncertainty |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Uncertainty of $\epsilon_r$ | $5.6 \times 10^{-3}$ | $-$ | $6.0 \times 10^{-4}$ | $9.5 \times 10^{-4}$ | $2.3 \times 10^{-3}$ | $5.9 \times 10^{-3}$ | $3.4 \times 10^{-6}$ | $-$ | $4.2 \times 10^{-3}$ | $9.5 \times 10^{-3}$ |
| | | | | | | | | | Expanded uncertainty ($k=2$) | $1.9 \times 10^{-2}$ |
| Uncertainty of $\tan \delta$ | $4.3 \times 10^{-7}$ | $1.5 \times 10^{-4}$ | $3.1 \times 10^{-6}$ | $8.8 \times 10^{-9}$ | $9.0 \times 10^{-9}$ | $1.6 \times 10^{-6}$ | $7.5 \times 10^{-8}$ | $1.6 \times 10^{-5}$ | $5.4 \times 10^{-6}$ | $1.5 \times 10^{-4}$ |
| | | | | | | | | | Expanded uncertainty ($k=2$) | $3.1 \times 10^{-4}$ |

The second-largest source is the uncertainty of $t$ and that of $f_{0m0}$ for the COP and RO4350B samples, respectively. For the uncertainty of $\tan \delta$, the effects of the uncertainty of $Q_u$ dominates the total uncertainties for both samples.

We should note that the loss tangent of the COP sample increases with frequency and becomes flat at approximately 70 GHz. Then, it increases again, although this trend is almost within the range of the uncertainties. This result may be attributed to the reduction in the conductivity $\sigma$ with the frequency; we assume that $\sigma$ does not change from the value at 10 GHz over the entire frequency band. Another reason may be the difference between the thicknesses of the sample pair, as discussed in Section VI.

## V. NUMERICAL VERIFICATION OF THE PROPOSED ANALYSIS

We make three assumptions to construct the proposed analysis of the BCDR method. First, we solve the boundary condition problem for determining the relative permittivity by combining the two approximate analysis geometries shown in Fig. 3(a) and (b). Second, we assume that the circular disk is surrounded by the dielectric material to be measured, as shown in Fig. 3(b); in the experiments, the shim and air gap are actually placed between the upper and lower samples, as shown in Fig. 7(a). Third, we assume that the upper and lower samples are exactly the same in terms of the complex permittivity and thickness. Although the validity of the proposed analysis is experimentally verified by obtaining the reasonable measurement results, as discussed in Section IV-D, additional verification of the above-mentioned assumptions is required. The influences of the approximation on the analysis geometry and of the shim are discussed here, and the influence of the difference between the upper and lower samples is considered in Section VI.

> **[Figure 7]:** (a) Schematic of the analysis geometry of the BCDR used in the simulations. (b) Deviations in the simulated resonant frequencies normalized by the analyzed frequencies for the $\text{TM}_{0m0}$ modes. (c) Deviations in the analyzed sample permittivities normalized by the set values calculated from the simulated resonant frequencies of the $\text{TM}_{0m0}$ modes.
> *   **(a):** Shows the simulation model including the shim and air gap.
> *   **(b):** Graph of frequency deviation vs mode number.
> *   **(c):** Graph of permittivity deviation vs sample permittivity.

To investigate the influence of the assumptions on the analysis, we perform full-wave electromagnetic simulations with the HFSS eigenmode solver. In the simulations, dielectric samples with a relative permittivity of $\epsilon_r^{\text{sample}}$ and thickness of $t = 0.25$ mm are set in the BCDR used in this paper ($2a = 0.93$ mm and $M = 1.5$ mm), which has a circular disk of $2R = 18$ mm and $t_c = 0.06$ mm and a donut-shaped shim with a relative permittivity $\epsilon_r^{\text{shim}} = 2.3$ and thickness $t_s = 0.05$ mm [see Fig. 7(a)]. Note that an air gap of $t_c - t_s = 0.01$ mm exists between the upper and lower samples. Both loss tangents of the sample and shim and the conductor loss are assumed to be zero in order to reduce the computational time.

First, we consider the case of $\epsilon_r^{\text{sample}} = \epsilon_r^{\text{shim}}$ in order to focus on the effect of the air gap and approximate handling of the boundary condition problem. Table III presents the simulated resonant frequencies of the $\text{TM}_{0m0}$ modes ($m = 1, 2, \dots, 15$) for the case of $\epsilon_r^{\text{sample}} = \epsilon_r^{\text{shim}} = 2.3$. The analytically calculated results obtained from the proposed analysis are also presented in Table III. It can be seen from the table that the simulated results are consistent with the analyzed results within the numerical errors in the simulations. Therefore, we can conclude that the proposed analysis is sufficiently accurate up to 170 GHz for measurements using a shim with the same relative permittivity as the sample to be measured (cf. the measurements of the COP sample in this paper).

**TABLE III**
SIMULATED AND ANALYZED RESONANCE FREQUENCIES OF THE $\text{TM}_{0m0}$ MODES OF THE BCDR WITH $\epsilon_r^{\text{sample}} = \epsilon_r^{\text{shim}} = 2.3$

| Mode number | Simulated results $f_{0m0}^{\text{sim}}$ (GHz) | Analyzed results $f_{0m0}^{\text{anal}}$ (GHz) | Difference (%) |
| :--- | :--- | :--- | :--- |
| 1 | 13.2239 | 13.2236 | 0.0022 |
| 2 | 24.2709 | 24.2698 | 0.0048 |
| 3 | 35.2676 | 35.2685 | $-0.0025$ |
| 4 | 46.2678 | 46.2726 | $-0.010$ |
| 5 | 57.2822 | 57.2874 | $-0.0092$ |
| 6 | 68.3004 | 68.3089 | $-0.012$ |
| 7 | 79.3252 | 79.3349 | $-0.012$ |
| 8 | 90.3436 | 90.3547 | $-0.012$ |
| 9 | 101.3491 | 101.3628 | $-0.013$ |
| 10 | 112.3359 | 112.3508 | $-0.013$ |
| 11 | 123.2939 | 123.3088 | $-0.012$ |
| 12 | 134.2090 | 134.2257 | $-0.012$ |
| 13 | 145.0639 | 145.0828 | $-0.013$ |
| 14 | 155.8373 | 155.8542 | $-0.011$ |
| 15 | 166.4691 | 166.4869 | $-0.011$ |

Additional simulations for the case of $\epsilon_r^{\text{sample}} \neq \epsilon_r^{\text{shim}}$ are performed to study the effect of the shim. The simulated resonant frequencies of the $\text{TM}_{0m0}$ modes ($m = 1, 3, 5, 7$) for the sample with $\epsilon_r^{\text{sample}} = 2, 3, 5, 7, 9$ are shown in Fig. 7(b), where the difference between the simulated and analyzed results is plotted against the sample permittivity $\epsilon_r^{\text{sample}}$. Let $\epsilon_r^{\text{anal}}$ be the sample permittivity calculated by using the proposed analysis and the simulated resonant frequencies. Fig. 7(c) shows the difference between the analyzed permittivities and set values, $(\epsilon_r^{\text{anal}} - \epsilon_r^{\text{sample}}) / \epsilon_r^{\text{sample}}$, plotted against $\epsilon_r^{\text{sample}}$. It can be seen from Fig. 7(c) that the relative permittivity is underestimated when $\epsilon_r^{\text{sample}} < \epsilon_r^{\text{shim}}$, whereas it is overestimated when $\epsilon_r^{\text{sample}} > \epsilon_r^{\text{shim}}$, and the deviation ratio increases as the difference between the permittivities of the sample and shim increases. This result can be attributed to the influence of the electric field leaking to the shim. As the mode number (i.e., frequency) increases, the deviation ratio decreases when $\epsilon_r^{\text{sample}} > \epsilon_r^{\text{shim}}$, whereas it increases when $\epsilon_r^{\text{sample}} < \epsilon_r^{\text{shim}}$. This trend can be explained by the fact that the electric field is more concentrated in the high-permittivity region with increasing frequency.

It should be noted that the uncertainty evaluation described in Section IV-D does not include the effect of the shim. The shim has no effect on the measurement of the COP sample because the sample and shim are made of the same material. However, it affects the measurements of the RO4350B sample, especially with regard to the relative permittivity. Thus, we revise the uncertainty evaluation of the relative permittivity given in Table II. We assume that the uncertainty of the relative permittivity due to the effect of the shim follows a uniform distribution. By using the results in Fig. 7(c), the uncertainty is set as $6.8 \times 10^{-3}$ (0.2 % of $\epsilon_r = 3.404$) $/ \sqrt{3} = 3.9 \times 10^{-3}$ for the measurements of the RO4350B sample with the $\text{TM}_{060}$ mode resonance. The expanded uncertainty that includes the effect of the shim and other uncertainty sources described in Table II is $2.1 \times 10^{-2}$, which is 8% larger than the value in Table II.

## VI. EFFECT OF DIFFERENCES IN THE SAMPLE PAIR

In the analysis of the BCDR method, we assume that the relative permittivity $\epsilon_r$, loss tangent $\tan \delta$, and thickness $t$ of the two plate samples (sample pair) are equal. In this section, we evaluate the effect of the difference in the sample pair. We let $\epsilon_r, \tan \delta$, and $t$ of the two plate samples be $(\epsilon_{r1}, \tan \delta_1, t_1)$ for samples 1 and $(\epsilon_{r2}, \tan \delta_2, t_2)$ for sample 2. The resonant frequency and $Q$-factor corresponding to samples 1 and 2 are denoted as $(f_{0m0}^1, Q_u^1)$ and $(f_{0m0}^2, Q_u^2)$, respectively, and defined as the solutions of (2) and (3) with $(\epsilon_r = \epsilon_{r1}, \tan \delta = \tan \delta_1, t = t_1)$ and $(\epsilon_r = \epsilon_{r2}, \tan \delta = \tan \delta_2, t = t_2)$, respectively. For a BCDR composed of samples 1 and 2 with slightly different characteristics, $S_{21}$ near the resonant frequencies is given by the sum of two Lorentzian functions [18]

$$
S_{21} = \frac{d_1}{1 + 2j Q_l^1 (f - f_{0m0}^1)/f_{0m0}^1} + \frac{d_2}{1 + 2j Q_l^2 (f - f_{0m0}^2)/f_{0m0}^2} \quad (19)
$$

where $d_1$ and $d_2$ are the resonant strengths, and $Q_l^1$ and $Q_l^2$ are the loaded $Q$-factors that can be expressed for a weakly coupled resonator as [4]

$$
Q_l^{1,2} = Q_u^{1,2} (1 - d_{1,2}). \quad (20)
$$

The effective resonant frequency and $Q$-factor are determined by treating $S_{21}$ calculated from (19) as a resonant trace consisting of a single Lorentzian function. The effective relative permittivity $\epsilon_r^{\text{BCDR}}$ and loss tangent $\tan \delta^{\text{BCDR}}$ obtained from the BCDR method are calculated from the effective resonant parameters with (2) and (3). It can be expected that the difference in the sample pair should broaden or split the resonance; this would deteriorate the $Q$-factor and cause the loss tangent to be overestimated.

In order to evaluate this tendency quantitatively, we calculate $\epsilon_r^{\text{BCDR}}$ and $\tan \delta^{\text{BCDR}}$ under the condition that the samples differ for one of the three parameters ($\epsilon_r, \tan \delta, t$), while the other two parameters are equal for both samples. The set values of the parameters for sample 1 are $\epsilon_{r1} = 2.3$, $\tan \delta_1 = 4 \times 10^{-4}$, and $t_1 = 0.25$ mm, which are similar to those for the COP sample used in this paper. The set values of the parameters for sample 2 are as follows.
1) $\epsilon_{r2} = (1 + \Delta)\epsilon_{r1} (\Delta = 0.01, 0.02, 0.05, 0.1\%)$, $\tan \delta_2 = \tan \delta_1, t_2 = t_1$.
2) $\epsilon_{r2} = \epsilon_{r1}, \tan \delta_2 = (1 + \Delta)\tan \delta_1 (\Delta = 1, 2, 5, 10\%)$, and $t_2 = t_1$.
3) $\epsilon_{r2} = \epsilon_{r1}, \tan \delta_2 = \tan \delta_1$, and $t_2 = (1 + \Delta)t_1 (\Delta = 0.1, 0.2, 0.5, 1\%)$.
We set $d_1 = d_2 = -40$ dB and the diameter of the circular disk $2R = 18$ mm.

Under each calculation condition, we calculate $\epsilon_r^{\text{BCDR}}$ and $\tan \delta^{\text{BCDR}}$ and consider the differences between the calculated values and the averages of the set values: $\overline{\epsilon_r} = (\epsilon_{r1} + \epsilon_{r2})/2$, $\overline{\tan \delta} = (\tan \delta_1 + \tan \delta_2)/2$. Fig. 8 plots the deviations of the calculated values ($\epsilon_r^{\text{BCDR}}, \tan \delta^{\text{BCDR}}$) from the set values ($\overline{\epsilon_r}, \overline{\tan \delta}$) normalized by the set values against the mode number. Fig. 8(a)–(c) and (d)–(f) shows the deviations obtained for the relative permittivity and loss tangent, respectively, and Fig. 8(a) and (d), (b) and (e), and (c) and (f) shows the results for the calculation conditions 1, 2, and 3, respectively.

> **[Figure 8]:** Deviations in the calculated values normalized by the set values for the (a)–(c) relative permittivity and (d)–(f) loss tangent plotted against the mode number. Results for the deviations between the sample pair in terms of the (a) and (d) relative permittivity ($\Delta = 0.01, 0.02, 0.05, 0.1\%$), (b) and (e) loss tangent ($\Delta = 1, 2, 5, 10\%$), and (c) and (f) sample thickness ($\Delta = 0.1, 0.2, 0.5, 1\%$).
> *   **(a)-(c):** Permittivity deviations are generally small (< 0.1%).
> *   **(d)-(f):** Loss tangent deviations can be significant, especially for higher modes and larger differences in permittivity or thickness.

According to Fig. 8(a)–(c), the deviations in the relative permittivity obtained from the BCDR method because of the difference in the sample pair is rather small when the differences in $\epsilon_r, \tan \delta$, and $t$ are less than 0.1%, 10%, and 1%, respectively. On the other hand, the loss tangent from the BCDR method is overestimated when the differences in $\epsilon_r$ and $\tan \delta$ are more than 0.05% and 0.5%, respectively, and slightly overestimated when the difference in $\tan \delta$ is more than 5%. Note that $f_{0m0}^1 = f_{0m0}^2$ for calculation condition 2 ($\epsilon_{r1} = \epsilon_{r2}$ and $t_1 = t_2$); therefore, no split of the resonant trace occurs. For the other two calculation conditions, $f_{0m0}^1 > f_{0m0}^2$ and the resonant trace broadens, which reduces the effective $Q$-factor and causes the loss tangent to be overestimated.

For the COP sample used in this paper, we confirm that the difference between the sample thicknesses of the pair is approximately 0.4%. Therefore, the increase in the loss tangent in the $D$-band shown in Fig. 6(a) may be partly due to the difference in sample thicknesses of the pair.

Note that the contribution of the difference between the samples in the pair is not included in the uncertainty evaluation presented in Section IV-D. Let us consider the effect of the difference in thickness between the samples in the pair on the uncertainty of the loss tangent for the COP sample in Table I. When the difference in thickness is 0.4%, the deviation in the loss tangent is estimated to be less than 23%. We assume that the uncertainty of the loss tangent due to the difference in thickness follows a uniform distribution and set it to $1.4 \times 10^{-4}$ (23 % of $\tan \delta = 6.3 \times 10^{-4}$) $/ \sqrt{3} = 8.4 \times 10^{-5}$. The expanded uncertainty including the effect of the thickness difference and other uncertainty sources described in Table I is $2.6 \times 10^{-4}$. Thus, the uncertainty presented in Section IV-D is a slight underestimation because it does not consider the effect of differences between the samples in the pair.

## VII. CONCLUSION

We have developed a BCDR excited by a 0.8-mm coaxial line to increase the maximum measurable frequency of the BCDR method to 170 GHz. In addition, we have proposed a new analysis method to derive the permittivity with the BCDR method, where the effective radius of the circular disk is rigorously determined by mode-matching analysis. We clarified that the improved analysis plays an essential role in using the BCDR method to measure the relative permittivity in the millimeter-wave band with high accuracy.

By using the developed resonator and proposed analysis, we have demonstrated that the BCDR method has the possibility to perform significantly broadband permittivity measurements at a large number of frequencies with a single resonator by measuring the two-dielectric samples. Our resonator with five circular disks of different radii provided complex permittivities of the COP sample from 11.3 to 167 GHz at 59 frequency points and of the RO4350B sample from 9.35 to 67.7 GHz at 28 frequency points. We confirmed that the measured relative permittivity and loss tangent obtained with five circular disks were consistent within the uncertainties over the entire frequency range.

We evaluated the measurement uncertainties for this method by considering the uncertainty propagations of the resonant frequency, $Q$-factor, dimensions of the resonator and samples, and conductivity of the resonator and by estimating the effect of errors in the mode-matching analysis. The total uncertainty of the relative permittivity was less than 0.8% for the two samples at all frequencies. The total uncertainty of the loss tangent decreased with increasing frequency. For the highest measured frequency, the total uncertainty of the loss tangent was 31% at 167 GHz for the COP sample and 7.1% at 67.7 GHz for the RO4350B sample.

In addition, we verified the proposed analysis by performing full-wave electromagnetic simulations. We clarified that the proposed analysis is sufficiently accurate up to 170 GHz when the sample and shim are made of the same material. We also confirmed that the BCDR method can overestimate or underestimate the relative permittivity when the sample has lower or higher permittivity, respectively, than the shim.

Furthermore, we evaluated the effect of the difference between samples in the sample pair used in the BCDR method. We clarified that the BCDR method can overestimate the loss tangent, especially for measurements at higher frequencies, if there was a difference in the relative permittivity or sample thickness in the sample pair.

It should be noted that the uncertainty evaluation presented in this paper might be underestimated for several reasons: 1) the effect of the shim is not included; 2) the samples of the pair are assumed to be exactly the same; and 3) the frequency dependence of the conductivity of the resonator is not considered. These factors should be studied in greater detail in the future research in order to derive correction formulas for them and/or integrate them into the uncertainty evaluation.

## ACKNOWLEDGMENT

The authors would like to thank Y. Todaka (Keysight Technologies) for the valuable discussion.

## REFERENCES

[1] D. K. Ghodgaonkar, V. V. Varadan, and V. K. Varadan, “Free-space measurement of complex permittivity and complex permeability of magnetic materials at microwave frequencies,” *IEEE Trans. Instrum. Meas.*, vol. 39, no. 2, pp. 387–394, Apr. 1990.
[2] D. Bourreau, A. Péden, and S. Le Maguer, “A quasi-optical free-space measurement setup without time-domain gating for material characterization in the W-band,” *IEEE Trans. Instrum. Meas.*, vol. 55, no. 6, pp. 2022–2028, Dec. 2006.
[3] A. Kazemipour et al., “Design and calibration of a compact quasi-optical system for material characterization in millimeter/submillimeter wave domain,” *IEEE Trans. Instrum. Meas.*, vol. 64, no. 6, pp. 1438–1445, Jun. 2015.
[4] R. N. Clarke, Ed., “A guide to the characterisation of dielectric materials at RF and microwave frequencies,” Inst. Meas. Control/Nat. Phys. Lab., London, U.K., Tech. Rep., 2003.
[5] J. Krupka, W.-T. Huang, and M.-J. Tung, “Complex permittivity measurements of low-loss microwave ceramics employing higher order quasi $\text{TE}_{0np}$ modes excited in a cylindrical dielectric sample,” *Meas. Sci. Technol.*, vol. 16, no. 4, pp. 1014–1020, 2005.
[6] J. Krupka, “Frequency domain complex permittivity measurements at microwave frequencies,” *Meas. Sci. Technol.*, vol. 17, no. 6, pp. R55–R70, 2006.
[7] T. M. Hirvonen, P. Vainikainen, A. Lozowski, and A. V. Raisanen, “Measurement of dielectrics at 100 GHz with an open resonator connected to a network analyzer,” *IEEE Trans. Instrum. Meas.*, vol. 45, no. 4, pp. 780–786, Aug. 1996.
[8] M. N. Afsar and H. Ding, “A novel open-resonator system for precise measurement of permittivity and loss-tangent,” *IEEE Trans. Instrum. Meas.*, vol. 50, no. 2, pp. 402–405, Apr. 2001.
[9] H. Suzuki and T. Kamijo, “Millimeter-wave measurement of complex permittivity by perturbation method using open resonator,” *IEEE Trans. Instrum. Meas.*, vol. 57, no. 12, pp. 2868–2873, Dec. 2008.
[10] H. Kawabata and Y. Kobayashi, “The analysis of a balanced-type circular disk resonator excited by coaxial cable lines to measure the complex permittivity,” in *Proc. Asia–Pacific Microw. Conf.*, vol. 3, Dec. 2001, pp. 1322–1325.
[11] H. Kawabata, K.-I. Hasuike, Y. Kobayashi, and Z. Ma, “Multi-frequency measurements of complex permittivity of dielectric plates using higher order modes of a balanced-type circular disk resonator,” in *Proc. Eur. Microw. Conf.*, Sep. 2006, pp. 388–391.
[12] J. Nakatsutsumi, Y. Kobayashi, and Z.-W. Ma, “Discussions on measurement accuracy of complex relative permittivity using a balanced-type circular disk resonator method,” in *Proc. Asia–Pacific Microw. Conf.*, Nov. 2014, pp. 522–524.
[13] Y. Kato and M. Horibe, “Permittivity measurements and associated uncertainties up to 110 GHz in circular-disk resonator method,” in *Proc. 46th Eur. Microw. Conf. (EuMC)*, Oct. 2016, pp. 1139–1142.
[14] Y. Kato, Y. She, M. Horibe, and S. Kurokawa, “Development of permittivity measurement system at microwave and millimeter wave frequencies for low-loss substrate characterization,” in *Proc. IEEE Conf. Antenna Meas. Appl. (CAMA)*, Dec. 2017, pp. 76–78.
[15] Y. Kato and M. Horibe, “Broadband permittivity measurements using a frequency-variable balanced-type circular-disk resonator,” in *Proc. Conf. Precis. Electromagn. Meas. (CPEM)*, Jul. 2018, pp. 1–2.
[16] M. Sugawara, M. Emoto, K. Masaoka, Y. Nishida, and Y. Shishikui, “Super hi-vision for the next generation television,” *ITE Trans. Media Technol. Appl.*, vol. 1, no. 1, pp. 27–33, 2013.
[17] [Online]. Available: https://www.imec-int.com/en/articles/imec-demonstrates-compact-low-power-140ghz-cmos-radar-with-on-chip-antennas
[18] Y. Kato and M. Horibe, “Comparison of calculation techniques for Q-factor determination of resonant structures based on influence of VNA measurement uncertainty,” *IEICE Trans. Electron.*, vol. E97-C, no. 6, pp. 575–582, 2014.
[19] K. Tanabe, Y. Kobayashi, and S. Tanaka, “Numerical analysis of eigenvalue solution of disk resonator (short papers),” *IEEE Trans. Microw. Theory Techn.*, vol. MTT-23, no. 6, pp. 508–511, Jun. 1975.
[20] S. B. Cohn, “Problems in strip transmission lines,” *IRE Trans. Microw. Theory Techn.*, vol. 3, no. 2, pp. 119–126, Mar. 1955.
[21] A. C. Lynch, “Relationship between permittivity and loss tangent,” *Proc. Inst. Elect. Eng.*, vol. 118, no. 1, pp. 244–246, Jan. 1971.
[22] N. Marcuvitz, *Waveguide Handbook*. New York, NY, USA: McGraw-Hill, 1951.
[23] M. D. Janezic, “Nondestructive relative permittivity and loss tangent measurements using a split-cylinder resonator,” Ph.D. dissertation, Dept. Elect. Comput. Eng., Univ. Colorado Boulder, Boulder, CO, USA, 2003.
[24] M. D. Janezic, E. F. Kuester, and J. B. Jarvis, “Broadband complex permittivity measurements of dielectric substrates using a split-cylinder resonator,” in *IEEE MTT-S Int. Microw. Symp. Dig.*, vol. 3, Jun. 2004, pp. 1817–1820.

---

**Yuto Kato** received the B.S. and M.S. degrees in physics from the University of Tokyo, Tokyo, Japan, in 2010 and 2012, respectively.
Since 2012, he has been with the Electromagnetic Fields Section, National Metrology Institute of Japan, National Institute of Advanced Industrial Science and Technology, Tsukuba, Japan. His current research interests include complex permittivity measurements at RF, microwave, millimeter-wave, and submillimeter-wave frequencies.

**Masahiro Horibe** (M’08–SM’–17) received the Ph.D. degree in quantum engineering from Nagoya University, Nagoya, Japan, in 2001.
From 1999 to 2001, he was a Post-Doctoral Fellow with the Japan Society for the Promotion of Science, Tokyo, Japan. In 2001, he joined Fujitsu Limited, Kanagawa, Japan. From 2001 to 2003, he was with the Superconductivity Research Laboratory, International Superconductivity Technology Center, Tokyo. In 2003, he was with Fujitsu Laboratories Ltd., Kanagawa, where he was involved in carbon nanotube applications. He is currently with the National Metrology Institute of Japan, National Institute of Advanced Industrial Science and Technology, Tsukuba, Japan. He was involved in the research and development of national metrology standards for scattering parameters and material characterization in RF, microwave, millimeter-wave, and Terahertz frequency ranges. His current research interests include material characterization of nanoelectronics, applications of flexible electronics, and characterization of power-electronic devices, i.e., SiC and GaN.
Dr. Horibe is the Japan National Committee Chairperson of the IEC TC46 and SC46F, the Subchair of the IEC TC 113 WG3 Japanese committee, and a member of ARFTG, IEEE MTT-11 Technical Committee, URSI Commission A, IEEE P1785, 287, 1765, and the 1770 Standard Working Group. He is also an ISO17025 Assessor for International Accreditation in Japan.