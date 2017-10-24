Title: Vom Handy zum Beamer: Das RPi im Klassenzimmer
Date: 2015-03-15 21:19
Category: IT
Tags: Android, Raspberry Pi, UPnP
Slug: rpi-im-klassenzimmer
Status: published
HeaderImage: /images/rpi.png
Summary: Du willst deine Medien vom Handy an den Beamer senden?<!--more-->

Du willst deine Medien vom Handy an den Beamer senden?<!--more-->

Dann kannst du dir von einem beliebigen Hersteller einen WLAN-Stick
kaufen, der das kann (ca. 35-60 €) oder du bastelst dir mit einer
Raspberry Pi (RPi) deine Lösung selbst.

-   **Google Chromecast**. Ich habe Googles Chromecast ausprobiert und
    für gut befunden - unter bestimmten Bedingungen. Aber unter meinen
    Voraussetzungen ist es nicht geeignet, und zwar (1) weil ich bei
    meinen Schülern nicht ständig Werbung von Google zeigen möchte, und
    (2) weil in unseren Klassenzimmern kein WLAN zur Verfügung steht.
    Ich muss also bei meinem Handy die Internetverbindung aktivieren und
    einen AccessPoint bereit stellen. Dann brauche ich ein zweites
    Handy, um Medien streamen zu können. Oder ich nehme mein Handy als
    Client, brauche aber einen mobilen Router.
-   **AppleTV**. Einen Erfahrungsbericht zu AppleTV mit dem iPad hat
    [Spannagel](https://cspannagel.wordpress.com/2015/01/15/mobil-prasentieren-im-horsaal/)geschrieben.


Raspberry Pi - Meine Lösung
---------------------------

In das Raspberry Pi mit Kodi/XBMC  einen (speziellen s.u.) WLAN-Dongle
stecken, ein paar wenige Einstellungen tätigen, fertig. Wenn man weiß
wie es geht, dauert die Installation ca. 5 Min. Beim ersten Mal dauert
es länger.

Jetzt kann man das Handy mit dem vom RPi bereit gestellten WLAN
verbinden und Medien (über das UPnP/DLNA-Protokoll) zum RPi senden, das
RPi sendet sie dann über den HDMI-Ausgang an den Beamer[.  
](http://xcosx.de/wp-content/uploads/2015/02/RPi-am-Mobi.png)

[![Screenshot\_2015-02-17-11-46-33\~01](http://xcosx.de/wp-content/uploads/2015/02/Screenshot_2015-02-17-11-46-3301-300x144.png)](http://xcosx.de/wp-content/uploads/2015/02/Screenshot_2015-02-17-11-46-3301.png)

Funktionsweise
--------------

Das Besondere an meiner Lösung ist, dass das RPi ein WLAN bereit stellt,
das quasi offline ist, also einen AccessPoint, der nicht mit dem
Internet verbunden ist, quasi ein WLAN-Hotspot ohne Internet, ein WLAN
ad-hoc Netzwerk. Das ist nicht Wifi-Direct, sondern im wörtlichen Sinne
ein WLAN, ein lokales Funknetzwerk. LibreELEC bzw. Kodi beherrscht die
Protokolle UPnP und AirPlay, sodass man mit Android- und Apple-Handys
Medien streamen kann.

Screen-Mirroring ist mit Apps wie [Screen Stream
Mirroring](https://play.google.com/store/apps/details?id=com.mobzapp.screenstream.trial)
auch möglich, allerdings benötigt man auf dem Handy Superuser-Rechte.
([Android-Handy
rooten.](http://www.kuketz-blog.de/grundstein-legen-android-ohne-google-teil2/))
Ob es eine Opensource-Software gibt, die das kann, weiß ich nicht.

Details
-------

-   Raspberry Pi kaufen:
    [http://www.rasppishop.de/boards/](http://www.rasppishop.de/)
    -   Evtl. gleich noch Zubehör
        -   [HDMI-Kabel](http://www.rasppishop.de/diverse/kabel-adapter/hdmidvivideoaudio/130/audio/videokabel-hdmi-19pol-stecker-hdmi-19pol-stecker-1-8-m-mit-ethernet)
            oder [HDMI zu
            DVI-Kabel](http://www.rasppishop.de/diverse/kabel-adapter/hdmidvivideoaudio/39/audio/videokabel-dvi-zu-hdmi-2m)
        -   [Micro-USB-Kabel](http://www.rasppishop.de/diverse/kabel-adapter/usb/137/usb-zu-micro-usb-kabel-1-m-raspberry-pi-power-supply)
            oder einen ganzen
            [Stromanschluss](http://www.rasppishop.de/stromversorgung/3/steckernetzteil-erp-micro-usb-5volt-1-0-a-geeignet-fuer-raspberry-pi)
        -   Eine SD-Karte (theoretisch genügt 1 GB)
-   WLAN-Dongle von LogiLink kaufen:
    [WL0084B](http://www.amazon.de/gp/product/B007JWB1N2?psc=1&redirect=true&ref_=oh_aui_detailpage_o01_s00)
    (nur mit wenigen Sticks funktioniert diese WLAN-Variante. Bei einem
    vorhandenen WLAN kann man auch den [üblichen
    WLAN-Dongle](http://www.rasppishop.de/diverse/netzwerk/w-lan/146/wireless-usb-11n-nano-adapter-802.11n-wifi-dongle-fuer-raspberry-pi)
    oder den TL-WN725N nehmen, da man kein Tethering aktivieren muss.)
-   LibreELEC mit Kodi (ehemals XBMC) installieren
    -   [LibreELEC (mit Kodi)
        herunterladen](https://libreelec.tv/downloads/)
    -   [LibreELEC (mit Kodi) auf der SD-Karte
        installieren](https://wiki.libreelec.tv/index.php?title=Installation)
-   WLAN-Dongle anschließen und im Kodi vier Optionen aktivieren
    -   Optionen/LibreELEC/Netzwerk: aktiv + WLAN-AccesPoint
        ('tethered') aktivieren
    -   Optionen/Einstellungen/Dienste/UPnP: UPnP-Server aktivieren +
        Steuerung über UPnP zulassen
-   Auf Android beherrschen z.B.[diese Opensource-Apps
    UPnP](https://f-droid.org/repository/browse/?fdfilter=upnp&fdpage=1&page_id=0),
    oder, wer GooglePlay benutzt: BubbleUPnP.
-   Tipp: Das RPi immer brav herunterfahren, z.B. mit der App
    [Kore](https://f-droid.org/repository/browse/?fdfilter=kodi&fdid=org.xbmc.kore)
    oder Yatse oder sicher gehen, dass die RPi nichts schreibt, während
    man aus schaltet.
-   Powerpoint und PDF-Dateien können nicht direkt gestreamt werden
    (zurzeit noch nicht?). Als Workaround mache ich von den Seiten, die
    ich den Schülern zeigen möchte, Screenshots direkt in das
    Verzeichnis, das ich mit meinem Handy
    [synchronisiere](https://f-droid.org/repository/browse/?fdfilter=syncthing&fdid=com.nutomic.syncthingandroid).
    Hier mein Bash-Skript:

<!-- -->

    #!/bin/bash
    PFAD_B="/home/x/PDF/jpg_of_pdf"
    cd /home/x/PDF/to_jpg
    for i in *.pdf
     do convert -verbose -interlace none -density 300 -quality 90  $i   $file "$PFAD_B/${i/pdf/jpg}"
    done
    exit
