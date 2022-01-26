import tkinter,sys,time,threading

root = tkinter.Tk()
root.overrideredirect(True)
root.attributes("-alpha",0.8)
root.wm_attributes('-topmost',1)
root.geometry("160x200+1375+200")
tkinter.Label(root,justify='left',font=(None,12),text='''00:00-07:30睡\n07:30-08:00刷洗吃
08:00-10:00自由\n10:00-11:00吹口琴\n11:00-11:30背单词\n11:30-12:00词汇自测\n12:00-15:00自由
15:00-15:30\n19:00-21:00自由\n21:00-23:00看电影\n23:30-00:00看书''').place(x=0,y=0)
all_y=root.winfo_screenheight()
all_x=root.winfo_screenwidth()
x,y=0,0
rootalpha=0.1
is_hide='right'

def get_pos(event):
    global x,y
    x,y = event.x,event.y
def window_move(event):
    global x,y
    new_x = min(all_x-160,(event.x-x)+root.winfo_x())
    new_y = max(0,        (event.y-y)+root.winfo_y())
    root.geometry("160x200+"+str(new_x)+"+"+str(new_y))
    
def change_alpha(event):
    global rootalpha
    if rootalpha==0.1:rootalpha=0.8
    else:rootalpha=0.1
    root.attributes("-alpha",rootalpha)
    
def close(event):
    root.destroy()
    sys.exit()
    
def move_3(a,b,root=root):
    global lab
    while root.winfo_x()<all_x-40 and is_hide=='right':
        root.geometry("160x200+"+str(root.winfo_x()+4)+"+"+str(root.winfo_y()))
        time.sleep(0.001)     
    while root.winfo_x()>all_x-160 and is_hide=='left':
        root.geometry("160x200+"+str(root.winfo_x()-4)+"+"+str(root.winfo_y()))
        time.sleep(0.001)
    while root.winfo_y()>=40-200 and is_hide=='up':
        root.geometry("160x200+"+str(root.winfo_x())+"+"+str(root.winfo_y()-5))
        time.sleep(0.001)
    while root.winfo_y()<0 and is_hide=='down':
        root.geometry("160x200+"+str(root.winfo_x())+"+"+str(root.winfo_y()+5))
        time.sleep(0.001)
            
def move_1(event):
    global is_hide
    if   root.winfo_x()>=all_x-160 and str(event.type)=='Leave':is_hide='right'
    elif root.winfo_x()<=all_x-40  and str(event.type)=='Enter' and not is_hide in'updown':is_hide='left'
    elif 0>=root.winfo_y()>=40-200 and str(event.type)=='Leave':is_hide='up'
    elif root.winfo_y()<=0      and str(event.type)=='Enter':is_hide='down'
    else:pass   
    threading.Thread(target=move_3,args=(root.winfo_x(),root.winfo_y())).start()

root.bind("<B1-Motion>",window_move)
root.bind("<Button-1>",get_pos)

root.bind("<Double-Button-1>",change_alpha)
root.bind("<Double-Button-3>",close)

root.bind("<Leave>",move_1)
root.bind("<Enter>",move_1)

root.mainloop()