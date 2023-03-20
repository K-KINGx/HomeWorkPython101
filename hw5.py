import tkinter as tk

class NumberMultiplier:
    def __init__(self, master):
        self.master = master
        master.title("ควรดื่มน้ำวันละกี่ลิตร")
        master.geometry('340x130')
        master.option_add("*Font", ("Lamoon", 15))

        # Create the lable
        self.inputweight_label = tk.Label(text="กรอกน้ำหนักของคุณ")
        self.inputweight_label.grid(row=0, column=0, columnspan=1, padx=10, pady=5)

        # Create the input field
        self.number_entry = tk.Entry(master)
        self.number_entry.grid(row=1, column=0, padx=10, pady=5)
        
        # Create the "Calculate" button
        self.calculate_button = tk.Button(master, text="ตรวจสอบ", command=self.calculate)
        self.calculate_button.grid(row=1, column=2, pady=5, padx=10)
        
        # Create the result label
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=1)
        
    def calculate(self):
        try:
            # Get the input number
            number = float(self.number_entry.get())

            # Calculate the result
            result = round(number * 2.2 * 30 / 2)

            # Update the result label
            self.result_label.configure(text=f"ควรกินน้ำวันละ : {result} มิลลิลิตร")
        
        except ValueError:
            # Display an error message if the input is not a number
            self.result_label.configure(text="กรอกตัวเลข")


# Create the tkinter window
root = tk.Tk()

# Create the NumberMultiplier object
app = NumberMultiplier(root)

# Run the tkinter event loop
root.mainloop()
