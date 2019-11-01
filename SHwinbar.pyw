##  本python脚本的目的就是查看任务栏的状态
##  如果是任务栏显示就让它隐藏，如果任务栏隐藏就让它显示
import ctypes
import win32gui
import win32con
import ctypes.wintypes 
import time

#APPBARDATA类型定义 类
class APPBARDATA(ctypes.Structure):
#{
    _fields_ = [("cbSize", ctypes.wintypes.DWORD),
        ("hWnd", ctypes.wintypes.HANDLE),
        ("uCallbackMessage", ctypes.wintypes.UINT),
        ("uEdge", ctypes.wintypes.UINT),
        ("rc", ctypes.wintypes.RECT),
        ("lParam", ctypes.wintypes.LPARAM)]
#}

#设置是否自动隐藏  函数
ABM_SETSTATE=0x0000000a
def setAutoHide(autoHide):
#{
    appbarData.lParam = int(autoHide)  #是否自动隐藏
    ctypes.windll.shell32.SHAppBarMessage(ABM_SETSTATE, ctypes.byref(appbarData))
#}

##################################################################################################################
#初始化appbarData
appbarData = APPBARDATA(ctypes.sizeof(APPBARDATA)
                ,None
                ,0
                ,0
                ,ctypes.wintypes.RECT(0,0,0,0)
                ,0
            )
win_bar = win32gui.FindWindow("Shell_TrayWnd",None)
appbarData.hWnd=win_bar


###############################开始设置###########################################################################
isVisible=win32gui.IsWindowVisible(win_bar)

#如果任务栏显示就隐藏，如果任务栏隐藏就显示
if isVisible == True :
    #开始任务栏显示，隐藏
    #print("V to invisible")
    setAutoHide(True)    #设置是否自动隐藏
    time.sleep(0.06)    #这样才能正确把两个设置一起做好，如果不行可以试试先调整一下sleep延迟
    win32gui.ShowWindow(win_bar,win32con.SW_HIDE)
    
else :
    #开始任务栏隐藏，显示
    #print("Inv to visible")
    setAutoHide(False)    #设置是否自动隐藏
    time.sleep(0.01)    #这样才能正确把两个设置一起做好，如果不行可以试试先调整一下sleep延迟
    win32gui.ShowWindow(win_bar,win32con.SW_SHOW)
    
    

