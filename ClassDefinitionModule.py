class fooditems():
    # Initializer
    def __init__(self, food, pounds):
        # Setting initial values -- hidden parameter
        self._food = food  # As per input parameter
        self._pounds = pounds  # As per input parameter
        self._standard_price = 0
        self._calcprice = 0
        self.PriceList()

    # Private method storing item list and price per pound (from table)
    def PriceList(self):
        if self._food == 'Dry Cured Iberian Ham':
            self._standard_price = 177.80
        elif self._food == 'Wagyu Steaks':
            self._standard_price = 450.00
        elif self._food == 'Matsutake Mushrooms':
            self._standard_price = 272.00
        elif self._food == 'Kopi Luwak Coffee':
            self._standard_price = 306.50   
        elif self._food == 'Moose Cheese':
            self._standard_price = 487.20 
        elif self._food == 'White Truffles':
            self._standard_price = 3600.00
        elif self._food == 'Blue Fin Tuna':
            self._standard_price = 3603.00
        elif self._food == 'Le Bonnotte Potatoes':
            self._standard_price = 270.81
        else:
            self._standard_price = 0

    # Accessor
    def cost(self):
        return self._standard_price * self._pounds
