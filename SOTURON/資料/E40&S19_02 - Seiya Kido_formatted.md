# Influence of Copper Conductor Surface Treatment for High Frequency PCB on Electrical Properties and Reliability

**Seiya Kido, Tsuyoshi Amatani**
MEC Company LTD.
Amagasaki, Hyogo, Japan

---

## Abstract

Development of information and the telecommunications network has been outstanding in recent years, and it is required for the related equipment such as communication base stations, servers and routers, to process huge amounts of data in short periods of time. As an electrical signal becomes faster and faster, how to prevent signal delay by transmission loss is a big issue for Printed Circuit Boards (PCB) loaded on such equipment. There are two main factors as the cause of transmission loss; dielectric loss and conductor loss. To decrease the dielectric loss, materials having low dielectric constant and low loss tangent have been developed. On the other hand, reducing the surface roughness of the copper foil itself to be used or minimizing the surface roughness by modifying the surface treatment process of the conductor patterns before lamination is considered to be effective in order to decrease the conductor loss. However, there is a possibility that reduction in the surface roughness of the conductor patterns will lead to the decrease in adhesion of conductor patterns to dielectric resin and result in the deterioration of reliability of PCB itself. In this paper, we will show the evaluation results of adhesion performance and electrical properties using certain types of dielectric material for high frequency PCB, several types of copper foil and several surface treatment processes of the conductor patterns. Moreover, we will indicate a technique from the aspect of surface treatment process in order to ensure reliability and, at the same time, to prevent signal delay at the signal frequency over 20 GHz.

---

## Introduction

### Background

Recent developments of information and telecommunications network technologies are remarkable. Especially, it is important for related devices such as base station, servers and routers to process large amount of information instantaneously for the development of IoT in the future. With increase in data transfer rates and amounts, signal delay by transmission loss has become a big issue for PCB. Therefore, prevention of signal transmission loss is important to high frequency PCBs.

### Factor of Transmission Loss

Transmission loss can be separated into dielectric loss and conductor loss. Dielectric loss is influenced by the dielectric properties (dielectric constant ($\epsilon_r$) / dissipation factor ($tan\delta$)) of insulation materials, and it increases in proportion to the frequency ($f$). Conductor loss is influenced by the size or kind of conductor, and it increases in proportion to the square root of frequency ($f$). The more frequency increases, the more signal concentrates on the copper surface. Consequently, the area of current flow is limited (Skin effect loss). Furthermore, if conductor surfaces are rough, the transmission loss is bigger than that of the flat surface. It is because current flow is inhibited by the conductor surface roughness (Surface roughness effect loss).

### Adhesion Performance for Reliability

To ensure the reliability of PCB product, adhesion between copper conductors and insulation materials is especially important. Generally, conventional copper surface treatment such as chemical roughening has been used to ensure the adhesion by etching (anchoring effect). However, it does not be apply to high-speed or high-frequency applications due to transmission loss of signal. To solve these problems of conventional copper surface roughening treatment, MEC has developed a copper surface treatment process as the flat bonding treatment (FB treatment) process specialized for high-speed PCBs. Even though the FB treatment process contains neither chemical etching process nor chemical roughening process, it can ensure the adhesion between copper conductors and insulation materials with its smooth and profile free surface.

---

## FB Treatment Process

> **[Figure 1: FB treatment process flow]**
> The diagram illustrates the three steps of the FB treatment:
> 1.  **Acid Treatment:** Surface Cleaning of Copper.
> 2.  **Tin Alloy:** Metal layer Forming on Copper.
> 3.  **Coupling Treatment:** Anti-tarnish Layer Forming on top of the Metal layer.

Figure 1 is the FB treatment basic process flow.

### Acid Cleaning

The purpose of acid treatment is a cleaning of copper surfaces by removing foreign materials, stains or oxide existing on the surface to conduct subsequent FB treatment appropriately. Depending on the degree of staining on the copper surface, acid treatment such as sulfuric acid is generally applicable.

### Tin Alloy (Chemical-A)

By conducting Chemical-A treatment, a very thin metal layer is formed on copper surface. Figure 2 shows the depth analysis result of copper surface treated with Chemical-A by X-ray Photoelectron Spectroscopy (XPS). The constituent elements of the Chemical-A metal layer are mainly tin, copper and very small amounts of metal A. According to Figure 2, it is also found that the thickness of Chemical-A layer is very thin at around 50~100nm. The base chemical of Chemical-A treatment is electroless tin plating chemical, nevertheless the Chemical-A can be used more stably in the production condition compared to the conventional electroless tin plating chemical. Because the air oxidization of stannous ion ($Sn^{2+} \rightarrow Sn^{4+}$ which occurs in conventional electroless tin plating) does not occur in the case of Chemical-A. In addition, since the chemical can induce copper and metal A into the layer, this Chemical-A treatment can be called as a 'functional electroless tin plating chemical'.

> **[Figure 2: XPS depth analysis of copper surface treated Chemical-A]**
> A graph showing Atomic% vs Ar sputtering time (sec).
> * At 0 sec (surface): Carbon (C) and Oxygen (O) are high.
> * As sputtering time increases (going deeper): Copper (Cu) rises sharply to ~90%. Tin (Sn) starts around 20% and decreases. Metal A is present in small amounts near the surface.
> * The data indicates a layer thickness of approximately 50-100nm (based on 20nm/min $SiO_2$ rate).

### Coupling Treatment (Chemical-B)

By conducting Coupling treatment (Chemical-B), the anti-tarnish layer is formed on the tin alloy metal layer. This layer can perform as both an anti-tarnish and a coupling effect between tin alloy layer and the insulation resin (Figure 3). The coupling layer bonds covalently to the metal surface of the tin alloy layer and also links strongly to insulation resin. This is because functional group R2 in coupling layer reacts with functional group R3 in the insulation resin. Especially, the functional group R2 in coupling layer is important to deliver high adhesion performance. In this way, FB treatment process (Tin alloy + Coupling treatment) can achieve high adhesion performance by choosing the proper functional group to low dielectric resin. In general, it is known that operating this kind of coupling chemicals stably is difficult due to the self-condensation. In the case of Chemical-B, however, the stability of the chemical is enhanced by its molecular structure. Therefore, the Chemical-B also can be used stably in the mass-production condition.

> **[Figure 3: Bonding model of FB treatment layer]**
> * **Layer Structure:** Copper Base -> Tin Alloy Layer -> Coupling Layer (Silane based) -> Resin.
> * **Chemical Bonding:** Shows $-Si-O-Si-O-$ bonds attached to the Tin Alloy Layer.
> * **Coupling:** Functional groups $R_2$ from the coupling layer bond with functional groups $R_3$ in the Resin.

### Surface Topography of Copper Treated with FB Treatment

We observed copper surface treated with FB treatment by using Scanning Electron Microscope (SEM). Figure 4 is the topography images with SEM observation with 3,500 magnification of i) plated copper without surface treatment as a reference, ii) copper surface treated with FB treatment process, and iii) copper surface treated with our conventional chemical which forms a rough copper surface. According to Figure 4, the copper surface treated with FB treatment is smoother than that of chemical roughening and as flat as plated copper surface without treatment.

> **[Figure 4: Surface topography comparison]**
> SEM images comparing three surfaces:
> 1.  **Untreated Copper:** Smooth surface.
> 2.  **FB Treatment:** Smooth surface, very similar to untreated.
> 3.  **Our Chemical Roughening:** Highly textured, rough surface with visible nodules.

### Surface Roughness after FB treatment

Table 1 is the surface roughness value ($Ra$ and $Rz$) of the FB treatment layer. According to Table 1, it is confirmed that surface roughness of FB treatment layer is not roughened and almost the same as the plated copper without treatment.

**Table 1 - Surface roughness comparison**

| Parameter | Untreated Plated Cu | FB Treatment | Our Chemical Roughening |
| :--- | :--- | :--- | :--- |
| $Ra(\mu m)$ | 0.04 | 0.04 | 0.21 |

### Copper Pattern Width after FB Treatment

We also observed the copper pattern before and after the FB treatment by SEM. Figure 5 are the observation results of copper conductor pattern $L/S=50/50\mu m$. According to Figure 5, pattern width hardly changed before and after FB treatment.

> **[Figure 5: Copper pattern SEM images]**
> Angled SEM views of copper lines ($L/S=50/50\mu m$).
> * **Before FB Treatment:** Clean lines.
> * **After FB Treatment:** Lines remain clean with no visible reduction in width or surface degradation.

---

## Methodology/Experimental

### Transmission Loss Evaluation

To confirm the transmission performance of copper conductor treated with FB treatment, we measured the insertion loss of the signal data of copper conductor treated with FB treatment comparing to that of conventional surface roughening treatment. We used the test coupons which have strip-line structure like Figure 6 to measure insertion loss. The details of test coupons are listed as below.

* **Copper foil:** H-VLP foils (35$\mu m$ thickness)
* **Inner layer copper surface treatment:** 1) FB treatment, 2) Chemical roughening treatment
* **Laminated resin:** Low dielectric resin A (PPE type, $\epsilon=3.7$, $tan\delta=0.002$ at 1GHz, CCL thickness 0.13mm, prepreg thickness 0.06mm×2 sheets)
* **Circuit length:** 200mm
* **Impedance:** $50\Omega$

For the copper surface treatment, we applied FB treatment and surface roughening treatment. The S21 parameters were measured on a network analyzer up to 50GHz of frequency.

> **[Figure 6: Test coupon design image]**
> Cross-section diagram of a Stripline structure.
> * Central conductor: Copper (35$\mu m$ thickness, 0.28mm width).
> * Surrounded by dielectric material (Mat-Side).
> * Top and Bottom ground planes: Chemical Surface Treatment applied.

### Adhesion Performance (Peel Strength)

We used peel strength as a parameter of adhesion between the copper surface treated with FB treatment and the low dielectric resins (prepregs). We measured peel strength according to JIS (Japan Industrial Standard) C 6481. Copper materials were 35$\mu m$ thickness standard copper foils with each chemical treatment. Our copper surface roughening treatment was used for reference. They were pressed with the prepregs by a vacuum-heated press machine, after that the copper foils were peeled in 10mm widths with the peel tester.
*(Note: Absolute values of the peel strength vary, depending on the following factors: storage condition of resins, pressing conditions, measuring conditions and so on. We evaluate the peel strength as an inter-comparison between evaluation samples.)*

We used two types of low dielectric commercial materials (resin A and resin B) for high-frequency applications (prepregs) in this evaluation. Below are details of Resin A and B.

* **Low dielectric resin A:** PPE type $\epsilon=3.7$, $tan\delta=0.002$ at 1GHz
* **Low dielectric resin B:** PPE type $\epsilon=3.6$, $tan\delta=0.0015$ at 1GHz

---

## Results

### Transmission Loss Evaluation

Figure 7 shows insertion loss of signal data of copper conductor treated with FB treatment compared to that of conventional surface roughening treatment. Insertion loss of FB treatment was lower than that of the chemical roughening treatment and almost the same as untreated copper conductor. The difference of insertion loss between FB treatment and chemical roughening became bigger in accordance with increase in frequency. According to this result, it is found that the FB treatment process delivered superior performance for transmission loss over 20GHz. It is because the conductor surface treated with FB treatment is flat and hardly affected by surface roughness effect loss.

> **[Figure 7: Transmission loss of signal data]**
> A graph of S21 (dB/m) vs Frequency (0.0 to 50.0 GHz).
> * **FB Treatment (Black line):** Shows less signal loss (line is higher). At 50GHz, loss is around -105 dB/m.
> * **Our Chemical Roughening (Grey line):** Shows more signal loss (line is lower). At 50GHz, loss is around -120 dB/m.

### Peel Strength

Figure 8 is the result of the peel strength measurements. From this result, it is confirmed that the adhesion performance of copper surface treated with FB treatment process for both the low dielectric Resin A and Resin B is higher than that of our conventional roughening treatment even though the FB treatment surface is not roughened or etched.

> **[Figure 8: Adhesion performance for low dielectric Resin A and Resin B (Peel strength)]**
> Bar chart comparing Peel Strength [N/mm].
> * **Our Chemical Roughening:** Resin A ~0.35 N/mm, Resin B ~0.42 N/mm.
> * **FB Treatment:** Resin A ~0.69 N/mm, Resin B ~0.77 N/mm.
> * Result: FB Treatment provides approximately double the peel strength of roughening.

### Peel Strength after Multiple Reflow Testing

Figure 9 shows peel strength evaluation results of FB treatment process after multiple reflow testing ($260^\circ C$). According to Figure 9, the peel strength of FB treatment does not change even after 10 times reflow.

> **[Figure 9: Adhesion performance for low dielectric resin A after reflow testing (Peel strength)]**
> Bar chart comparing Initial vs Reflow 5 times vs Reflow 10 times.
> * **Our Chemical Roughening:** Strength drops from ~0.38 (Initial) to ~0.29 (Reflow 5x) and ~0.28 (Reflow 10x).
> * **FB Treatment:** Strength remains stable at ~0.70 for Initial, Reflow 5x, and Reflow 10x.

---

## Conclusions

The company developed a new surface treatment process (FB treatment process) on copper conductor for high-speed and high-frequency PCBs. As mentioned above, the FB treatment process achieved superior performance for transmission loss over 20GHz frequency, and its adhesion performance for low dielectric resins was confirmed as superior to that of our surface roughening treatment. FB treatment process improved the transmission loss of signals especially in the high frequency region, in which roughening treatments have problems for transmission loss. Furthermore, it can deliver the high adhesion performance for low dielectric resins with smooth and profile free surfaces. In the future, technologies of electric devices related to base stations, servers and routers will grow more and more for the development of information and telecommunications network such as IoT. Accordingly, the requirement for the high-speed and high-frequency applications should increase more and more. We believe that our FB treatment process will help solve the issues of signal transmission loss and improve the reliability of advanced PCBs.

---

# Presentation Slides (IPC APEX EXPO 2017)

**Influence of Copper Conductor Surface Treatment for High Frequency PCB on Electrical Properties and Reliability**
*Seiya Kido, MEC Company LTD.*

## Agenda
* Introduction
* Flat Bonding Process (FB Treatment Process)
* Transmission Property
* Adhesion Performance
* Adhesion Mechanism
* Conclusion

## Introduction

### Data Traffic Increase
> **[Graph: Data Traffic Increase]**
> A bar chart showing global mobile data traffic (BH-Tbyte) from 2009 to 2021.
> * The trend shows an **Explosive Increase** (Yellow Arrow).
> * 2017: ~700.
> * 2021 (Projection): ~4600.
> * Reference: [1] Trends of 5G mobile communication systems and activities, SoftBank Co.

### Development of Telecommunication
Visuals: Laptop, Cloud Server, Security Camera, Phone, Base Station antenna.

### Adhesion Interface between Metal/Resin in PCB
Diagram showing a PCB cross-section:
* Cu/Solder Mask
* Cu/Via-fill resin
* Cu/Build-up resin
* Cu/Prepreg
* **Current Adhesion Technology:** Physical Bonding by Roughening Copper Surface.

### Potential Issues of Current Technology
1.  **Transmission Loss:**
    * Table: Relation between Frequency and Skin Depth.
    
    | Frequency (GHz) | Cu Skin Depth ($\mu m$) |
    | :--- | :--- |
    | 1 | 2.09 |
    | 5 | 0.93 |
    | 10 | 0.66 |
    | 30 | 0.38 |
    | 50 | 0.30 |
    
    * **Issue 1:** Increase of signal transmission loss by surface roughness as frequency increases (Skin depth becomes smaller than roughness).

2.  **Adhesion on Smooth Copper:**
    * Rough Copper Surface = Good Adhesion.
    * Flat Copper Surface = Low Adhesion with insulation resin.
    * **Issue 2:** Low adhesion with insulation materials due to smooth copper surface required for signal integrity.

### Development of New Surface Treatment
* **Current:** Physical bonding by surface roughening.
    * Issue 1: Transmission loss.
    * Issue 2: Low adhesion on smooth surfaces.
* **Future:** **Flat Bonding (FB) Treatment**.
    * Profile free surface for high transmission property.
    * High adhesion performance with insulation materials.

## FB Treatment Process Flow

1.  **Pre-Treatment (Acid Cleaning):** Clean Copper Surface.
2.  **Form Metal Layer (Chemical-A):** Forms Tin Alloy (Cu/Sn/Metal-A Alloy) Layer.
3.  **Form Anti-Tarnish Layer (Chemical-B):** Forms Anti-Tarnish Layer.

### Surface Topography & Roughness (Ra)
Comparison of surfaces:

| Type | Untreated Plated Copper | FB Treatment | Our Chemical Roughening |
| :--- | :--- | :--- | :--- |
| **Image** | Smooth | Smooth | Rough/Nodular |
| **Ra ($\mu m$)** | **0.04** | **0.04** | 0.21 |

* **Conclusion:** FB treatment provides smooth and profile free surface.

### Copper Pattern before/after FB Treatment
SEM Images ($L/S=50\mu m$) show no change in line width or quality after FB treatment.

## Transmission Property

### Measuring Method
* **Base construction:** Stripline.
* **Copper Type:** HVLP (35$\mu m$), 0.28mm width.
* **Inner Treatment Types:**
    1.  #1 Untreated Copper
    2.  #2 FB Treatment
    3.  #3 Black Oxide
    4.  #4 Our Chemical Roughening 1.5$\mu m$
    5.  #5 Our Chemical Roughening 2.5$\mu m$
* **Laminated Resin:** Low Dielectric Resin A (PPE type, $\epsilon=3.7$, $tan\delta=0.002$ at 1GHz).
* **Evaluation Method:** S21 Measurement by Network Analyzer (0-50GHz).

### Surface Topography of Inner Treatment
* **#1 Untreated:** Smooth.
* **#2 FB Treatment:** Smooth.
* **#3 Black Oxide:** Micro-roughness.
* **#4 Chemical Roughening 1.5$\mu m$:** Rough.
* **#5 Chemical Roughening 2.5$\mu m$:** Very Rough.

### Results of Insertion Loss
* **0GHz - 50GHz:**
    * FB Treatment (Red) tracks closely with Untreated Copper (Yellow).
    * Black Oxide (Black) shows higher loss.
    * Chemical Roughening 1.5$\mu m$ (Light Green) and 2.5$\mu m$ (Dark Green) show the highest loss.
* **20GHz - 50GHz (Zoomed):**
    * The divergence increases significantly at higher frequencies.
    * FB Treatment maintains superior performance compared to roughening methods.

## Adhesion Performance

### Measuring Method
* **Resin Type:** Resin A ($\epsilon=3.7, tan\delta=0.002$), Resin B ($\epsilon=3.6, tan\delta=0.0015$).
* **Copper Foil:** Electro-deposited foil (35$\mu m$).
* **Surface Treatment:** a) Our Chemical Roughening, b) FB Treatment.
* **Items:** Peel Strength, Delamination.

### Peel Strength Results
* **Initial:**
    * Chemical Roughening: ~0.35-0.45 N/mm.
    * FB Treatment: ~0.70-0.78 N/mm. (Superior)
* **After Reflow ($260^\circ C$):**
    * Chemical Roughening drops after 5/10 cycles.
    * FB Treatment remains stable after 5/10 cycles.

### Delamination TEST
Condition: $PCT(121^\circ C, 100\%RH, 2atm)$ 8 hrs $\rightarrow$ Solder Dip 30sec.

| Treatment | $260^\circ C$ | $270^\circ C$ | $280^\circ C$ | $290^\circ C$ |
| :--- | :--- | :--- | :--- | :--- |
| **Our Chemical Roughening** | Pass | Pass | Fail | Fail |
| **FB Treatment** | Pass | Pass | Pass | Pass |

* FB Treatment shows better thermal resistance.

## Adhesion Mechanism

**Q: Why can FB treatment process deliver High Adhesion Performance with its Smooth Surface?**

### 1. Physical Bonding (Nano-scale)
* **Untreated Plated Copper:** Smooth at x100,000 mag.
* **FB Treatment:** At x100,000 mag (FE-SEM), **~100nm Minute Holes** are visible.
* This provides nano-scale Physical Bonding.

### 2. Chemical Bonding (Coupling Agent)
Chemical-B contains a Silane Coupling Agent.

**Mechanism:**
1.  **Hydrolysis:**
    $$R_2-Si(OR_1)_3 + 3H_2O \rightarrow R_2-Si(OH)_3 + 3R_1OH$$
    (Silane alkoxide hydrolyzes to silanol)

2.  **Adsorption (Hydrogen Bonding):**
    Silanol groups ($Si-OH$) form hydrogen bonds with hydroxyl groups ($-OH$) on the Tin Alloy surface.

3.  **Dehydration Condensation (Covalent Bonding):**
    $$-Si-OH + HO-Surface \rightarrow -Si-O-Surface + H_2O$$
    Forms a covalent metalloxane bond.

> **[Adhesion Mechanism Model]**
> * **Tin Alloy Layer** at the bottom.
> * **Coupling Layer:** Forms chemical bonds ($Si-O-Sn$) with the metal and presents functional groups ($R_2$) upwards.
> * **Resin:** Functional groups ($R_3$) in the resin react with $R_2$.
> * **Result:** High adhesion via Chemical Bonding + Physical Bonding (nano-holes).

## Conclusion

**New Surface Treatment <Flat Bonding (FB) Process>**
* Profile free surface.
* Copper pattern reduction is very limited.
* High adhesion performance with insulation materials.

**Performance of FB Treatment**
* FB treatment process can decrease the signal transmission loss at high frequency region because of its profile free surface.
* FB treatment process can deliver sufficient adhesion strength for low dielectric resin, even though the treated surface is flat.
* Both chemical bonding and physical bonding are contributing for the high adhesion performance, which are derived by the covalent bonding of coupling effect and the nano-scale minute structure.