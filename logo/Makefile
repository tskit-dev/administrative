all: logo.png

# I did this by hand, as I'm on OS X, 
# but I think this should be right??
logo.png: logo.svg
	inkscape -z -f logo.svg -w 500 -j -e logo.png

logo.svg: make_logo.py
	PYTHONPATH=$(HOME)/src/msprime python make_logo.py

