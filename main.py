import random, string, datetime
import tkinter as tk

# Generate a password based on inputs
def generate_password():
	# Get values from UI
	password_length = int(length_entry.get())
	num_symbols = int(num_symbols_entry.get())
	allowed_symbols_input = allowed_symbols_entry.get()

	if allowed_symbols_input != '':
		allowed_symbols = allowed_symbols_entry.get()
	else:
		allowed_symbols = '!@#$%^&*()_+'

	# Generate password
	password_characters = string.ascii_letters + string.digits + allowed_symbols
	password_characters = ''.join(random.choice(password_characters) for i in range(password_length - num_symbols))
	password_characters += ''.join(random.choice(allowed_symbols) for i in range(num_symbols))

	# Display password in UI
	password_entry.configure(state='normal')
	password_entry.delete(0, tk.END)
	password_entry.insert(0, password_characters)
	password_entry.configure(state='readonly')

# Copy password to clipboard
def copy_password():
	password = password_entry.get()
	window.clipboard_clear()
	window.clipboard_append(password)

# Initialise UI window
def initialise_ui():
	global length_entry, num_symbols_entry, allowed_symbols_entry, password_entry, window

	window = tk.Tk()
	window.title('Password Generator')
	window.iconbitmap('favicon.ico')

	# Width for all entries
	entry_width = 14
	output_width = 35

	length_label = tk.Label(window, text='Length:')
	length_label.grid(column=0, row=0, padx=10, pady=10)

	length_entry = tk.Entry(window, width=entry_width)
	length_entry.grid(column=1, row=0, padx=10, pady=10)

	num_symbols_label = tk.Label(window, text='Number of Symbols:')
	num_symbols_label.grid(column=0, row=1, padx=10, pady=10)

	num_symbols_entry = tk.Entry(window, width=entry_width)
	num_symbols_entry.grid(column=1, row=1, padx=10, pady=10)

	allowed_symbols_label = tk.Label(window, text='Allowed symbols: (optional)')
	allowed_symbols_label.grid(column=0, row=2, padx=10, pady=10)

	allowed_symbols_entry = tk.Entry(window, width=entry_width)
	allowed_symbols_entry.grid(column=1, row=2, padx=10, pady=10)

	generate_button = tk.Button(window, text='Generate', command=generate_password)
	generate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

	password_entry = tk.Entry(window, width=output_width, state='readonly')
	password_entry.grid(column=0, row=4, columnspan=2, padx=10, pady=20)

	password_context_menu = tk.Menu(window, tearoff=0)
	password_context_menu.add_command(label='Copy', command=copy_password)

	def show_password_context_menu(event):
		password_context_menu.tk_popup(event.x_root, event.y_root)

	password_entry.bind('<Button-3>', show_password_context_menu)

	window.resizable(False,False)
	window.mainloop()


if __name__ == '__main__':
	initialise_ui()
