import tkinter as tk
import os

def show_current_pdf(listbox):
    listbox.delete(0, tk.END)
    all_files = os.listdir()
    
    for file in all_files:
        if file.endswith(".pdf"):
            listbox.insert(tk.END, file)

def show_main_page():
    main_frame.pack(fill='both', expand=True)

def show_second_page():
    main_frame.pack_forget()  # Hide the main frame
    second_frame.pack(fill='both', expand=True)  # Show the second frame

def show_upload_image_page():
    second_frame.pack_forget()  # Hide the second frame
    upload_image_frame.pack(fill='both', expand=True)  # Show the upload image frame

def simulate_camera_capture():
    # Placeholder for actual camera capture functionality
    print("Simulating Camera Capture")

def back_to_second_page():
    upload_image_frame.pack_forget()  # Hide the upload image frame
    show_second_page()  # Show the second frame

def show_upload_pdf_page():
    second_frame.pack_forget()  # Hide the second frame
    upload_pdf_frame.pack(fill='both', expand=True)  # Show the upload PDF frame
    # Update listbox with files in current directory
    update_file_list()

def update_file_list():
    file_list.delete(0, tk.END)  # Clear existing items
    files = os.listdir()
    for file in files:
        file_list.insert(tk.END, file)

def back_to_second_page_from_pdf():
    upload_pdf_frame.pack_forget()  # Hide the upload PDF frame
    show_second_page()  # Show the second frame

# Create the main window
root = tk.Tk()
root.title("JPG to PNG Converter")

# Create the main frame (first page)
main_frame = tk.Frame(root)
start_button = tk.Button(main_frame, text="Start", command=show_second_page)
start_button.pack(pady=20)
main_frame.pack(fill='both', expand=True)

# Create the second frame (second page)
second_frame = tk.Frame(root)
upload_image_button = tk.Button(second_frame, text="Upload Image", command=show_upload_image_page)
upload_pdf_button = tk.Button(second_frame, text="Open PDF", command=show_upload_pdf_page)
upload_image_button.pack(pady=10)
upload_pdf_button.pack(pady=10)

# Create the upload image frame
upload_image_frame = tk.Frame(root)
camera_button = tk.Button(upload_image_frame, text="Camera", command=simulate_camera_capture)
back_button_upload_image = tk.Button(upload_image_frame, text="Back", command=back_to_second_page)
camera_button.pack(pady=10)
back_button_upload_image.pack(pady=10)

# Create the upload PDF frame
upload_pdf_frame = tk.Frame(root)
file_list = tk.Listbox(upload_pdf_frame, selectmode=tk.SINGLE)
file_list_scroll = tk.Scrollbar(upload_pdf_frame, orient=tk.VERTICAL, command=file_list.yview)
file_list.config(yscrollcommand=file_list_scroll.set)
file_list_scroll.pack(side=tk.RIGHT, fill=tk.Y)
file_list.pack(fill='both', expand=True)
show_current_pdf(file_list)
back_button_upload_pdf = tk.Button(upload_pdf_frame, text="Back", command=back_to_second_page_from_pdf)
back_button_upload_pdf.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
