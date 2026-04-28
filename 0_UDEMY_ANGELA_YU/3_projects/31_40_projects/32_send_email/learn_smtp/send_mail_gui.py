from tkinter import *
from tkinter import messagebox
import smtplib
import random

#=== CONSTANT VALUE ====#
HOST_MAIL = "smtp.gmail.com"
MY_EMAIL = "sams.seul@gmail.com"
MY_PASSWORD = "ugji mwpp xaig kacr"
PATH = r"0_UDEMY_ANGELA_YU/3_projects/31_40_projects/32_send_email/quotes.txt"

def send_mail():
    get_from = from_entry.get()
    get_to = to_entry.get()
    get_subject = subject_entry.get()
    get_message = message_entry.get()
    
    with open(PATH, encoding='utf-8', errors="error") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    
    # check empty
    if len(get_to) == 0:
        messagebox.showinfo(title="Empty", message="Please fill To input field.")
    else:
        if len(get_subject) == 0:
            get_subject = "No Subject"
        if len(get_message) == 0:
            get_message = quote
        
        with smtplib.SMTP(HOST_MAIL) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWORD)
            conn.sendmail(
                from_addr=get_from,
                to_addrs=get_to,
                msg=f"Subject:{get_subject}\n\n{get_message.encode(encoding="ascii", errors="replace")}"
            )
            
            messagebox.showinfo(title="Successful", message=f"To:{get_to}\nSubject:{get_subject}\nMessage Successfully Send")
        
        # Clear input filed
        to_entry.delete(0,END)
        subject_entry.delete(0,END)
        message_entry.delete(0,END)

#===== UI ====#
display = Tk()
display.config(padx=50, pady=50)
display.title(string="Send mail by smtplib")

from_label = Label(text="From")
from_label.grid(row=0, column=0)
to_label = Label(text="To")
to_label.grid(row=1, column=0)
subject_label = Label(text="Subject")
subject_label.grid(row=2, column=0)
message_label = Label(text="Message")
message_label.grid(row=3, column=0)

from_entry = Entry()
from_entry.grid(row=0, column=1)
from_entry.insert(index=0, string=MY_EMAIL)
to_entry = Entry()
to_entry.grid(row=1, column=1)
subject_entry = Entry()
subject_entry.grid(row=2, column=1)
message_entry = Entry()
message_entry.grid(row=3, column=1)

send_mail_btn = Button(text="Send Mail", command=send_mail)
send_mail_btn.grid(row=4, column=1)





display.mainloop()

