all: pdf html

pdf: test_notebook.pdf
html: test_notebook.html

clean:
	rm -f *.output.ipynb
	rm -f *.html
	rm -f *.pdf

# Makefiles don't a allow a target to depend on 
# itself, so we execute foo.ipynb to
# create foo.output.ipynb.  This is our
# ".o" file analog in C/C++.
%.output.ipynb: %.ipynb
	python execute.py $< $@

# Convert our intermediate file to html.
# We send nbconvert output to stdout and
# redirect to the target name, else we'd
# end up with foo.output.html
%.html: %.output.ipynb
	jupyter nbconvert --to html $< --stdout > $@

%.pdf: %.output.ipynb
	jupyter nbconvert --to pdf $< 
	mv -f $*.output.pdf $@

.PHONY: pdf html
.PRECIOUS: %.output.ipynb
