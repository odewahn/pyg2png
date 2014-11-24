This repo converts code examples in HTMLBook files into PNGs.  The code listings are highlighted using the [pygments](http://pygments.org/) syntax highlighter.

## Requirements

* Docker 1.3

## To Start

Build the image:

```bash
docker build -t odewahn/pyg2png .
```

Then start the container:


```bash
docker run -it -v $(pwd):/usr/src odewahn/pyg2png /bin/bash
```

This will leave you at a bash prompt.  The `-v` option will map  your local directory on your host into the container, so commands you run here will save their files on your host machine. 