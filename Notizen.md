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
cd ..
git add --all
git commit -m "update"
git push origin master
dorkeinath


# Git
https://ansas-meyer.de/programmierung/cheatsheet-git-branching/
https://git-scm.com/docs/git-credential-cache

# Fotos
## Neu
Den convert-Befehl aus der py-Datei im images-Ordner verwenden. TODO: Die py-Datei umschreiben.

## Alt
In Gimp das png auf 900x300 ändern: Bild/Leinwandgröße
Dann evtl: Ebene/Ebene skalieren auf Höhe 270

# Suche mit Metager/searches
    <!--
    <form action="https://metager.de" method="get" accept-charset="UTF-8">
        <style type="text/css" scoped>
            input[type=text] {
                width: 53px;
                box-sizing: border-box;
                border: 0px solid #fff;
                background-color: #fff;
                /*Picture*/
                background-image: url('/images/searchicon8.png');
                background-size: 18px;
                background-repeat: no-repeat;
                background-position-x: 50%;
                background-position-y: 50%;
                /*Picture end*/
                /*Für den Text bzw. Platzhalter */
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
                background-size:0px;
              }
              /*.search-bar .input-text {
              }*/
        </style>
        <input type="text" name="a" placeholder="Suche mit Qwant" required>
        <input type="hidden" name="q" value="site:xcosx.github.io">
    </form>
     -->

# Suche mit Qwant alt
Neu: https://help.qwant.com/de/help/qwant-search/wie-kann-ich-eine-suche-von-qwant-in-meine-webseite-einfugen/
<!-- Suche mit Quant -->
<form method="GET" action="http://www.qwant.com">
<div align="left">
<table bgcolor="#FFFFFF">
<tbody>
<tr>
<td>
<a href="http://www.qwant.com"> <img src="https://www.qwant.com/img/logo/q-48.png" border="0" alt="Qwant" align="absmiddle"></a>
<input type="text" name="q" size="31" maxlength="255" value="">
<input type="hidden" name="l" value="fr">
<input type="submit" name="btnG" value="@">
</td>
</tr>
</tbody>
</table>
</div>
</form>
<!-- Suche Ende -->

# Suche mit Qwant ne
