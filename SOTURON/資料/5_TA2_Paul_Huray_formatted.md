# A 53 GHz - 125 GHz Chip to Double-Ridge Rectangular Waveguide Transition

**Authors:** M. Pittermann, T. Zwick and A. Bhutani
**Publication:** ELECTRONICS LETTERS 17th January 2024

---

### Abstract
A novel chip to double-ridge rectangular waveguide transition, with an ultra-broadband operation bandwidth exceeding three standard rectangular waveguide (WR) bands of WR15, WR12 and WR10 is demonstrated for the first time in this letter, to the best of authors knowledge. This bandwidth is achieved by coupling the microstrip mode directly to the fundamental TE mode of the waveguide. A unique feature of this transition is that the transition design can be implemented on substrates with a high dielectric constant, which makes it suitable for integration with monolithic microwave integrated circuits (MMICs). A back-to-back transition is realized using a split-block assembly and 254 µm thickness alumina substrate ($\epsilon_{r}=9.8$ at 80 GHz). The latter acts as an MMIC substrate substitute, including a tapered microstrip and a $50\Omega$ coplanar waveguide pad for probe-based measurement. Two novel mechanical assembly concepts, involving die-attach-foil and indium solder, are used to build two split-block prototypes. The simulated and measured S-parameters of the transition are demonstrated from 35 GHz to 125 GHz.

---

## Introduction
There is an ongoing push for ultrawideband circuits, driven by applications in wireless and optical communication. Monolithic microwave integrated circuits (MMICs) with bandwidths exceeding 300 GHz have recently been demonstrated [1, 2, 3]. At such bandwidths, packaging and interconnects become a key challenge. Due to their low attenuation, metal waveguide split block designs are the gold standard for connecting MMICs, passive elements and antennas. Therefore, a chip-to-waveguide transition with good impedance matching and low insertion loss over a large operational bandwidth is an essential building block for a high-performance waveguide-based split-block MMIC package.

There are several common designs for microstrip-to-waveguide transitions that use radiative elements, for example E-field probes [4, 5] or aperture coupled patches [6]. However, designs with radiative elements have an inherently limited bandwidth, operating only in a single waveguide band. This is sufficient for rectangular waveguides, but higher bandwidth applications require different waveguide geometry and transitions.

Rectangular waveguides are limited in their usable bandwidth by the cutoff frequencies $f_c$ of their fundamental mode $TE_{10}$ and their next-higher mode $TE_{20}$. Below $f_{c,TE_{10}}$ an electromagnetic wave cannot propagate. Above $f_{c,TE_{20}}$ multiple modes with different dispersion characteristics are allowed to propagate, which leads to resonances. Due to their geometry, rectangular waveguides are limited to an operational bandwidth of $f_{c,TE_{20}}/f_{c,TE_{10}}=2$. In practice, only around 70% of the bandwidth is typically used since dispersion or evanescent wave effects can lead to unwanted behavior near the band edges.

Ridged waveguides are used in applications where higher bandwidths are required. One or two ridges create additional capacitive loading which decreases the cutoff frequency of the fundamental mode. The cutoff frequency of their next-higher mode is also slightly increased. By choosing the ridge dimensions accordingly, much greater single-mode bandwidths can be achieved. In addition to the increased bandwidth, the electric field is concentrated between the ridges, which proves useful for the design presented in this letter.

---

## Design
The waveguide transition is implemented on a 254 µm thick Alumina substrate ($\epsilon_{r}=9.8$, $\tan \delta=3\times10^{-2}$ at 80 GHz [7]). Due to the high dielectric constant of the alumina substrate, it serves as a good choice for replicating an MMIC substrate (for example, GaAs has $\epsilon_{r}=13$, $\tan \delta=1\times10^{-3}$ at 100 GHz [8]).

> **[Fig. 1]:** 3D model used for the back-to-back simulation with half of the top split block half cut away. The waveguide taper has a length of 5 mm but is cut short in this illustration. The gap between the ridges measures 0.07 mm at the transition and tapers to 0.35 mm (cut off). The red dot at the near end of the alumina substrate marks the coordinate origin. The probe model, outlined in red, consists of a short stub of $50\Omega$ coax with three needles.
> * Key dimensions: Microstrip length 2 mm, Width 0.25 mm (at tip), Ridge gap 0.07 mm, Signal line width 0.7 mm, Substrate width 2.54 mm, Waveguide height 1.27 mm.

Figure 1 shows the simulation model of the chip-to-double-ridge rectangular waveguide transition. Note that the top-left corner of the double-ridge rectangular waveguide is kept hidden for clarity in representing the transition geometry for the reader. The bottom half of the split-block waveguide ends in a platform that holds the microstrip substrate in a way that positions the microstrip signal line at the mid H-plane of the double-ridge rectangular waveguide. This platform is in direct electrical contact with the metallized bottom of the microstrip substrate. The top half of the waveguide ends at the position where the microstrip substrate begins, i.e., $y=0$ mm. Only the waveguide ridge extends beyond this point and makes contact with the microstrip signal line.

This approach works well because the field configuration of the microstrip quasi-TEM mode is very similar to the dominant TE mode of the ridged waveguide.

> **[Fig. 2]:** Absolute electric field strength $|E_{z}|$ in kV $m^{-1}$ at multiple planes transversal to the microstrip and waveguide. The colors correspond to the magnitude of the electric field in z-direction, the geometry of the alumina substrate and split block are overlaid. $y=0$ mm corresponds to the edge of the alumina substrate.
> * Panels show cross-sections at $y=0.5$ mm, $y=0.2$ mm, $y=0.05$ mm, and $y=-0.05$ mm.
> * The field evolution shows the transition from microstrip mode to the ridged waveguide mode.

Figure 2 shows the evolution of the electric field starting at the microstrip, at two points along the microstrip-ridge overlap and, finally, in the ridged waveguide. At a distance of 0.5 mm from the edge of the alumina substrate, the microstrip mode is virtually undisturbed. The overlap region begins at $y=0.25$ mm. Since the field on top of the microstrip is very weak, the emergence of the waveguide ridge does not disturb the fields significantly. At position $y=0.07$ mm, the fields from the narrow ridge gap are observed to extend outwards, curving into the alumina substrate. The conversion to the final TE mode of the ridged waveguide is very gradual, which makes the bandwidth of this transition very wide. The best matching is achieved when the width of the microstrip matches the width of the waveguide ridge.

The prototype is designed for a maximum frequency of 110 GHz, a return loss of greater than 10 dB and an insertion loss of less than 1 dB. WR10 (75 GHz to 110 GHz) was chosen for the outer dimensions of the rectangular waveguide. The addition of the ridges lowers the cutoff frequency of the fundamental mode to 35 GHz according to numerical simulation. Importantly, approaching the transition, the gap narrows to only 0.07 mm, as seen in Fig. 1.

A microstrip with a signal line width of 0.7 mm on alumina substrate has a characteristic impedance of only $26\Omega$. With the gap of 0.07 mm at the transition, the parallel plate waveguide formed by the ridges (ignoring the rectangular waveguide) has a line impedance of $30\Omega$. The impedance values are estimated on the basis of electromagnetic simulations carried out in CST Studio Suite 2023. This is slightly higher than the impedance of the microstrip, but results in the best matching. The ideal size of the gap is found on the basis of full-wave electromagnetic simulations.

> **[Fig. 3]:** Simulated S-parameters of a single-sided transition, without the microstrip taper (port 1 = waveguide, port 2 = microstrip). At the bottom end, the bandwidth is limited by the cutoff frequency of the waveguide.
> * Graph shows $S_{12}$ (Insertion Loss) and $S_{11}/S_{22}$ (Return Loss) vs Frequency (40-125 GHz).
> * $S_{12}$ is consistently above -0.6 dB except for a resonance at 124 GHz.
> * $S_{11}$ and $S_{22}$ are generally below -10 dB from 40 GHz to 125 GHz.

Figure 3 shows the scattering parameters for the single-sided chip to double-ridge rectangular waveguide transition without ground pads and microstrip taper, simulated using CST Studio Suite 2023. The reflection loss is better than 10 dB from 40 GHz to 125 GHz and better than 15 dB from 43 GHz to 103 GHz. The insertion loss is better than -0.6 dB in the entire frequency range except for a narrow resonance at 124 GHz. The simulation also shows good performance well above 125 GHz. However, at 120 GHz substrate modes and higher order waveguide modes emerge, necessitating thinner substrate and adjustments in the waveguide dimensions for practical use.

The transition was also simulated with a 10 µm air gap between the microstrip and the top ridge, resulting in only a <0.1 dB increase in insertion loss. Besides relaxing the manufacturing tolerances, this enables the integration of a DC-block by filling the air gap with a dielectric.

Since the input and output pads of an MMIC are usually in a ground-signal-ground configuration with an impedance of $50\Omega$, a cosinusoidal microstrip taper of length 12 mm is added to serve as an impedance transformer. The width profile of the microstrip taper is $w(x)=(a+b)/2+(b-a)/2\cdot \cos(\pi x/l)$, $a=0.19$ mm, $b=0.7$ mm. The tapered impedance transformer is connected to a GSG pad, where the ground pads are connected to the microstrip ground plane with vias. The GSG pad provides the benefit that a back-to-back configuration of this chip-to-waveguide transition can be characterized using two GSG probes.

The chip-to-double-ridge rectangular waveguide transition shown in Fig. 1 is manufactured in a back-to-back configuration. The S-parameters of this transition are measured using two GSG probes on either end. Furthermore, the same back-to-back configuration chip-to-waveguide transition, along with two idealized GSG probe tips, is simulated using CST Studio Suite 2023. The measured and simulated S-parameters are shown in Fig. 5.

---

## Fabrication
The double-ridge rectangular waveguide is manufactured using brass in two split-block halves. Due to the geometry of the ridge and to facilitate clamping of the microstrip, the waveguide is split in the H-plane. Since split-block waveguides are very sensitive to contact resistance in the H-plane, two prototypes are built. One prototype uses an electrically conductive die-attach-foil (DAF) with a thickness of 10 µm [9], while the other prototype uses pure indium solder foil with a thickness of 50 µm [10] to minimize the contact resistance between the split-block halves. Simulations predict identical performance for both DAF and indium solder. Additionally, the upper part of the waveguide has relief channels to either side of the waveguide to decrease the contact area with the lower part. This results in increased contact pressure between the waveguide halves.

> **[Fig. 4]:** Assembled back-to-back transition. The 10 mm long double-ridge waveguide section consists of two back-to-back cosinusoidal tapers from a ridge gap of 0.07 mm to 0.35 mm. From the outside, the two samples with die-attach-foil and indium solder look identical. Two dowel pins are used for alignment and four M2 screws fasten the two halves together. Dimensions shown: 20 mm x 15 mm.

The split block halves are machined on a 5-axis micromachining center. After machining, critical dimensions are verified using a white light interferometer. Special attention is paid to the distance between the mating surface of the split block halves and the surfaces that clamp the microstrip. The finished parts are within 3 µm of the nominal dimensions.

Due to the requirement for vias of the microstrip launcher ground pads, the alumina pieces are manufactured in multiple steps: Alumina sheet with a thickness of 254 µm, covered on both sides with gold, is used as the base material. Through-holes are created by a laser prototyping system. Then a thin layer of nickel (100 nm) is deposited via sputtering, followed by a galvanic layer of gold (2 µm). Finally, a laser prototyping system is used to structure the top side and to dice the samples.

For final assembly, DAF or indium solder is applied to the bottom split block half in the areas that contact the top half. Then, DAF is applied to the bottom side of the alumina substrate and the substrate is placed on the bottom split block half. A small piece of DAF is placed on the end of the microstrip, where it contacts the top ridge. The alignment pins are used to precisely place the top split block half on the rest of the assembly. Finally, the assembly is heated to $120^{\circ}C$ for two hours to cure the DAF for the first prototype, whereas the second prototype with indium solder is heated to $200^{\circ}C$ for reflowing. During curing, the screws are re-tightened periodically to ensure good contact pressure. The first prototype using the mechanical assembly concept based on DAF is shown in Fig. 4.

---

## Measurement and Results
The measurements are performed using a Keysight N5247B network analyzer and N5295A broadband frequency extender modules. Two microwave probes are used to contact the device. The setup is calibrated at the probe tips with a short-open-load-through (SOLT) calibration on an impedance standard substrate.

The measured scattering parameters of the first and second prototype based on DAF and indium solder, respectively along with the simulation results are shown in Fig. 5. Both samples exhibit very similar scattering parameters and the insertion loss lies within 1 dB to 2 dB in the frequency range of interest. Periodic resonances in the reflection loss, spaced by about 13 GHz, indicate reflections at the ends of the 10 mm long waveguide section. Except for a slightly higher loss, the simulations match the measured scattering parameters very well. The DAF sample has no reflections exceeding 10 dB between 53 GHz and 125 GHz, a bandwidth of 1:2.3.

> **[Fig. 5]:** Measured S-parameters of the two back-to-back samples. The device is probed with the calibration plane at the probe tips. Since the microstrip taper, ground pads and probe tips are included in the back-to-back simulation as well, the performance is slightly worse than what could be expected from Fig. 3.
> * Top Graph: $S_{12}$ in dB vs Frequency (40-120 GHz). Comparison of B2B Simulation, Meas. DAF, and Meas. Indium. Values mostly between -1 dB and -2 dB.
> * Bottom Graph: $S_{11}$ in dB vs Frequency (40-120 GHz). Comparison of B2B Simulation, Meas. DAF, and Meas. Indium. Values generally below -10 dB.

Table 1 compares the presented chip-to-double-ridge rectangular waveguide transition with microstrip/CPW to rectangular waveguide transitions operating at similar or higher frequencies that have been reported in literature to date. The previously demonstrated transition designs have a much smaller bandwidth, all limited to a single standard waveguide band, whereas the transition presented in this letter demonstrates the largest operating bandwidth of 53 GHz to 125 GHz, which translates to a relative bandwidth of 1:2.3. Regarding insertion loss, this transition also performs similar or better than other designs for 75 to 110 GHz. No complex assembly steps such as wire bonding [4] or fabrication of very thin features [12] is necessary.

| Method | Ref. | f (GHz) / BW | IL (dB) |
| :--- | :--- | :--- | :--- |
| **This work** | | **53-125 / 1:2.3** | **1-2** |
| double ridge wire bond | [4] | 140-220 / 1:1.6 | 3-5 |
| quartz probe | [5] | 140-220 / 1:1.6 | 2.9 |
| inline dipole | [11] | 340-380 / 1:1.1 | 6 |
| thin ridge | [12] | 75-110 / 1:1.5 | 3.5 |
| ridge | [13] | 75-110 / 1:1.5 | 1-3 |
| single ridge stepped | [14] | 60-90 / 1:1.5 | 1.5-2.7 |

*Table 1: Comparison of microstrip/CPW to waveguide transitions presented in other works. The bandwidth is defined by $S_{11} \le -10$ dB in this context. All designs are housed in a CNC machined split block assembly. All characteristics are for a back-to-back transition.*

---

## Conclusion
In this work, a novel direct chip-to-double-ridge rectangular waveguide transition is presented for the first time. The transition establishes a direct connection between a microstrip signal line and the ridges of a double-ridge rectangular waveguide in its H-plane. This feature gives the transition a distinct advantage over previously demonstrated chip-to-waveguide transitions based on radiating elements. Implemented on a high dielectric constant alumina substrate, the design is well-suited for integration into an MMIC substrate.

Two prototypes, employing different mechanical assembly concepts using a die-attach-foil and indium solder, have been successfully realized in a back-to-back configuration. The measured S-parameters of these prototypes exhibit excellent agreement with their electromagnetic simulation results. Operating over a broad bandwidth from 53 GHz to 125 GHz, covering three standard waveguide bands (WR15, WR12, and WR10), the transition demonstrates a return loss better than 10 dB and a single-sided insertion loss of less than 1 dB across the entire operational bandwidth.

---

### Acknowledgment
The authors acknowledge the financial support by the Federal Ministry of Education and Research of Germany in the projects "ForMikro 2.0 - ECLIPSE" (grant number: 16ME0913) and "Open6GHub" (grant number: 16KISK010). Furthermore, the authors thank A. Lipp for his help with indium soldering and assembling the prototypes.

**Affiliation:** M. Pittermann, T. Zwick, A. Bhutani (Institute of Radio Frequency Engineering and Electronics (IHE), Karlsruhe Institute of Technology (KIT), 76131 Germany)
**E-mail:** martin.pittermann@kit.edu

### References
1.  Thome, F., Leuther, A.: First demonstration of distributed amplifier mmics with more than 300-ghz bandwidth. IEEE Journal of Solid-State Circuits 56(9), 2647-2655 (2021). doi:10.1109/JSSC.2021.3052952
2.  Baeyens, Y., Mansha, M.W., Rücker, H.: A single-stage low-noise sige hbt distributed amplifier with 13 dbm output power and 20 db gain in d-band and over 170 ghz bandwidth. In: 2022 17th European Microwave Integrated Circuits Conference (EuMIC), pp. 52-55. (2022)
3.  Tang, D., et al.: An ultra-wideband amplifier with a novel non-distributed butterfly topology achieving 2-250 ghz bandwidth and 4.67 thz gbw in 130nm sige bicmos. In: 2023 IEEE Custom Integrated Circuits Conference (CICC), pp. 1-2. (2023)
4.  Stärke, P., Carta, C., Ellinger, F.: Direct chip-to-waveguide transition realized with wire bonding for 140-220 ghz g-band. IEEE Transactions on Terahertz Science and Technology 10(3), 302-308 (2020). doi:10.1109/TTHZ.2020.2971690
5.  Tessmann, A., et al.: 220 ghz low-noise amplifier modules for radiometric imaging applications. In: 2006 European Microwave Integrated Circuits Conference, pp. 137-140. (2006)
6.  Lee. H.Y., et al.: Wideband aperture coupled stacked patch type microstrip to waveguide transition for v-band. In: 2006 Asia-Pacific Microwave Conference, pp. 360-362. (2006)
7.  Kato, Y., Horibe, M.: Permittivity measurements and associated uncertainties up to 110 ghz in circular-disk resonator method. In: 2016 46th European Microwave Conference (EuMC), pp. 1139-1142. (2016)
8.  Xu, H., et al.: Electromagnetic characterization techniques for dielectric materials at millimeter-wave range. In: 2023 International Conference on Microwave and Millimeter Wave Technology (ICMMT), pp. 1-3. (2023)
9.  The Furukawa Electric Co. Ltd. Electrically/thermally conductive dicing die attach film. https://www.furukawa.co.jp/uvtape/en/technology/cdaf.html (accessed February 12, 2024)
10. Indium Corporation: Product data sheet solder ribbon and foil. https://www.indium.com/technical-documents/product-data-sheets/download/564/ (2023, accessed February 12, 2024)
11. Leong, K.M.K.H., et al.: A 340-380 ghz integrated ch-cpw-to-waveguide transition for sub millimeter-wave mmic packaging. IEEE Microwave and Wireless Components Letters 19(6), 413-415 (2009). doi:10.1109/LMWC.2009.2020043
12. Shireen, R., et al.: A w-band transition from coplanar waveguide to rectangular waveguide. In: 2008 IEEE Antennas and Propagation Society International Symposium, pp. 1-4. (2008)
13. Wang, C., et al.: A wideband contactless cpw to w-band waveguide transition. IEEE Microwave and Wireless Components Letters 29(11), 706-709 (2019), doi:10.1109/LMWC.2019.2945242
14. Hannachi, C., Djerafi, T., Tatu, S.O.: Broadband e-band wr12 to microstrip line transition using a ridge structure on high-permittivity thin-film material. IEEE Microwave and Wireless Components Letters 28(7), 552-554 (2018). doi:10.1109/LMWC.2018.2835475