Title: Raspberry Pi: 30-€-PC mit vielen Einsatzmöglichkeiten
Date: 2014-03-01 13:15
Category: IT
Tags: Android, App, Freiheit, Musik, OwnCloud, PC, Raspberry Pi, Sicherheit, TV, UPnP
Slug: raspberry-pi-30-e-pc-mit-vielen-einsatzmoeglichkeiten
Status: published
HeaderImage: /images/rpi.png
Summary: Das Raspberry Pi ist eine Platine, die mit ihrem USB, HDMI, LAN und Audio-Anschluss viele Möglicheiten bietet. Sie ist ein kleiner
Computer.<!--more-->

Das Raspberry Pi ist eine Platine, die mit ihrem USB, HDMI, LAN und
Audio-Anschluss viele Möglicheiten bietet. Sie ist ein kleiner
Computer.<!--more-->

1.  RPi als Stereoanlage verwenden.
2.  Mittels RPi  Handy-Fotos oder Internet-Videos auf dem eigenen
    Fernseher anschauen (ZDF-Mediathek,...).
3.  RPi als eigenen Server verwenden.
4.  [Weitere
    Möglichkeiten](http://www.pcwelt.de/ratgeber/Die_besten_Verwendungsmoeglichkeiten_fuer_Raspberry_Pi-Mini-PC-7663628.html)

Die RPi hat meines Erachtens mehrere Vorteile. (1) Der Preis ist recht
günstig. WLAN-Lautsprecher oder Internet- bzw. Medien-taugliche
Fernseher sind teuer, die Software basiert oft auf keinem öffentlichen
Standard, sie bieten meist nur unregelmäßig Software-Updates und zudem
senden manche ungewollt Daten ins Netz. (2) Mit der RPi kann man leicht
alte Geräte zur Ausgabe moderner Medien umfunktionieren, was auch die
Umwelt schont. Der Betrieb eines Raspi ist resourcenschonend, sie
verbraucht sehr wenig Strom. (3) Ist der jetzige Verwendungszweck nicht
mehr gewünscht, kann die RPi für einen möglicherweise ganz anderen Zweck
verwendet werden.

Der Nachteil ist, dass man sich ein bisschen mit der Software
auseinandersetzen muss.

[Nettes Video, das einige Möglichkeiten des RPi
zeigt](https://www.youtube.com/watch?v=gflfzQs9JJs)

### Bedienung mit dem Handy

Im Prinzip geht die Bedienung einer RPi mit allen Apps, die das
UPnP-Protokoll oder Airplay beherrschen. Das kann z.B. die
Fritz-Box-App.

Eine gute Android-App, mit der man alle Medien auf einer RPi abspielen
kann
ist [BubbleUPnP](https://play.google.com/store/apps/details?id=com.bubblesoft.android.bubbleupnp)
(3,49 €). Falls du eine bessere App kennst, bitte Bescheid sagen. Das
Abspielen mit der BubbleUPnP funktioniert so:

1.  Unter "DEVICES" den "RENDERER" (das ist das Abspielgerät, also die
    Raspberry Pi) und die "LIBRARY" (das ist die Quelle, auf der die
    abzuspielenden Daten liegen) auswählen. Bei der Raspi muss zuvor
    natürlich unter den Einstellungen "UPnP Renderer aktivieren"
    ausgewählt und die Fernsteuerung zugelassen werden.
2.  Unter "LIBRARY" die abzuspielenden Daten auswählen.

1. RPi als Stereoanlage
-----------------------

Zum Beispiel kann man in die Küche eine RPi legen, die mit dem Router
([über
LAN](http://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=netgear+powerline)oder
WLAN) verbunden ist. An die RPi über ein
[Audio-Kabel](http://www.thomann.de/de/cat_cableguy~ncx.html?ccmem=1)
(Miniklinkenstecker) einen Lautsprecher oder ein altes Radio mit einem
Line-In-Eingang anschließen. Und schon kann man über das eigene Handy
gesteuert Musik hören. Die Musik-Dateien können dabei im Internet, auf
dem Handy, auf dem eigenen Computer, auf einer NAS, auf einer an die
Raspberry Pi angeschlossenen USB-Festplatte oder einem angeschlossenen
USB-Stick liegen.

### Installation

Hat man alle Kabel, braucht man nur noch eine SD-Karte, auf die man das
Betriebssystem installieren muss. Das dauert, wenn man's ein Mal gemacht
hat, ca. 5 Minuten. Die SD-Karte sollte 4 GB groß sein. (Für Kodi reicht
1 GB.)

-   [Anleitungen für alle offiziellen
    RPi-Betriebssysteme](http://www.raspberrypi.org/documentation/installation/noobs.md)

Danach einfach die Karte in die RPi stecken. Jetzt will man vermutlich
noch ein paar Einstellungen im Betriebssystem vornehmen, z. B. ob der
Audio-Ausgang der analoge oder der HDMI-Ausgang sein soll. Dazu einfach
einen Bildschirm (evtl. über einen Adapter) und eine USB-Maus oder
-Tastatur anschließen. Sobald das Raspi Strom bekommt, fährt es hoch und
ist bereit.

### Optimierung der Audio-Qualität

Bei den alten Modellen ist anscheinend die Audio-Qualität nur
mittelmäßig, wenn man den normalen Stereo-Ausgang benutzt. Das habe ich
zwar nicht gehört, aber für rund 40 € kann man wohl schönere
Sinus-Kurven bekommen. Die Zusatzkarte, die man dazu auf's RPi montieren
kann, heißt
[HiFiBerry](http://www.crazy-audio.com/projects/hifiberry-mini/).
Teurere Alternativen, und eine Begründung warum ein direktes Anlöten
einers D/A-Wandlers besser ist als einen
[DAC](http://www.raspyfi.com/the-right-usb-dac-for-your-raspberry-pi/)über
USB zu verwenden (7 bis unendlich Euro), findet man
[hier](http://volumio.org/raspberry-pi-i2s-dac-sounds-so-good/).

Mehr zum Thema Optimierung der Audio-Qualität kann man bei
[Raspyfi](http://www.raspyfi.com/project/) bzw.
[Volumio](http://volumio.org/)nachlesen. Hier kann man auch ein für
Audio optimiertes Betriebssystem
([Volumio](http://volumio.org/get-started/) statt Raspbmc oder OpenElec)
finden, das ich aber noch nicht selbst ausprobiert habe. Eine Anleitung
findet man auch beim
[Raspi-Forum](http://www.forum-raspberrypi.de/Thread-volumio-der-ultimative-musikplayer-fuer-den-raspberry-pi).

2. Mittels RPi Internet-Videos auf dem eigenen Fernseher anschauen
------------------------------------------------------------------

Funktioniert genau so wie bei 1.

Gute Apps, um Videos aus dem Internet zu streamen sind

-   [ZDF
    Mediathek](https://play.google.com/store/apps/details?id=com.zdf.android.mediathek)
-   [Theke](https://play.google.com/store/apps/details?id=com.sh.theke)

Man kann aber auch einfach über den Handy-Browser auf die gewünschte
Internetseite gehen und dort den Link des abzuspielenden Mediums an
BubbleUPnP senden. Dazu ist die App

-   [SemperVidLinks](https://play.google.com/store/apps/details?id=com.semperpax.sempervidlinksFree)

notwendig. Außerdem bietet sich <span style="line-height: 1.5;">für das
Streamen von Medien aus dem Internet die Android-App</span>

-   [vGet](https://play.google.com/store/apps/details?id=mb.videoget)

<span style="line-height: 1.5;">an.</span>

3. RPi als eigener Server
-------------------------

Stichworte: ArkOS, SSL, OwnCloud

1.  <http://www.kuketz-blog.de/projekt-arkos-raus-aus-der-cloud/>
2.  <http://www.kuketz-blog.de/projekt-arkos-hardware-und-installation/>
3.  <http://www.kuketz-blog.de/projekt-arkos-erste-konfigurationsschritte/>
4.  <http://www.kuketz-blog.de/projekt-arkos-installation-ssl-zertifikat/>
5.  <http://www.kuketz-blog.de/owncloud-eine-alternative-zu-nebuloesen-cloud-diensten/>

4. Weitere Möglichkeiten
------------------------

<http://www.forum-raspberrypi.de/Thread-tutorial-uebersicht>

[Das RPi im
Klassenzimmer](http://xcosx.de/rpi-im-klassenzimmer/ "Vom Handy zum Beamer: Das RPi im Klassenzimmer")
