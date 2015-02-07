import Button
from PyMain import PyManMain

window = PyManMain()
button = Button(note="MY BUTTON")
but02 = Button(coords=(50,50))
window.add_render_object(button)
window.add_render_object(but02)
window.MainLoop()
