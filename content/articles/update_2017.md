Title: Update der Homepage
Date: 2017-10-23 10:00
Tags: HTML, Datensicherheit 
Slug: update_2017
Status: published
Category: IT-Ethik
HeaderImage: /images/update_2017.png
Summary: Ich habe meiner Internetseite ein Update verpasst.

Ich habe meiner Internetseite ein Update verpasst. Sie basiert jetzt auf reinem HTML und CSS, verwendet kein Javascript mehr, keine Links zu Google-Analytics und keinen Canvas-Blödsinn. Das hat für dich den Vorteil, dass du aufgrund meiner Seite keinem möglichen Tracking ausgesetzt bist und die Seite schneller läd, und für mich, dass ich kein Wordpress verwenden muss.

Statt Wordpress, verwende ich zur Erzeugung dieser Internetseiten ein Programm namens [Pelican](http://getpelican.com/), das aus Markdown-Dateien eine statische Internetseite macht. Ich habe [diese Anleitung](http://mathamy.com/migrating-to-github-pages-using-pelican.html) und [dieses Styling](https://github.com/art1fa/minimalX) verwendet, etwas modifiziert, und den Quellcode auf GitHub hinterlegt.

## Details
Ich habe die Arbeitsverzeichnisse auf meinem GitHub-Account *DorKeinath* gespeichert unter *xcosx.github.io*, also in *https://github.com/DorKeinath/xcosx.github.io*.
Die HTML-Dateien liegen in meinem GitHub-Account *xcosx* im Verzeichnis *xcosx.github.io*, Also in https://github.com/xcosx/xcosx.github.io.git.

### Suche mit MetaGer
Der HTML-Code für die coole Suchlupe ist der folgende. Weil er mich ein bisschen Zeit gekostet hat, poste ich ihn hier. Ich würde gerne statt des Bildes Fontawesome benutzen, habe aber noch keine Lösung ohne Javascript gefunden.

```HTML
<!-- Suche mit MetaGer -->
<form class="w3-bottombar w3-border-white w3-hover-border-red" action="https://metager.de//meta/meta.ger3" method="get" accept-charset="UTF-8">
    <style type="text/css" scoped>
    input[type=text] {
        width: 53px;
        box-sizing: border-box;
        border: 0px solid #fff;
        background-color: #fff;
        /*Für die Lupe*/
        background-image: url('/images/searchicon8.png');
        background-size: 18px;
        background-repeat: no-repeat;
        background-position-x: 50%;
        background-position-y: 50%;
        /*Für den Text "Suche mit MetaGer"*/
        font-size: 14pt;
        padding-left: 51px;
        -webkit-transition: width 0.4s ease-in-out;
        transition: width 0.4s ease-in-out;
      }
      input[type=text]:focus {
        width: 100%;
        background-position-x: 95%;
        padding-left: 15px;
        background-color: rgb(241, 241, 241);
        color: #868282;
      }
    </style>
    <input type="text" name="eingabe" placeholder="Suche mit Metager" required></input>
    <input type="hidden" name="encoding" value="utf8"></input><input type="hidden" name="site" value="xcosx.de">
    <input type="hidden" name="lang" value="all">
    <input type="hidden" name="wdgt-version" value="1">
</form>
<!-- Suche Ende -->
```

### Workflow
Für's Erstellen und Posten eines neuen Artikels verwende ich die folgenden Befehle.

```bash
# Voransicht
source bin/activate
sudo make devserver
firefox localhost:8000

# Inhalt veröffentlichen
sudo pelican content -s publishconf.py
cd output
git add --all
git commit -m "update"
git push origin master
xcosx

# Quellcode auf GitHub speichern
git add --all
git commit -m "update"
git push origin master
dorkeinath
```
