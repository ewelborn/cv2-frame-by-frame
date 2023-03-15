import sys
import cv2
import copy

if len(sys.argv) < 2:
    print("Expected video file")
    exit()

videoPath = sys.argv[1]

cap = cv2.VideoCapture(videoPath)
fps = cap.get(cv2.CAP_PROP_FPS)
videoName = videoPath
windowTitle = videoName

if cap.isOpened() == False:
    print("Could not open video file")
    exit()

print(f"Opened video file at {videoPath}")
print("Buffering video...")

frames = []

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break

    frames.append(frame)

if len(frames) == 0:
    print("Could not buffer video")
    exit()

width = frames[0].shape[1]
height = frames[0].shape[0]

print(f"Video buffered: {len(frames)} frames at {width}x{height}")

cap.release()

currentFrameIndex = 0

cv2.namedWindow(windowTitle, cv2.WINDOW_NORMAL)

while True:
    #_, __, windowWidth, windowHeight = cv2.getWindowImageRect(windowTitle)
    print(f"Frame: {currentFrameIndex}")
    cv2.imshow(windowTitle, frames[currentFrameIndex])

    key = cv2.waitKey(0) & 0xFF

    # Did the user close the window?
    if cv2.getWindowProperty(windowTitle, cv2.WND_PROP_VISIBLE) < 1:
        break

    if key == ord("d") or key == ord("D"):
        # Go forwards
        currentFrameIndex = min(currentFrameIndex + 1, len(frames) - 1)
    elif key == ord("a") or key == ord("A"):
        # Go backwards
        currentFrameIndex = max(currentFrameIndex - 1, 0)

    elif key == ord("e") or key == ord("E"):
        # Go forwards by 1 second
        currentFrameIndex = min(currentFrameIndex + int(fps), len(frames) - 1)
    elif key == ord("q") or key == ord("Q"):
        # Go backwards by 1 second
        currentFrameIndex = max(currentFrameIndex - int(fps), 0)

    elif key == ord("z") or key == ord("Z"):
        # Jump to beginning
        currentFrameIndex = 0
    elif key == ord("c") or key == ord("C"):
        # Jump to end
        currentFrameIndex = len(frames) - 1

    elif key == 27:
        # Quit
        break