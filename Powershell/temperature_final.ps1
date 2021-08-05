

do{
    #$temp =$true
    $tEntry = $null
    $t1 = $null
    $t2 = $null
    $convertdone = $true
    $t1 = Read-Host "-----------------`nConvert Temperature`n1:Celsius to Fahrenheit `n2:Fahrenheit to Celsius `nSelect 1 or 2"

    if($t1 -eq 1)
    {
        Write-Host 'Convert C to F'
        $t2 = Read-Host 'Enter a Temperature in Celsius'

        do{
            try {
                [int]$tEntry=$t2
                [int]$tConvert=($tEntry/5*9)+32
                Write-Host 'Celsius:'$tEntry "`n" 'Fahrenheit:'$tConvert
                $convertdone = $false
            }catch [System.Management.Automation.RuntimeException] {
                Write-Host 'Not a Valid Number'
                $t2 = Read-Host "Enter a Temperature in Celsius"
                $convertdone = $true            
            }            
        }while ($convertdone)
        $temp =$false
    }  
    elseif ($t1 -eq 2)
    {
        Write-Host 'convert F to C'
        $t2 = Read-Host 'Enter a Temperature in Fahrenheit'

        do{
            try {
                [int]$tEntry=$t2
                [int]$tConvert=($tEntry-32)*5/9
                Write-Host 'Fahrenheit:'$tEntry "`n" "Celsius:"$tConvert
                $convertdone = $false
            }catch [System.Management.Automation.RuntimeException] {
                Write-Host 'Not a Valid Number'
                $t2 = Read-Host "Enter a Temperature in Fahrenheit"
                $convertdone = $true            
            }            
        }while ($convertdone)      

    }   
    else 
    {
    Write-Host "-----------------`nInvalid Entry"
    $temp=$true
    }
}while ($convertdone)