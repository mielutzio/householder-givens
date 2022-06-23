from functions import givens, householder
import numpy as np
import numpy.linalg as la

from tkinter import W, Button, Entry, IntVar, Label, LabelFrame, OptionMenu, Radiobutton, StringVar, Tk, messagebox


def run_alg():
    x_str = []
    children_widgets = frame1.winfo_children()
    for child_widget in children_widgets:
        if child_widget.winfo_class() == 'Entry':
            x_str.append(child_widget.get())
    x = np.array(x_str)
    try:
        x = np.array(x, dtype=float)
    except Exception:
        messagebox.showerror(
            title='Error', message='Vectors elements must be numbers')
    else:
        if r.get() == 0:
            messagebox.showerror(
                title='Error', message='Select an algorithm')

    if r.get() == 1:
        v_str = []
        children_widgets = frame2.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                v_str.append(child_widget.get())
        v = np.array(v_str)
        try:
            v = np.array(v, dtype=float)
        except Exception:
            messagebox.showerror(title='Error', message='Vectors elements must be numbers')
        else:
            householder(x, v)

    elif r.get() == 2:
        degrs = degrees.get()
        if degrs == 'pi':
            givens(x, np.pi)
        elif degrs == 'pi/2':
            givens(x, np.pi/2)
        elif degrs == 'pi/3':
            givens(x, np.pi/3)
        elif degrs == 'pi/6':
            givens(x, np.pi/6)


root = Tk()
root.title('Householder & Givens Visualization')
root.geometry("400x450")
root.resizable(False, False)

frame1 = LabelFrame(root, text='')
frame1.grid(row=0, column=0, pady=20, padx=10)
frame2 = LabelFrame(root, text='')
frame2.grid(row=1, column=0, pady=10, padx=50)

Label(frame1, text='x', font='Helvetica 12').grid(row=0, column=0)
Entry(frame1, width=5).grid(row=1, column=0)
Entry(frame1, width=5).grid(row=2, column=0)


r = IntVar()
Radiobutton(frame2, text='Householder reflection  ', variable=r, value=1,
            font='Helvetica 12').grid(row=0, column=0, sticky=W)
Label(frame2, text='v', font='Helvetica 12').grid(row=1, column=0)
Entry(frame2, width=5).grid(row=2, column=0)
Entry(frame2, width=5).grid(row=3, column=0)

Radiobutton(frame2, text='Givens rotation  ', variable=r, value=2,
            font='Helvetica 12').grid(row=4, column=0, sticky=W)
degrees = StringVar()
degrees.set('pi')
degrees_drop = OptionMenu(frame2, degrees, 'pi', 'pi/2', 'pi/3', 'pi/6')
degrees_drop.grid(row=5, column=0)

btn_start = Button(frame2, text='Start', command=run_alg)
btn_start.grid(row=6, column=0, pady=50)

root.mainloop()
