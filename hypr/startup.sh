pactl load-module module-null-sink sink_name=mumblemic sink_properties=device.description="MumbleMic"
pactl load-module module-remap-source source_name=mumblemicuser source_properties=device.description="MumbleMicUser" master=mumblemic.monitor &
