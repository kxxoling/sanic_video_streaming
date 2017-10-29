from sanic import Sanic
from sanic import response

from utils.camera import Camera

app = Sanic(__name__)


@app.route('/')
async def index(request):
    return response.html('''<img src="/camera-stream/">''')


@app.route('/camera-stream/')
async def camera_stream(request):
    camera = Camera()
    return response.stream(
        camera.stream,
        content_type='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == '__main__':
    app.run(port=5000)
