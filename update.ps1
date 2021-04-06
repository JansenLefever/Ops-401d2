Set-ExecutionPolicy Bypass -Scope Process -Force

Install-Module -Name PSWindowsUpdate

Import-Module PSWindowsUpdate

Get-WindowsUpdate

Get-WUInstall -AcceptAll –AutoReboot

#Resource:https://www.nakivo.com/blog/automate-windows-updates-using-powershell-short-overview/
