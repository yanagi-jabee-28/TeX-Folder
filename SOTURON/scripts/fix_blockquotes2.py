from pathlib import Path
p = Path(r"c:\Users\kaito\TeX-Folder\SOTURON\資料\Transmission_Line_formatted.md")
text = p.read_text(encoding='utf-8')
lines = text.splitlines(keepends=True)

def is_list_quote(line):
    return line.startswith('> *') or line.startswith('> -') or line.startswith('>   *') or line.startswith('>     *')

out = []
i=0
n=len(lines)
changes=0
while i<n:
    line=lines[i]
    if line.startswith('> ') and not is_list_quote(line):
        buf = line.lstrip('> ').rstrip('\n')
        j=i+1
        merged=False
        while j<n and lines[j].startswith('> ') and not is_list_quote(lines[j]):
            buf += ' ' + lines[j].lstrip('> ').rstrip('\n')
            j+=1
            merged=True
        out.append('> '+buf+'\n')
        if merged:
            changes+=1
        i=j
    else:
        out.append(line)
        i+=1

if changes>0:
    bak = p.with_suffix('.md.bak2')
    bak.write_text(text, encoding='utf-8')
    p.write_text(''.join(out), encoding='utf-8')
    print(f"Merged {changes} additional blockquote paragraph(s). Backup saved to {bak}")
else:
    print("No additional merges needed.")
