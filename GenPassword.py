from hashlib import sha256
from tkinter import *
from tkinter.ttk import *

known_sites = sorted([
	"",
	"github.com",
	"bitbucket.org",
	"steam",
	"gmail.com",
	"google.com",
	"reddit.com",
	"linode.com",
	"discordapp.com",
	"rekt.live",
	"www.twitch.tv",
	"blockchain.com"
])


def gen_password(host, password):
	return sha256('{}@{}'.format(password, host).encode('utf-8')).hexdigest()


def main():
	window = Tk()
	window.title("GenPASS")
	combo = Combobox(window,  width=80, justify=LEFT)
	hash_value = StringVar()
	pass_value = StringVar()

	def on_close():
		window.quit()

	def on_values_changed(event):
		hv = gen_password(combo.get(), pass_value.get())
		hash_value.set(hv)
		return True

	def on_copy():
		window.clipboard_clear()
		window.clipboard_append(hash_value.get())

	menu = Menu(window)
	new_item = Menu(menu)
	new_item.add_command(label='Exit', command=on_close)
	menu.add_cascade(label='File', menu=new_item)
	window.config(menu=menu)

	# Row 0
	lbl = Label(window, text="Host", font=("Helvetica", 14), width=14, justify=RIGHT)
	lbl.grid(column=0, row=0)

	combo.bind('<<ComboboxSelected>>', on_values_changed)
	combo.bind('<KeyRelease>', on_values_changed)
	combo['values'] = known_sites
	combo.current(0)
	combo.grid(column=1, row=0)

	# Row 1
	lbl_p = Label(window, text="Password", font=("Helvetica", 14), width=14, justify=RIGHT)
	lbl_p.grid(column=0, row=1)
	txt = Entry(window, width=80, justify=LEFT, textvariable=pass_value)
	txt.grid(column=1, row=1)
	txt.bind('<KeyRelease>', on_values_changed)

	# Row 2
	lbl_h = Label(window, text="Generated Hash", font=("Helvetica", 14), width=14, justify=RIGHT)
	lbl_h.grid(column=0, row=2)

	h = Entry(window, textvariable=hash_value, width=80, justify=LEFT)
	h.grid(column=1, row=2)

	# Row 3
	btn_copy = Button(window, text="Copy", width=14, command=on_copy)
	btn_copy.grid(column=0, row=3)

	window.mainloop()


if __name__ == "__main__":
	main()
