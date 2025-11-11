# mach

# Comptes-rendus

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