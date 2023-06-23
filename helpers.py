

def filedialog():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)    

    file_paths = filedialog.askopenfilenames()
    root.destroy()

    return file_paths        

def saveDirectory():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)    
    # open the file dialog box
    directory_paths = filedialog.askdirectory()
    root.destroy()
    # print the selected file path
    return directory_paths





