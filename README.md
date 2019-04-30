# COMDB


CLI utility and python module used for querying OMDB for rotten tomatoes ratings

# Usage

```
$ comdb --help
usage: comdb [-h] [-d] -k KEY movie

Search OMDB for Rotten Tomatoes movie ratings

positional arguments:
  movie              Movie title to search for in OMDB

optional arguments:
  -h, --help         show this help message and exit
  -d, --debug        Enable debug output
  -k KEY, --key KEY  OMDB API Key
```

# Installation

PIP installation
```
pip install git+https://github.com/jhedden/comdb.git
```

Development
```
git clone https://github.com/jhedden/comdb.git
pip install -e comdb
```

Docker
```
git clone https://github.com/jhedden/comdb.git
cd comdb
docker build . -t comdb
docker run comdb --env APIKEY=<omdb api key> --env MOVIE=<movie title>
```
