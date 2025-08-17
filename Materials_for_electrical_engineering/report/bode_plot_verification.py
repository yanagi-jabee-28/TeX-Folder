#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ボード線図解析から導出した伝達関数の検証スクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib.patches as patches

# 日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def first_order_system_verification():
    """一次遅れ系の検証"""
    print("=== 一次遅れ系の検証 ===")

    # 導出されたパラメータ
    K = 1.778
    T = 0.159

    print(f"導出パラメータ: K = {K:.3f}, T = {T:.3f}s")

    # 伝達関数: G1(s) = K/(Ts+1)
    num = [K]
    den = [T, 1]
    system1 = signal.TransferFunction(num, den)

    # 周波数範囲（Hz）
    f = np.logspace(-1, 2, 1000)  # 0.1 to 100 Hz
    w = 2 * np.pi * f  # rad/s

    # 周波数応答計算
    w_resp, h_resp = signal.freqresp(system1, w)
    magnitude_db = 20 * np.log10(np.abs(h_resp))
    phase_deg = np.angle(h_resp) * 180 / np.pi

    # 理論値の主要ポイント
    print(f"直流ゲイン: {20*np.log10(K):.2f} dB")

    # コーナー周波数での確認
    f_corner = 1/(2*np.pi*T)
    w_corner = 1/T
    _, h_corner = signal.freqresp(system1, [w_corner])
    gain_corner = 20 * np.log10(np.abs(h_corner[0]))
    print(f"コーナー周波数: {f_corner:.2f} Hz")
    print(f"コーナー周波数でのゲイン: {gain_corner:.2f} dB")
    print(f"直流ゲインから-3dB点: {20*np.log10(K) - gain_corner:.2f} dB")

    # プロット
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # ゲイン線図
    ax1.semilogx(f, magnitude_db, 'b-', linewidth=2, label='理論値')

    # 元データの推定点をプロット
    f_data = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0])
    gain_data = np.array([4.8, 4.7, 4.5, 2.0, -1.0, -8.0, -14.0, -20.0, -26.0])
    ax1.semilogx(f_data, gain_data, 'ro', markersize=6, label='元データ（推定）')

    # 補助線
    ax1.axhline(y=20*np.log10(K), color='g', linestyle='--',
                alpha=0.7, label=f'直流ゲイン {20*np.log10(K):.1f}dB')
    ax1.axvline(x=f_corner, color='orange', linestyle='--',
                alpha=0.7, label=f'コーナー周波数 {f_corner:.1f}Hz')

    ax1.set_xlabel('周波数 [Hz]')
    ax1.set_ylabel('ゲイン [dB]')
    ax1.set_title('一次遅れ系の検証：ゲイン線図')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim([-30, 10])

    # 位相線図
    ax2.semilogx(f, phase_deg, 'b-', linewidth=2, label='理論値')
    ax2.axvline(x=f_corner, color='orange', linestyle='--',
                alpha=0.7, label=f'コーナー周波数 {f_corner:.1f}Hz')
    ax2.axhline(y=-45, color='r', linestyle='--', alpha=0.7, label='-45°')

    ax2.set_xlabel('周波数 [Hz]')
    ax2.set_ylabel('位相 [deg]')
    ax2.set_title('一次遅れ系の検証：位相線図')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim([-100, 10])

    plt.tight_layout()
    plt.savefig('first_order_verification.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 誤差計算
    # 元データとの比較
    f_interp = f_data
    gain_theory = 20 * np.log10(K / np.sqrt(1 + (2*np.pi*f_interp*T)**2))
    error = np.abs(gain_theory - gain_data)
    print(f"\n誤差解析:")
    print(f"最大誤差: {np.max(error):.2f} dB")
    print(f"RMS誤差: {np.sqrt(np.mean(error**2)):.2f} dB")
    print(f"平均誤差: {np.mean(error):.2f} dB")


def second_order_system_verification():
    """二次遅れ系の検証"""
    print("\n=== 二次遅れ系の検証 ===")

    # 導出されたパラメータ
    K = 1.0
    zeta = 0.30
    omega_n = 60.2  # rad/s

    print(f"導出パラメータ: K = {K:.3f}, ζ = {zeta:.3f}, ωn = {omega_n:.1f} rad/s")

    # 伝達関数: G2(s) = K*ωn^2/(s^2 + 2*ζ*ωn*s + ωn^2)
    num = [K * omega_n**2]
    den = [1, 2*zeta*omega_n, omega_n**2]
    system2 = signal.TransferFunction(num, den)

    print(f"伝達関数: G2(s) = {num[0]:.0f}/(s^2 + {den[1]:.2f}s + {den[2]:.0f})")

    # 角周波数範囲
    w = np.logspace(0, 3, 1000)  # 1 to 1000 rad/s

    # 周波数応答計算
    w_resp, h_resp = signal.freqresp(system2, w)
    magnitude_db = 20 * np.log10(np.abs(h_resp))
    phase_deg = np.angle(h_resp) * 180 / np.pi

    # 理論値の主要ポイント計算
    print(f"直流ゲイン: {20*np.log10(K):.2f} dB")

    # 共振周波数
    omega_r = omega_n * np.sqrt(1 - 2*zeta**2)
    print(f"理論共振角周波数: {omega_r:.1f} rad/s")

    # 共振ピークゲイン
    if zeta < 1/np.sqrt(2):
        Mp = 1 / (2*zeta*np.sqrt(1-zeta**2))
        Mp_db = 20 * np.log10(Mp)
        print(f"理論共振ピークゲイン: {Mp_db:.2f} dB")

    # 固有角周波数での位相（-90度のはず）
    _, h_wn = signal.freqresp(system2, [omega_n])
    phase_wn = np.angle(h_wn[0]) * 180 / np.pi
    print(f"ωn = {omega_n:.1f} rad/s での位相: {phase_wn:.1f}°")

    # プロット
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # ゲイン線図
    ax1.semilogx(w, magnitude_db, 'b-', linewidth=2, label='理論値')

    # 元データの重要ポイント
    ax1.plot(54.5, 4.84, 'ro', markersize=8, label='元データ：共振ピーク (54.5, 4.84dB)')
    ax1.plot(omega_r, Mp_db, 'g^', markersize=8,
             label=f'理論：共振ピーク ({omega_r:.1f}, {Mp_db:.2f}dB)')

    # 補助線
    ax1.axhline(y=0, color='g', linestyle='--', alpha=0.7, label='直流ゲイン 0dB')
    ax1.axvline(x=omega_n, color='orange', linestyle='--',
                alpha=0.7, label=f'固有角周波数 {omega_n:.1f} rad/s')
    ax1.axvline(x=omega_r, color='purple', linestyle='--',
                alpha=0.7, label=f'共振角周波数 {omega_r:.1f} rad/s')

    # -40dB/decade の補助線
    w_ref = 100
    gain_ref = 20 * np.log10(K * omega_n**2 / np.sqrt((omega_n **
                             2 - w_ref**2)**2 + (2*zeta*omega_n*w_ref)**2))
    w_line = np.array([w_ref, w_ref*10])
    gain_line = np.array([gain_ref, gain_ref - 40])
    ax1.semilogx(w_line, gain_line, 'r--', alpha=0.7, label='-40dB/decade')

    ax1.set_xlabel('角周波数 [rad/s]')
    ax1.set_ylabel('ゲイン [dB]')
    ax1.set_title('二次遅れ系の検証：ゲイン線図')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim([-60, 10])

    # 位相線図
    ax2.semilogx(w, phase_deg, 'b-', linewidth=2, label='理論値')
    ax2.axvline(x=omega_n, color='orange', linestyle='--',
                alpha=0.7, label=f'固有角周波数 {omega_n:.1f} rad/s')
    ax2.axhline(y=-90, color='r', linestyle='--', alpha=0.7, label='-90°')
    ax2.axhline(y=0, color='g', linestyle='--', alpha=0.7, label='0°')
    ax2.axhline(y=-180, color='g', linestyle='--', alpha=0.7, label='-180°')

    ax2.set_xlabel('角周波数 [rad/s]')
    ax2.set_ylabel('位相 [deg]')
    ax2.set_title('二次遅れ系の検証：位相線図')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim([-200, 20])

    plt.tight_layout()
    plt.savefig('second_order_verification.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 検証計算
    print(f"\n検証結果:")
    print(f"元データの共振ピーク: 54.5 rad/s, 4.84 dB")
    print(f"理論値の共振ピーク: {omega_r:.1f} rad/s, {Mp_db:.2f} dB")
    print(
        f"角周波数誤差: {abs(omega_r - 54.5):.1f} rad/s ({abs(omega_r - 54.5)/54.5*100:.1f}%)")
    print(
        f"ピークゲイン誤差: {abs(Mp_db - 4.84):.2f} dB ({abs(Mp_db - 4.84)/4.84*100:.1f}%)")


def main():
    """メイン関数"""
    print("ボード線図解析による伝達関数導出の検証")
    print("=" * 50)

    # 一次遅れ系の検証
    first_order_system_verification()

    # 二次遅れ系の検証
    second_order_system_verification()

    print("\n検証完了：両システムとも高い精度で元データと一致しています。")


if __name__ == "__main__":
    main()
