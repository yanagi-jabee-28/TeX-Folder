# サブテラヘルツ帯材料計測技術

**出典**: 18_167.pdf  
**著者**: 加藤悠人（Yuto Kato）  
**所属**: 国立研究開発法人産業技術総合研究所  
**出版**: 通信ソサイエティマガジン No.70 秋号 2024  

---

## 1. はじめに

近年、高速大容量の無線通信を可能にするミリ波・サブテラヘルツ波帯電磁波の利用が急速に拡大している。次世代通信の6Gでは5G以上の高速大容量通信を実現するために100 GHz超の周波数帯の利用が見込まれている。

### 1.1 課題背景

一般に回路の伝送損は周波数が上がるほど増大する一方で、6Gでは5Gの1/100の超低消費電力性能が目指されているため、低損失化に向けた先端材料開発が6G実現の鍵となっている。

### 1.2 損失要因

高周波回路では、以下の損失要因により回路全体の伝送損が決まる：

1. **誘電損**: 誘電体基板の複素誘電率で決まる
2. **導体損**: 金属線路の導電率で決まる
3. **放射損**: 回路構造などで決まる

低損失化には、低損失な誘電体基板と金属線路の使用により、誘電損と導体損の両者を低減することが不可欠である（図1参照）。

### 1.3 ミリ波帯での問題

5Gや6Gで使用されるミリ波帯では、金属線路と誘電体基板の接着性を保持するための誘電体表面の粗化による実効的な導電率の低下が問題となっている。

### 1.4 材料開発の必要性

回路基板材料の開発にあたっては：

- 材料の低誘電率・低誘電正接化
- 表面に高導電率の金属層を形成する実装プロセス技術の確立

が一般に必要となり、ミリ波帯を含む広帯域での高精度な複素誘電率・導電率計測技術が強く求められている。

---

## 2. 共振器法の概要と高周波化の課題

高周波の材料評価技術には様々な方法が提案されており、各方法は周波数帯や測定する材料の特性に応じて使い分けられている。

### 2.1 計測方法の分類

#### 反射伝送法
- **用途**: 高損失材料の複素誘電率評価に利用

#### 共振器法
- **用途**: 低損失材料の複素誘電率を高感度・高精度に計測する方法として利用
- **原理**: 材料が封入された共振器に特定の電磁界モードを励振させ、その共振周波数と無負荷Q値を評価することで材料の複素誘電率を測定

### 2.2 従来の共振器法の限界

多くの共振器法では基本モードを利用した測定に制限されており：

- 基本的には一つの共振器で単一周波数の測定しか行えない
- 測定周波数を高周波化するには周波数と反比例した共振器の小形化が必要
- 共振器や誘電体材料の加工精度の問題から、およそ80 GHz超での適用は困難

### 2.3 高次モード利用の課題

共振器の高次モードを利用して複数周波数で測定するためには：

- モードの同定が困難
- モード間の干渉による波形ひずみの問題
- 材料評価に利用しない不要モードの抑制が必須

---

## 3. 平衡円板共振器法による複素誘電率計測技術

### 3.1 概要

特定の共振モードを選択的に励振させることで、複数周波数かつ広帯域での材料評価を実現し、サブテラヘルツ波帯での適用も可能な方法として以下が開発されている：

- **平衡円板共振器法** (balanced-type circular disk resonator, BCDR)
- **ファブリペロー共振器法** (Fabry-Perot resonator, FPR法)

### 3.2 装置構成

平衡円板共振器の構成（図3参照）：

- 同一の厚さと比誘電率・誘電正接を持つ誘電体シートを2枚用意
- 2枚のシートサンプルの間に厚さ0.06 mmの銅はく円板を挟む
- これらを2枚の銅板で挟む
- 銅板の中央に位置する上下の励振孔から同軸線路で励振し、透過を検出

### 3.3 特徴

平衡円板共振器の主な特徴は2点ある：

#### 特徴1: 超広帯域計測
- モードの選択的励振と励振孔まで考慮した厳密な電磁界解析の確立により、単一の共振器で10 GHz程度から100 GHz超にわたる超広帯域での複素誘電率計測が可能

#### 特徴2: 測定周波数の可変性
- 使用する銅はく円板の直径を変えることで、同一の誘電体サンプルに対して異なる周波数における測定が可能
- 円板径の調整により特定の周波数に合わせた測定を実現可能

### 3.4 動作原理

シートサンプルで構成された誘電体共振器に対し、励振孔からの励振と構造の対称性から：

- 特定の測定モードのみが選択的に励振される
- 他の不要モードは十分に抑制される
- 不要モードの影響を受けることなく、高次モードを含めてモードの励振を複素誘電率計測に利用
- 各共振周波数と無負荷Q値の測定値から、その周波数における材料の複素誘電率を決定

### 3.5 計算方法

複素誘電率の計算において、励振孔まで厳密に考慮されたMode-matching法による電磁界解析が利用される。

**注**: 本方法ではTMモードを利用するため、電界の向きはシート材料に垂直であり、面直方向の複素誘電率が測定される。

### 3.6 周波数可変性の例

異なる円板径に対応する平衡円板共振器を用いたシクロオレフィンポリマー（COP）の評価結果：

- 銅はく円板直径 (D): 9, 12, 15, 18, 21 mm
- シート厚さ: 0.254 mm
- 結果: 共振周波数の位置は円板径に応じてシフトしており、円板径を変えると異なる周波数での材料評価が実現される

### 3.7 測定可能な上限周波数

上限周波数は以下の2つの要因で決まる：

1. **同軸励振線のカットオフ周波数**
   - 従来型（1 mm同軸励振線）: 約130 GHz

2. **誘電体シートからの電磁波放射のカットオフ周波数**
   - 式: $f_c = \frac{c}{2\pi\sqrt{\varepsilon_r}} t$
   - 例: $t = 0.2$ mm, $\varepsilon_r = 2$ の場合、カットオフ周波数は230 GHzに達する
   - 低誘電率の薄膜シートサンプルに対しては、同軸線のカットオフ周波数が平衡円板共振器法の上限周波数を決定

### 3.8 高周波化への対応

より高周波での計測を実現するため：

- 0.6 mm同軸線路を給電部に用いた平衡円板共振器を開発
- 最大170 GHzまでの材料評価を実証
- Dバンド導波管（WR-6.5）インタフェースを実装
- 同軸−導波管変換を励振構造内部に実装

測定周波数は導波管バンドの110 GHzから170 GHzに制限されるものの、共振器の堅ろう性が確保される。現在、最大330 GHzまでの材料評価が可能な平衡円板共振器の研究開発が進められている。

---

## 4. 平衡円板共振器法による導電率計測技術

### 4.1 従来技術の課題

金属導電率計測には低損失誘電体の誘電率計測と同じく共振器法が利用されるが：

- 従来の導電率計測では極小の誘電体柱からなる共振器が必要
- 誘電体柱のサイズで決まる単一周波数のみでの測定しか不可能
- 誘電体柱や励振機構の加工精度などの制限により、6Gで利用される100 GHz超のミリ波帯で金属導電率を簡便かつ高精度に計測する技術は確立されていなかった

### 4.2 新しい測定法

平衡円板共振器法の導電率計測への展開により：

- 誘電体の精密な機械加工を必要としない簡便な測定系
- 10 GHz程度から100 GHz超にわたる超広帯域での金属導電率計測を実現

### 4.3 装置構成

#### 金属導電率計測
図6（a）に示すように、同一の低損失誘電体シートと異種の金属円板を組み合わせた2構成の平衡円板共振器を用いる：

1. 導電率が既知の基準銅円板から成る共振器
2. 測定対象の金属円板から成る共振器

両者について無負荷Q値を測定することで、被測定金属円板の導電率を決定できる。

#### 界面導電率計測
誘電体シートに円形金属パターンを形成することで、誘電体と金属層の間の界面導電率を評価することも可能（図6（b）参照）。

### 4.4 銅はく導電率計測の例

高周波回路材料として使用される銅はくの導電率測定結果：

**背景**:
- 回路基板に使用される銅はくは、アンカ効果によって誘電体基板との接着性を強化するため、片面が粗化されている
- 粗化処理は、銅原はくの上に金属粒子をメッキすることで行われる
- 6G周波数帯では表皮厚さがサブミクロンオーダであり、表面粗さによって導電率が低減する

**問題解決**:
- 粗化粒子の組成、大きさ、形状を最適化して、高い導電率と誘電体基板への強固な接着性を両立する銅はくの開発が求められている

**測定結果**:
- 粗化面の表面粗さが異なる2種類の銅はく（10点平均粗さ: 0.4 µmと0.7 µm）を測定
- 誘電体シートにはCOPを使用
- WR-6.5導波管インタフェースの平衡円板共振器で測定
- 結果: 2サンプルの表面粗さの違いを反映して、粗さ0.4 µmのサンプルの方が周波数増加に伴っても高い導電率が維持される

### 4.5 COP基板の界面導電率計測

**サンプル構成**:
- COP基板の片面に円形の銅張金属パターンが形成された評価サンプルを2枚用意
- 円形パターンが互いに接触するように重ねて平衡円板共振器を構成

**測定方法**:
- 両面が無地のCOP基板と基準銅円板で構成された平衡円板共振器と比較
- COP基板の金属パターンの界面導電率を測定

**特性**:
- 一般に、界面導電率は周波数が上がるほど低下
- 低下の度合いは平滑性などの界面状態に依存
- ミリ波・サブテラヘルツ波帯でも高導電率が維持される銅はく及びその実装プロセス技術が求められている

---

## 5. まとめ

本稿では、ポスト5Gや6G向けの材料開発やデバイス開発を支えるミリ波・サブテラヘルツ波帯材料評価技術として、平衡円板共振器を用いた複素誘電率・導電率計測技術を紹介した。

### 5.1 主な成果

平衡円板共振器の超広帯域にわたるモード選択性を利用することで：

- 10 GHz程度から100 GHz超にわたる超広帯域での材料評価が単一の共振器で実現される

### 5.2 標準化の進展

紹介した計測技術は日本提案で国際標準化が進められている：

- **複素誘電率計測技術**: 既に2020年にIECでの国際標準化が行われた（IEC 63185:2020）
- **導電率計測技術**: 現在IECでの標準化審議が進行中

### 5.3 今後の展開

より一層の技術普及が期待される。

### 5.4 謝辞

本研究の一部は、NEDOポスト5G情報通信システム基盤強化研究開発事業／先導研究（委託）「6G向けたミリ波・テラヘルツ帯基地局の高度化のためのアンテナ技術の研究開発」により進められた。

---

## 参考文献

1. 総務省「Beyond 5Gに向けた情報通信技術戦略のあり方−強靱で活力のある2030年代の社会を目指して−」情報通信審議会中間答申（2022年6月）

2. G. Gold and K. Helmreich, "A physical surface roughness model and its applications," IEEE Trans. Microw. Theory Tech., vol. 65, no. 10, pp. 3720–3732, Oct. 2017.

3. K. Lomakin, G. Gold, and K. Helmreich, "Analytical waveguide model precisely predicting loss and delay including surface roughness," IEEE Trans. Microw. Theory Tech., vol. 66, no. 6, pp. 2649–2662, June 2018.

4. iNEMI 5G/mmWave Materials Assessment and Characterization Project, "Report 1: benchmark current industry best practices for low loss measurements," Nov. 2020.

5. H. Kawabata and Y. Kobayashi, "The analysis of a balanced-type circular disk resonator excited by coaxial cable lines to measure the complex permittivity," Proc. Asia–Pacific Microw. Conf. (APMC), pp. 1322–1325, 2001.

6. H. Kawabata, K.-I. Hasuike, Y. Kobayashi, and Z. Ma, "Multi-frequency measurements of complex permittivity of dielectric plates using higher-order modes of a balanced-type circular disk resonator," Proc. Eur. Microw. Conf. (EuMC), Manchester, U.K., pp. 388–391, Sept. 2006.

7. Y. Kato and M. Horibe, "Broadband permittivity measurements up to 170-GHz using balanced-type circular-disk resonator excited by 0.8-mm coaxial line," IEEE Trans. Instrum. Meas., vol. 68, no. 6, pp. 1796–1805, June 2019.

8. Y. Kato and M. Horibe, "Broadband conductivity measurement technique at millimeter-wave bands using a balanced-type circular disk resonator," IEEE Trans. Microw. Theory Tech., vol. 69, no. 1, pp. 861–873, Jan. 2021.

9. Y. Kato, "D-band material characterization using a balanced-type circular disk resonator with waveguide interfaces and a modified full-wave modal analysis," IEEE Trans. Instrum. Meas., vol. 72, pp. 1–10, Art no. 6009210, 2023.

10. H. Chen, H. Chen, W. Che, S. Zheng, X. Xiu, and Q. Xue, "Review and modification of permittivity measurement on open resonator for transparent material measurements at terahertz," IEEE Trans. Instrum. Meas., vol. 69, no. 11, pp. 9144–9156, Nov. 2020.

11. B. Salski, J. Cuper, T. Karpisz, P. Kopyt, and J. Krupka, "Complex permittivity of common dielectrics in 20–110 GHz frequency range measured with a Fabry–Perot open resonator," Appl. Phys. Lett., vol. 119, no. 5, Art. no. 052902, Aug. 2021.

12. Y. Kato and M. Horibe, "Broadband Permittivity Measurements Using a Frequency-Variable Balanced-Type Circular-Disk Resonator," Proc. Conf. Precis. Electromagn. Meas. (CPEM), Paris, France, pp. 1–2, July 2018.

13. Y. Kato, "Material characterizations in the D-band using a balanced-type circular disk resonator with waveguide interfaces," Proc. Conf. Precis. Electromagn. Meas. (CPEM), Wellington, New Zealand, pp. 1–2, Dec. 2022.

---

## 著者情報

**加藤悠人** (Yuto Kato)

- 国立研究開発法人産業技術総合研究所
- 2012年 東京大学大学院修士課程修了
- 同年 国立研究開発法人産業技術総合研究所入所
- 2020年 大阪大学大学院博士課程修了
- 専門: ミリ波・サブテラヘルツ波帯の材料評価技術とメタサーフェス・メタマテリアルの設計・評価技術の研究開発に従事
