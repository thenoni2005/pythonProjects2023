#ANTHONY TRUJILLO
#12/14/2022
#Testing Exam
from applications import *



def main():
    root = Tk()
    getFile = GetFileName(root)
    if createApp:
        app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()