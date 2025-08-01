grim -c -g "$(slurp)" - | magick png:- -shave 1x1 png:- | wl-copy -t image/png
notify-send "Screenshot copied to clipboard"

# | magick png:- -shave 1x1 \
# png:- | magick png:- \
# \( +clone  -alpha extract \
#   -draw 'fill black polygon 0,0 0,15 15,0 fill white circle 15,15 15,0' \
#   \( +clone -flip \) -compose Multiply -composite \
#   \( +clone -flop \) -compose Multiply -composite \
# \) -alpha off -compose CopyOpacity -composite \
# png:- | magick png:- \
# -bordercolor none -border 10x10 \
# \( +clone -background black -shadow 50x5+0+5 \) \
# +swap -background none -layers merge +repage \
# png:- \
