from .base import AbstractProvider
import json
import importlib.resources

class Exclusions(AbstractProvider):
    """
    List of strings to remove from the user agent before running the crawler regex
    """

    def getAll(self):
        # json_file_path = pkg_resources.resource_filename('crawlerdetect.src.providers', "newExclusions.json")
        with importlib.resources.path('crawlerdetect.src.providers', 'newExclusions.json') as json_file_path:
            with open(json_file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)

        json_list = [rf"{item}" for item in json_data]
        local_list = [
            r"Safari.[\d\.]*",
            r"Firefox.[\d\.]*",
            r" Chrome.[\d\.]*",
            r"Chromium.[\d\.]*",
            r"MSIE.[\d\.]",
            r"Opera\/[\d\.]*",
            r"Mozilla.[\d\.]*",
            r"AppleWebKit.[\d\.]*",
            r"Trident.[\d\.]*",
            r"Windows NT.[\d\.]*",
            r"Android [\d\.]*",
            r"Macintosh.",
            r"Ubuntu",
            r"Linux",
            r"[ ]Intel",
            r"Mac OS X [\d_]*",
            r"(like )?Gecko(.[\d\.]*)?",
            r"KHTML,",
            r"CriOS.[\d\.]*",
            r"CPU iPhone OS ([0-9_])* like Mac OS X",
            r"CPU OS ([0-9_])* like Mac OS X",
            r"iPod",
            r"compatible",
            r"x86_..",
            r"i686",
            r"x64",
            r"X11",
            r"rv:[\d\.]*",
            r"Version.[\d\.]*",
            r"WOW64",
            r"Win64",
            r"Dalvik.[\d\.]*",
            r" \.NET CLR [\d\.]*",
            r"Presto.[\d\.]*",
            r"Media Center PC",
            r"BlackBerry",
            r"Build",
            r"Opera Mini\/\d{1,2}\.\d{1,2}\.[\d\.]*\/\d{1,2}\.",
            r"Opera",
            r" \.NET[\d\.]*",
            r"cubot",
            r"; M bot",
            r"; CRONO",
            r"; B bot",
            r"; IDbot",
            r"; ID bot",
            r"; POWER BOT",
            r"OCTOPUS-CORE",
            r"htc_botdugls",
            r"super\/\d+\/Android\/\d+",
        ]

        return list(set(local_list + json_list))
