' LaTeXToWordMath_XITS.bas
' 作成日: 2026-01-13
' 説明: 文書内のインライン LaTeX スタイル ($...$) を Word の数式に変換し
'       文書内すべての数式フォントを "XITS Math" に統一します。

Option Explicit

Sub LaTeXToWordMath_XITS()
    Dim rng As Range
    Dim mathRng As Range
    Dim om As OMath

    Application.ScreenUpdating = False

    On Error Resume Next
    ActiveDocument.OMathFontName = "XITS Math"
    On Error GoTo 0

    Set rng = ActiveDocument.Content

    With rng.Find
        .ClearFormatting
        .Text = "\$([!$]@)\$"
        .MatchWildcards = True
        .Wrap = wdFindStop

        Do While .Execute
            Set mathRng = ActiveDocument.Range(Start:=rng.Start + 1, End:=rng.End - 1)
            rng.Text = mathRng.Text
            rng.OMaths.Add rng
            rng.OMaths(1).BuildUp
            rng.Collapse Direction:=wdCollapseEnd
        Loop
    End With

    For Each om In ActiveDocument.OMaths
        om.Range.Font.Name = "XITS Math"
    Next om

    Application.ScreenUpdating = True
    MsgBox "変換およびフォント変更(XITS Math)が完了しました。", vbInformation
End Sub