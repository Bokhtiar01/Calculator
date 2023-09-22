from tkinter import *


def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text=f'Your BMI: {bmi:.2f}')

    health_condition = get_health_condition(bmi)
    health_condition_label.config(text=f'Health Condition: {health_condition}')


def get_health_condition(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


root = Tk()
root.title("BMI Calculator")
height_label = Label(root, text="Height (m):")
height_label.pack()
height_entry = Entry(root)
height_entry.pack()
