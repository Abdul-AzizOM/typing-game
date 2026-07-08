from nicegui import ui
import time
import random
import asyncio

#list of paraghraphs
from paragraphs import paragraphs




class Round(ui.label):
    def __init__(self):
        super().__init__()
        self.state = False
        self.Time = 0
        self.wpw = 0

    def update_time(self):
        self.Time += 1
        self.set_text(str(self.Time))

    def start_round(self):
        if self.state:
            return
        self.state = True
        ui.timer(interval=1,callback=self.update_time)



thee_round = Round()


ui.button('START!', on_click=thee_round.start_round)




ui.run()


