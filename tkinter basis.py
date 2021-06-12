#keydown function
# .get() to get a value ,,, you can get a value from a Spinbox,textarea,...
# .delete(0.0 ,END) to delete a data
# .insert(END ,data_to_insert) to insert a data
def click():
    text_entered = textentry.get()
    lower_text_entered = text_entered.lower()
    output.delete(0.0,END) #clear the box first
    try : #this will do test ,if value exist
        definition = my_dictionary[lower_text_entered]
    except : #if the value doesn't exist
        definition = "Sorry ,I don't know what you mean ,try again"
    output.insert(END ,definition)

    

#exit function    
def close_window():
    window.destroy()
    exit()
    




#from tkinter import all
from tkinter import *

### create a main window :
window = Tk() #object of the attribute Tk()
#window's title :
window.title("My Computer Science Glossary")
#window's size :
#window.geometry("800x500")
window.resizable(width=False, height=False) #prevent window from being resized
window.configure(background='#111111') #make the bg of the window black

#add a bg image variable: [gif]
#label will allow you to display something unto the window
# .grid is how we layer things out ,sticky = East ,Weast
# .grid has also pady and padx method
photo1 = PhotoImage(file = "home.gif") 
Label (window,image=photo1 ,bg='black').grid(row=0, column=0,sticky=E)

#create a label : bg(background) fg(foreground) font(font)
#Label(where to display ,what to display,parameters).method
Label(window ,text="Enter the word you would like a definition for :",bg="#001100",fg="#66ccff",font="none 12 bold") .grid(row=0 ,column = 0,sticky = W)

#create a text entry box :
textentry = Entry(window ,width=20 ,bg="#FFDDFF")
textentry.grid(row=2 ,column = 0 ,sticky = W)

#add a submit button :
subbutton = Button (window ,text="SUBMIT",width=6,command =click)
subbutton.grid(row=3 ,column = 0 ,sticky = W)

#create another label :
Label (window ,text="\nDefinition :",bg='black',fg='white', font="none 12 bold").grid(row = 4, column =0 ,sticky = W)

#create a textbox :
output = Text(window ,width=75,height=6, wrap=WORD ,bg = "#8c8cba")
output.grid(row=5 ,column = 0,columnspan=2 ,sticky = W)


#the dictionnary :
my_dictionary = {'fandresena':'Is a surname of a geek','ny avo':'Is a name of a geek'}

#exit label :
Label(window ,text="Click to exit :",bg="#001100",fg="#999999",font="none 12 bold") .grid(row=6 ,column = 0,sticky = W)
#exit button :
exbutton = Button (window ,text="Exit",width=14,command =close_window)
exbutton.grid(row=7 ,column = 0 ,sticky = W)


###run the main loop to display all the window all the time
window.mainloop()






