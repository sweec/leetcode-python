class Solution:
    decs = [3000, 2000, 1000]+range(900, 0, -100)+range(90, 0, -10)+range(9, 0, -1)
    romans = ['MMM', 'MM', 'M',
              'CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C',
              'XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X',
              'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    offsets = [3]*3+[12]*9+[21]*9+[30]*9
    
    # @return a string
    def intToRoman(self, num):
        roman = []
        offset = 0
        size = len(self.decs)
        while num > 0:
            for i in range(offset, size):
                if num >= self.decs[i]:
                    roman.append(self.romans[i])
                    num -= self.decs[i]
                    offset = self.offsets[i]
                    break;
        return ''.join(roman)