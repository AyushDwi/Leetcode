class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.cells = {}

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.cells[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.cells.pop(cell, None)

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # Remove the '=' and split by '+'
        expression = formula[1:]
        operands = expression.split('+')
        
        total = 0
        for operand in operands:
            if operand[0].isdigit():
                # It's a number
                total += int(operand)
            else:
                # It's a cell reference
                total += self.cells.get(operand, 0)
        
        return total
