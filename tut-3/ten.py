from breezypythongui import EasyFrame

class BouncyBall(EasyFrame):
    def __init__(self):
        """Initialize the GUI components."""
        EasyFrame.__init__(self, title="Bouncy Ball Calculator")
        self.setSize(400, 250)

        # Labels and input fields
        self.addLabel(text="Initial Height (meters):", row=0, column=0)
        self.heightField = self.addFloatField(value="", row=0, column=1, width=10)

        self.addLabel(text="Bounciness Index (0-1):", row=1, column=0)
        self.bouncinessField = self.addFloatField(value="", row=1, column=1, width=10)

        self.addLabel(text="Number of Bounces:", row=2, column=0)
        self.bouncesField = self.addIntegerField(value="", row=2, column=1, width=10)

        # Compute button
        self.addButton(text="Compute Distance", row=3, column=0, columnspan=2, command=self.computeDistance)

        # Output label
        self.resultLabel = self.addLabel(text="Total Distance: 0.0 meters", row=4, column=0, columnspan=2)

    def computeDistance(self):
        """Calculate the total distance traveled by the bouncing ball."""
        try:
            height = self.heightField.getNumber()
            bounciness = self.bouncinessField.getNumber()
            bounces = self.bouncesField.getNumber()

            # Validate inputs
            if height <= 0 or not (0 < bounciness < 1) or bounces < 0:
                raise ValueError

            total_distance = height  # First drop
            for _ in range(bounces):
                height *= bounciness
                total_distance += 2 * height  # Up and down movement

            # Display result
            self.resultLabel["text"] = f"Total Distance: {total_distance:.2f} meters"

        except ValueError:
            self.messageBox(title="ERROR", message="Invalid input! Please enter valid values.")

# Run the application
if __name__ == "__main__":
    BouncyBall().mainloop()
