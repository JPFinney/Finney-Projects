def border_msg(msg):

    count = len(msg) + 2

    dash = "-"*count 

    return "+{dash}+\n| {msg} |\n+{dash}+".format(dash=dash,msg=msg)


user = input("Sup playa?")
print(border_msg(user))

longstring = r"""
   (,_    ,_,    _,)
  /|\`-._(*-*)_.-'/|\
  / | \`-'/ \'-`/ | \
 /__|.-'`-\_/-`'-.|__\
  `                    `
"""
print(longstring)
