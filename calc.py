import sys

prompt = "please write an equation (quit or q or Q or QUIT or Quit or escape or ESC to quit) "
on = True
while on:
    equation = input(prompt)
    if equation == "quit" or equation == "q"or "Q" or "QUIT" or "Quit" or "escape" or "ESC":
        on == False

    v = eval(equation)
    print(v)
