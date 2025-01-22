FNAME = "flag2of2-final.pdf"

FLAG_FROM_PNG = "picoCTF{f1u3n7_"
FLAG_FROM_PDF = "1n_pn9_&_pdf_249d05c0}"

"""
ghostscript			            \
	-P-			                \
	-dSAFER			            \
	-dCompatibilityLevel=1.4	\
	-q			                \
	-P-			                \
	-dNOPAUSE			        \ # no pause after page
	-dBATCH			            \ # exit after last file
	-sDEVICE=pdfwrite			\ # select device
	-sstdout=?			        \ # 
	-sOutputFile=?			    \ # select output fule: - for stdout, |command for pipe, embed %d or %ld for page #
	-P-			                \
	-dSAFER			            \ # File access restrictions
	-dCompatibilityLevel=1.4	\
	?



ghostscript -P- -dSAFER -dCompatibilityLevel=1.4 -q -P- -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sstdout=stdout.pdf -sOutputFile=out.pdf -P- -dSAFER -dCompatibilityLevel=1.4 flag2of2-final.ps
"""

print(FLAG_FROM_PNG + FLAG_FROM_PDF)
