from sense_hat import SenseHat

class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)
    BLUE = (0, 0, 255)  # Define BLUE attribute

    def __init__(self, complexion=YELLOW):
        """
        Add complexion parameter with a default value of Smiley.YELLOW
        Allows flexibility to specify a different complexion colour
        while having a default value if no colour is provided
        """
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()

        # a new instance variable called my_complexion
        self.my_complexion = complexion

        Y = self.my_complexion  # replaces self.YELLOW
        O = self.BLANK
        self.pixels = [
            O, Y, Y, Y, Y, Y, Y, O,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            O, Y, Y, Y, Y, Y, Y, O,
        ]

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)

    # a method that updates the pixels attribute by replacing all non-blank pixels with the specified color.
    # The blank pixels remain unchanged.
    def complexion(self, colour):
        """
        Set the complexion (colour) of the smiley face.

        :param colour: Tuple representing the RGB colour value
        """
        colour = [colour if pixel != self.BLANK else self.BLANK for pixel in self.pixels]
        return self.my_complexion

