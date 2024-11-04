from tkinter import *
from tkinter.font import Font

class Empty(Exception):
    pass

class ArrayStack():
    
    def __init__(self) -> None:
        self._data = []
        
        
    def push(self,value):
        self._data.append(value)
        
    def top(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data[-1]
    def isEmpty(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return len(self._data) == 0  #
    
    
    def pop(self):
        """_summary_
        """
        if self.isEmpty():
             raise Empty("Stack is Empty")
        return self._data.pop()
       
        
    def __len__(self):
        return len(self._data)

############-------------------


def parenthesis_matched(expr)-> bool:
    """_summary_
    Returns True when delimiters match and false when delimiters do not match

    Args:
        expr (_type_): enter a description containing delimiters
    """
    
    lefty = '{[('
    righty = '}])'
    
    S1 = ArrayStack()
    
    for c in expr:
        if c in lefty:
            S1.push(c)
        elif c in righty:
            if S1.isEmpty():
                return False
            if righty.index(c) != lefty.index(S1.pop()):
                return False
    return S1.isEmpty()






## function declaration



############-------------------


class Window():
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Parentheses Checker")
        self.window.geometry("400x700")
        
        self.window.resizable(False,True)
        
        self.font1 = Font(family='Poppins',size=11)
        self.font2 = Font(family="Poppins" , size = 7)
        
        ##starting the design of the Window
        
        self.label = Label(self.window,text="Enter an expression with parenthesis:",justify="left",font=self.font2)
        self.label.pack(pady=20,padx=10)
        
        self.expr = Entry(self.window,width=300,font=self.font1)
        self.expr.pack(pady=(20,20),padx=5,ipadx=5,ipady=20)
        
        
        
        self.result =  Label(self.window,width=300,font=self.font1)
        self.result.pack(pady=(50,50),padx=5,ipadx=5,ipady=20)
        
        self.check = Button(self.window,text="Check" , width=20,border=None, command=self.parenthesis_checker)
        self.check.pack(padx=5,pady=10)
        self.window.mainloop()
        
        
        
        
        
    def parenthesis_checker(self)->str:
  
        expr = self.expr.get()
        
        parenthesis_matched(expr)
    
        if parenthesis_matched(expr):
            self.result.config(text="Parenthesis properly matched",fg='green')
        else:
            self.result.config(text="Parenthesis not properly matched",fg='red')
            



   
        
    
    
    
    
    
    
    
    
   
   
   
   
    
    
    
    




    
    
if __name__ == "__main__":
    Window()