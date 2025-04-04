from breezypythongui import EasyFrame

class ComputerGuessGame(EasyFrame):
    def __init__(self):
        """Initialize the GUI and game logic."""
        EasyFrame.__init__(self, title="Computer Guessing Game")
        self.setSize(400, 200)

        # Label to display computer's guess
        self.addLabel(text="Computer's Guess:", row=0, column=0)
        self.guessLabel = self.addLabel(text="", row=0, column=1)

        # Buttons for user feedback
        self.smallerButton = self.addButton(text="Too Small", row=1, column=0, command=self.tooSmall)
        self.largerButton = self.addButton(text="Too Large", row=1, column=1, command=self.tooLarge)
        self.correctButton = self.addButton(text="Correct", row=2, column=0, columnspan=2, command=self.correctGuess)

        # New Game Button (initially disabled)
        self.newGameButton = self.addButton(text="New Game", row=3, column=0, columnspan=2, command=self.newGame)
        self.newGameButton["state"] = "disabled"

        # Start the first game
        self.newGame()

    def newGame(self):
        """Start a new game by resetting values."""
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.nextGuess()

        # Enable buttons
        self.smallerButton["state"] = "normal"
        self.largerButton["state"] = "normal"
        self.correctButton["state"] = "normal"
        self.newGameButton["state"] = "disabled"

    def nextGuess(self):
        """Make the computer guess a new number."""
        self.attempts += 1
        self.computerGuess = (self.low + self.high) // 2  # Middle value
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
        
        # Disable buttons after correct guess
        self.smallerButton["state"] = "disabled"
        self.largerButton["state"] = "disabled"
        self.correctButton["state"] = "disabled"
        
        # Enable "New Game" button
        self.newGameButton["state"] = "normal"

# Run the application
if __name__ == "__main__":
    ComputerGuessGame().mainloop()
