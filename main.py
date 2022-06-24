from pynput.mouse import Button, Controller

mouse = Controller()

var = mouse.position
print(var)
# result (x_pos, y_pos)

mouse.position = (1500, 200)

mouse.position = (1300, 900)

mouse.move(20, -13)

mouse.move(150, -130)

mouse.move(-150, 130)

mouse.click(Button.right, 1)

mouse.click(Button.left, 1)

mouse.click(Button.left, 2)

mouse.press(Button.right)

mouse.release(Button.right)

mouse.scroll(0, -100)

mouse.scroll(0, 2)

mouse.scroll(0, -200)
