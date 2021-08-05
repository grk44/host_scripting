#Greg Kessel
#1/28/2021

#set initial variables and array
$port='HTTP'
$servers=@('www.google.com','www.pitt.edu','www.cnn.com')

#add unixs.cis.pitt.edu to the array
$servers +='unixs.cis.pitt.edu'

#display the thrird item in the array (index 2)
$servers[2]

#display total number of items in the array
$servers.Count

#take array $servers | into foreach and {$_} references each index | each index is passed 
#       to test-netconnection using variable $port for the flag value
$servers |ForEach-Object -Process {$_} | Test-NetConnection -CommonTCPPort $port

$arr=@() #blank array creation
[arry]$arr2 #also blank array

foreach($i in $arr){ #adds all values in the array
    $total +=$i
}