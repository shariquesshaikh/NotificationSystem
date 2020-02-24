#pip install win10toast
import win10toast 

def func():
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('Notification','Notification from python script',duration=10)   #icon_path="image.ico"

func()
