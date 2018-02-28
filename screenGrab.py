import win32gui
import win32ui
import win32con
import win32api
import random
# grab a handle to the main desktop window
from time import sleep
sleep(5)
hdesktop = win32gui.GetDesktopWindow()

# determine the size of all monitors in pixels
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
print left
print top
print width
print height
# create a device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# create a memory based device context
mem_dc = img_dc.CreateCompatibleDC()

# create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc,width, height)
mem_dc.SelectObject(screenshot)

# copy the screen into our memory device context
mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)

# save the bitmap to a file
screenshot.SaveBitmapFile(mem_dc, 'screenshot.jpg')
# free our objects
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())

sizeWidth=800
sizeHeight=600
for x in range(20):
  left= random.randint(0,width-sizeWidth)
  right=random.randint(0,height-sizeHeight)
  # create a device context
  desktop_dc = win32gui.GetWindowDC(hdesktop)
  img_dc = win32ui.CreateDCFromHandle(desktop_dc)

  # create a memory based device context
  mem_dc = img_dc.CreateCompatibleDC()

  # create a bitmap object
  screenshot = win32ui.CreateBitmap()
  screenshot.CreateCompatibleBitmap(img_dc, sizeWidth, sizeHeight)
  mem_dc.SelectObject(screenshot)

  # copy the screen into our memory device context
  mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, right), win32con.SRCCOPY)
  name='screen'+str(x)+".PNG"
  # save the bitmap to a file
  screenshot.SaveBitmapFile(mem_dc, name)
  # free our objects
  mem_dc.DeleteDC()
  win32gui.DeleteObject(screenshot.GetHandle())
