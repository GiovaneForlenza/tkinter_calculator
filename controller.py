from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()

    def main(self):
        self.view.main()



    def on_btn_click(self, caption):
        print(f'Button {caption} pressed')

if __name__ == '__main__':
    agenda = Controller()
    agenda.main()
