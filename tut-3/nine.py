from breezypythongui import EasyFrame

class ComputerGuessGame(EasyFrame):
    def __init__(self):
        """Initialize the GUI and game logic."""
        EasyFrame.__init__(self, title="Computer Guessing Game")
        self.setSize(400, 200)

        
        self.addLabel(text="Computer's Guess:", row=0, column=0)
        self.guessLabel = self.addLabel(text="", row=0, column=1)

        
        self.smallerButton = self.addButton(text="Too Small", row=1, column=0, command=self.tooSmall)
        self.largerButton = self.addButton(text="Too Large", row=1, column=1, command=self.tooLarge)
        self.correctButton = self.addButton(text="Correct", row=2, column=0, columnspan=2, command=self.correctGuess)

        
        self.newGameButton = self.addButton(text="New Game", row=3, column=0, columnspan=2, command=self.newGame)
        self.newGameButton["state"] = "disabled"

        
        self.newGame()

    def newGame(self):
        """Start a new game by resetting values."""
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.nextGuess()

        
        self.smallerButton["state"] = "normal"
        self.largerButton["state"] = "normal"
        self.correctButton["state"] = "normal"
        self.newGameButton["state"] = "disabled"

    def nextGuess(self):
        """Make the computer guess a new number."""
        self.attempts += 1
        self.computerGuess = (self.low + self.high) // 2  
        self.guessLabel["text"] = str(self.computerGuess)

    def tooSmall(self):
        """Adjust range when the guess is too small."""
        self.low = self.computerGuess + 1
        self.nextGuess()

    def tooLarge(self):
        """Adjust range when the guess is too large."""
        self.high = self.computerGuess - 1
        self.nextGuess()

    def correctGuess(self):
        """Handle the case where the computer guessed correctly."""
        self.guessLabel["text"] = f"🎉 Got it in {self.attempts} tries!"
        
        
        self.smallerButton["state"] = "disabled"
        self.largerButton["state"] = "disabled"
        self.correctButton["state"] = "disabled"
        
        
        self.newGameButton["state"] = "normal"


if __name__ == "__main__":
    ComputerGuessGame().mainloop()
