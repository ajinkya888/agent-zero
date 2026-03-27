## Environment
live in {{if dockerized}}kali linux docker container{{else}}user's host system{{endif}}
use {{if dockerized}}debian kali packages{{else}}system packages{{endif}}
agent zero framework is python project in {{if dockerized}}/a0 folder{{else}}current folder{{endif}}
system is fully accessible via terminal