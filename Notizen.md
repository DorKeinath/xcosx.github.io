# Voransicht
source bin/activate
sudo make devserver
firefox localhost:8000

# Inhalt veröffentlichen
pelican content -s publishconf.py

# Inhalt der alten haccess auf xcosx.de

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
