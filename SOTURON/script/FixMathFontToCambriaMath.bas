Attribute VB_Name = "FixMathFontToCambriaMath"
Option Explicit

' FixMathFontToCambriaMath.bas
' 作成日: 2026-01-16
' 説明: 文書内のすべての数式フォントを "Cambria Math" に統一します。
'       PDF変換時の数式崩れを防ぐため、Cambria Math（Word標準数式フォント）に強制変更します。

Sub FixMathFontToCambriaMath()
    Dim om As OMath
    Dim omRange As OMathFunction
    Dim processedCount As Long
    Dim totalCount As Long
    
    ' 画面の更新を停止して高速化
    Application.ScreenUpdating = False
    
    On Error GoTo ErrorHandler
    
    ' 処理開始メッセージ
    totalCount = ActiveDocument.OMaths.Count
    
    If totalCount = 0 Then
        MsgBox "文書内に数式が見つかりませんでした。", vbInformation, "数式フォント修正"
        Application.ScreenUpdating = True
        Exit Sub
    End If
    
    ' ステータスバーに進捗表示
    Application.StatusBar = "数式フォント変更中..."
    
    ' 1. ドキュメント全体のデフォルト数式フォントを Cambria Math に設定
    ActiveDocument.OMathFontName = "Cambria Math"
    
    ' 2. 既存の全数式のフォントを Cambria Math に統一
    processedCount = 0
    For Each om In ActiveDocument.OMaths
        ' 数式全体のフォントを変更
        om.Range.Font.Name = "Cambria Math"
        om.Range.Font.NameAscii = "Cambria Math"
        om.Range.Font.NameFarEast = "Cambria Math"
        om.Range.Font.NameOther = "Cambria Math"
        
        ' 数式を再構築（フォント変更を確実に適用）
        om.BuildUp
        
        processedCount = processedCount + 1
        
        ' 進捗表示（10個ごと）
        If processedCount Mod 10 = 0 Or processedCount = totalCount Then
            Application.StatusBar = "数式フォント変更中... " & processedCount & "/" & totalCount
        End If
    Next om
    
    ' 3. 数式エリア（OMathZone）内のテキストも確実に変更
    Dim rng As Range
    Set rng = ActiveDocument.Content
    
    With rng.Find
        .ClearFormatting
        .Replacement.ClearFormatting
        .Replacement.Font.Name = "Cambria Math"
        .Text = ""
        .Replacement.Text = ""
        .Format = True
        .MatchWildcards = False
        .Wrap = wdFindContinue
        
        ' 数式オブジェクト内のみを対象に検索置換
        Dim i As Long
        For i = 1 To ActiveDocument.OMaths.Count
            Set rng = ActiveDocument.OMaths(i).Range
            rng.Font.Name = "Cambria Math"
        Next i
    End With
    
    ' ステータスバーをクリア
    Application.StatusBar = False
    
    ' 画面更新を再開
    Application.ScreenUpdating = True
    
    ' 完了メッセージ
    MsgBox "数式フォント変更が完了しました。" & vbCrLf & vbCrLf & _
           "処理した数式: " & processedCount & " 個" & vbCrLf & _
           "変更後フォント: Cambria Math", _
           vbInformation, "完了"
    
    Exit Sub

ErrorHandler:
    Application.ScreenUpdating = True
    Application.StatusBar = False
    MsgBox "エラーが発生しました。" & vbCrLf & vbCrLf & _
           "エラー内容: " & Err.Description & vbCrLf & _
           "エラー番号: " & Err.Number, _
           vbCritical, "エラー"
End Sub

' クイック実行用（ショートカットキーに割り当て可能）
Sub QuickFixMathFont()
    Call FixMathFontToCambriaMath
End Sub
