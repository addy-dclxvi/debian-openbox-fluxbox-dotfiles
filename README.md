## Preview
### ThinkPad X230 Debian Openbox
![openbox](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/openbox.jpg)
<br />
### Aspire A514 Debian Fluxbox
![fluxbox](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/fluxbox.jpg)
<br />
## Details
### Both ThinkPad X230 & Aspire A514
- **Distro** Debian Buster
- **Display Server** X11
- **Display Manager** LightDM
- **Greeter** LightDM GTK Greeter
- **Desktop Environment** None
- **Launcher** Rofi
- **Terminal** URxvt
- **Compositor** Compton
- **GTK Theme** Arc
- **Icons** Faba
- **Cursor** Breeze
- **Web Browser** Chromium VA-API
- **VA-API Driver** i965-va-driver
- **Encoder/Decoder** ffmpeg
- **Task Manager** HTOP
- **Power Manager** TLP
- **Image Viewer** Viewnior
- **Sound Mixer** PulseAudio
- **Policy Kit Frontend** Gnome Polkit
- **Notification Daemon** Dunst
- **Pager** Less
- **CLI Shell** Fish
- **CLI File Manager** Ranger
- **CLI Image Viewer** Caca
- **CLI Text Editor** Vim
- **GUI Text Editor** Geany
- **Graphic Editor** GIMP
- **Vector Drawer** Inkscape
- **Screenshooter** scrot
- **Wallpaper Handler** Hsetroot
- **Brightness Manager** xbacklight
- **Music Player** Audacious
- **Office Suite** LibreOffice
- **Printer Driver** GutenPrint

### ThinkPad X230
- **Non-free Drivers** Broadcom Bluetooth & Intel Wifi
- **WM** Openbox
- **Panel** i3status piped to Lemonbar
- **Start Menu** LXMenu-Data piped to Openbox-Menu
- **File Manager** PCManFM, GVFS, LibMTP
- **System Tray** Trayer
- **Archiver** XArchiver
- **Video Player** MPV
- **Network Manager** WICD

### Aspire A514
- **Non-free Drivers** Realtek Audio & Atheros Wifi
- **WM** Fluxbox
- **Panel** Fluxbox Toolbar (Tray icon theme is
[Diminished](https://github.com/addy-dclxvi/diminished-tray-icons))
- **Start Menu** Fluxbox Menu (*~/.fluxbox/menu* edited manually)
- **File Manager** Thunar, Thunar Volman, Tumblr, GVFS, LibMTP
- **Archiver** File Roller
- **PDF Reader** Evince
- **Video Player** Parole
- **Battery Applet** Xfce4 Power Manager
- **Clipboard Manager** Clipit
- **Sound Applet** PNMixer
- **Network Applet** nm-applet

## How I Restore My Setup
- Install Debian Buster minimal, without any DE
- Enable `contrib` and `non-free` repository (*/etc/apt/sources.list*)
- Connect to the internet
- Install git
- Clone this repo `git clone --depth=1 https://github.com/addy-dclxvi/dotfiles ~/.dotfiles`
- Deploy the dotfiles `cp -a ~/.dotfiles/. ~`
- Restore the packages `sh ~/.scripts/openboxpack` or `sh ~/.scripts/fluxboxpack`
- Add user to sudoers using `visudo`
- Change the systemclock to localtime `timedatectl set-local-rtc 1` then set the time in BIOS
(because I set my BIOS clock to localtime insted of UTC)
- Change the default CLI Shell `chsh $(whoami) -s /usr/bin/fish`
- Edit some system configuration, example in ~/.dotfiles/.system
- Reboot
- Fix some errors
- Start working

## Keybinds & Mousebinds
### Both Openbox & Fluxbox Are Same
- **Super + Enter** launch URxvt
- **Super + D** launch Rofi with wrapper script
- **Super + Space** launch root menu (like right click on the desktop)
- **Alt + Tab** switch to next window
- **Alt + Shift + Tab** switch to previous window
- **Control + Alt + Left/Right** switch to previous/next workspace
- **Control + Alt + Up/Down**  switch to previous/next window, just like Alt + Tab
- **Super + Arrows** "Aero Snap"
- **Super + 1-4** switch to workspace 1-4
- **Super + Shift + 1-4** take the current active window to workspace 1-4
- **Super + Shift + Left/Right** take the current active window to prev/next workspace
- **Super + Alt + Arrows** switch focus to other window in the desired direction
- **Super + Control + Arrows** teleport
- **Super + A** central the current focus window
- **Super + C** close
- **Super + Z** minimize
- **Super + F** maximize
- **Super + T** toggle the window decoration
- **Super + U** roll up the window
- **Super + Shift + Backspace** reload, do this after modify the configuration files
- **Double Click Titlebar** maximize
- **Scroll Up Titlebar** roll up window
- **Scroll Down Titlebar** restore rolled up window
- **Double Click Desktop** list opened programs,
so I could survive without a taskbar (Openbox only)
- **Hold Control While Dragging Window** tabbing mode (Fluxbox only)
- **Scrol Up/Down on Volume (Panel)** turn up/down the volume
- ..More keybinds just read the *~/.config/openbox/rc.xml* 
or *~/.fluxbox/keys* file

### Mouse Action on Lemonbar (Openbox only)
- **Click on Disk (Panel)** launch PCManFM 
- **Click on Volume (Panel)** open Pavucontrol 
- **Click on SSID (Panel)** open WICD
- **Click on CPU Load (Panel)** open htop


## Notes
- If you want to use this configuration, inspect the code before use.
- If you find "addy" in the configuration file, replace it with your own username.
- My Wifi interface is wlp3s0 & my ethernet interface is enp0s25 (ThinkPad X230),
if you find them in the configuration file, replace with your own. Use `ip a` to find yours.
- My Wifi interface is wlp2s0 & my ethernet interface is enp1s0 (Aspire A514),
if you find them in the configuration file, replace with your own. Use `ip a` to find yours.
