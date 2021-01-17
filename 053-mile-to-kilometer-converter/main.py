import tkinter as tk

window = tk.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=40)

def calculate_km():
    km_value = round(int(input_mile.get()) * 1.6, 2)
    #print(x)
    output_km.config(text=km_value)

input_mile = tk.Entry(width=10)
input_mile.grid(row=0, column=1)


label1 = tk.Label(text="is equal to")
label1.grid(row=1, column=0)
label1.config(pady=5)

output_km = tk.Label()
output_km.grid(row=1, column=1)

label1 = tk.Label(text="Km")
label1.grid(row=1, column=2)

calculate = tk.Button(text="Calculate", command=calculate_km)
calculate.grid(row=2, column=1)
calculate.config(pady=5)


window.mainloop()
