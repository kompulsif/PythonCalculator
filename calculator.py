
import tkinter as tk

form = tk.Tk()
form.title("Calculator")
form.geometry("300x400")
form.minsize(300, 400)
form.config(background="black")

operation = tk.Entry(form, justify=tk.RIGHT, font="Verdana 10 bold")
operation.place(relheight=0.12, relwidth=0.758, relx=0.12, rely=0.02)

adOp = 1
pi = None
us = None
kr = None
kl = None


def keyboard_control(k):

    if (k.char == "\r"):
        calc_func()

    elif (k.char != "") and (k.char in ("1234567890.,/*-+^%() ")):
        pass

    elif (k.keysym in ("Left", "Right", "BackSpace", "Delete", "End", "Home")):
        pass

    else:
        return "break"


def writer(b):

    cur_i = operation.index(tk.INSERT)

    if (b["text"] == "π"):
        operation.insert(cur_i, "π")

    else:
        operation.insert(cur_i, b["text"])
        if (b["text"] == "√()"):
            operation.icursor(operation.index(tk.INSERT)-1)


def deleter():
    i = operation.index(tk.INSERT)
    operation.delete(first=i-1, last=i)


def calc_func():

    try:

        i = operation.get().replace(",", ".")

        if ("**" in i):
            raise SyntaxError

        i = i.replace("^", "**")
        i = i.replace("π", "3.1415926535897932384626433832795")
        sq_count = i.count("√")
        sq_count2 = i.count("√(")

        if (sq_count) and (not sq_count == sq_count2):
            raise SyntaxError

        for x in i:
            if (x not in "1234567890-*/+()√%. "):
                raise SyntaxError

        i = i.replace("√", "__import__('math').sqrt").strip()

        result = eval(i.replace(" ", ""))

    except:
        pass

    else:
        operation.delete(0, "end")
        operation.insert(0, result)


def clear_func():
    operation.delete(0, "end")


def advanced_options_func():
    global adOp, pi, us, kr, kl

    if (adOp):

        pi = tk.Button(form, text="π", command=lambda: writer(
            pi), font="Arial 10 bold")
        pi.place(relx=0.12, rely=0.88, relwidth=0.16, relheight=0.10)

        us = tk.Button(form, text="^", command=lambda: writer(
            us), font="Verdana 10 bold")
        us.place(relx=0.32, rely=0.88, relwidth=0.16, relheight=0.10)

        kl = tk.Button(form, text="%", command=lambda: writer(
            kl), font="Verdana 10 bold")
        kl.place(relx=0.52, rely=0.88, relwidth=0.16, relheight=0.10)

        kr = tk.Button(form, text="√()", command=lambda: writer(
            kr), font="Verdana 10 bold")
        kr.place(relx=0.72, rely=0.88, relwidth=0.16, relheight=0.10)

        adop_but.config(text="Hide Advanced Options")
        adOp = 0

    else:

        pi.destroy()
        us.destroy()
        kl.destroy()
        kr.destroy()
        adop_but.config(text="Show Advanced Options")
        adOp = 1


to = tk.Button(form, text="+", command=lambda: writer(to),
               font="Verdana 10 bold", bg="white")
ci = tk.Button(form, text="-", command=lambda: writer(ci),
               font="Verdana 10 bold", bg="white")
ca = tk.Button(form, text="*", command=lambda: writer(ca),
               font="Verdana 10 bold", bg="white")
bo = tk.Button(form, text="/", command=lambda: writer(bo),
               font="Verdana 10 bold", bg="white")

n1 = tk.Button(form, text="1", command=lambda: writer(n1),
               font="Verdana 10 bold", bg="white")
n2 = tk.Button(form, text="2", command=lambda: writer(n2),
               font="Verdana 10 bold", bg="white")
n3 = tk.Button(form, text="3", command=lambda: writer(n3),
               font="Verdana 10 bold", bg="white")

n4 = tk.Button(form, text="4", command=lambda: writer(n4),
               font="Verdana 10 bold", bg="white")
n5 = tk.Button(form, text="5", command=lambda: writer(n5),
               font="Verdana 10 bold", bg="white")
n6 = tk.Button(form, text="6", command=lambda: writer(n6),
               font="Verdana 10 bold", bg="white")

n7 = tk.Button(form, text="7", command=lambda: writer(n7),
               font="Verdana 10 bold", bg="white")
n8 = tk.Button(form, text="8", command=lambda: writer(n8),
               font="Verdana 10 bold", bg="white")
n9 = tk.Button(form, text="9", command=lambda: writer(n9),
               font="Verdana 10 bold", bg="white")

si = tk.Button(form, text="C", command=clear_func,
               font="Verdana 10 bold", bg="white")
n0 = tk.Button(form, text="0", command=lambda: writer(n0),
               font="Verdana 10 bold", bg="white")

no = tk.Button(form, text=".", command=lambda: writer(no),
               font="Verdana 10 bold", bg="white")
de = tk.Button(form, text="Del", command=deleter,
               font="Verdana 10 bold", bg="white")

p1 = tk.Button(form, text="(", command=lambda: writer(p1),
               font="Verdana 10 bold", bg="white")
p2 = tk.Button(form, text=")", command=lambda: writer(p2),
               font="Verdana 10 bold", bg="white")

en = tk.Button(form, text="=", command=calc_func,
               font="Verdana 10 bold", bg="white")


adop_but = tk.Button(form, text="Show Advanced Options",
                     command=advanced_options_func, font="Verdana 10 bold", bg="white")
adop_but.place(relx=0.12, rely=0.76, relwidth=0.758, height=40)

to.place(relx=0.12, rely=0.16, relwidth=0.16, relheight=0.10)
ci.place(relx=0.32, rely=0.16, relwidth=0.16, relheight=0.10)
ca.place(relx=0.52, rely=0.16, relwidth=0.16, relheight=0.10)
bo.place(relx=0.72, rely=0.16, relwidth=0.16, relheight=0.10)

n1.place(relx=0.12, rely=0.28, relwidth=0.16, relheight=0.10)
n2.place(relx=0.32, rely=0.28, relwidth=0.16, relheight=0.10)
n3.place(relx=0.52, rely=0.28, relwidth=0.16, relheight=0.10)
de.place(relx=0.72, rely=0.28, relwidth=0.16, relheight=0.10)

n4.place(relx=0.12, rely=0.40, relwidth=0.16, relheight=0.10)
n5.place(relx=0.32, rely=0.40, relwidth=0.16, relheight=0.10)
n6.place(relx=0.52, rely=0.40, relwidth=0.16, relheight=0.10)
p1.place(relx=0.72, rely=0.40, relwidth=0.16, relheight=0.10)

n7.place(relx=0.12, rely=0.52, relwidth=0.16, relheight=0.10)
n8.place(relx=0.32, rely=0.52, relwidth=0.16, relheight=0.10)
n9.place(relx=0.52, rely=0.52, relwidth=0.16, relheight=0.10)
p2.place(relx=0.72, rely=0.52, relwidth=0.16, relheight=0.10)

si.place(relx=0.12, rely=0.64, relwidth=0.16, relheight=0.10)
n0.place(relx=0.32, rely=0.64, relwidth=0.16, relheight=0.10)
no.place(relx=0.52, rely=0.64, relwidth=0.16, relheight=0.10)

en.place(relx=0.72, rely=0.64, relwidth=0.16, relheight=0.10)


operation.bind("<Key>", keyboard_control)
form.mainloop()
