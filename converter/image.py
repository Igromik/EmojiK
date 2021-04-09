import cv2
from numpy import ndarray
from ext import JSONLoader


json_loader = JSONLoader()
config = json_loader("config.json")

class ImageConverter:
    async def _to_emoji(self, file: ndarray, conv=False):
        try:
            if conv:
                file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
            shape = file.shape
        except:
            return ""

        EMOJIS = config["emojis"]
        step = int((shape[0] / 500) * config["step"]) or 1
        image = ""
        for x in range(0, shape[0], step):
            for y in range(0, shape[1], step):
                color = file[x, y]

                if color >= 127:
                    image += EMOJIS["white"]
                elif color <= 127:
                    image += EMOJIS["black"]
                    
            image += "\n"

        print(image)

    async def _to_rgb_emoji(self, file: ndarray):
        try:
            shape = file.shape
        except:
            return ""
            
        EMOJIS = config["emojis"]
        step = int((shape[0] / 500) * config["step"]) or 1
        image = ""
        for x in range(0, shape[0], step):
            for y in range(0, shape[1], step):
                (b, g, r) = file[x, y]

                if g <= b > r:
                    image += EMOJIS["blue"]
                elif (r < g > b) and r <= 170 >= b:
                    image += EMOJIS["green"]
                elif (b < r >= g) and int(g/2) > b:
                    image += EMOJIS["red"]
                
                # Extra checks
                elif b < r > g:
                    image += EMOJIS["red"]
                elif r < g > b:
                    image += EMOJIS["green"]
                elif r < b > g:
                    image += EMOJIS["blue"]
                else:
                    grsc_color = 0.2126*r + 0.7152*g + 0.0722*b
                    if grsc_color >= 127:
                        image += EMOJIS["white"]
                    elif grsc_color <= 127:
                        image += EMOJIS["black"]

            image += "\n"

        print(image)


    async def convert(self, file: str, RGB=False):
        if RGB:
            image = cv2.imread(file)
            return await self._to_rgb_emoji(image)
        else:
            image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            return await self._to_emoji(image)
