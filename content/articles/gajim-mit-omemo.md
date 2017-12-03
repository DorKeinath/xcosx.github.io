Title: Gajim mit OMEMO
Date: 2016-12-05 20:33
Category: IT
Slug: gajim-mit-omemo
Tags: Datensicherheit, Apps
Status: published
HeaderImage: /images/gajim-mit-omemo.png
Summary: Bei Gajim das OMEMO-Plugin zum Laufen zu bringen ist nicht ganz trivial. Hier ist eine Anleitung.

Bei Gajim das OMEMO-Plugin zum Laufen zu bringen ist nicht ganz
trivial. Gajim ist ein Programm, mit dem man Chatten kann und OMEMO ist die aktuellste Verschlüsselungstechnik.

Wenn man nur in Konferenzen unterwegs
ist, braucht man es nicht installieren, aber um mit Gajim sicher
verschlüsselt und praktisch zu chatten, braucht man das OMEMO-Plugin.

[Hier](http://barfoos.blogsport.eu/gajim-mit-omemo-verschluesselung/)
findet man eine tolle Anleitung. Bei mir musste vorher noch pip
installiert werden und das sudo dann mit -H angewendet werden. Deswegen
hier meine Terminal-Befehle

Aktuellstes Gajim installieren

```bash
sudo add-apt-repository 'deb ftp://ftp.gajim.org/debian unstable main'
sudo apt-get update
sudo apt-get upgrade
```    


Zum Überprüfen ob die Installation erfolgreich war
```bash
dpkg -l gajim
```  
python-axolotl unter Ubuntu 16.04 LTS

```bash
sudo apt install python-axolotl python-protobuf
```  

python-axolotl unter Ubuntu 14.04.5 TLS

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
cd Downloads/
wget https://bootstrap.pypa.io/get-pip.py
sudo chmod +x get-pip.py
sudo -H python get-pip.py
sudo -H pip install cryptography --upgrade
sudo -H pip install python-axolotl
sudo -H pip install protobuf==2.6.1 python-axolotl
```  

Dann mit gajim das Plugin OMEMO

```bash
gajim -l gajim.plugin_system.omemo=DEBUG
```  
und weiter mit Klicken. Nach dem Installieren das **Aktivieren** nicht vergessen.
