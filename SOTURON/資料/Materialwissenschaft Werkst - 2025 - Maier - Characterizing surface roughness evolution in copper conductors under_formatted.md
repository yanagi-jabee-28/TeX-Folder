# Characterizing surface roughness evolution in copper conductors under mechanical strain using power spectral density analysis

**Charakterisierung der Entwicklung der Oberflächenrauheit in Kupferleitern unter mechanischer Beanspruchung mit Hilfe der Leistungsspektraldichteanalyse**

**C. Maier | P. Rachwalsky¹ | A. Wittmann¹ | K. P. Koch¹ | G. Fischer²**

1. Trier University of Applied Sciences, Department of Engineering, Schneidershof 1, 54293 Trier, Germany
2. Friedrich-Alexander-Universität Erlangen-Nürnberg, Institute for Smart Electronics and Systems, Cauerstraße 9, 91058 Erlangen, Germany

**Correspondence**
C. Maier, Trier University of Applied Sciences, Department of Engineering, Schneidershof 1, 54293 Trier, Germany.
Email: maierc@hochschule-trier.de

---

## Abstract

This study investigates the effects of mechanical strain on the surface roughness of copper conductors, focusing on the electrolyte-refined copper (Cu-ETP, CW004A) used in H07V-U $1.5~mm^{2}$ single-core cables. For the first time, the surface roughness evolution is characterized using the power spectral density (PSD) function, enabling a detailed roughness analysis across different spatial length scales. Conductors were subjected to mechanical stress, with measurements taken at multiple stages of service life. The study confirms the results from other studies that surface roughness increases significantly in the early stages of loading, with a plateau observed in 50%-75% of cycles to failure. Micro crack formation and material extrusion are identified as key mechanisms driving roughness growth, especially at small length scales, with a shift towards larger length scales as strain intensifies. The increasing Hurst exponent suggests a transformation from a random to a more persistent and correlated surface. The results underscore the potential of power spectral density analysis in understanding surface behavior in copper conductors.

**KEYWORDS**
copper conductors, surface roughness, power spectral density, mechanical strain, Hurst exponent

**Abstract**

In dieser Studie werden die Auswirkungen mechanischer Belastung auf die Oberflächenrauheit von Kupferleitern untersucht, wobei der elektrolytisch raffinierte Kupferleiter (Cu-ETP, CW004A) in H07V-U 1.5 mm² Aderleitung im Fokus steht. Erstmals wird die Entwicklung der Oberflächenrauheit unter Verwendung der spektralen Leistungsdichte (PSD) charakterisiert, die eine detaillierte Analyse der Rauheit über verschiedene Längenskalen ermöglicht. Die Leiter wurden mechanischen Belastungen ausgesetzt, wobei Messungen in mehreren Phasen bis zum Versagen durchgeführt wurden. Die Studie bestätigt die Ergebnisse aus anderen Arbeiten, dass die Oberflächenrauheit in den frühen Phasen der Beanspruchung deutlich zunimmt, wobei bei 50%-75% der Zyklen bis zum Versagen ein Plateau zu beobachten ist. Die Bildung von Mikrorissen und Materialextrusion werden als Hauptmechanismen für das Wachstum der Rauheit identifiziert, insbesondere auf kleinen Längenskalen, mit einer Verschiebung hin zu größeren Längenskalen, wenn die Belastung zunimmt. Die Steigerung des Hurst-Exponenten deutet auf eine Transformation von einer zufälligen hin zu einer persistenteren und korrelierten Oberfläche hin. Die Ergebnisse unterstreichen das Potenzial der spektralen Leistungsdichte, ein umfassendes Verständnis des Oberflächenverhaltens unter mechanischer Belastung in Kupferleitern zu liefern.

**SCHLÜSSELWÖRTER**
Kupferleiter, Oberflächenrauheit, spektrale Leistungsdichte, mechanische Belastung, Hurst-Exponent

---

**DOI:** 10.1002/mawe.70029
**Received:** 12 March 2025 | **Revised:** 25 June 2025 | **Accepted:** 29 August 2025
*Materialwiss. Werkstofftech.* 2025:56:1225-1234
© 2025 The Author(s). Materialwissenschaft und Werkstofftechnik published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License.

---

## 1 | INTRODUCTION

Surface roughness influences the transmission line attenuation at high frequencies due to the skin effect [1-4]. Since all forms of mechanical stress can cause roughness on metal surfaces [5, 6]. This has led to a new application area in which the roughness of copper conductors is used as a direct indicator of service life. This application now encompasses cable maintenance systems as well as the structural health monitoring of composite materials [7-9].

Most commonly, it is assumed that the roughness of conducting surfaces is irregular or random [10, 11]. Therefore, surface roughness is usually described by two-dimensional root mean square roughness $S_{q}$ [6, 7, 9, 12]. The advantage of this approach over line roughness is that it does not give excessive weight to outliers caused by inhomogeneous damage [9]. However, it leads to the loss of all information regarding the surface's spectral properties, including its lateral structure and periodicity [12, 13].

Surfaces can be fully characterized by using the power spectral density function (PSD), which describes the surfaces by calculating the contributions from different spatial frequencies (wavevectors) [14]. Knowledge derived from the power spectral density function can be used, e.g., in losses due to roughness in transmission lines and also for contact mechanics models, the latter being able to model contact mechanics, friction, and adhesion by entering the full power spectral density [15-21].

In this study, we aim to utilize power spectral density to explore the evolution of surface roughness and structures over the lifespan of conventional copper conductors at two distinct optical magnifications. The power spectral density across various wavenumbers were analysed and these findings compared with the effective roughness. Additionally, the surfaces were examined for self-similarity and assessed whether the surface exhibits persistent or anti-persistent behavior by calculating the Hurst exponent, concluding the underlying causes of the roughness.

## 2 | METHODS

### 2.1 | Sample preparation

The conductors studied in this paper are composed of electrolyte-refined copper (Cu-ETP, CW004A) in the form of H07V-U 1.5 $mm^{2}$ single-core cables provided by ICEL Scpa. Electrolyte-refined copper (Cu-ETP, CW004A), which contains oxygen and has a good electrical conductivity, was chosen as it exhibits the most significant roughness growth under mechanical strain [6, 9, 22]. The copper conductors were subjected to stress on the multi-roll bending machine (MRB), which is based on the alternating bending test with two rollers as outlined in DIN EN 50396 [23]. To determine a 100% service life, 50 conductors were loaded until they broke. Additional tests were conducted at 25%, 50%, and 75% of the maximum service life, based on the average number of load cycles. With an additional new, unloaded conductor, five stages of service life were thus investigated.

### 2.2 | Measurement of the surfaces

Surface roughness can be easily analyzed using standard techniques based on optical and cantilever methods, such as atomic force microscopy (AFM) [20]. Specifically, atomic force microscopy enables surface profiling within a range of approximately 1 nm to $100~\mu m$, while optical methods extend from around $1~\mu m$ to kilometers [20, 24, 25]. Due to the curvature of the conductors and the need to analyze larger surface regions, atomic force microscopy was unsuitable for this study [26]. Thus, the confocal microscopy was used. The surfaces were measured using the confocal chromatic microscope Confovis Toolinspect S. When using an optical method, almost any curvature and very rough surfaces can be measured, but the analyzable length scale is limited due to the Rayleigh criterion [25]. With the numerical aperture of $NA=0.6$ for the lenses used and the wavelength $\lambda=528$ nm of the illuminating light, the length scale is limited to [25]:

$$
d = \frac{0.61 \lambda}{NA} = \frac{0.61 \cdot 528 \text{ nm}}{0.6} = 536.8 \text{ nm} \quad (1)
$$

Another limiting factor is the influence of noise on the measured values [27]. This impact is typically quantified as the signal-to-noise ratio SNR [27, 28]. The SNR was 40 dB for the unstressed conductor and 52 dB for the failed conductor, as calculated in [28]:

$$
SNR = 10 \text{ dB} \log_{10} \frac{RMS}{\sigma_{\text{noise}}} \quad (2)
$$

Every conductor of the distinct stages of service life was measured with magnifications of 20x and 50x. For each magnification, the conductors were scanned 42 times. The individual measurements were taken from the top of the conductor and were spaced approximately 0.5 mm to 1 mm lengthways along the conductor. Overlapping scans were possible. The measurements, taken with a 20x magnification, contained 2,554 pixels in both the x- and y-directions, with a pixel width of 247 nm, resulting in an edge length of $630~\mu m$. The 50x scans contain 2,316 pixels, with a pixel width of 109 nm and an edge length of $252~\mu m$.

### 2.3 | Data processing pipeline

To prepare the surface topography data for spectral analysis, individual measurements were first exported from the Confovis software and imported into the MountainsMap software. Within MountainsMap, the data were reformatted into a three-column CSV file representing the spatial coordinates and corresponding height values. This format facilitated the subsequent processing in MATLAB, where the data were structured into an $m \times n$ matrix (z-matrix), with m and n denoting the number of pixels in the x- and y-directions, respectively. The z-matrix encapsulated the surface height profile.

As the raw surface height data included the macroscopic curvature of the conductor, this general trend was removed to isolate the surface roughness. A polynomial surface was fitted to the data and subtracted to eliminate the curvature component, **Figure 1**. Due to limitations inherent in the optical scanning method, the dataset contained missing values [26]. These gaps were interpolated either along columns or rows, depending on the direction in which the power spectral density was to be computed.

Subsequently, the one-dimensional power spectral density was calculated for each column or row of the interpolated z-matrix, corresponding to the selected analysis direction. The power spectral densities were then averaged across all columns or rows, respectively, to obtain representative spectral profiles for each measurement condition, **Figure 1** [29]. This procedure was repeated for each magnification level, scanning direction, and stage of the conductor's service life, resulting in a total of 42 power spectral densities plots per condition.

> **[Figure 1]:** Data processing pipeline from the measured two-dimensional height profile. The two-dimensional height profiles of copper conductors were obtained using confocal chromatic microscopy with two different magnifications (20x and 50x). The height data was detrended by fitting a polynomial surface. To compute the one-dimensional power spectral density, the height data was interpolated separately in the x- and y-directions. Individual PSDs were averaged to obtain a master power spectral density, applying a 90/10 filter before averaging. Parseval's theorem was verified for the master power spectral densities. To extend the wavevector range, the master power spectral densities for 20x and 50x magnifications were gradually weighted. Consequently, two gradually weighted power spectral densities were calculated for each stage of mechanical strain.

To mitigate the impact of limited measuring fields when applying the Fourier transform, the Welch window function was applied to the data, which is particularly suitable for power spectral density functions [12, 29, 30]. The conductor surfaces are expected to be anisotropic due to structures that develop during manufacturing. Therefore, the radially averaged two-dimensional power spectral density function was not calculated, as an isotropic surface is required [12, 14, 31]. Every power spectral density plot was tested for compliance with Parseval's theorem, where the area under the curve $({\sigma^{2}}_{g})$ is equal to the variance of the height $({\sigma^{2}}_{h})[12,14,32]$. The integral of the power spectral density function is given by [12]:

$$
{\sigma_{q}}^{2} = 2 \int_{q_{min}}^{q_{max}} PSD^{1D}(q) dq \quad (3)
$$

The interval $[q_{min}, q_{max}]$ is limited by the edge length of the surface scan and the length scale, which is constrained by the Rayleigh criterion and the Nyquist-Shannon criterion [25, 33]. Therefore, the limits are given by [12]:

$$
q_{min} = \frac{2\pi}{L} \quad (4)
$$

$$
q_{max} = \frac{2\pi}{2d} \quad (5)
$$

The resulting wavevector intervals were: $[9.97e-3~\mu m^{-1}, 5.85~\mu m^{-1}]$ for a 20x magnification and $[2.49e-2~\mu m^{-1}, 5.85~\mu m^{-1}]$ for a 50x magnification. Then, a 90/10 filter was applied, **Figure 1**. Afterward, the individual power spectral density functions were averaged over all scans to obtain a master power spectral density function (Master-PSD) for each magnification, **Figure 1**.

Since the estimation of the power spectral density from normal distributed roughness produces a $x^{2}$ sampling distribution for the power spectral density, the uncertainty of the power spectral density values can be described by the standard deviation of the measurements [29]. The standard deviation decreases by $1/\sqrt{M}$, where M is the number of measured power spectral density functions [29]. Therefore, the resulting master power spectral density function (Master-PSD) was averaged with $33 \times 2,554$ individual power spectral density functions for the 20x magnification and $33 \times 2,316$ individual power spectral density functions for the 50x magnification. As a result, the confidence interval of 95% was $[0.9905~PSD^{1D}(q), 1.0096~PSD^{1D}(q)]$ for the 20x magnification and $[0.99~PSD^{1D}(q), 1.0101~PSD^{1D}(q)]$ for the 50x magnification.

Using the two master power spectral density functions (Master-PSDs) for each magnification, a single power spectral density function with an increased wavevector interval was calculated. The two functions were weighted gradually, depending on their individual wavevector interval. The gradual weighting of the two power spectral density functions with different wavevector intervals was applied to ensure a smooth transition between their contributions. Initially, the 20x magnification measurements had a high weight, which decreased as the wavevector increased. Both magnification measurements were equally weighted in the mid-wavevector range, while only the 50x magnification measurements contributed at high wavevectors. The gradually weighted power spectral density function (GW-PSD) was calculated for each stage of service life and dimension, **Figure 1**. Therefore, every stage has two gradually weighted power spectral density functions for the x- and y-directions. The gradually weighted power spectral density functions were then utilized to characterize the surface by calculating the Hurst exponent. The Hurst exponent is determined from the gradient of the power spectral density and is given by [20]:

$$
H = \frac{-\alpha-1}{2} \quad (6)
$$

The gradient $\alpha$ was estimated by regression, which follows the power-law behavior: $PSD^{1D}(q) \sim q^{\alpha}$.

## 3 | RESULTS AND DISCUSSIONS

The gradually weighted power spectral density functions, calculated from mechanically stressed electrolyte-refined copper conductors (Cu-ETP), exhibit power-law behavior, $PSD^{1D}(q) \sim q^{\alpha}$, in the wavevector interval $[3e-2~\mu m^{-1}, 5.85~\mu m^{-1}]$ and a long distance roll off vector in the wavevector interval $[9.97e-2~\mu m^{-1}, 3e-2~\mu m^{-1}]$, **Figure 2**. The difference between the power spectral density of the new, unstressed (MRB 0%), and failed (MRB 100%) conductor in the x-direction is described by a factor of 17.5 at low wavevectors and decreases to 2.2 at high wavevectors as the exponent $\alpha$ of the power-law scaling decreases. The factor is generally smaller for the y-direction, where it starts at 8.5 and decreases to 1.8. This is mainly caused by a higher power spectral density in the y-direction for the new, unstressed conductor (MRB 0%), which can be explained by the overall higher roughness in the y-direction due to structures formed during the manufacturing process.

Additionally, the power spectral density calculated in the y-direction, particularly for the new, unstressed conductor (MRB 0%), exhibits distinct peaks at various spatial wavevectors. These peaks, which appear exclusively in the y-direction—the corresponding manufacturing direction—are also attributable to structures formed during the manufacturing process and can be seen at wavevectors of $q=2.4~\mu m^{-1}$ and $q=5.7\mu m^{-1}$. These manufacturing structures are visible in the surface plot of the new conductor and disappear with increasing service life, **Figure 2a-e**. The manufacturing process also influences the power spectral density function in the x-direction. The new conductor's power spectral density (MRB 0%) shows greater oscillation than in the y-direction. The structures formed by the manufacturing process change the autocorrelation of the surface, which leads to a different power-law scaling and more significant oscillation at the attributable wavevector interval $[4e-1~\mu m^{-1}; 1.4~\mu m^{-1}]$.

> **[Figure 2]:** Power spectral density of copper conductors. Surfaces of copper conductors were examined using confocal chromatic microscopy. The conductors were subjected to stress in a multi-roll bending machine (MRB) at distinct stages of mechanical strain, expressed as percentage of cycles till failure. The stages were 0% (a), 25% (b), 50% (c), 75% (d) and 100% (e). The one-dimensional power spectral density functions (PSDs) were obtained by detrending and interpolating the data. The PSDs were then calculated, averaged and gradually weighted over magnifications of 20x and 50x for the x-direction (f) and the y-direction (g) at each stage of mechanical strain. The PSDs exhibit power-law behavior at all stages and increases with increasing service life (f, g). The corresponding surface roughness also increases, as can be seen from the exemplary surface images (a-e). The vertical lines (f, g) mark the distinct wavevectors at which the progression of the PSD is presented in Figure 2 and Figure 3.

In the x-direction at a magnification of 20x, the Hurst exponent is, in all cases, smaller than 0.5, which shows anti-persistent behavior. In contrast, at a magnification of 50x, the Hurst exponent becomes larger than 0.5 above 50% service life, **Table 1**. This indicates a multi-scale roughness, meaning that different features dominate at various scales [5, 20]. In the y-direction at a magnification of 20x, the Hurst exponent remains below 0.5 at 0% service life but increases beyond this threshold as service life progresses, indicating a transition from anti-persistent to persistent behavior. At a magnification of 50x, the Hurst exponent is consistently above 0.5% from 25% service life onward, **Table 1**. Like in the x-direction, the consistently higher Hurst exponents for higher magnification also show a multi-scale roughness [5, 20]. The difference between the Hurst exponents of the power spectral density plots for the new, unstressed conductor in the x- and y-directions indicates an anisotropic surface [20, 34]. This difference decreases with increasing service life, suggesting that the surface of a copper conductor becomes more isotropic as it is stressed. Thus, the radially averaged two-dimensional power spectral density cannot be calculated due to the lack of isotropy [12, 14, 31]. Therefore, the surface of a new electrolyte-refined copper conductor (Cu-ETP) can be characterized as anisotropic, anti-persistent, and self-affine. In contrast, at higher service lifes, the surface becomes more isotropic, persistent, and self-affine. As a result, contact mechanics models [17-21], which depend on isotropic surfaces are only suitable for stressed conductors [20].

**TABLE 1 Hurst exponents and R² values for the averaged power spectral density (PSD) of copper conductors.**

| Stage of mechanical strain | Number of Cycles | Magnification of 20x (x-direction H / R²) | Magnification of 20x (y-direction H / R²) | Magnification of 50x (x-direction H / R²) | Magnification of 50x (y-direction H / R²) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0%** | 0 | 0.0589 / 0.9377 | 0.2355 / 0.9401 | 0.3293 / 0.8367 | 0.2927 / 0.9700 |
| **25%** | 165 | 0.9175 / 0.1232 | 0.2281 / 0.9949 | 0.9906 / 0.3333 | 0.3484 / 0.9696 |
| **50%** | 337 | 0.3415 / 0.9867 | 0.3935 / 0.9889 | 0.4562 / 0.9713 | 0.9308 / 0.4523 |
| **75%** | 505 | 0.4562 / 0.9657 | 0.5231 / 0.9975 | 0.9334 / 0.6741 | 0.6529 / 0.9617 |
| **100%** | 674 | 0.4663 / 0.9690 | 0.5605 / 0.9899 | 0.6601 / 0.9823 | 0.6628 / 0.9331 |

In general, the increasing Hurst exponent across all stages of service life for both the averaged and gradually weighted power spectral density indicates a transformation towards a less random surface with more correlated structures, **Table 2** [5, 35]. The Hurst exponent quantifies the degree of long-range dependence in surface profiles, indicating how current surface heights influence subsequent heights. A Hurst exponent between $0.5 < H < 1$ suggests a persistent, more self-similar surface, which implies that regions of high heights are likely to be followed by similarly high values, and low heights by similarly low values [5, 35, 36]. This leads to the conclusion that surface roughness develops through crack initiation, crack propagation, and material extrusion [9, 37-39]. As cracks develop and extend, they create rough profiles with correlated features. Additionally, material extrusion forms sharp, small-scale mounds, leading to clearly distinguishable height values and a more persistent surface. For the early stages of service life ($0 < H < 0.5$), the Hurst exponent suggests an antipersistent surface, where structures are uncorrelated and shows the characteristic of 'mean-reverting', where regions of high heights are likely to be followed by low values, and low heights by high values [5, 40].

**TABLE 2 Hurst exponents and $R^{2}$ values for the gradually weighted power spectral density (GW-PSD) of copper conductors.**

| Stage of mechanical strain | x-direction (H / R²) | y-direction (H / R²) |
| :--- | :--- | :--- |
| **0%** | 0.2365 / 0.8716 | 0.9548 / 0.3697 |
| **25%** | 0.2815 / 0.9958 | 0.3328 / 0.9675 |
| **50%** | 0.4539 / 0.9970 | 0.4783 / 0.9869 |
| **75%** | 0.8106 / 0.6424 | 0.9471 / 0.6911 |
| **100%** | 0.9152 / 0.6759 | 0.9726 / 0.7125 |

While the surface of the copper conductor becomes persistent and isotropic, the root mean square roughness increases up to 50% service life, after which it reaches a plateau of 75%, confirming the results of other studies [6]. Afterward, the surface roughness increases once again until the end of life, **Figure 3** [9]. The power spectral density in the x-direction increases for low wavevectors up to 50% of the service life and reaches a plateau until 75%, then increases again in the last 25% of the service life. The power spectral density shows the same behavior until 50% of service life for high wavevectors. Afterward, the power spectral density decreases noticeably until 75% of the service life and then increases slightly to 100% of the service life. For very high wavevectors, the power spectral density at 100% service life is smaller than at 25% service life, **Figure 4**. For the y-direction, the power spectral density for distinct stages in service life behaves the same as in the x-direction, with a slightly different power spectral density, **Figure 5**.

> **[Figure 3]:** Progression of the root mean square surface roughness at 0%, 25%, 50%, 75% and 100% service life. The graph presents the evolution of the root mean square height $(S_{q})$ of a surface as a function of mechanical strain. The x-axis represents the stages of service life in percentage, ranging from 0% (new surface) to 100% (failure), while the y-axis quantifies the $S_{q}$ value in micrometers (µm). The $S_{q}$ value is calculated out of the detrended surface data obtained by confocal chromatic microscopy. The overall root mean square surface roughness increases over service life, while showing a plateau between 50% and 75% of service life.

> **[Figure 4]:** Progression of surface roughness in x-direction at distinct wavevectors. The progression of the PSD value, calculated from the detrended and interpolated height data interpreted as roughness is presented at the wavevector $q=0.01~\mu m^{-1}$ (a), $q=0.1~\mu m^{-1}$ (b), $q=1\mu m^{-1}$ (c) and $q=5.7~\mu m^{-1}$ (d). The wavevector positions are indicated in Figure 1. The overall surface roughness increases over mechanical strain, but the spatial roughness may evolve differently across the examined wavevectors (a-d), Figure 3.

> **[Figure 5]:** Progression of surface roughness in y-direction at distinct wavevectors. The progression of the PSD value, calculated from the detrended and interpolated height data interpreted as roughness is presented at the wavevector $q=0.01~\mu m^{-1}$ (a), $q=0.1~\mu m^{-1}$ (b), $q=1~\mu m^{-1}$ (c) and $q=5.7~\mu m^{-1}$ (d). The wavevector positions are indicated, Figure 1. The overall surface roughness increases over mechanical strain, but the spatial roughness may evolve differently across the examined wavevectors, Figure 3a-d.

Since surface roughness can be considered the sum of roughness across all spatial length scales, the observed plateau can be explained by a reduction in roughness at small length scales or high wavevectors, **Figures 2, 3**. The power spectral density increases more at high wavevectors during the first 50% of cycles to failure compared to small wavevectors. As a result, the power spectral density for the moderately stressed conductor is higher at high wavevectors compared to that of the failed conductor, **Figures 1-3**. Then, the power spectral density decreases for high wavevectors and increases for smaller wavevectors, **Figures 2, 3**. This behavior is consistent in both the x- and y-directions.

The manufacturing structures, which are restricted to specific spatial wavevectors, contribute to higher roughness at these particular wavevectors. However, during the service life, these manufacturing structures are smoothed out and no longer visible in any of the stressed conductors' power spectral density. Since high wavevectors correspond to small length scales, the primary increase in roughness at small length scales can be attributed to the formation of micro-cracks and the onset of material extrusion [9, 37-39]. As service life increases, these micro-cracks grow, and plastic deformation further enhances material extrusion, leading to an increase in length scale and a shift in roughness growth towards smaller wavevectors [9, 37-39]. The formation and propagation of micro cracks, along with material extrusion, are also reflected in the increasing Hurst exponent, which indicates that the surface becomes more persistent and correlated [5, 35, 36].

## 4 | SUMMARIES

This study investigates the surface roughness evolution of copper conductors with increasing service life, using the power spectral density as the primary tool for characterization. The research is the first to apply power spectral density analysis to copper conductors (Cu-ETP) and provides new insights into the strain-induced changes in their surface properties. Specifically, the study focuses on electrolyte-refined copper conductors (Cu-ETP) used in high-frequency applications, where surface roughness plays a critical role in transmission properties due to the skin effect. The analysis reveals how different mechanisms, such as micro crack formation and material extrusion, dominate at various spatial scales and contribute to surface evolution. An increasing Hurst exponent indicates a shift from a random to a more correlated surface pattern as strain progresses. These findings lay the foundation for developing more accurate transmission line models that incorporate the effects of surface roughness evolution over time in copper conductors.

The conductors, in the form of H07V-U 1.5 mm² single-core cables, underwent mechanical stress using a multi-roll bending machine, with measurements taken at various stages of service life, from unstressed to failure. The surface roughness was evaluated through both two-dimensional root mean square roughness $S_{q}$ and the one-dimensional power spectral density function, the latter providing a more comprehensive view of the surface properties.

The study reveals that mechanical strain leads to significant changes in surface roughness, with clear evidence of micro-crack formation and material extrusion. These processes initially increase roughness at smaller length scales, but as the strain progresses, the roughness progressively shifts to larger scales. The results show that surface roughness increases by up to 50% of the cycles to failure, followed by a plateau in roughness growth until 75% of the cycles, after which there is a renewed increase, which is confirmed by other studies. This pattern reflects the evolution of surface structures, with the power spectral density indicating that, during strain, high wavevectors (small length scales) dominate the roughness changes due to micro-crack growth and material extrusion. These phenomena were further confirmed by an increasing Hurst exponent, suggesting that the surface transitions from anti-persistent to more persistent and correlated as the strain progresses. Furthermore, the study highlights that the surface of unstressed copper conductors is anisotropic and self-affine, while under mechanical strain, it evolves to become more isotropic and self-affine.

In conclusion, this work provides a novel analysis of copper conductor surfaces under mechanical strain, offering valuable insights into the underlying processes of roughness evolution. By employing power spectral density functions, the study demonstrates the critical role of surface characterization in understanding the performance of copper conductors in high-frequency applications.

### AUTHOR CONTRIBUTIONS
C.M. was involved in conceptualization, research design, data interpretation, first draft writing, revision and editing, illustrations, figures, and visualization. P.R. was involved in conducting experiments, collecting data, data interpretation, writing software, writing the first draft, figures, and visualization. A.W., K.K., and G.F. were involved in revising and editing the manuscript, funding, providing equipment and materials, supervision, project management, and final approval.

### ACKNOWLEDGEMENTS
This work was supported by the Carl Zeiss Foundation through the project "Intelligent Composite Materials". Open Access funding enabled and organized by Projekt DEAL.

### CONFLICT OF INTEREST
The authors declare no financial or commercial conflict of interest.

### DATA AVAILABILITY STATEMENT
The data that support the findings of this study are available from the corresponding author upon reasonable request.

### REFERENCES
1.  ...
2.  ...
(Note: References were truncated in the source text, but indicated as [1-40] in the text)