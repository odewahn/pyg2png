This repo converts code examples in HTMLBook files into PNGs.  The code listings are highlighted using the [pygments](http://pygments.org/) syntax highlighter.

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




