from tkinter import *

root = Tk()
root.title('Codemy.com - center')
app_width = 1366
app_height = 768

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f'{app_width}x{app_height}+{100}+{100}')

app_height = 500
myLabel = Label(root, text=f'width:{screen_width}height:{screen_height}')
myLabel.pack()

root.mainloop() 

