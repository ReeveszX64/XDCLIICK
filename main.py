import random,win32api,time,win32con,win32gui,keyboard

r_cps = 60
l_cps = 60

# Create a random number generator using the Mersenne Twister algorithm
gen = random.Random()

# Generate a random delay for right click
rclick_delay = gen.randint(4, 7)

# Calculate delay for right click based on r_cps
rdelay = 1000 // r_cps

# Generate a random delay for left click
lclick_delay = gen.randint(4, 7)

# Calculate delay for left click based on l_cps
ldelay = 1000 // l_cps

while True:
    if win32api.GetAsyncKeyState(win32con.VK_RBUTTON) < 0:
        # Find the window handle by its name ("LWJGL" in this case)
        lwjgl_window_handle = win32gui.FindWindow("LWJGL", None)
        
        # Send a mouse button down message
        win32api.PostMessage(lwjgl_window_handle, win32con.WM_RBUTTONDOWN, 0, 0)
        
        # Introduce a delay
        time.sleep(rclick_delay / 1000)  # Convert milliseconds to seconds
        
        # Send a mouse button up message
        win32api.PostMessage(lwjgl_window_handle, win32con.WM_RBUTTONUP, 0, 0)
        
        # Introduce a delay
        time.sleep(rdelay / 1000)  # Convert milliseconds to seconds
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0:
            # Find the window handle by its name ("LWJGL" in this case)
            lwjgl_window_handle = win32gui.FindWindow("LWJGL", None)
            
            # Send a mouse button down message
            win32api.PostMessage(lwjgl_window_handle, win32con.WM_LBUTTONDOWN, 0, 0)
            
            # Introduce a delay
            time.sleep(rclick_delay / 1000)  # Convert milliseconds to seconds
            
            # Send a mouse button up message
            win32api.PostMessage(lwjgl_window_handle, win32con.WM_LBUTTONUP, 0, 0)
            
            # Introduce a delay
            time.sleep(rdelay / 1000)  # Convert milliseconds to seconds
