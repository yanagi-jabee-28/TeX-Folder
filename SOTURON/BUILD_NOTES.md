✅ Quick build & portability notes for `Yanagihara_BCDR_MEGTRON6_2026.tex`

Purpose
- Capture immediate fixes and TeX Live commands so reproductions on other machines succeed.

Immediate workaround (project-local)
- If `kpsewhich junsrt.bst` fails on another machine, copy a local `junsrt.bst` into the project root (same dir as the .tex). LaTeX will then always find it.

Suggested TeX Live checks & fixes (use in PowerShell / WSL / macOS terminal)
- Check whether `junsrt.bst` is present in the TeX tree:
  - kpsewhich junsrt.bst
- If missing, locate package that provides it:
  - tlmgr search --file junsrt.bst
- Install the relevant package or the Japanese collection (broad fix):
  - tlmgr install collection-langjapanese
  - OR: tlmgr install <package-found-by-search>

Notes for MiKTeX users (Windows)
- Use the MiKTeX Console to install the missing BibTeX style or enable on-the-fly package installation.

Build / test commands (what I ran locally)
- kpsewhich junsrt.bst   # check availability
- latexmk -pdf Yanagihara_BCDR_MEGTRON6_2026.tex  # full build (latexmk handles bibtex)

Rationale for recent source edits
- `microtype` added and global `\sloppy` removed: better typography and fewer global side-effects.
- `\imunit` introduced; `\mi` kept as alias (backwards compatible).
- Bibliography uses a conditional: if `junsrt.bst` is missing the build falls back to `unsrt` rather than failing.

Recommended follow-ups
1. (High) Install the package that provides `junsrt.bst` on CI/build machines.
2. (Medium) Replace the conditional fallback with the project-local `junsrt.bst` if you must guarantee exact citation formatting across environments.
3. (Low) Add a CI job that runs `latexmk` on this repository and fails if `kpsewhich junsrt.bst` is not found (to catch portability regressions).

If you want, I can (A) search for `junsrt.bst` on your system, (B) add the file to the repo if you approve, or (C) add a CI/Action workflow to enforce availability.