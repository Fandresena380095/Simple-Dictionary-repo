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
        definition = "Sorry for that one,maybe you should google it"
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
Label(window ,text="Confused with CS terms,look for its definition here",bg="#001100",fg="#66ccff",font="none 12 bold") .grid(row=0 ,column = 0,sticky = W)

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
my_dictionary = { "algorithm": "An algorithm is a set of instructions or rules designed to solve a definite problem. The problem can be simple like adding two numbers or a complex one, such as converting a video file from one format to another.",
                  "program": "A computer program is termed as an organized collection of instructions, which when executed perform a specific task or function. A program is processed by the central processing unit (CPU) of the computer before it is executed.",
                  "api": "Application Programming Interface (API) is a set of rules, routines, and protocols to build software applications. APIs help in communication with third party programs or services, which can be used to build different software.",
                  "argument": "Argument or arg is a value that is passed into a command or a function. For example, if SQR is a routine or function that returns the square of a number, then SQR(4) will return 16. Here, the value 4 is the argument. Similarly, if the edit is a function that edits a file, then in edit myfile.txt, ‘myfile.txt’ is the argument.",
                  "boolean": "A Boolean expression or Boolean logic is an expression used for creating statements that are either TRUE or FALSE. Boolean expressions use AND, OR, XOR, NOT and NOR operators with conditional statements in programming, search engines, algorithms, and formulas. Boolean expressions are also called comparison expressions, conditional expressions, and relational expressions.",
                  "bug": "A bug is a general term used to denote an unexpected error or defect in hardware or software, which causes it to malfunction. Even though bugs are often considered to be insignificant computer glitches, there have been instances where bugs have caused life-threatening conditions and led to major financial losses.",
                  "object": "An object is a combination of related variables, constants and other data structures which can be selected and manipulated together. An object can include shapes that appear on a screen or the age of students in a school.",
                  "object-oriented-programming": "Object-oriented programming (OOP) is a model defined by programmers that revolve around objects and data rather than ‘actions’ and ‘logic’. In OOP, not only the data type of a data structure is defined, but also the types of functions that can be applied to it. Through this, the data structure becomes an object that consists of both data and functions.",
                  "oop": "Object-oriented programming (OOP) is a model defined by programmers that revolve around objects and data rather than ‘actions’ and ‘logic’. In OOP, not only the data type of a data structure is defined, but also the types of functions that can be applied to it. Through this, the data structure becomes an object that consists of both data and functions.",
                  "class": "In Object-Oriented programming, a class refers to a set of related objects with common properties. Classes and the ability to create new classes render OOP a powerful and flexible programming model. ",
                  "code": "Code or source code is a term used to describe a written set of instructions, written using the protocols of a particular language, such as Java, C or Python. The code can also be used informally to describe text written in a specific language. There are instances where references to the code are made for different languages, such as ‘PHP Code’, ‘HTML Code’,  ‘Java Code’ or ‘CSS Code’.",
                  "shell": "The command-line interface is a user interface based on the text. The UI is used to view and manage computer files. Command-line interfaces are also called command-line user interfaces, console user interfaces and character user interfaces. During the early 1960s and through the 1970s and 1980s, the command line interface was the primary means of interaction with most computers on terminals.",
                  "compilation": "The process of creating an executable program through code written in a compiled programming language is called compilation. Through compiling, the computer can understand and run the program without using the programming software used to create it. A compiler is a program that translates computer programs written using letters, numbers, and characters into a machine language program. ",
                  "conditional": "Conditionals, conditional statements, and conditional expressions are features of programming language, which help the code make a choice and result in either TRUE or FALSE.",
                  "data types": "A data type is the classification of a particular type of data. We as humans can understand the difference between a name and a number, but the computer cannot. The computer uses special internal codes to distinguish between different types of data it receives and processes. The most common data types include integer type which are numbers, a floating-point number data type which are decimal based numbers, Boolean values which are TRUE or FALSE and character data type which is alphabets.",
                  "array": "Arrays are lists or groups of similar types of data values that are grouped. All values in the array are of the same data type and are only differentiated by their position in the array.",
                  "declaration": "A statement that describes a variable, function or any other identifier is called a declaration. A declaration helps the compiler or interpreter identify the word and understand its meaning, and how the process should be continued.",
                  "exception": "A special, unexpected and anomalous condition encountered during the execution of a program is known as an exception. It can also be termed as an error or a condition that alters the way of the program or the microprocessor to a different path. An example of an exception can be the case when a program tries to load a file from the disk, but the file does not exist. The exceptions must be handled and eradicated in the program code to avoid any fatal error.",
                  "framework": "Framework in programming is a foundation with a specified level of complexity that may be altered by the programmer, making use of their code. A framework might include different software libraries, APIs, compilers and much more. In simpler terms, a framework provides a favorable environment for a certain type and level of programming for a project. A framework allows the developers to bypass the general necessities and focus on more project-related specifics.",
                  "hardcode": "In computer programming, the term hard code or hardcode is used to describe code that is not likely to change. Hardcoded features are built into hardware or software in such a way so that they cannot be modified later on. For example, if font size 10 is hardcoded in the software, then it might not change for a long time.",
                  "loop": "A loop is a sequence of instructions that repeat the same process over and over until a condition is met and it receives the order to stop. In a loop, the program asks a question, and if the answer directs the program to perform an action, the action is performed, and the loop runs again, performing the same task. It runs until the answer is such that no action is required and the code can proceed further.",
                  "endless loop": "An endless loop or infinite loop is a continuous repetition of a program snippet, which is everlasting. This occurs majorly due to conditional operators and functions which redirect the code back to the snippet, making it endless.",
                  "iteration": "In simple terms, iteration is the process to repeat a particular snippet of code over and over again to perform a certain action.",
                  "keywords": "Words that are reserved by a programming language or a program as they have special meaning are known as keywords. These keywords are reserved to perform certain tasks, and they can be either commands or parameters. Each programming language has a set of reserved keywords (also known as reserved names) which cannot be used as variable names. Some keywords in ‘C’ language are ‘return’, ‘while’, ‘if’, ‘static’, ‘continue’ and ‘default’.",
                  "null": "Null defines the lack of any value whatsoever. A null character is a programming code, which represents a character with no value, missing value or the end of a character string. If we state $val1= ”” and $val2= “1”, $val1 has a null value.",
                  "operand": "An operand is a term used to denote the objects which can be manipulated using different operators. In the expression ‘A+F+Q’, ‘A’, ‘F’ and ‘Q’ are operands.",
                  "operator": "An operator is a term used to denote the object which can manipulate different operands. In the expression ‘A+F-Q’, ‘+’ and ‘-‘are operators. Examples of different operators are + (addition), -- (decrement), = (equals), != (not equal) and >= (greater than or equal to).",
                  "variable": "A variable is a location that stores temporary data within a program which can be modified, store and display whenever need.",
                  "pointer": "In programming, a pointer is a variable that contains the address of a location in the memory. The location is the commencing point of an object, such as an element of the array or an integer. Using pointers improves the performance of the program as it is cheaper in time and space to copy and dereference pointers than to copy and access the data to which the pointer is referring.",
                  "hll": "A high-level language (HLL) is a programming language that lets the developer write programs irrespective of the nature or type of computer. But if a computer has to understand a high-level language, it should be compiled into a machine language. HLLs are considered high-level because they are in close proximity to human languages and further from machine languages. High-level languages include BASIC, C, C++, Pascal, Prolog, and FORTRAN.",
                  "high-level language": "A high-level language (HLL) is a programming language that lets the developer write programs irrespective of the nature or type of computer. But if a computer has to understand a high-level language, it should be compiled into a machine language. HLLs are considered high-level because they are in close proximity to human languages and further from machine languages. High-level languages include BASIC, C, C++, Pascal, Prolog, and FORTRAN.",
                  "low-level language": "A low-level language is a language that is very close to machine language and provides a little abstraction of programming concepts. Low-level languages are closer to the hardware than human languages. The most common examples of low-level languages are assembly and machine code.",
                  "machine language": "Also known as machine code, machine language is a lowest-level programming language consisting of binary digits or bits that are read by computers. Machine language is the only language understood by computers. As it consists of only numbers, they cannot be comprehended by humans. Therefore, programmers write code in the high-level language, which is then translated into assembly language or machine language by a compiler, which is then converted to a machine language by an assembler.",
                  "markup language": "A markup language is a relatively simple language that consists of easily understood keywords and tags, used to format the overall view of the page and its contents. The language specifies codes for formatting the layout and style of a page, within a text file only. The most common markup languages are Hypertext Markup Language (HTML), Extensible Markup Language (XML) and Standard Generalized Markup Language (SGML).",
                  "package": "A package is an organized module of related interfaces and classes. Packages are used to organize classes that belong to the same category or provide related functionality.",
                  "runtime": "Runtime or runtime is the time period during which a program is, in fact, running on a computer. If an operation occurs at ‘runtime’, it occurred when a program is running or the moment at which the program begins to run. Also known as execution time, the runtime is part of the life cycle of the program, and it denotes the time between when the program begins running and until it is closed by the OS or the user.",
                  "backend": "Backend is another term used for background in programming. A backend task is the one that is performed in the background with the user’s direct interaction. Similarly, a backend developer is a person who designs programs that process data and perform tasks that users don’t directly see.",
                  "front-end": "The Front-end is the user interface of a computer or any device. For example, any operating system provides users with the ease of navigation. A program or OS is considered good if the UI or Front-end is easy to use and seamless to navigate. Front-end developers are the programmers who design and develop the user interface of a device.",
                  "server-side": "When procedures and processes are performed on the server, they are deemed server-side. On the other hand, the client-side is at the end of the user. Many programming languages are designed for server-side programmings such as PHP, Perl, and ASP. With the internet boom, almost all websites make use of both server-side and client-side processing. An excellent example of a server-side script is a search engine.",
                  "source data": "Source data or data source is the key location from which data is used in the program. The source data can come from a database, spreadsheet or even a hard-coded data location. When a program is executed to display data in a table, the program retrieves the data from its source and then presents it in the arrangement as defined in the code.",
                  "statement": "In programming, a statement is a single line of code written legally in a programming language that expresses an action to be carried out. A statement might have internal components of its own, including expressions, operators and functions. ",
                  "syntax": "Similar to human languages, programming languages have their own set of rules on how statements can be conveyed. The set of these rules is known as syntax. While a number of programming languages share many features, functions, and capabilities, they differ in syntax. Without the proper use of the syntax, one cannot write an executable program, and a wrong syntax will lead to a plethora of errors.",
                  "token": "A token is the smallest individual unit in a program, often referring to a portion of a much larger data piece. For example, if a person’s name is John Thomas Wood, it can be broken into tokens; ‘John’, ‘Thomas’ and ‘Wood’. The programmer can then go on to use only the portion or token they wish to. Tokens are classified into keywords, identifiers, literals, operators, and punctuators.",
                  }

#exit label :
Label(window ,text="Click to exit :",bg="#001100",fg="#999999",font="none 12 bold") .grid(row=6 ,column = 0,sticky = W)
#exit button :
exbutton = Button (window ,text="Exit",width=14,command =close_window)
exbutton.grid(row=7 ,column = 0 ,sticky = W)


###run the main loop to display all the window all the time
window.mainloop()






