# Note that for aesthetic purposes, the original tskit logo at ../tskit_logo.svg
# was altered slightly for this makefile, to create a version where the root branch
# is centred.

all: tskit_logo_hexsticker.png

tskit_logo.png: ../tskit_logo.svg
	inkscape --export-type="png" -d 300 -o tskit_logo.png tskit_logo_root_centred.svg

tskit_logo_square.png: tskit_logo.png
	convert tskit_logo.png -background white -gravity center -resize 3000x3000 \
	-extent 4000x3650 -gravity south -splice 0x350 tskit_logo_square.png

# Two colours in logo: #045167 #12e3a8
tskit_logo_hexsticker.png: tskit_logo_square.png
	hexsticker -v --padding-size 25 --supersample 2 \
		--border-size 640 --border-color '#045167' \
		-o tskit_logo_hexsticker.png tskit_logo_square.png
clean:
	rm *.png
