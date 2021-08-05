
$scores=$null
$isint=$true
[int]$ScoresSum=$null

$scores=Read-Host('How Many Scores to Enter?')
do{
    try {
        [int]$intScores=$scores
        $isint = $false
    }catch [System.Management.Automation.RuntimeException] {
        Write-Host 'Not a Valid Number'
        $scores=Read-Host('How Many Scores to Enter?')
        $isint = $true            
    }
}while ($isint)
$i=0
While ($i -lt $intScores) 
{   
   do{
    try {        
        [int]$ScoresSum += Read-Host('Enter Score ',$i)
        $i++
        $isint2=$false
    }catch [System.Management.Automation.RuntimeException] {
        Write-Host 'Not a Valid Number'
        $isint2=$true             
    }
    }while ($isint2) 
}
[int]$scoreAvg=$ScoresSum/$scores
Write-Host ('Score average:', $scoreAvg)
