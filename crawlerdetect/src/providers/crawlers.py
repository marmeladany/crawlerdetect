from .base import AbstractProvider
import json
import importlib.resources

# noinspection SpellCheckingInspection
class Crawlers(AbstractProvider):
    """
    List of regular expressions to match against the user agent
    """

    def getAll(self):
        # json_file_path = pkg_resources.resource_filename('crawlerdetect.src.providers', 'newCrawlers.json')
        with importlib.resources.path('crawlerdetect.src.providers', 'crawlers.json') as json_file_path:
            with open(json_file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)

        json_list = [rf"{item}" for item in json_data]

        return json_list
