# mach

# TO DO

- [ ] Construire une classe efficiente pour gérer les jeux de lumière
- [ ] Faire une v1 de la platine avec la batterie
- [ ] Faire un test de fonctionnement sur batterie
- [ ] Faire une liste d'achats pour la veste
- [ ] Commencer la note d'intention du Lorenshow 4

# Comptes-rendus

## 2026_01_17

Je me suis rendu comtpe en décembre que j'utilisais mal la librairie rpi_ws281x? le mieux est de l'utiliser avec le protocole SPI, qui ne nécessite pas sudo et qui laisse libre l'accès à l'audio.

J'ai refais une install fraîche sur ma pi (pi@raspberrypi.local), et modifié beat et test_led pour que cela marche.

J'ai enfin pu tester la librairie librosa, qui s'est révélée tout à fait satisfaisante, il me semble? J'ai fait quelques autres tests, nottament pour un effet stroboscope.

Finalement, j'ai fait un peu de rangement, maintenant que les pricnipes de base sont validés, il va être temps de s'y mettre serieusement.

## 2025_11_11

Je me rends compte que j'arrive face à un problème insoluble :
- La libraire que j'utilise poru controler les leds, rpi_ws281x, ne peux fonctionner que si j'utilise root
MAIS
- PulseAudio ne permet pas l'accès au son à un utilisateur qui a des privilèges système (donc root)

Je ne peux donc pas avvoir à la fois du son et du contrôle des leds.
J'ai essayé un tuto qui dit pouvoir permettre l'accès root à PulseAudio : https://stackoverflow.com/questions/74591584/running-part-of-python-program-with-without-sudo
Je n'ai aps eu d'erreurs en suivant les tuto, et je n'ai maintenant plus d'erreurs quand j'essaye d'accéder au son via root. Mais poru autant le son ne sort pas dans mon casque en bluetooth.

J'ai essayé cette commande : sudo usermod -a -G bluetooth pulse
conseillée ici : https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SystemWide/

Mais pas mieux.

EN REVANCHE, il marche sis je le connecte via la prise jack. Mais comme le module rpi_ws281 bloque aussi le port jack, cela ne résout pas mon problème.

J'ai essayé d'installer blueman, sans succès.

La commande bluetoothctl se comporte exactement de la même façon avec et sans sudo.

Il doit y avoir un problème entre pulseaudio et le gestionnaire bluetooth lié au passage de pulse audio en system wide (utilisable par root)

J'ai essayé d'jouter les droits suivants :

sudo usermod -a -G bluetooth pi
sudo usermod -a -G bluetooth root
sudo usermod -a -G pulse-access pi
sudo usermod -a -G pulse-access root

Sans succès. Je m'arrête là pour ce soir