from tkinter import Tk, ttk, StringVar, messagebox
from tkinter.filedialog import askopenfilename
import os
from encode_file import encode_file
from decode_file import decode_file

def select_file(filename):
    filetypes = (
        ('Text files', '*.TXT'),
        ('All files', '*.*'),
    )

    filename.set(askopenfilename(
        filetypes=filetypes))

def encode(filename):
    file_to_encode = filename.get()
    print("Encode - ", file_to_encode)
    if os.path.exists(file_to_encode):
        encoded_file = encode_file(file_to_encode)
        messagebox.showinfo("Completed", "Encoded file available at {}".format(encoded_file))
    else:
        messagebox.showwarning("Error", "Selected file does not exist.")


def decode(filename):
    file_to_decode = filename.get()
    print("Decode - ", filename.get())
    if os.path.exists(file_to_decode):
        decoded_file = decode_file(file_to_decode)
        messagebox.showinfo("Completed", "Decoded file available at {}".format(decoded_file))
    else:
        messagebox.showwarning("Error", "Selected file does not exist.")

def create_window():
    root = Tk()
    root.title("File Compressor")
    root.geometry("500x150")

    encode_file = StringVar(root, "")
    decode_file = StringVar(root, "")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

    encoder_frame = create_frame(notebook, encode_file, "Encode", encode)
    decoder_frame = create_frame(notebook, decode_file, "Decode", decode)
    # add frames to notebook

    notebook.add(encoder_frame, text='Encoder')
    notebook.add(decoder_frame, text='Decoder')
    return root


def create_frame(root, filename, action_text, command_to_execute):
    frame = ttk.Frame(root, width=400, height=200)
    frame.pack(fill='both', expand=True)
    file_label = ttk.Label(frame, text="Select File")
    file_label.grid(column=0, row=0, pady=10)
    text_select = ttk.Entry(frame, textvariable=filename)
    text_select.grid(column=1, row=0)
    browse_button = ttk.Button(frame, text="Browse", command=lambda : select_file(filename))
    browse_button.grid(column=2, row=0)
    action_button = ttk.Button(frame, text=action_text, command=lambda : command_to_execute(filename))
    action_button.grid(column=2, row=1)
    return frame


root = create_window()

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)
root.mainloop()
