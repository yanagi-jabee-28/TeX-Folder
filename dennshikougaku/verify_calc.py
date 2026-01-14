import math

# constants
k = 1.38e-23
e = 1.60e-19
m = 9.11e-31
h = 6.63e-34
c = 3.00e8

# Question 1
d = 1.0e-2
DeltaV = 200.0
E = -DeltaV/d
a = e*abs(E)/m
t = math.sqrt(2*d/a)
v = math.sqrt(2*e*DeltaV/m)
DeltaK = e*DeltaV

# Question 2
KE = 100.0 * e
B2 = 0.05
v2 = math.sqrt(2*KE/m)
r = m*v2/(e*B2)
f = e*B2/(2*math.pi*m)

# Question 3
D = 1.0e-2
Va = 100.0
B3 = 0.10
E3 = Va/D
S = (m*E3)/(e*B3*B3)
xm = 2*S
ym = math.pi*S

# helper


def sig(x, n=3):
    if x == 0:
        return 0.0
    return float(f"{x:.{n-1}e}")


print("Question 1 computed values:")
print(f"E = {E:.6e} V/m")
print(f"a = {a:.6e} m/s^2")
print(f"t = {t:.6e} s")
print(f"v = {v:.6e} m/s")
print(f"DeltaK = {DeltaK:.6e} J = {DeltaK/e:.6e} eV")
print()

print("Question 2 computed values:")
print(f"v = {v2:.6e} m/s")
print(f"r = {r:.6e} m")
print(f"f = {f:.6e} s^-1")
print()

print("Question 3 computed values:")
print(f"E = {E3:.6e} V/m")
print(f"S = {S:.6e} m")
print(f"x_m = {xm:.6e} m")
print(f"y_m = {ym:.6e} m")
print()

# compare to expected from file
expected = {
    'a': 3.515e15,
    't': 2.39e-9,
    'v': 8.38e6,
    'DeltaK': 3.20e-17,
    'v2': 5.93e6,
    'r': 6.75e-4,
    'f': 1.40e9,
    'xm': 1.14e-5,
    'ym': 1.79e-5,
}

print('Comparisons (relative error):')
for kname, exp in expected.items():
    comp = {'a': a, 't': t, 'v': v, 'DeltaK': DeltaK,
            'v2': v2, 'r': r, 'f': f, 'xm': xm, 'ym': ym}[kname]
    rel = abs(comp-exp)/exp
    print(f"{kname}: computed={comp:.6e}, expected={exp:.6e}, rel_err={rel:.3e}")

# simple pass/fail
print('\nPass/Fail (tol rel 1e-3):')
for kname, exp in expected.items():
    comp = {'a': a, 't': t, 'v': v, 'DeltaK': DeltaK,
            'v2': v2, 'r': r, 'f': f, 'xm': xm, 'ym': ym}[kname]
    rel = abs(comp-exp)/exp
    ok = 'PASS' if rel < 1e-3 else 'FAIL'
    print(f"{kname}: {ok} (rel_err={rel:.3e})")
