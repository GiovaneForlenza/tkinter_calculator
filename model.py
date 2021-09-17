class Model:
    def __init__(self):
        self.value = ''
        self.operator = ''
        self.prev_value = ''

    def calculate(self, caption):
        if caption == 'C':
            self.value = ''
            self.operator = ''
            self.prev_value = ''

        elif caption == '+/-':
            # self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
            value = float(self.value)
            value *= -1
            self.value = str(value)

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)

        elif caption == '=':
            value = self._evaluate()
            if '.0' in str(value):
                self.value = int(value)
            self.value = str(value)

        else:
            if self.value:
                self.operator = caption
                self.prev_value = self.value
                self.value = ''


        return self.value


    def _evaluate(self):
        return eval(self.prev_value + self.operator + self.value)