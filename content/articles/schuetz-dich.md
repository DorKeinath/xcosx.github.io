Title: Schütz dich!
Date: 2016-03-14 19:51
Category: IT-Ethik
Tags: Apps, Datensicherheit
Slug: schuetz-dich
Status: published
HeaderImage: /images/schuetz-dich.png
Summary: Mit diesen Apps kannst du deine Privatsphäre schützen, und die deiner Freunde.

Mit diesen Apps kannst du deine Privatsphäre schützen, und die deiner Freunde.

<!--more-->Unsere tolle Regierung hat die Vorratsdatenspeicherung (VDS)
wieder einmal eingeführt. Das zeigt wie wenig sich viele Bundestags und
-ratsabgeordnete beim Thema Datensicherheit auskennen und mit dem damit
untrennbar verbundenen Schutz der Privatsphäre der Bürger. [Meine
Zusammenfassung der Argumente gegen die
VDS.](http://xcosx.de/wp-content/uploads/2015/10/VDS_Vorratsdatenspeicherung.pdf)
[Meine Präsentation Freiheit vs.
VDS](http://www.xcosx.de/mgb/keineph-slides/slides/vds.md.html). Bis das
Verfassungsgericht die VDS wieder für illegal beurteilt, kann man nur
eins tun: sich selbst schützen. Die wirksamsten Möglichkeiten sind der
Verzicht auf's Internet und das vorübergehende Einmotten der SIM-Karte.
Zu radikal? Dann kannst du folgendes tun:

Für Jedermann: Schöne Apps, leicht zu bedienen
----------------------------------------------

Mit diesen netten Apps kann man sicherstellen, dass Mitteilungen
verschlüsselt übertragen werden. Im Vergleich zu normalen SMS und
WhatsApp sind diese Apps sehr sicher.

### Android

-   **Conversations**
    ([Playstore](https://play.google.com/store/apps/details?id=eu.siacs.conversations),
    [F-Droid](https://f-droid.org/repository/browse/?fdfilter=conversation&fdid=eu.siacs.conversations)).
    Das ist zurzeit die sicherste App mit dem besten Konzept.
    [Mehr.](http://xcosx.de/conversations/)
-   Es gibt noch weitere Apps, die eine gute Verschlüsselung haben oder
    vertrauenswürdig aussehen, aber aus anderen Sicherheitsaspekten
    heraus *nicht* so gut sind
    -   **Signal**. Benutzt einen zentralen Server und ist nicht so offen
        für eine Entwickler-Community. Ist also nicht optimal. Dafür kann man telefonieren und die Nachrichten kommen zuverlässig an.
    -   **Threema**. Benutzt einen zentralen Server und ist nicht
        open-source. Außerdem steht der Server in der Schweiz, und die
        Schweiz hat Ende 2016 ihrem Geheimdienst quasi alle Rechte
        gewährt. Ist also nicht optimal.

### Apple-Zeug

-   Der beste iPhone-Messenger
    heißt[**ChatSecure.**](https://xcosx.de/messenger-fuers-iphone/)
    Beim ersten Start unter "Neues Konto" eine Jabber-ID anlegen, zum
    Beispiel als Benutzername deinen Namen und als Domäne
    ubuntu-jabber.de. Fürs Chatten mit einer anderen Person braucht man
    seine Jabber-ID also z.B. person@ubuntu-jabber.de.

### Windoof

-   **Threema**
    ([WindowsStore](https://www.microsoft.com/en-us/store/apps/threema/9nblggh095s5)).
    Einschränkungen s.o.

 

Für Anspruchsvollere: Noch mehr Privatsphäre
--------------------------------------------

Um zu erschweren, dass beim Surfen und Kommunizieren deine Inhalte *und
Metadaten* gespeichert werden, muss man Verschlüsselungsprogramme in
Kombination mit Tor verwenden.

### Android

-   **Orbot**
    ([F-Droid](https://f-droid.org/repository/browse/?fdfilter=orbot&fdid=org.torproject.android)/
    [Playstore](https://play.google.com/store/apps/details?id=org.torproject.android)).
    Für die Verbindung mit Tor. Dann Firefox mit Orbot verwenden.

### Apple-Zeug

-   **Onion Browser**
    ([iTunes](https://itunes.apple.com/us/app/onion-browser/id519296448?mt=8)).
    Browser fürs Surfen mit Tor.

### Windoof

-   **TorBundle**
    ([chip.de](http://www.chip.de/downloads/Tor-Browser-Paket_22479695.html))
-   **Pidgin**
    ([chip.de](http://www.chip.de/downloads/Pidgin_13009923.html)) + OTR
    für Pidgin
    ([chip.de](http://www.chip.de/downloads/OTR-fuer-Pidgin_24518582.html)).
    Das OTR-Plugin aktivieren. Beim Erstellen eines neuen Kontos XMPP
    auswählen, bei Benutzer zum Beispiel deinen Namen und als Domäne
    jabber.de. Fürs Chatten mit einer anderen Person braucht man seine
    Jabber-ID also person@xmppserver.de. Als Proxy Tor einstellen.
-   Alternativ zu Pidgin: torchat

### Linux

-   **Tor** (<https://www.torproject.org/projects/torbrowser.html.en>)
-   **Gajim**. Verwendet XMPP und OMEMO, als wie Conversations und
    ChatSecure.
    [Installationsanleitung](https://xcosx.de/gajim-mit-omemo/).

 

Weitere Maßnahmen
-----------------

Natürlich ist die optimale Sicherheit durch die Installation von ein,
zwei Apps noch nicht erreicht. Dadurch kann man zum Beispiel noch nicht
sicherstellen, dass keine App nach Hause telefoniert, oder auch das
Betriebssystem, der Prozessor,... Will man noch mehr Maßnahmen
ergreifen, kann man sich am
[kuketz-blog](http://www.kuketz-blog.de/projekte/) orientieren. Eine
übersichtliche Darstellung von weiteren Maßnahmen findet man auf
[netzpolitik](https://netzpolitik.org/2015/2-jahre-snowden-enthuellungen-special-zur-digitalen-selbstverteidigung/).
Wer sich umfassend einarbeiten will, kann das gut auf
[capulcu](https://capulcu.blackblogs.org/bandi/)angehen. Die Seite
[privacytools.io](https://www.privacytools.io/) ist handlich und
beinhaltet viele praktische Tipps zu Apps usw.

### Was ist mit E-Mails?

Den Inhalt von E-Mails kann man inzwischen recht komfortabel mit PGP
verschlüsseln. Leider ist es aber umständlich, per E-Mail ohne die
Preisgabe von Metadaten zu kommunizieren. Auf capulcu (s.o.) sind einige
Möglichkeiten beschrieben.

Die sichersten (und nachhaltigsten!) E-Mail-Anbieter sind
[Posteo](https://posteo.de/de) und [Mailbox.org](http://mailbox.org/).
Bei anderen Anbietern sind eure E-Mails oft unverschlüsselt gespeichert,
bei manchen werden sogar die Inhalte statistisch ausgewertet.
