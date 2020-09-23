Sub stocks():
    'Set CurrentWs Variable as a Worksheet
    Dim CurrentWs As Worksheet
    
    'Loop through each worksheet in workbook
    
    For Each CurrentWs In Worksheets
    
        'Set variables for each value stored
        Dim Ticker As String
        Ticker = " "
        
        Dim TotalVolume As Double
        TotalVolume = 0
    
        Dim OpenPrice As Double
        OpenPrice = 0

        Dim ClosePrice As Double
        ClosePrice = 0

        Dim PriceChange As Double
        PriceChange = 0
        
        Dim PercentChange As Double
        PercentChange = 0
        
        Dim Lastrow As Long
        Dim i As Long

        Dim MaxTicker As String
        MaxTicker = " "

        Dim MinTicker As String
        MinTicker = " "

        Dim MaxPercent As Double
        MaxPercent = 0

        Dim MinPercent As Double
        MinPercent = 0

        Dim MaxVolumeTicker As String
        MaxVolumeTicker = " "

        Dim MaxVolume As Double
        MaxVolume = 0
        
         'Set where the first Summary Table row output should be
        Dim SummaryTableRow As Long
        SummaryTableRow = 2
        
    '-------------------------------------------------------------------------'
        
        'Create variable to calculate last row
        Lastrow = CurrentWs.Cells(Rows.Count, 1).End(xlUp).Row
        
        'Insert Summary Table Headers
        CurrentWs.Range("I1").Value = "Ticker"
        CurrentWs.Range("J1").Value = "Yearly Change"
        CurrentWs.Range("K1").Value = "Percent Change"
        CurrentWs.Range("L1").Value = "Total Stock Volume"
        CurrentWs.Range("O2").Value = "Greatest % Increase"
        CurrentWs.Range("O3").Value = "Greatest % Decrease"
        CurrentWs.Range("O4").Value = "Greatest Total Volume"
        CurrentWs.Range("P1").Value = "Ticker"
        CurrentWs.Range("Q1").Value = "Value"
        
        'Set the first Open Price to the second row third column on the each worksheet
        OpenPrice = CurrentWs.Cells(2, 3).Value
    
        'Loop through the Current worksheet
        For i = 2 To Lastrow
            'Determine if the next row matches the previous row (to know when you have reach the end of the rows for a ticker)
            If CurrentWs.Cells(i + 1, 1).Value <> CurrentWs.Cells(i, 1).Value Then
                'Give variables for each row values
                Ticker = CurrentWs.Cells(i, 1).Value
                
                ClosePrice = CurrentWs.Cells(i, 6).Value
                
                PriceChange = ClosePrice - OpenPrice
                'Check if there are any divide by 0
                If OpenPrice <> 0 Then
                    PercentChange = (PriceChange / OpenPrice) * 100
                Else
                    MsgBox ("For " & Ticker & ", Row " & CStr(i) & ": Open Price =" & OpenPrice & ". Fix <open> field manually and save the spreadsheet.")
                End If
                'Create running total for volume
                TotalVolume = TotalVolume + CurrentWs.Cells(i, 7).Value
                'Set the Column I and summary table row to Corresponding values
                CurrentWs.Range("I" & SummaryTableRow).Value = Ticker
            
                CurrentWs.Range("J" & SummaryTableRow).Value = PriceChange
                'Color the Yearly Change Value in the Summary Table
                 If (PriceChange > 0) Then
                    'If positive color Green
                    CurrentWs.Range("J" & SummaryTableRow).Interior.ColorIndex = 4
                ElseIf (PriceChange <= 0) Then
                    'If 0 or negative color red
                    CurrentWs.Range("J" & SummaryTableRow).Interior.ColorIndex = 3
                End If
                'Set the last 2 summary table columns to corresponding values and change format
                CurrentWs.Range("K" & SummaryTableRow).Value = (CStr(PercentChange) & "%")

                CurrentWs.Range("L" & SummaryTableRow).Value = TotalVolume
                'move to next summary table row
                SummaryTableRow = SummaryTableRow + 1
                'Reset price change and close price
                PriceChange = 0
                
                ClosePrice = 0
                'Have the next Open PRice be the cell after the last row with current ticker
                OpenPrice = CurrentWs.Cells(i + 1, 3).Value
                'Calculate the max, min, and max volume
                If (PercentChange > MaxPercent) Then
                    MaxPercent = PercentChange
                    MaxTicker = Ticker
                ElseIf (PercentChange < MinPercent) Then
                    MinPercent = PercentChange
                    MinTicker = Ticker
                End If
                       
                If (TotalVolume > MaxVolume) Then
                    MaxVolume = TotalVolume
                    MaxVolumeTicker = Ticker
                End If
                'Reset Percent change and total volume
                PercentChange = 0

                TotalVolume = 0
               
            Else
                'Keep adding to total volume running total if ticker still matches
                TotalVolume = TotalVolume + CurrentWs.Cells(i, 7).Value

            End If
        'Run through next ticker
        Next i
                'Input max, min, ticker, and max volume in second summary table
                CurrentWs.Range("Q2").Value = (CStr(MaxPercent) & "%")
                CurrentWs.Range("Q3").Value = (CStr(MinPercent) & "%")
                CurrentWs.Range("P2").Value = MaxTicker
                CurrentWs.Range("P3").Value = MinTicker
                CurrentWs.Range("Q4").Value = MaxVolume
                CurrentWs.Range("P4").Value = MaxVolumeTicker
                
      
    'Run through next worksheet
    Next CurrentWs
    
End Sub