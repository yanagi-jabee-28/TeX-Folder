import sys
from pathlib import Path

p = Path(r"c:\Users\kaito\TeX-Folder\SOTURON\資料\Transmission_Line_formatted.md")
text = p.read_text(encoding='utf-8')
lines = text.splitlines(keepends=True)

def is_para_quote(line):
    return line.startswith('> ') and not line.startswith('> *') and not line.startswith('> -') and not line.startswith('>   *') and not line.startswith('> * ')

out = []
i = 0
n = len(lines)
changes = 0
while i < n:
    line = lines[i]
    if is_para_quote(line):
        buf = line.lstrip('> ').rstrip('\n')
        j = i + 1
        merged = False
        while j < n and is_para_quote(lines[j]):
            # join with single space
            buf += ' ' + lines[j].lstrip('> ').rstrip('\n')
            j += 1
            merged = True
        out.append('> ' + buf + '\n')
        if merged:
            changes += 1
        i = j
    else:
        out.append(line)
        i += 1

if changes > 0:
    bak = p.with_suffix('.md.bak')
    bak.write_text(text, encoding='utf-8')
    p.write_text(''.join(out), encoding='utf-8')
    print(f"Merged {changes} blockquote paragraph(s). Backup saved to {bak}")
else:
    print("No blockquote paragraphs needed merging.")
