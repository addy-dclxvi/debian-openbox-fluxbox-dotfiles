<p align="center">
<a name="top" href="https://github.com/addy-dclxvi/Ultimate-Dotfiles/"><img src="https://raw.githubusercontent.com/addy-dclxvi/Ultimate-Dotfiles/master/logo.png"></a>
</p>

## Introduction
A collection of configs to be placed in the users home directory usually prefixed with a period, hence the name dotfiles.
This repo is actually intended for my personal backup, but everyone are welcome to use these resources.

## Preview
![alt text](https://raw.githubusercontent.com/addy-dclxvi/Ultimate-Dotfiles/master/preview.jpg) <br />
![alt text](https://raw.githubusercontent.com/addy-dclxvi/Ultimate-Dotfiles/master/preview2.jpg)
I can't give You preview for every part, but You can view My Deviant Art [Gallery](http://addy-dclxvi.deviantart.com/gallery/) if you want to see more preview of these dotfiles.

## Containing

- **Openbox** <br /> Fairly complete *rc.xml*, very organized main menu (some menu are using [ARCHLabs pipemenu](https://aur.archlinux.org/packages/archlabs-pipemenus-git)), and option to use *menu.xml* with icons (I'm using [Sardi Ghost Flexible](https://aur.archlinux.org/packages/sardi-icons) icons).
For my themes, please check my [Openbox Theme Collections](https://github.com/addy-dclxvi/Openbox-Theme-Collections).

- **i3** <br /> Pretty stock simple config. My default config is using i3blocks as statusbar. To replace it with Polybar simply edit the config, uncomment the Polybar execution and remove the i3bar.

- **i3blocks** <br /> A simple i3blocks config for i3bar. I'm using modules from [Anachron](https://github.com/Anachron/i3blocks).

- **Polybar** <br /> Multi head 2 bar setup for i3 or Openbox. I'm using resources from [Nath](https://github.com/natemaia), [Boris](https://github.com/appath), and [Mazhar](https://github.com/m47h4r).
  
- **zshrc** <br /> Eye candy yet useful [Power Level 9k](https://github.com/bhilburn/powerlevel9k) config. Also contains some useful alias.
In order to use my zshrc, You need to install [Nerd Font Complete](https://aur.archlinux.org/packages/nerd-fonts-complete), [Power Level 9k](https://aur.archlinux.org/packages/zsh-theme-powerlevel9k-git) and [Oh-My-Zsh](https://aur.archlinux.org/packages/oh-my-zsh-git).
Their combinations is decent. Autocorrect, autocomplete with TAB button, and many useful features. <br />
![alt text](https://raw.githubusercontent.com/addy-dclxvi/Ultimate-Dotfiles/master/powerlevel9k.gif)
  
- **Compton** <br /> Eye candy shadow. Also some useful "exclude" to avoid broken compositing.

- **Conky** <br /> Just a single conkyrc. For my another Conky collections please check my other [repos](https://github.com/addy-dclxvi?tab=repositories).

- **Tint2** <br /> Just a single tint2rc. For my another Tint2 collections please check my [Tint2 Themes Collections](https://github.com/addy-dclxvi/Tint2-Theme-Collections).

- **termite** <br /> My custom color schemes for termite.

- **Xresources** <br /> My custom color schemes & config for Urxvt, including copy paste support by [Muennich](https://github.com/muennich/urxvt-perls). Hit Alt+C to copy, and Alt+V to paste.

- **ncmpcpp** <br /> A simple ncmpcpp config, with album art support. The album art script is taken from [Marco](https://marcocheung.wordpress.com/). Slightly modified to get rid the transparency bug. <br />
![alt text](https://raw.githubusercontent.com/addy-dclxvi/Ultimate-Dotfiles/master/ncmpcpp.gif)

- **CAVA** <br /> Some [CAVA Visualizer](https://aur.archlinux.org/packages/cava) configs, with different color. Integrated with zshrc & bashrc alias for easy launch. 

- **Rofi** <br /> A simple program launcher, only include one color scheme for now.

- **gtk.css** <br /> Add paddings for vte-based terminal, including termite.

- **Neofetch** <br /> Some color configs for neofetch, integrated with zshrc & bashrc alias for easy launch.

- **bin** <br /> The only useful command here is gitsetup & gitpush by [Erik Dubois](http://erikdubois.be/quick-easy-way-set-personal-github-repository),
the rest are only toys from [Crunchbang Forum](https://crunchbang.org/forums/viewtopic.php?id=13645).

## Additional Information
Some of these configs are hardcoded, that mean You need to edit the configs before it would work. Like the path and default apps.
- My username at my machine is addy@freako, so some of these configs path are pointing to ```/home/addy``` 

- My wlan id is wlp2s0, and my ethernet id is enp1s0. If you find these in the configs, replace them with your own. Use ```iwconfig``` to find yours. 

- My fonts are M+ 1mn (for terminal) and Roboto & Noto Sans (for GTK, openbox, panel, and other things that don't need a fixed space font). For iconic fonts, depends on what You see inside the config file. 

- My Web Browser is Firefox.

- My terminal is termite, and Urxvt as spare.

- My program launcher is rofi.

- My text editor is Geany.

- My wallpaper handler is Nitrogen.

- My screenshooter is scrot, and xfce4-screenshooter as spare. You will see that my keybind for printscreen is executing scrot.

- My music player is ncmpcpp, my media player is VLC.

- My image viewers are GPicView, Viewnior, and feh (sometimes I use feh as wallpaper handler too).

- The distro I'm using are BunsenLabs and ARCHLabs.

- My Window Managers are Openbox, i3-gaps, [Xfwm Standalone](https://github.com/addy-dclxvi/xfwm4-standalone), [Compiz Standalone](https://github.com/addy-dclxvi/compiz-standalone), and still learning how to use herbstluftwm & fvwm.
Yes, I don't use any complete DE. I only pull some of DE component that I find useful for my setup.

- My panels are tint2 (with executor support), polybar (with libmpdclient support), i3-blocks (for i3bar), and rarely using xfce4-panel. I gave up with lemonbar & dzen2.

## Package List
I can't remember one by one what packages need to be installed to make everything works.
But I have generated a [pkg.txt](https://github.com/addy-dclxvi/Ultimate-Dotfiles/blob/master/pkg.txt) file. It contains a list of my installed packages, excluding packages that only installed as dependency (it will be automaticcally pulled afterall, if needed).
Or, if You want to know my complete packages, just open the [pkgf.txt](https://github.com/addy-dclxvi/Ultimate-Dotfiles/blob/master/pkgf.txt) file. Maybe those two files can help You.

## My Links
[Google+](https://plus.google.com/+AdhiPambudi)
[Deviant Art](http://addy-dclxvi.deviantart.com/)
