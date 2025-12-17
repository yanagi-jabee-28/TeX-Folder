# **PCM通信実験報告書のための包括的技術調査：理論、実装、および歴史的考察**

## **1\. 序論**

本報告書は、パルス符号変調（Pulse Code Modulation, PCM）通信実験における「報告事項」および「考察」セクションを、学術的かつ実務的な観点から充実させるために作成された包括的な調査資料である。PCMは、連続的なアナログ信号を離散的なデジタル信号へと変換し、伝送・保存・処理を行うための基盤技術であり、現代のデジタル通信インフラストラクチャの根幹を成している。

実験報告書の質を高めるためには、単に実験手順や結果を羅列するのではなく、観測された現象の背後にある数学的理論（標本化定理、量子化理論）、回路実装上の物理的制約（オペアンプの帯域制限、スルーレート、ジッタ）、そして技術標準化の歴史的経緯（T1/E1キャリア、CD規格の策定）を有機的に結びつけ、多角的な視点から論じることが不可欠である。本資料では、これらの要素技術について、提供された文献に基づき、数式を用いた理論的導出から実際のシステム設計におけるトレードオフまでを網羅的に詳述する。

## ---

**2\. 標本化定理と信号再構成の理論的深化**

アナログ信号をデジタル領域へ移行させる最初の工程である「標本化（サンプリング）」は、通信品質を決定づける最も重要なプロセスの一つである。実験報告書においては、ナイキスト・シャノン定理の形式的な記述にとどまらず、エイリアシングのメカニズム、アンチエイリアシングフィルタの設計、そして理想的な再構成と現実のゼロ次ホールド（Zero-Order Hold）との乖離について深く考察する必要がある。

### **2.1 ナイキスト・シャノン標本化定理の数理的構造**

ナイキスト・シャノン標本化定理は、帯域制限された信号を情報の損失なしに離散的なサンプル列として表現するための必要十分条件を与える 1。時間領域における連続信号 $x(t)$ が、周波数 $f\_{max}$ 以上のスペクトル成分を持たない（帯域制限されている）場合、標本化周波数 $f\_s$ は以下の条件を満たす必要がある。

$$f\_s \> 2f\_{max}$$  
この閾値 $2f\_{max}$ はナイキストレートと呼ばれる 1。数学的には、理想的な標本化は、元の信号 $x(t)$ とディラックの櫛（Dirac comb）関数 $\\delta\_T(t) \= \\sum\_{n=-\\infty}^{\\infty} \\delta(t \- nT\_s)$ との積としてモデル化される（ここで $T\_s \= 1/f\_s$ は標本化周期である）3。

$$x\_s(t) \= x(t) \\cdot \\sum\_{n=-\\infty}^{\\infty} \\delta(t \- nT\_s)$$  
この操作を周波数領域で考えると、畳み込み定理により、元の信号のスペクトル $X(f)$ が周波数軸上で $f\_s$ ごとに無限に複製（イメージ）される現象として説明される。

$$X\_s(f) \= \\frac{1}{T\_s} \\sum\_{k=-\\infty}^{\\infty} X(f \- kf\_s)$$  
実験報告書では、この数理モデルに基づき、なぜ $f\_s \< 2f\_{max}$ の条件下で隣接するスペクトル同士が重なり合い（オーバーラップ）、元の信号情報を破壊するのかを図解とともに論じるべきである。この重なりこそが「エイリアシング」の実体であり、一度発生すると線形フィルタリングでは除去不可能な歪みとなる 2。

### **2.2 エイリアシングの現象論と観測される周波数**

エイリアシング（折り返し雑音）は、高周波成分がサンプリング周波数の半分（ナイキスト周波数）で折り返され、低周波の信号として誤認される現象である 1。入力信号周波数を $f\_{in}$、サンプリング周波数を $f\_s$ としたとき、エイリアシングによって観測される見かけの周波数 $f\_{alias}$ は次式で予測される。

$$f\_{alias} \= | f\_{in} \- N \\cdot f\_s |$$  
ここで $N$ は最も近い整数である 5。例えば、オーディオ帯域の実験において、$f\_s \= 8\\text{kHz}$ のシステムに $f\_{in} \= 5\\text{kHz}$ の正弦波を入力した場合、ナイキスト周波数 $4\\text{kHz}$ を超えているため、出力には $|5 \- 8| \= 3\\text{kHz}$ の正弦波が現れる。これは元の信号とは異なる周波数成分であり、音楽信号においては調波構造を破壊する不快な雑音として知覚される 2。実験報告書の考察では、意図的にアンダーサンプリングを行い、計算された $f\_{alias}$ と実測値が一致することを定量的に示すことが推奨される。

### **2.3 アンチエイリアシングフィルタの設計とトレードオフ**

エイリアシングを回避するための唯一の手段は、A/D変換器の前段に低域通過フィルタ（LPF）、すなわちアンチエイリアシングフィルタを挿入し、ナイキスト周波数以上の成分を物理的に遮断することである 4。しかし、理想的な矩形特性（ブリックウォール特性）を持つフィルタは物理的に実現不可能であるため、現実の設計では通過帯域（Passband）と阻止帯域（Stopband）の間に遷移帯域（Transition Band）を設ける必要がある 5。

#### **フィルタ特性と信号品質への影響**

実験で使用されるアクティブフィルタ（Sallen-Key回路など）の特性は、PCMシステムの位相特性や過渡応答に多大な影響を与える。以下の表に代表的なフィルタ特性の比較を示す。

| フィルタ形式 | 振幅特性 | 位相特性・群遅延 | 用途とPCMへの影響 |
| :---- | :---- | :---- | :---- |
| **バターワース (Butterworth)** | 通過帯域が極めて平坦（Maximally Flat）。 | 遮断周波数付近で位相が非線形となり、群遅延が増大する。 | 振幅の正確さが求められる計測用途に適するが、パルス波形においてはオーバーシュート（リンギング）が生じる可能性がある 6。 |
| **チェビシェフ (Chebyshev)** | 遷移領域が急峻で、高い減衰率を持つ。 | 通過帯域にリップル（脈動）が存在し、群遅延特性が悪い。 | 厳しい帯域制限が必要な場合に有利だが、波形歪みが大きいため、時間領域の波形再現性が重視される音声通信には不向きな場合がある 6。 |
| **ベッセル (Bessel)** | 遷移領域は緩やか。 | 位相特性が線形に近く、群遅延が一定（Maximally Flat Delay）。 | 入力波形の形状を維持する能力（過渡応答）に優れるため、矩形波やパルス伝送を行うデジタル通信の前処理フィルタとして理想的である 8。 |

サレン・キー（Sallen-Key）回路などの2次アクティブフィルタを設計する場合、Q値（Quality Factor）の設定が重要となる。バターワース特性を得るためには $Q \= 1/\\sqrt{2} \\approx 0.707$ に設定するが、これより高いQ値（例：$Q \> 1$）を設定すると、遮断周波数付近でゲインのピークが生じ、ステップ応答において発振的な挙動（リンギング）が観測される 6。実験報告書では、使用したフィルタの回路定数からQ値を逆算し、観測された波形のオーバーシュートや整定時間との相関を論じることが、深い洞察を示すポイントとなる。

### **2.4 信号再構成とアパーチャ効果**

D/A変換後の信号再構成において、理想的な標本化定理はインパルス列の出力を仮定しているが、現実のDACは次のサンプルが来るまで電圧を保持する「ゼロ次ホールド（ZOH）」動作を行う 1。この矩形パルス列は、周波数領域においてはsinc関数（$\\text{sin}(x)/x$）の包絡線を持つスペクトル特性を示す。

これを「アパーチャ効果（Aperture Effect）」と呼び、高周波成分において振幅の低下を引き起こす（ナイキスト周波数付近で約-3.92dBの減衰が生じる）3。報告書では、このアパーチャ効果を補正するための「アパーチャ補正イコライザ」の必要性や、あるいはオーバーサンプリングによってこの影響を可聴域外へ追いやる現代的な手法について言及することで、理論と実装のギャップに対する理解を示すことができる。

## ---

**3\. 量子化の数理とSN比の限界**

標本化された離散時間信号は、振幅軸方向での離散化、すなわち量子化（Quantization）を経てデジタルデータとなる。この過程は不可逆であり、元の信号と量子化された信号との差分は「量子化雑音（Quantization Noise）」として現れる。PCMシステムの通信品質を定量的に評価するためには、量子化ビット数とS/N比（信号対雑音比）の関係を数学的に厳密に導出することが求められる。

### **3.1 量子化S/N比の理論的導出（$6.02N \+ 1.76$ dB）**

実験報告書において頻繁に参照される理論限界式 $SNR \= 6.02N \+ 1.76$ dB の導出過程を記述することは、実験結果の妥当性を評価する上で不可欠である 11。

#### **1\. 量子化誤差のモデル化**

量子化ステップ幅を $\\Delta$（LSB: Least Significant Bitの電圧）とする。入力信号が十分に変動し、量子化レベル間をランダムに行き来する場合、量子化誤差 $e$ は区間 $$ において一様分布（Uniform Distribution）すると仮定できる 11。  
このとき、誤差の確率密度関数 $p(e)$ は次のように表される。  
$$ p(e) \= \\begin{cases} \\frac{1}{\\Delta} & (-\\frac{\\Delta}{2} \\le e \\le \\frac{\\Delta}{2}) \\ 0 & (\\text{otherwise}) \\end{cases} $$

#### **2\. 量子化雑音電力の計算**

量子化雑音電力（分散）$P\_{noise} \= \\sigma\_e^2$ は、誤差の二乗平均値として計算される。  
$$ P\_{noise} \= \\int\_{-\\infty}^{\\infty} e^2 p(e) de \= \\int\_{-\\Delta/2}^{\\Delta/2} e^2 \\cdot \\frac{1}{\\Delta} de $$  
$$ \= \\frac{1}{\\Delta} \\left\[ \\frac{e^3}{3} \\right\]\_{-\\Delta/2}^{\\Delta/2} \= \\frac{1}{\\Delta} \\left( \\frac{(\\Delta/2)^3}{3} \- \\frac{(-\\Delta/2)^3}{3} \\right) \= \\frac{\\Delta^2}{12} $$

#### **3\. 信号電力の計算**

フルスケールの正弦波入力信号 $v(t) \= A \\sin(\\omega t)$ を想定する。NビットのADCにおいて、フルスケール範囲（Peak-to-Peak）は $2A \= 2^N \\Delta$ であるため、振幅 $A$ は $A \= 2^{N-1} \\Delta$ と表せる。  
正弦波の信号電力 $P\_{signal}$ は振幅の二乗平均（RMSの二乗）であるため、

$$P\_{signal} \= \\frac{A^2}{2} \= \\frac{(2^{N-1}\\Delta)^2}{2} \= \\frac{2^{2N-2}\\Delta^2}{2}$$

#### **4\. S/N比の導出**

$$ SNR \= \\frac{P\_{signal}}{P\_{noise}} \= \\frac{2^{2N-2}\\Delta^2 / 2}{\\Delta^2 / 12} \= \\frac{12 \\cdot 2^{2N-2}}{2} \= 3 \\cdot 2^{2N-1} \= 1.5 \\cdot 2^{2N} $$

これをデシベル（dB）表記に変換すると、以下の有名な公式が得られる。

$$SNR(dB) \= 10 \\log\_{10}(1.5 \\cdot 2^{2N}) \= 10 \\log\_{10}(1.5) \+ 20N \\log\_{10}(2)$$

$$\\approx 1.76 \+ 6.02N$$  
この導出過程を報告書に含めることで、実験で得られたS/N比が理論値（例えば8ビットなら約49.9dB、16ビットなら約98.1dB）に対してどの程度劣化しているかを評価する基準が得られる。劣化要因としては、電源ノイズ、クロックジッタ、あるいはアナログ回路の高調波歪みなどが挙げられる 13。

### **3.2 圧伸（Companding）によるダイナミックレンジの拡大**

上記の理論式は、量子化ステップ幅が一定の「線形量子化（一様量子化）」を前提としている。しかし、音声信号のような振幅分布が不均一（小振幅の時間が長く、大振幅は稀）な信号に対して一様量子化を適用すると、小振幅信号においてS/N比が著しく低下するという問題が生じる 14。この問題を解決するために導入されるのが「非線形量子化」、すなわち圧伸（Companding: Compression \+ Expansion）技術である。

報告書では、国際的に標準化されている二つの主要な圧伸法則、$\\mu$-law（北米・日本）とA-law（欧州）の特性とその違いについて詳述すべきである 16。

#### **$\\mu$\-law（ミュー則）とA-law（A則）の比較**

| 特性項目 | μ-law (北米・日本・韓国) | A-law (欧州・その他の地域) |
| :---- | :---- | :---- |
| **圧縮関数 $F(x)$** | $$F(x) \= \\text{sgn}(x) \\frac{\\ln(1+\\mu | x |
| **標準パラメータ** | 通常 $\\mu \= 255$ | 通常 $A \= 87.6$ |
| **量子化特性** | 原点付近での傾きが大きく、小信号に対する分解能が高い。全域で対数的な特性を持つ。 | 原点付近（$ |
| **S/N比とダイナミックレンジ** | A-lawに比べて小信号時の量子化ノイズがわずかに大きいが、全体のダイナミックレンジはわずかに広い 16。 | 小信号時のS/N比（S/Q比）が$\\mu$-lawより良好である。 |
| **実装** | 14ビット相当のダイナミックレンジを8ビットに圧縮する。 | 13ビット相当のダイナミックレンジを8ビットに圧縮する 16。 |

これらの圧伸処理により、8ビットのデータ長（線形量子化では約50dBのSNR）でありながら、聴感上は12〜13ビット相当（約72〜78dB）の品質を達成している 16。実験においてCODECを使用した場合、これらの対数圧縮がハードウェア内部で行われている可能性が高く、入出力特性の測定データ（リニアリティ）が直線にならないことは、この圧伸特性によるものであると考察できる。

## ---

**4\. 回路実装上の物理的制約と信号劣化要因**

理想的な数学モデルとは異なり、現実のPCM通信実験回路にはオペアンプやスイッチ素子の物理的特性に起因する限界が存在する。これらの「非理想性」を実験データと結びつけて論じることは、報告書の技術的水準を飛躍的に向上させる。

### **4.1 精密整流回路（スーパーダイオード）の周波数限界**

PCM信号の振幅測定や復調回路において、微小信号を整流するためにオペアンプを用いた「精密整流回路（スーパーダイオード）」が使用されることがある。通常のシリコンダイオードは約0.6V〜0.7Vの順方向電圧降下（$V\_F$）を持つため、それ以下の微小信号を整流できないが、精密整流回路はオペアンプのフィードバックループ内にダイオードを配置することで、見かけ上の$V\_F$をほぼゼロ（$V\_F / A\_{OL}$、$A\_{OL}$は開ループ利得）にまで低減させる 18。

しかし、報告書の考察においては、この回路が高周波信号に対して脆弱であるという「スルーレート（Slew Rate）による限界」に言及すべきである。

1. **ゼロクロス時の挙動**: 入力信号が正から負（またはその逆）へ遷移するゼロクロス点において、ダイオードが逆バイアスとなりオフ状態になる瞬間が存在する。このとき、オペアンプのフィードバックループが切断され、オペアンプはオープンループ状態となる 18。  
2. **飽和からの復帰**: オープンループ状態のオペアンプは、出力が電源電圧レール付近（飽和電圧）まで振り切れてしまう。信号極性が再び反転してダイオードがオンになる際、オペアンプの出力電圧は飽和レベルからゼロ付近まで戻る必要があるが、これには有限の時間（リカバリタイム）がかかる 20。  
3. **スルーレート制限**: オペアンプの出力電圧の変化速度はスルーレート（V/$\\mu$s）によって制限されるため、高周波信号ではこの復帰が間に合わず、ゼロクロス付近で著しい波形歪みが発生する 21。

実験データとして、低周波（1kHz程度）では綺麗な整流波形が得られているのに対し、高周波（10kHz〜100kHz）では波形の根元が欠けるような歪みが観測された場合、それはオペアンプのスルーレートと飽和回復特性に起因するものであると結論付けることができる 22。

### **4.2 クロックジッタによるS/N比の劣化**

A/D変換におけるもう一つの重要な劣化要因は、サンプリングクロックの時間的な揺らぎ、すなわち「ジッタ（Jitter）」である。理想的なサンプリングは完全に等間隔な時刻で行われるが、現実のクロックには位相雑音が含まれる。

入力信号の周波数が高いほど、信号の電圧変化率（スルーレート）が大きくなるため、わずかなサンプリング時刻のズレ（$\\Delta t$）が大きな電圧誤差（$\\Delta v$）として記録されてしまう。ジッタに起因するS/N比の制限（$SNR\_{jitter}$）は以下の式で表される 23。

$$SNR\_{jitter} (dB) \= \-20 \\log\_{10}(2\\pi f\_{in} t\_{jitter\\\_rms})$$  
ここで、$f\_{in}$ は入力アナログ信号の周波数、$t\_{jitter\\\_rms}$ はクロックのRMSジッタである。  
この式から導き出される重要な洞察は、\*\*「量子化ビット数を増やしても、ジッタが存在する限り、高周波信号のS/N比は改善しない」\*\*という事実である。例えば、非常に高性能な16ビットADCを使用していても、クロックジッタが大きければ、実効的な分解能（ENOB: Effective Number of Bits）は10ビット程度にまで低下する可能性がある。報告書では、実験に使用した発振回路の安定性や、測定環境のノイズがジッタ源となり得る点について触れるべきである。

## ---

**5\. 時分割多重（TDM）とフレーム同期技術**

PCM技術の最大の利点の一つは、複数のチャネルを時間軸上で切り替えて一本の伝送路で送る「時分割多重（Time Division Multiplexing, TDM）」が容易な点にある。実験においてTDMを扱った場合、チャネル間の分離と同期確立のメカニズムについて詳細な記述が求められる。

### **5.1 T1キャリアとE1キャリアのアーキテクチャ比較**

世界的なデジタル通信網の黎明期において、北米・日本を中心とする「T1規格」と、欧州を中心とする「E1規格」という二つの異なるTDM規格が策定された。これらはチャネル数、フレーム構成、同期方式において異なる設計思想を持っている。これらの比較を表形式で示し、それぞれの技術的特徴を論じることは、報告書の視野を広げる。

| 特徴 | T1 (DS1) \[北米・日本\] | E1 \[欧州・国際\] |
| :---- | :---- | :---- |
| **伝送速度** | 1.544 Mbps | 2.048 Mbps |
| **多重化チャネル数** | 24チャネル (64kbps $\\times$ 24\) | 32チャネル (64kbps $\\times$ 32\) |
| **1フレームあたりのビット数** | 193ビット (データ192bit \+ フレーミング1bit) | 256ビット (8bit $\\times$ 32タイムスロット) |
| **フレームレート** | 8,000 フレーム/秒 | 8,000 フレーム/秒 |
| **同期方式（Framing）** | **分散型**: 各フレームの末尾にある1ビット（Fビット）を使用。複数のフレーム（12または24）にまたがって同期パターンを形成する 26。 | **集中型**: タイムスロット0（TS0）を使用。奇数フレームと偶数フレームで交互にFAS（Frame Alignment Signal）パターンを送信する 27。 |
| **信号制御（Signaling）** | **ビットロビング (Bit Robbing)**: 音声データのLSB（最下位ビット）を定期的に信号用に流用する（D4では6/12フレーム目）。これによりデータ品質が若干劣化する（実質56kbps）場合がある 26。 | **専用チャネル (CAS/CCS)**: タイムスロット16（TS16）を信号専用に割り当てる。音声データ（TS1-15, TS17-31）は常に完全な8ビット（64kbps）を利用可能 30。 |

#### **T1のフレーミング：D4 (SF) vs ESF**

T1規格においては、初期の **D4 (Super Frame)** と、後に拡張された **ESF (Extended Super Frame)** が存在する。

* **D4 (SF)**: 12フレームを1つのスーパーフレームとし、Fビットで同期信号（100011011100）を形成する。エラー検出機能を持たない 26。  
* **ESF**: 24フレームを1単位とし、Fビットを「同期（6bit）」、「CRCエラー検出（6bit）」、「データリンク（12bit, FDL）」に分割使用する。これにより、回線品質の常時監視（CRCチェック）が可能となった点が大きな進歩である 26。

#### **E1の同期パターン：FAS**

E1では、TS0において **FAS (Frame Alignment Signal)** と呼ばれる固定パターン 0011011 を偶数フレームで送信し、奇数フレームではアラーム情報（Remote Alarm Indication: RAI）などを送信する 30。受信側はこのパターンを検出することでフレームの先頭を特定する。

### **5.2 ガードタイムと符号間干渉（ISI）**

TDM伝送において、各タイムスロットの間には信号の重なりを防ぐための隙間時間、「ガードタイム」が必要となる場合がある 32。  
伝送路が帯域制限を持つ場合、パルス波形は時間的に広がり（なまり）を持ち、隣接するタイムスロットへエネルギーが漏れ出す。これを「符号間干渉（Inter-Symbol Interference, ISI）」と呼ぶ 34。  
ISIが増大すると、受信側での「0/1」判定の閾値マージンが減少し、ビット誤り率（BER）が悪化する。実験報告書でアイパターン（Eye Pattern）を観測している場合、目の開き（Eye Opening）の垂直方向の高さがノイズ耐性を、水平方向の幅がジッタ耐性を示していることを解説し、ガードタイムの設定やフィルタ帯域幅がアイパターンに与える影響について考察を加えるべきである 34。

## ---

**6\. 歴史的背景と技術標準の決定要因**

PCM技術の仕様は、純粋な理論だけでなく、開発当時の技術的制約や他メディアとの互換性によって決定された側面が強い。特にCD（コンパクトディスク）の規格はPCMの代表例であり、そのパラメータ決定の背景を知ることは技術への深い理解につながる。

### **6.1 なぜサンプリング周波数は44.1kHzなのか？**

オーディオCDのサンプリング周波数 44.1kHz は、一見すると不自然な数値に見える（48kHzや40kHzの方がキリが良い）。しかし、これには明確な歴史的・技術的理由が存在する。  
1970年代後半、大量のデジタル音声データを記録できる安価で信頼性の高いメディアは「ビデオテープ（U-maticなど）」しか存在しなかった。ソニー等は、PCM音声データを白黒の映像信号（擬似ビデオ信号）としてエンコードし、ビデオテープに記録する「PCMプロセッサー」を開発した 35。  
この際、北米・日本のテレビ規格である **NTSC**（走査線525本、60Hz）と、欧州の **PAL**（走査線625本、50Hz）の両方に対して、整数個のサンプルを格納できる周波数である必要があった。

* **NTSC (60Hz)**: 1フィールドあたりの有効走査線数 245本 $\\times$ 3サンプル/行 $\\times$ 60Hz \= **44,100 Hz**  
* **PAL (50Hz)**: 1フィールドあたりの有効走査線数 294本 $\\times$ 3サンプル/行 $\\times$ 50Hz \= **44,100 Hz**

このように、44.1kHzは当時のビデオ技術との互換性から導き出された「最大公約数」的な解であった 37。報告書でこの事実に触れることは、既存インフラの上に新しい技術が構築される工学的な連続性を示す良い例となる。

### **6.2 16ビット vs 14ビットの攻防と「第九」の伝説**

CDの量子化ビット数と収録時間を巡っては、ソニーとフィリップスの間で激しい議論があった。

* **ビット数**: フィリップスは当時開発済みだった14ビットDACの使用を提案したが、ソニーは音質を重視して16ビットを主張した。結果的に16ビットが採用されたが、フィリップスは14ビットDACで16ビット相当の解像度を出すために「オーバーサンプリング」と「ノイズシェーピング」技術を実用化した。これは現在のハイレゾDACでも使用される $\\Delta \\Sigma$ 変調の基礎となった重要な技術革新である 37。  
* **収録時間**: フィリップスは直径11.5cm（カセットテープの対角線長）で60分収録を提案したが、ソニー（特に大賀典雄氏）は「ベートーヴェンの交響曲第九番（約74分）が1枚に収まること」を要求し、直径12cm・74分に決定されたという逸話がある 39。真偽には諸説あるものの、この決定がCDというメディアの物理規格を決定づけたことは事実であり、技術仕様が文化的背景の影響を受ける興味深い事例である。

### **6.3 現代のハイレゾリューション・オーディオへの展望**

最後に、現代の「ハイレゾ」技術についても言及し、従来のPCM（CDスペック）からの進化を考察する。  
サンプリング周波数を 96kHz や 192kHz に上げる主な利点は、単に可聴域外（超音波）を記録することだけではない。より重要なのは、\*\*「アンチエイリアシングフィルタの設計を容易にし、可聴帯域内の位相特性（時間応答）を改善すること」\*\*にある 41。急峻なフィルタ（ブリックウォール）は大きな群遅延とリンギングを引き起こすが、サンプリング周波数を上げれば、遮断特性が緩やかなフィルタを使用でき、結果として時間領域での波形再現性が向上する。これは2.3節で述べたフィルタ理論の実践的応用である。

## ---

**7\. 結論**

本調査報告書では、PCM通信実験の結果を深く考察するために必要な理論的背景、回路実装上の課題、および歴史的経緯について詳述した。  
実験における「誤差」や「波形歪み」は、単なる失敗や精度の問題ではなく、標本化定理の物理的制約（アパーチャ効果、エイリアシング）、回路素子の限界（オペアンプのスルーレート、ジッタ）、あるいはシステム設計上のトレードオフ（T1/E1のフレーム構造、フィルタ特性）に起因する必然的な現象である。  
今後の実験報告書作成においては、これらの理論的根拠（例えば $6.02N+1.76$dB の式やジッタによるSNR限界式など）を用いてデータを定量的に評価し、理想と現実のギャップを工学的視点から論じることが期待される。これらの考察は、現代のデジタル通信、オーディオ工学、計測技術の基礎理解において極めて重要である。

#### **引用文献**

1. Nyquist–Shannon sampling theorem \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon\_sampling\_theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)  
2. Aliasing – Knowledge and References \- Taylor & Francis, 12月 4, 2025にアクセス、 [https://taylorandfrancis.com/knowledge/Engineering\_and\_technology/Electrical\_%26\_electronic\_engineering/Aliasing/](https://taylorandfrancis.com/knowledge/Engineering_and_technology/Electrical_%26_electronic_engineering/Aliasing/)  
3. Sampling (signal processing) \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/Sampling\_(signal\_processing)](https://en.wikipedia.org/wiki/Sampling_\(signal_processing\))  
4. Effects of Undersampling (Aliasing) and Anti-Aliasing Filter \- Tutorials Point, 12月 4, 2025にアクセス、 [https://www.tutorialspoint.com/signals\_and\_systems/effects\_of\_undersampling\_aliasing\_and\_anti\_aliasing\_filter.htm](https://www.tutorialspoint.com/signals_and_systems/effects_of_undersampling_aliasing_and_anti_aliasing_filter.htm)  
5. Anti-Aliasing Filters and Their Usage Explained \- NI \- National Instruments, 12月 4, 2025にアクセス、 [https://www.ni.com/en/shop/data-acquisition/measurement-fundamentals/analog-fundamentals/anti-aliasing-filters-and-their-usage-explained.html](https://www.ni.com/en/shop/data-acquisition/measurement-fundamentals/analog-fundamentals/anti-aliasing-filters-and-their-usage-explained.html)  
6. Sallen–Key topology \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/Sallen%E2%80%93Key\_topology](https://en.wikipedia.org/wiki/Sallen%E2%80%93Key_topology)  
7. Second Order Filters and the 2nd-order low pass filter circuit \- Electronics Tutorials, 12月 4, 2025にアクセス、 [https://www.electronics-tutorials.ws/filter/second-order-filters.html](https://www.electronics-tutorials.ws/filter/second-order-filters.html)  
8. Sallen-Key LPF frequency scaling factor \- EEVblog, 12月 4, 2025にアクセス、 [https://www.eevblog.com/forum/projects/sallen-key-lpf-frequency-scaling-factor/](https://www.eevblog.com/forum/projects/sallen-key-lpf-frequency-scaling-factor/)  
9. What Is a Low Pass Filter? Theory, Design & Practical Implementation \- Wevolver, 12月 4, 2025にアクセス、 [https://www.wevolver.com/article/what-is-a-low-pass-filter-theory-design-practical-implementation](https://www.wevolver.com/article/what-is-a-low-pass-filter-theory-design-practical-implementation)  
10. Sallen and Key Filter Design for Second Order Filters \- Electronics Tutorials, 12月 4, 2025にアクセス、 [https://www.electronics-tutorials.ws/filter/sallen-key-filter.html](https://www.electronics-tutorials.ws/filter/sallen-key-filter.html)  
11. Quantization Noise 101: Where does SNR about 6N dB come from? \- Audio Science Review (ASR) Forum, 12月 4, 2025にアクセス、 [https://www.audiosciencereview.com/forum/index.php?attachments/quantization-noise-rev1-pdf.300661/](https://www.audiosciencereview.com/forum/index.php?attachments/quantization-noise-rev1-pdf.300661/)  
12. MT-001: Taking the Mystery out of the Infamous Formula, "SNR=6.02N \+ 1.76dB," and Why You Should Care, 12月 4, 2025にアクセス、 [https://qtwork.tudelft.nl/\~schouten/linkload/adc-tutorial.pdf](https://qtwork.tudelft.nl/~schouten/linkload/adc-tutorial.pdf)  
13. Test Video A/D Converters Under Dynamic Conditions Application Note (AN-297) \- Analog Devices, 12月 4, 2025にアクセス、 [https://www.analog.com/media/en/technical-documentation/application-notes/38578121760556529004006638125720757383an297.pdf](https://www.analog.com/media/en/technical-documentation/application-notes/38578121760556529004006638125720757383an297.pdf)  
14. Signal Quantization and Compression Overview, 12月 4, 2025にアクセス、 [http://www.seas.ucla.edu/dsplab/sqc/over.html](http://www.seas.ucla.edu/dsplab/sqc/over.html)  
15. Telecomms Principles \- Pulse Code Modulation (PCM) \- TechnologyUK, 12月 4, 2025にアクセス、 [https://www.technologyuk.net/telecommunications/telecom-principles/pulse-code-modulation.shtml](https://www.technologyuk.net/telecommunications/telecom-principles/pulse-code-modulation.shtml)  
16. mu-law algorithm \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/Mu-law\_algorithm](https://en.wikipedia.org/wiki/Mu-law_algorithm)  
17. Companding: Logarithmic Laws, Implementation, and Consequences \- Technical Articles, 12月 4, 2025にアクセス、 [https://www.allaboutcircuits.com/technical-articles/companding-logarithmic-laws-implementation-and-consequences/](https://www.allaboutcircuits.com/technical-articles/companding-logarithmic-laws-implementation-and-consequences/)  
18. Precision rectifier \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/Precision\_rectifier](https://en.wikipedia.org/wiki/Precision_rectifier)  
19. Precision Full & Half-wave rectifier circuit using OP-AMP \- ElecCircuit.com, 12月 4, 2025にアクセス、 [https://www.eleccircuit.com/full-wave-rectifier-with-an-op-amp-ic/](https://www.eleccircuit.com/full-wave-rectifier-with-an-op-amp-ic/)  
20. When a Diode Simply Isn't Good Enough: The Superdiode \- Technical Articles, 12月 4, 2025にアクセス、 [https://www.allaboutcircuits.com/technical-articles/when-a-diode-simply-isnt-good-enough-the-superdiode/](https://www.allaboutcircuits.com/technical-articles/when-a-diode-simply-isnt-good-enough-the-superdiode/)  
21. Precision Full-Wave Rectifier, Dual-Supply \- Texas Instruments, 12月 4, 2025にアクセス、 [https://www.ti.com/lit/pdf/tidu030](https://www.ti.com/lit/pdf/tidu030)  
22. A Precision Rectification Experiment : 11 Steps \- Instructables, 12月 4, 2025にアクセス、 [https://www.instructables.com/A-Precision-Rectification-Experiment/](https://www.instructables.com/A-Precision-Rectification-Experiment/)  
23. Improving ADC & DAC Characterization, 12月 4, 2025にアクセス、 [https://www.salland.com/downloads/pdf/Applicos-Clock-Jitter-Cancelation-in-Coherent-Data-Converter-Testing.pdf](https://www.salland.com/downloads/pdf/Applicos-Clock-Jitter-Cancelation-in-Coherent-Data-Converter-Testing.pdf)  
24. \[FAQ\] The relationship between SNR and ADC clock jitter \- Data converters forum \- TI E2E, 12月 4, 2025にアクセス、 [https://e2e.ti.com/support/data-converters-group/data-converters/f/data-converters-forum/890938/faq-the-relationship-between-snr-and-adc-clock-jitter](https://e2e.ti.com/support/data-converters-group/data-converters/f/data-converters-forum/890938/faq-the-relationship-between-snr-and-adc-clock-jitter)  
25. Effect of Clock Jitter on ADCs' SNR \- EEVblog, 12月 4, 2025にアクセス、 [https://www.eevblog.com/forum/projects/effect-of-clock-jitter-on-adcs-snr/](https://www.eevblog.com/forum/projects/effect-of-clock-jitter-on-adcs-snr/)  
26. T1 \- Sistemas Fratec S.A., 12月 4, 2025にアクセス、 [https://www.fratec.net/faq/diccionario/t1/](https://www.fratec.net/faq/diccionario/t1/)  
27. Framing \- Dialogic, 12月 4, 2025にアクセス、 [https://www.dialogic.com/webhelp/naturalaccess/release9.0/cg\_6060c\_install\_and\_dev\_manual/framing.html](https://www.dialogic.com/webhelp/naturalaccess/release9.0/cg_6060c_install_and_dev_manual/framing.html)  
28. Basic knowledge of E1,E1 interface converter, E1 converter, 12月 4, 2025にアクセス、 [https://www.takfiberoptic.com/basic-knowledge-of-e1-a-20.html](https://www.takfiberoptic.com/basic-knowledge-of-e1-a-20.html)  
29. T1 Line Coding, Framing, and Signaling: An In-Depth Guide \- Blog of Cody Deluisio, 12月 4, 2025にアクセス、 [https://deluisio.com/networking/2024/08/12/t1-line-coding-framing-and-signaling-an-in-depth-guide/](https://deluisio.com/networking/2024/08/12/t1-line-coding-framing-and-signaling-an-in-depth-guide/)  
30. E1 T1 Tutorial | PDF | Multiplexing | Data Transmission \- Scribd, 12月 4, 2025にアクセス、 [https://www.scribd.com/document/58443770/E1-T1-Tutorial](https://www.scribd.com/document/58443770/E1-T1-Tutorial)  
31. T1 vs. E1 Frames: Key Differences in Telecommunications \- RF Wireless World, 12月 4, 2025にアクセス、 [https://www.rfwireless-world.com/terminology/t1-vs-e1-frame-differences](https://www.rfwireless-world.com/terminology/t1-vs-e1-frame-differences)  
32. Types of Multiplexing in Data Communications \- GeeksforGeeks, 12月 4, 2025にアクセス、 [https://www.geeksforgeeks.org/computer-networks/types-of-multiplexing-in-data-communications/](https://www.geeksforgeeks.org/computer-networks/types-of-multiplexing-in-data-communications/)  
33. Time Division Multiplexing : Block Diagram, Working & Its Uses \- ElProCus, 12月 4, 2025にアクセス、 [https://www.elprocus.com/time-division-multiplexing/](https://www.elprocus.com/time-division-multiplexing/)  
34. Intersymbol interference \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/Intersymbol\_interference](https://en.wikipedia.org/wiki/Intersymbol_interference)  
35. 44,100 Hz \- Grokipedia, 12月 4, 2025にアクセス、 [https://grokipedia.com/page/44,100\_Hz](https://grokipedia.com/page/44,100_Hz)  
36. 44,100 Hz \- Wikipedia, 12月 4, 2025にアクセス、 [https://en.wikipedia.org/wiki/44,100\_Hz](https://en.wikipedia.org/wiki/44,100_Hz)  
37. Shannon, Beethoven, and the Compact Disc \- Turing Machines Inc, 12月 4, 2025にアクセス、 [http://www.turing-machines.com/pdf/beethoven.htm](http://www.turing-machines.com/pdf/beethoven.htm)  
38. Perfecting the Compact Disc System \- The six Philips/Sony meetings \- 1979-1980 \- DutchAudioClassics.nl, 12月 4, 2025にアクセス、 [https://www.dutchaudioclassics.nl/The-six-meetings-Philips-Sony-1979-1980-The-Start-of-Digital-Audio/](https://www.dutchaudioclassics.nl/The-six-meetings-Philips-Sony-1979-1980-The-Start-of-Digital-Audio/)  
39. 44.1kHz vs 48kHz: The Beethoven's Ninth Symphony Conspiracy \- Music Production, 12月 4, 2025にアクセス、 [https://www.levelsmusicproduction.com/blog/44-1khz-vs-48khz-the-beethoven-s-ninth-symphony-conspiracy](https://www.levelsmusicproduction.com/blog/44-1khz-vs-48khz-the-beethoven-s-ninth-symphony-conspiracy)  
40. Sony Chairman credited with developing Compact Disks (CDs) "insisted the CD be designed at 4.8 inches in diameter to hold 75 minutes worth of music — in order to store Beethoven's Ninth Symphony in its entirety." : r/classicalmusic \- Reddit, 12月 4, 2025にアクセス、 [https://www.reddit.com/r/classicalmusic/comments/2z5c6w/sony\_chairman\_credited\_with\_developing\_compact/](https://www.reddit.com/r/classicalmusic/comments/2z5c6w/sony_chairman_credited_with_developing_compact/)  
41. Digital audio basics: audio sample rate and bit depth \- iZotope, 12月 4, 2025にアクセス、 [https://www.izotope.com/en/learn/digital-audio-basics-sample-rate-and-bit-depth](https://www.izotope.com/en/learn/digital-audio-basics-sample-rate-and-bit-depth)  
42. Bits and sampling rates \- Is ultra high-res really necessary? \- Alpha Audio, 12月 4, 2025にアクセス、 [https://www.alpha-audio.net/academy/bits-and-sampling-rates-is-ultra-high-res-really-necessary/](https://www.alpha-audio.net/academy/bits-and-sampling-rates-is-ultra-high-res-really-necessary/)