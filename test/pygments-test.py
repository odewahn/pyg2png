# Example from 
#    daniweb.com/software-development/python/code/377426/write-an-image-file-displaying-source-code
# Options for ImageFormatter at:
#    http://pygments.org/docs/formatters/


from pygments import highlight
from pygments.lexers import JavaLexer
from pygments.formatters import ImageFormatter


def code2img(input_fileobj, output_fileobj):
    python_code = input_fileobj.read()
    png_code = highlight(python_code, JavaLexer(), ImageFormatter(
      font_size=16,
      line_pad=4
    ))
    output_fileobj.write(png_code)
    
if __name__ == "__main__":
    code2img(open("sample.java"), open("sample.java.png", "w"))