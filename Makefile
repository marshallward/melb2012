TEXFILE = melb2012.tex

.PHONY: maketex
maketex: ${TEXFILE}
	pdflatex $<

.PHONY: clean
clean:
	rm *.aux *.log *.nav *.out *.pdf *.snm *.toc *.vrb
