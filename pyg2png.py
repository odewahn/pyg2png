# Example from 
#    daniweb.com/software-development/python/code/377426/write-an-image-file-displaying-source-code
from pygments import highlight
from pygments.lexers import JavaLexer
from pygments.lexers import ScalaLexer
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter


from pyquery import PyQuery as pq

import glob


def code2img(code, code_type, outfile_name):

   # Set the apporpriate lexer based on the program type
   # Note that you have to import each lexer you want to use
   lexer = JavaLexer()
   if code_type == "scala":
      lexer = ScalaLexer()
   elif code_type == "python":
      lexer = PythonLexer()

   # convert the file to a PNG.  you can tweak the options for ImageFormatter at:
   #    http://pygments.org/docs/formatters/
   png_code = highlight(code, lexer, ImageFormatter(
      font_size=18,
      line_pad=4
   ))

   # Save the listing as a png
   out = open(outfile_name, "w")
   out.write(png_code)
   out.close()

    
if __name__ == "__main__":

   html_files = glob.glob("*.html")
   
   for fn in html_files:
      print("Processing file %s" % fn)
      source_fn = fn.split(".")[0]
    
      with file(fn) as f:
         s = f.read()
         doc = pq(s)
         idx = 1

         for ex in doc("pre"):
            out_fn = "%s_listing_%s.png" % (source_fn,idx)
            print("... Creating %s" % out_fn)
            listing_type = ex.attrib["data-code-language"]
            code2img(ex.text, listing_type, out_fn)
            idx += 1