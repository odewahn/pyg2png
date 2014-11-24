This repo converts code examples in HTMLBook files into PNGs.  The code listings are highlighted using the [pygments](http://pygments.org/) syntax highlighter.

## Requirements

* Docker 1.3

## To Start

Build the image:

```bash
docker build -t odewahn/pyg2png .
```

## To use it

Then start the container:


```bash
docker run -v $(pwd):/usr/data odewahn/pyg2png
```

This will leave you at a bash prompt.  The `-v` option will map  your local directory on your host into the container, so commands you run here will save their files on your host machine. 