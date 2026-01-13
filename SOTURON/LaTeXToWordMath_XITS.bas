' LaTeXToWordMath_XITS.bas
' 作成日: 2026-01-13
' 説明: 文書内のインライン LaTeX スタイル ($...$) を Word の数式に変換し
'       文書内すべての数式フォントを "XITS Math" に統一します。

Attribute VB_Name = "LaTeXToWordMath_XITS"
Option Explicit

Sub LaTeXToWordMath_XITS()
    Dim rng As Range
    Dim mathRng As Range
    Dim om As OMath

    ' 画面の更新を停止して高速化
    Application.ScreenUpdating = False

    ' 1. ドキュメント全体のデフォルト数式フォントを XITS Math に設定
    ' ※これをしないと、一部の数式記号が Cambria Math に戻ることがあります
    On Error Resume Next ' フォントがない場合のエラー回避
    ActiveDocument.OMathFontName = "XITS Math"
    On Error GoTo 0

    Set rng = ActiveDocument.Content

    ' 2. $...$ の変換処理（元のロジック）
    With rng.Find
        .ClearFormatting
        .Text = "\$([!$]@)\$"  ' $と$の間にある文字を検索（ワイルドカード利用）
        .MatchWildcards = True
        .Wrap = wdFindStop

        Do While .Execute
            ' $ 記号を除去して範囲を再設定
            Set mathRng = ActiveDocument.Range(Start:=rng.Start + 1, End:=rng.End - 1)

            ' 元のテキスト（$込み）を削除し、中身だけにする
            rng.Text = mathRng.Text

            ' 数式オブジェクトに変換
            rng.OMaths.Add rng
            rng.OMaths(1).BuildUp

            ' 次の検索へ（検索範囲をリセット）
            rng.Collapse Direction:=wdCollapseEnd
        Loop
    End With

    ' 3. 文書内の「すべての数式」のフォントを XITS Math に統一
    ' (変換したもの + すでに数式だったもの全て対象)
    For Each om In ActiveDocument.OMaths
        om.Range.Font.Name = "XITS Math"
    Next om

    ' 画面更新を再開
    Application.ScreenUpdating = True

    MsgBox "変換およびフォント変更(XITS Math)が完了しました。", vbInformation
End Sub
