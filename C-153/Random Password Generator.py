from tkinter import*
import random

root=Tk()
root.title("Password Generator")
root.geometry("500x500")

label=Label(root)

array_3d =[[[1,2,3,4,5,6],["Heads","Tails"],["A","B","C","D","E","F","G","H","I","J"]]]
print(array_3d[0][2][3])

def newpassword():
    random_no1 = random.randint(0,5)
    random_no2 = random.randint(0,1)
    random_no3 = random.randint(0,9)
    
    letter1 = str(array_3d[0][0][random_no1])
    letter2 = str(array_3d[0][1][random_no2])
    letter3 = str(array_3d[0][2][random_no3])
    label['text'] = letter1 + "" + letter2 + "" + letter3
    
btn=Button(root, text="New Password", command=newpassword)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()