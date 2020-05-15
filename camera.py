import cv2 as cv

class Camera(object):
    CAPTURES_DIR = "static/captures/"
    RESIZE_RATIO = 1.0

    def __init__(self):
        self.video = cv.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            return None

        if (Camera.RESIZE_RATIO != 1):
            frame = cv.resize(frame, None, fx=Camera.RESIZE_RATIO, \
                fy=Camera.RESIZE_RATIO)
        return frame

    def get_feed(self):
        frame = self.get_frame()
        if frame is not None:
            ret, jpeg = cv.imencode('.jpg', frame)
            return jpeg.tobytes()

    def set_contrast(self):
        frame = self.get_frame()