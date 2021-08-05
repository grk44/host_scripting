Get-Content -Path C:\Users\student\Desktop\log.txt 


Switch -Regex (Get-Content C:\Users\student\Desktop\log.txt){
    ‘.*failed' {echo ("Error Found")}
    '[^failed$]' {echo ("OK")}
}