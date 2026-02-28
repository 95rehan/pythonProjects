# import cv2
# import math

# path = 'image.png'
# img = cv2.imread(path)

# # Check if image loaded properly
# if img is None:
#     print("Error: Image not found. Check the path.")
#     exit()

# points = []


# def getAngle(points):
#     if len(points) < 3:
#         return

#     b, c, a = points[-3:]

#     ang = math.degrees(
#         math.atan2(c[1] - b[1], c[0] - b[0]) -
#         math.atan2(a[1] - b[1], a[0] - b[0])
#     )

#     # Normalize angle
#     ang = abs(ang)
#     if ang > 180:
#         ang = 360 - ang

#     ang = round(ang)
#     print("Angle:", ang)

#     cv2.putText(
#         img,
#         str(ang),
#         (b[0] - 40, b[1] - 20),
#         cv2.FONT_HERSHEY_COMPLEX_SMALL,
#         1,
#         (0, 255, 0),
#         2
#     )


# def click_event(event, x, y, flags, params):
#     img

#     if event == cv2.EVENT_LBUTTONDOWN:

#         # Draw line from previous point
#         if len(points) > 0:
#             cv2.line(img, tuple(points[-1]), (x, y), (0, 255, 0), 2)

#         cv2.circle(img, (x, y), 4, (0, 255, 0), -1)
#         points.append([x, y])

#         if len(points) % 3 == 0:
#             getAngle(points)

#         cv2.imshow('Image', img)

#     if event == cv2.EVENT_RBUTTONDOWN:
#         points.clear()
#         img = cv2.imread(path)
#         cv2.imshow('Image', img)


# cv2.imshow('Image', img)
# cv2.setMouseCallback('Image', click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
