pactl load-module module-null-sink sink_name=mumble sink_properties=device.description="Mumble"
pactl load-module module-remap-source source_name=mumbleuser source_properties=device.description="MumbleUser" master=mumble.monitor
