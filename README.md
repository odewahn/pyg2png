This repo converts code examples in HTMLBook files into PNGs.  The code listings are highlighted using the [pygments](http://pygments.org/) syntax highlighter.

It will process each html file and write out a PNG files for every program listing.  The output files follow the convention `<filename>_listing_#.png`.  So, if you have a file called `ch01.html` with 3 listings, and `ch02.html` with 2 listings, you'll get 5 files, like this:
	
```
ch01_listing_1.png
ch01_listing_2.png
ch01_listing_3.png
ch02_listing_1.png
ch02_listing_2.png
```

## Requirements

You need:

* Docker 1.3

The reason is that I use the auto-mount directory feature, and that's only in 1.3!

## To Start

*NB: remember to change _odewahn_ to your username!*

First, build the image:

```bash
docker build -t odewahn/pyg2png .
```

## To use it

Run this command from within the directory where you want to convert program files into PNGs:


```bash
docker run -v $(pwd):/usr/data odewahn/pyg2png
```

This will process each HTML file and turn code blocks within `<pre>` tags with a `data-program-listing` attribute into a PNG.




