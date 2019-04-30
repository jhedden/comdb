import argparse
import json
import logging
import sys
import requests


# Base OMDB API URL
OMDB_URL = "http://www.omdbapi.com"

LOGGER = logging.getLogger(__name__)

def bail(msg):
    """Log error to STDOUT, logger and exit

    Args:
      msg (str): Error message
    """
    LOGGER.error(msg)
    print("ERROR: {}".format(msg))
    sys.exit(1)


def query(title, key):
    """Query OMDB database for given movie title

    Args:
      title (str): Title of movie to search for
    Returns:
      dict: OMDB results
    """
    api_url = "{}/?apikey={}&t={}".format(OMDB_URL, key, title)
    LOGGER.debug("OMDB request URL: %s", api_url)

    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers)
    LOGGER.debug("OMDB response status code: %s", response.status_code)

    if response.status_code >= 500:
        bail("OMDB SERVER ERROR: {}".format(response.status_code))
    if response.status_code == 401:
        bail("INVALID OMDB API KEY")
    if response.status_code == 404:
        bail("INVALID OMDB API URL {}".format(OMDB_URL))

    try:
        result = json.loads(response.content.decode('utf-8'))
        LOGGER.debug("OMDB content: %s", result)
    except ValueError:
        bail("ERROR parsing JSON OMDB reponse {}")

    # If there was an error reported by OMDB exit
    # Typically this is 'movie not found'
    if 'Error' in result:
        bail("'{}' '{}'".format(title, result['Error']))

    return result


def rotten_ratings(content):
    """Extract Rotten Tomatoes ratings from OMDB JSON data

    Args:
      content (json dict): OMDB JSON data
    Returns:
      str: Movie title and Rotten Tomatoes rating
    """
    result = ""
    if "Ratings" in content and isinstance(content['Ratings'], list):
        for i in content['Ratings']:
            if "Source" in i and "Value" in i:
                if i["Source"] == "Rotten Tomatoes":
                    result = i['Value']

    if not result:
        bail("rating not found for movie: {}".format(content["Title"]))

    return "{} {}".format(content["Title"], result)


def main():
    # Setup CLI arguments
    parser = argparse.ArgumentParser(description="Search OMDB for Rotten Tomatoes movie ratings")
    parser.add_argument("-d", "--debug",
                        help="Enable debug output",
                        action="store_true")
    parser.add_argument("-k", "--key",
                        help="OMDB API Key",
                        type=str,
                        required=True)
    parser.add_argument("movie",
                        help="Movie title to search for in OMDB")
    args = parser.parse_args()

    # Setup logging
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    content = query(args.movie, args.key)
    print(rotten_ratings(content))


if __name__ == '__main__':
    main()

