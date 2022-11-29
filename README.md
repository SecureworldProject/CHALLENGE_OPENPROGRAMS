# CHALLENGE_OPENPROGRAMS
valida PC corporativo usando una lista de programas abiertos

Este challenge genera una cadena binaria con un bit por programa. en el ejemplo hay 7 programas y por lo tanto la cadena es de 7 bit
la cadena "correcta" es la que quiera el administrador , no necesariamente todo 1s

la lista de programas abiertos debe ser una cadena con los programas separados por comas
```json 
{
"FileName": "challenge_loader_python.dll",
"Description": "challenge de progs abiertos",
"Props": {
  "module_python": "openprogs",
  "validity_time": 3600,
  "refresh_time": 1000,
  "process_list": "chrome.exe,notepad.exe,Teams.exe,ccSvcHst.exe,sisipsutil.exe,vpnui.exe,ibmpmsvc.exe"
},
"Requirements": "none" 
}
```
