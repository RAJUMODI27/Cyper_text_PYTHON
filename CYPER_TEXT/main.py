from tkinter import *

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']




def encryption():


    main_text=text1.get()
    shift_key=i.get()
    cypher_text=''
    text1.set("")
    i.set("")

    for char in main_text:
        new_position=(alphabets.index(char)+shift_key)%26
        cypher_text+=alphabets[new_position]
    print(cypher_text)
    l3 = Label(root, text=f"The Encrypted text is :' {cypher_text}'")
    l3.grid(row=4,column=5)







def decryption():

    main_text=text1.get()
    shift_key=i.get()
    cypher_text=''
    text1.set("")
    i.set("")

    for char in main_text:
        new_position=(alphabets.index(char)-shift_key)%26
        cypher_text+=alphabets[new_position]
    print(cypher_text)
    l3 = Label(root, text=f"The original text is :'{cypher_text}'")
    l3.grid(row=4,column=5)





root=Tk()
text1=StringVar()
i=IntVar()
root.title("CYPER TEXT")
root.geometry("300x200")
l1=Label(root,text="Enter your text")
l1.grid(row=1,column=4)
t1=Entry(root,textvariable=text1)
t1.grid(row=1,column=5)


l2=Label(root,text="Enter shift key")
l2.grid(row=2,column=4)
t2=Entry(root,textvariable=i)
t2.grid(row=2,column=5)

b1=Button(root,text="encrypt",command=encryption)
b1.grid(row=4,column=5)

b2=Button(root,text="decrypt",command=decryption)
b2.grid(row=4,column=6)





root.mainloop()
