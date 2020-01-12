## Preview
![vim](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/vim.jpg)
<br />
![pcmanfm](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/pcmanfm.jpg)
<br />
![menu](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/menu.jpg)
<br />
![splash](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/splash.jpg)
<br />
![ranger](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/ranger.jpg)
<br />
![mpv](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/mpv.jpg)
<br />
![htop](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/htop.jpg)
<br />
![rofi](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/rofi.jpg)
<br />
![gimp](https://raw.githubusercontent.com/addy-dclxvi/dotfiles/master/.preview/gimp.jpg)
<br />

## Details
- **Devices** ThinkPad X230
- **Distro** Debian Buster
- **Display Server** X11
- **Display Manager** LightDM
- **Greeter** LightDM GTK Greeter
- **Desktop Environment** None
- **WM** Openbox
- **Start Menu** LXMenu-Data piped to Openbox-Menu
- **Launcher** Rofi
- **Panel** i3status piped to Lemonbar
- **Compositor** Compton
- **GTK Theme** Arc
- **Icons** Faba
- **Cursor** Breeze
- **GTK Fonts** Liberation
- **File Manager** PCManFM, GVFS, LibMTP
- **Web Browser** Chromium VA-API
- **VA-API Driver** i965-va-driver
- **Encoder/Decoder** ffmpeg
- **Task Manager** HTOP
- **System Tray** Trayer
- **Power Manager** TLP
- **Image Viewer** Viewnior
- **Sound Mixer** PulseAudio
- **Terminal** URxvt
- **Pager** Less
- **CLI Shell** Fish
- **Archiver** XArchiver
- **Notification Daemon** Dunst
- **CLI File Manager** Ranger
- **CLI Image Viewer** Caca
- **Graphic Editor** GIMP
- **Non-free Drivers** Broadcom Bluetooth & Intel Wifi
- **GUI Text Editor** Geany
- **CLI Text Editor** Vim
- **Policy Kit Frontend** Gnome Polkit
- **Video Player** MPV
- **Music Player** Audacious
- **Office Suite** LibreOffice
- **Printer Driver** GutenPrint
- **Screenshooter** scrot
- **Network Manager** WICD
- **Brightness Manager** xbacklight
- **Wallpaper Handler** Hsetroot

## How I Restore My Setup
- Install Debian Buster minimal, without any DE
- Enable `contrib` and `non-free` repository (/etc/apt/sources.list)
- Connect to the internet
- Install git
- Clone this repo `git clone --depth=1 https://github.com/addy-dclxvi/dotfiles ~/.dotfiles`
- Deploy the dotfiles `cp -a ~/.dotfiles/. ~`
- Restore the packages `sh ~/.scripts/packages`
- Change the default CLI Shell `chsh $(whoami) -s /usr/bin/fish`
- Edit some system configuration, example in ~/.dotfiles/.system
- Reboot
- Fix some errors
- Start working

## Keybinds & Mousebinds
- **Super + Enter** launch URxvt
- **Super + D** launch Rofi with wrapper script
- **Super + Space** launch Openbox Menu, just like right click on the desktop
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
- **Super + Shift + Backspace** reload Openbox, do this after modify the configuration files
- **Double Click Titlebar** maximize
- **Scroll Up Titlebar** roll up window
- **Scroll Down Titlebar** restore rolled up window
- **Double Click Desktop** list opened programs, so I could survive without a taskbar
- **Click on SSID (Panel)** open WICD
- **Click on Volume (Panel)** open Pavucontrol
- **Scrol Up/Down on Volume (Panel)** turn up/down the volume
- **Click on Disk (Panel)** launch PCManFM
- ..More keybinds just read the *~/.config/openbox/rc.xml* file

## Notes
- If you want to use this configuration, inspect the code before use.
- If you find "addy" in the configuration file, replace it with your own username.
- My Wifi interface is wlp3s0 & my ethernet interface is enp0s25, if you find them in the
configuration file, replace with your own. Use `ip a` to find yours.
