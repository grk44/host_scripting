

function findfeature {
    param ([string]$featName)
        $feat1=Get-WindowsFeature $featName | Where-Object -Property Name
        $instState=$feat1.Installed

        if ($instState -eq $True) {
            Write-Host $featName " is installed"
        }
        elseif ($instState -eq $false) {
            Write-Host $featName "Is not installed" `n "Installing Now"   
            Add-WindowsFeature $featName | Out-File -Append $env:USERPROFILE\feature.log 
            Get-WindowsFeature $featName
            Write-Host `n 'Installation of ' $featName ' Complete' `n 'Check log at' $env:USERPROFILE 'for details.'
        }
        else {
            Write-Host 'There was a problem finding that' `n 'Check Spelling and Feature Name'
        }    
}
