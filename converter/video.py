from .image import ImageConverter
import cv2


class VideoConverter(ImageConverter):
    async def convert(self, file: str, convert_gs=False):
        video = cv2.VideoCapture(file)
        self.run_video = True
        
        async def convert_frame(frame):
            if convert_gs:
                return await self._to_emoji(frame, conv=True)
            return await self._to_rgb_emoji(frame)
        
        status, frame = video.read()
        count = 0
        while status:
            status, frame = video.read()
            
            count += 1
            if count % 2 == 0:
                continue
            
            await convert_frame(frame)
