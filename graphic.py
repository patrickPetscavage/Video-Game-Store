#Code by Patrick Petscavage

import tkinter as tk
import games_list
from games_list import allGamesList 
import funcs
from tkinter import PhotoImage

#This is where the code starts. It allows for the frames to appear and destroy if there is a frame
class run(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self._frame = None
        self.nextPage(MainPage)

    #nextPage destroys the current frame and brings up the new frame that is entered in
    def nextPage(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
#MainPage is the starting page for the video game store. It has featured games, a cart, and a search bar 
class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="").pack(side="top", fill="x", padx = 300, pady=300)
        
        bg = PhotoImage(file=r"C:/Users/pjpet/Downloads/OIG4.jpg.png")
        background_label = tk.Label(self, image=bg) 

        background_label.image = bg 

        background_label.place(x=0, y=0, relheight=1, relwidth=1) 

#getText and gameText are what grabs the name of the button so that it is compared to the list of games later in the code
        def getText(button):
            buttonText = button.cget("text")
            return buttonText

        def gameText(button):
            funcs.gameClicked = getText(button)

        cartButton = tk.Button(self, text = "Cart", command = lambda: master.nextPage(cartPage))
        game1 = tk.Button(self, text = games_list.counterStrike.name, command = lambda: [gameText(game1),master.nextPage(gamePage)])
        game2 = tk.Button(self, text = games_list.detPik.name, command = lambda: [gameText(game2),master.nextPage(gamePage)])
        game3 = tk.Button(self, text = games_list.dayOfDefeat.name, command = lambda: [gameText(game3),master.nextPage(gamePage)])
        game4 = tk.Button(self, text = games_list.prinPeach.name, command = lambda: [gameText(game4),master.nextPage(gamePage)])
        game5 = tk.Button(self, text = games_list.ricochet.name, command = lambda: [gameText(game5),master.nextPage(gamePage)])
        game6 = tk.Button(self, text = games_list.halfLife.name, command = lambda: [gameText(game6),master.nextPage(gamePage)])
        game7 = tk.Button(self, text = games_list.recollection.name, command = lambda: [gameText(game7),master.nextPage(gamePage)])
        game8 = tk.Button(self, text = games_list.paperMario.name, command = lambda: [gameText(game8),master.nextPage(gamePage)])
        game9 = tk.Button(self, text = games_list.pokemonLeg.name, command = lambda: [gameText(game9),master.nextPage(gamePage)])
        searchButton = tk.Button(self, text = "Click Here", command = lambda: master.nextPage(searchPage))
        searchLabel = tk.Label(self, text = "Search Page")
        featuredGamesLabel = tk.Label(self,text = "FEATURED GAMES",font = ("Arial",25))
        
        searchLabel.place(x=10,y=10)
        featuredGamesLabel.place(x = 150,y=100)
        
        cartButton.place(x=550,y=20)
        game1.place(x=130,y=200)
        game2.place(x=250,y=200)
        game3.place(x=430,y=200)
        game4.place(x=110,y=300)
        game5.place(x=310,y=300)
        game6.place(x=430,y=300)
        game7.place(x=40,y=400)
        game8.place(x=210,y=400)
        game9.place(x=430,y=400)
        searchButton.place(x = 10, y =40)

#The search page is what comes up when you click the search button, It allows you to search for games and click to one you want
class searchPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="").pack(side="top", fill="x", padx = 300, pady=300)
        bg = PhotoImage(file=r"C:/Users/pjpet/Downloads/OIG4.jpg.png")
        background_label = tk.Label(self, image=bg) 

        background_label.image = bg 

        background_label.place(x=0, y=0, relheight=1, relwidth=1) 
        funcs.listOfSearchedGames = []
        
        mainButton = tk.Button(self, text = "Main Page",width = 25, command = lambda: master.nextPage(MainPage))
        mainButton.place(x=220,y=30)

        def getText(button):
            buttonText = button.cget("text")
            return buttonText

        def gameText(button):
            funcs.gameClicked = getText(button)
                
        text1 = tk.StringVar()
        text1Entry = tk.Entry(self, width=25, textvariable = text1)
        searchButton = tk.Button(self, text = "New Search", command = lambda: [master.nextPage(searchPage),showSearchedGames])
        searchButton.pack()
        searchButton.place(x = 10, y =70)
        searchLabel = tk.Label(self, text = "Search (Enter the first letter of the name of the game)")
        text1Entry.place(x=10,y=20)
        searchLabel.place(x=10,y=0)
        cartButton = tk.Button(self, text = "Cart", command = lambda: master.nextPage(cartPage))
        cartButton.pack()
        cartButton.place(x=550,y=20)
         
        '''The show searched games function is what runs when the search button is clicked. This brings up the buttons that begin 
        with the letter that the user types'''

        def showSearchedGames():
            text1String = text1.get()
            for i in range(len(allGamesList)):
                if(len(text1String)>0):
                    if(text1String[0] == allGamesList[i].name[0] or text1String[0] == allGamesList[i].name[0].lower() ):
                        newButton = tk.Button(self,text = allGamesList[i].name)
                        newButton.pack(fill = 'x',padx=7,pady=7)
                        funcs.listOfSearchedGames.append(newButton)
                        
            for j in range(len(funcs.listOfSearchedGames)):
                buttonIteration = funcs.listOfSearchedGames[j]
                buttonIteration.place(x=250,y=130+(j+1)*40)
                buttonIteration.config(command = lambda b = buttonIteration:[gameText(b),master.nextPage(gamePage)])
                        

        searchButton2 = tk.Button(self, text = "Search", command = showSearchedGames)
        searchButton2.place(x=10,y=40)
                
#The cart page is where the use can view what in their car and purchase whatever they have
class cartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="").pack(side="top", fill="x", padx = 300, pady=300)
        bg = PhotoImage(file=r"C:/Users/pjpet/Downloads/OIG4.jpg.png")
        background_label = tk.Label(self, image=bg) 

        background_label.image = bg 

        background_label.place(x=0, y=0, relheight=1, relwidth=1) 
        
        def check():
            funcs.listOfSearchedGames = []
            funcs.gamesAdded = []
            funcs.amountOfGamesInCart = 0
            funcs.totalPrice = 0.0
            funcs.gameClicked = ""
            funcs.listOfLabels = []
        
        mainButton = tk.Button(self, text = "Main Page",width = 25, command = lambda: master.nextPage(MainPage))
        mainButton.place(x=220,y=30)
        cartButton = tk.Button(self, text = "Cart", command = lambda: master.nextPage(cartPage))
        cartButton.pack()
        cartButton.place(x=550,y=20)
        searchButton = tk.Button(self, text = "Click Here", command = lambda: master.nextPage(searchPage))
        searchLabel = tk.Label(self, text = "Search Page")
        searchLabel.place(x=10,y=10)
        searchButton.place(x = 10, y =40)
        total = tk.Label(self,text = "Total Price: $"+ str(funcs.totalPrice), font = ("Arial",20))
        total.place(x=200,y=100)
        totGames = tk.Label(self,text = "Total Games " + str(funcs.amountOfGamesInCart), font = ("Arial",20))
        totGames.place(x=200,y = 70)
        
        checkout = tk.Button(self,text = "Checkout",command = lambda: [check(),master.nextPage(MainPage)])
        checkout.place(x=530,y=60)
        for i in range(len(funcs.gamesAdded)):
            cartGame = tk.Label(self, text = funcs.gamesAdded[i].name, font = ("Arial",15))
            cartGame.place(x=200,y=150+(i+1)*40)
        
'''The game page allows the user to view the game that they click so they can decide if they want 
to add it to their cart'''
class gamePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="").pack(side="top", fill="x", padx = 300, pady=300)
        bg = PhotoImage(file=r"C:/Users/pjpet/Downloads/OIG4.jpg.png")
        background_label = tk.Label(self, image=bg) 

        background_label.image = bg 

        background_label.place(x=0, y=0, relheight=1, relwidth=1) 
        
        '''Add game is the function that occurs when you want to add the game to the cart.
        This method allows the cart to show the price and how many games are in the cart'''
        
        def addGame(game):
            funcs.amountOfGamesInCart +=1
            funcs.totalPrice += game.price
            gameA = tk.Label(self,text = "Game Added!",font = ("Arial",10))
            gameA.place(x=210,y=210)
            funcs.gamesAdded.append(game)
            game.stock -=1
            
        mainButton = tk.Button(self, text = "Main Page",width = 25, command = lambda: master.nextPage(MainPage))
        mainButton.place(x=220,y=30)
        cartButton = tk.Button(self, text = "Cart", command = lambda: master.nextPage(cartPage))
        cartButton.pack()
        cartButton.place(x=550,y=20)
        searchButton = tk.Button(self, text = "Click Here", command = lambda: master.nextPage(searchPage))
        searchLabel = tk.Label(self, text = "Search Page")
        searchLabel.place(x=10,y=10)
        searchButton.place(x = 10, y =40)
        
        for i in range(len(allGamesList)):
            if (funcs.gameClicked == allGamesList[i].name):
                newLabel = tk.Label(self,text = allGamesList[i].name,font = ("Arial",15))
                newLabel.place(x=160,y=120)
                gameDescrip = tk.Label(self, text = allGamesList[i].getDescription(),font = ("Arial",9))
                gameDescrip.place(x=160,y=150)
                priceLabel = tk.Label(self, text = "Price: $"+ str(allGamesList[i].price),font = ("Arial",9))
                priceLabel.place(x=160,y = 180)
                addButton = tk.Button(self,text="Add",command = lambda: addGame(allGamesList[i]))
                addButton.place(x=160,y=210)
                break
            
if __name__ == "__main__":
    app = run()
    app.mainloop()
    
