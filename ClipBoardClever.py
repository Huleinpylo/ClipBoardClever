import win32clipboard,time

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)
    time.sleep(10)
    
