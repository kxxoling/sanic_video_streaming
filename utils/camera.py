import asyncio

import cv2


class Camera():
    """Using Camera as stream"""

    def __init__(self):
        self.video_source = 0

    async def frames(self):
        camera = cv2.VideoCapture(self.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            _, img = camera.read()
            yield cv2.imencode('.jpg', img)[1].tobytes()
            await asyncio.sleep(1/120)

    async def stream(self, rsp):
        async for frame in self.frames():
            rsp.write(
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )
