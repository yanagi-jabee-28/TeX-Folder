# LaTeX Workshop セットアップガイド

このワークスペースで Visual Studio Code の LaTeX Workshop 拡張機能を使って TeX ファイルをコンパイルするための手順をまとめています。

目標:
- LuaLaTeX (latexmk) を使って `Template1.tex` をコンパイルできるようにする。
- VS Code のワークスペース設定でビルドレシピを用意する。

チェックリスト:
- [ ] TeX（TeX Live もしくは MiKTeX）をインストール済みか
- [ ] latexmk がインストール済みで PATH に含まれているか
- [ ] VS Code に LaTeX Workshop がインストール済みか
- [ ] `.vscode/settings.json` と `.latexmkrc` がワークスペースに配置されているか

Windows（PowerShell）でのインストールと確認方法

1. TeX 環境のインストール（TeX Live 推奨）
   - TeX Live のならば https://tug.org/texlive/ からインストール
   - MiKTeX を使うなら https://miktex.org/ からインストール

2. latexmk の確認
   PowerShell で以下を実行して、latexmk と lualatex が利用できるか確認します。

```powershell
latexmk --version
lualatex --version
```

3. LaTeX Workshop の設定
- このワークスペースには、`.vscode/settings.json` を追加済みです。LaTeX Workshop のレシピとして luaLaTeX 用の latexmk を登録してあります。
- latexmk の設定はワークスペースルートの `.latexmkrc` に置かれています（Windows では拡張子なしファイルです）。

使用方法（VS Code）:
1. VS Code でワークスペースを開く
2. `Template1.tex` を開く
3. コマンドパレット (Ctrl+Shift+P) で「LaTeX Workshop: Build (Recipe)」を選ぶ。レシピにある "LuaLaTeX" を選択してビルドします。
   - もしくは、LaTeX Workshop のサイドバーの「Build」ボタンから実行できます。
4. 成功した場合は `out/` ディレクトリに PDF が出力されます。設定で `out` を指定しているためです。

トラブルシューティング:
- latexmk がない、または PATH の問題
  - `latexmk --version` の出力がない場合は latexmk をインストールするか、PATH に追加してください。
- lualatex が見つからない
  - TeX Live / MiKTeX のインストール時に LuaTeX のコンポーネントが入っていない場合があります。TeX Live の場合は tlmgr で lualatex を追加してください。
- `.latexmkrc` が反映されない
  - ファイル名は正確に `.latexmkrc`（先頭ドット、拡張子なし）である必要があります。Git で扱うときは隠しファイルとして表示されない場合があるので注意してください。

オプション: 自動ビルド設定
- 自動で保存時にコンパイルしたい場合は、`.vscode/settings.json` の `latex-workshop.latex.autoBuild.run` を `onSave` に変更してください（現在は `never` にしてあります）。

その他
- `Template1.tex` の先頭には `% !TEX program = lualatex` が既に入っているため、ファイルレベルで LuaLaTeX が使うことを明示しています。
- PDF ビューアは設定でタブで開くようになっています。

以上で、LaTeX Workshop から LuaLaTeX(latexmk) を使ったコンパイルができるようになります。問題が残る場合は、`latexmk --version` の出力と、VS Code の Output > LaTeX Workshop のログを教えてください。
