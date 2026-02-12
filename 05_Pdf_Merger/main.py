import tkinter as tk # tkinter is a built-in library for creating graphical user interfaces (GUIs) in Python
from tkinter import filedialog, messagebox # filedialog is used to open file dialogs for selecting files, and messagebox is used to display messages to the user
from pypdf import PdfWriter # pypdf is a library for working with PDF files, and PdfWriter is used to create and write PDF files
import os # os is a built-in library for interacting with the operating system, used here for file path operations


def select_pdfs(): # This function is called when the user clicks the "Select PDF Files" button. It opens a file dialog to select PDF files and adds them to the listbox.
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")]
    )

    if files: # If the user selected files, we loop through them and add them to the listbox if they are not already present.
        for file in files:
            if file not in pdf_list.get(0, tk.END): # Check if the file is already in the listbox to avoid duplicates
                pdf_list.insert(tk.END, file)

        update_merge_button_state()


def remove_selected(): # This function is called when the user clicks the "Remove Selected" button. It removes the selected items from the listbox.
    selected = pdf_list.curselection()
    for index in reversed(selected): # We reverse the selected indices to avoid issues with changing indices while deleting items from the listbox.
        pdf_list.delete(index)

    update_merge_button_state()


def clear_all(): # This function is called when the user clicks the "Clear All" button. It clears all items from the listbox.
    pdf_list.delete(0, tk.END)
    update_merge_button_state()


def update_merge_button_state(): # This function updates the state of the "Merge PDFs" button. It enables the button if there are 2 or more PDF files in the listbox, and disables it otherwise.
    if pdf_list.size() >= 2: # If there are 2 or more items in the listbox, enable the merge button
        merge_button.config(state=tk.NORMAL)
    else:
        merge_button.config(state=tk.DISABLED)


def merge_pdfs(): # This function is called when the user clicks the "Merge PDFs" button. It merges the selected PDF files and saves the merged PDF to a location specified by the user.
    pdfs = list(pdf_list.get(0, tk.END))

    if len(pdfs) < 2: # If there are less than 2 PDF files in the listbox, show an error message and return.
        messagebox.showerror("Error", "Select at least 2 PDF files.")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save merged PDF as"
    )

    if not output_file: # If the user cancels the save dialog, show an error message and return.
        messagebox.showerror("Error", "No output file selected.")
        return

    merger = PdfWriter()

    try: # We loop through the selected PDF files and append them to the PdfWriter object. Then we write the merged PDF to the specified output file.
        for pdf in pdfs: # Loop through each PDF file in the list of selected PDFs
            merger.append(pdf)

        with open(output_file, "wb") as f: # Open the output file in binary write mode and write the merged PDF content to it
            merger.write(f)

        messagebox.showinfo(
            "Success",
            f"PDFs merged successfully!\nSaved as: {os.path.basename(output_file)}"
        )

        clear_all()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    finally:
        merger.close()


# ---------------- UI SETUP ---------------- #
"""
This section sets up the graphical user interface (GUI) using tkinter. It creates the main window, adds labels, buttons, listbox, and scrollbar to allow users to select PDF files, view the selected files, and perform actions like removing selected files, clearing all files, and merging the PDFs. The layout is organized using frames and grid/pack geometry managers for better structure and usability.
"""

root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="PDF Merger Tool", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Select Button
select_button = tk.Button(root, text="Select PDF Files", width=20, command=select_pdfs)
select_button.pack(pady=5)

# Listbox Frame
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

pdf_list = tk.Listbox(list_frame, selectmode=tk.MULTIPLE, width=60, height=10)
pdf_list.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(list_frame, command=pdf_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

pdf_list.config(yscrollcommand=scrollbar.set)

# Control Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

remove_button = tk.Button(button_frame, text="Remove Selected", command=remove_selected)
remove_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all)
clear_button.grid(row=0, column=1, padx=5)

# Merge Button
merge_button = tk.Button(root, text="Merge PDFs", width=20, state=tk.DISABLED, command=merge_pdfs)
merge_button.pack(pady=15)

root.mainloop()