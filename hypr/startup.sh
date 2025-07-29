# mumble redirection loop for phone-to-computer microphone using mumble bridge
pactl load-module module-null-sink sink_name=mumble sink_properties=device.description="Mumble"
pactl load-module module-remap-source source_name=mumbleuser source_properties=device.description="MumbleUser" master=mumble.monitor

# autostart!
/usr/lib/polkit-kde-authentication-agent-1 &                            # polkit
waybar & hyprpaper & dunst & hyprpaper &                                # system level apps
vesktop & materialgram & google-chrome-unstable &                       # essential apps
steam -silent & kdeconnectd & ckb-next -b &                             # background startup apps
disown -a