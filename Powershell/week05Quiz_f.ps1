

function checkservice {
    param ([string]$svName)
        $sv1=Get-Service *$svName* | Sort-Object -Property Status
        # $sv1Run=$sv1.Status

        foreach ($r in $sv1){
            Write-Host ($r.Name + " is " + $r.Status)
        }
        
        $Userin1 = Read-Host "Output this list to a file? [Y/N]"
            switch ($Userin1) {
                Y { 
                    Get-Date | Out-File -Append $env:USERPROFILE\checkservice.txt
                    foreach ($r in $sv1){
                        ($r.Name + " is " + $r.Status) | Out-File -Append $env:USERPROFILE\checkservice.txt                    
                    }
                    Write-Host ("File located at " + $env:USERPROFILE)
                 }
                Default {
                    Write-Host ("File not created")  
                }
            }    

        
        $Userin2 = Read-Host "Do You want to start any stopped services? [Y/N]"
            switch ($Userin2) {
                Y { 
                    foreach ($r in $sv1){
                        if ($r.Status -eq 'Stopped') {
                            $uInStart = Read-Host $r.Name " is " $r.Status " Start Service? [Y/N]"
                            switch ($uInStart) {
                                Y { 
                                    Start-Service $r
                                    Write-Host ("Service " + $r + " is started")  }
                                Default { Write-Host ("Service " + $r + " NOT started")}
                            }
                            }                            
                        }
                    }
                 Default {
                    Write-Host "No Services will be started"
                }
            }
            

            
            $Userin3 = Read-Host "Output this new list to a file? [Y/N]"
            switch ($Userin3) {
                Y { 
                    Get-Date | Out-File -Append $env:USERPROFILE\checkservice.txt
                    foreach ($r in $sv1){
                        ($r.Name + " is " + $r.Status) | Out-File -Append $env:USERPROFILE\checkservice.txt                    
                    }
                    Write-Host ("File located at " + $env:USERPROFILE)
                 }
                Default {
                    Write-Host ("File not created")  
                }
            }
        }
                
            


    
