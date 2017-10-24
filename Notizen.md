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


# Git Cheatsheet
https://ansas-meyer.de/programmierung/cheatsheet-git-branching/

# Inhalt der alten haccess auf xcosx.de

```
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>

# END WordPress
```
