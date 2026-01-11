import heapq

# Frequencies extracted from SVG
freqs = {'4': 1, '1': 2, '3': 4, '5': 5, '2': 6, '6': 20, '0': 30, '7': 32}
# Codes read from SVG (ハフマン.svg / huffman_tree_q1_3.svg)
given_codes = {'4': '00000', '1': '00001', '3': '0001',
               '5': '0010', '2': '0011', '6': '01', '0': '10', '7': '11'}

# 1) Check total
total = sum(freqs.values())
print(f"Total frequency sum = {total}")

# 2) Internal node sums
A = freqs['4'] + freqs['1']
B = A + freqs['3']
C = freqs['5'] + freqs['2']
D = B + C
E = D + freqs['6']
F = freqs['0'] + freqs['7']
root = E + F
print(f"A (4+1) = {A}")
print(f"B (A+3) = {B}")
print(f"C (5+2) = {C}")
print(f"D (B+C) = {D}")
print(f"E (D+6) = {E}")
print(f"F (0+7) = {F}")
print(f"Root (E+F) = {root}")

# 3) Build Huffman tree (standard greedy)
heap = [(w, s) for s, w in freqs.items()]
heapq.heapify(heap)

# Use internal node markers as tuples ('*', left, right)
while len(heap) > 1:
    w1, n1 = heapq.heappop(heap)
    w2, n2 = heapq.heappop(heap)
    heapq.heappush(heap, (w1+w2, ('*', n1, n2)))

_, tree = heap[0]


def gen(node, prefix=''):
    # if leaf (string)
    if isinstance(node, str):
        return {node: prefix}
    # else internal
    _m, left, right = node
    d = {}
    d.update(gen(left, prefix + '0'))
    d.update(gen(right, prefix + '1'))
    return d


codes = gen(tree)
print('\nGenerated Huffman codes:')
for s in sorted(codes.keys()):
    print(f"{s}: {codes[s]}")

# 4) Average lengths
avg_generated = sum(len(codes[s]) * freqs[s] for s in freqs) / total
avg_given = sum(len(given_codes[s]) * freqs[s] for s in freqs) / total
print(f"\nAverage code length (generated) = {avg_generated:.4f}")
print(f"Average code length (given in SVG) = {avg_given:.4f}")

# 5) Check prefix-free for given codes


def is_prefix_free(code_dict):
    codes = list(code_dict.values())
    for i, a in enumerate(codes):
        for j, b in enumerate(codes):
            if i == j:
                continue
            if b.startswith(a):
                return False, a, b
    return True, None, None


pf, a, b = is_prefix_free(given_codes)
print(f"\nGiven codes prefix-free: {pf}")
if not pf:
    print(f"Conflict: {a} is a prefix of {b}")

# 6) Compare length multisets (optimality up to code assign)
len_generated = sorted([len(codes[s]) for s in freqs])
len_given = sorted([len(given_codes[s]) for s in freqs])
print(f"\nGenerated code lengths (sorted) = {len_generated}")
print(f"Given code lengths (sorted) =     {len_given}")
print(f"Lengths match: {len_generated == len_given}")

# 7) Note: multiple optimal trees may exist; if average lengths equal and length multisets match, given tree is optimal.
if abs(avg_generated - avg_given) < 1e-9 and len_generated == len_given:
    print('\nConclusion: Given codes are optimal (match Huffman average length and length distribution).')
else:
    print('\nConclusion: Given codes differ from one possible optimal assignment; check tree structure and tie-breakers.')
