import tkinter as tk

# Hauptfenster erstellen und Größe festlegen
root = tk.Tk()
root.title("Raketensteuerung")
root.geometry("400x400")

# Canvas hinzufügen, um die Rakete darzustellen
canvas = tk.Canvas(root, width=400, height=300, bg="lightblue")
canvas.pack()

# Eine einfache Rakete als Dreieck zeichnen
rocket = canvas.create_polygon(190, 250, 210, 250, 200, 220, fill="red")

# Funktion, um die Rakete zu starten
def start_rocket():
    try:
        thrust = float(thrust_entry.get())
        weight = float(weight_entry.get())
        gravity = 9.81  # Erdbeschleunigung in m/s²
        weight_force = weight * gravity
        
        if thrust > weight_force:
            # Wenn der Schub größer als die Gewichtskraft ist, bewege die Rakete nach oben
            canvas.move(rocket, 0, -50)
        else:
            print("Schub ist nicht ausreichend, um abzuheben.")
    except ValueError:
        print("Bitte gültige Zahlen eingeben.")

# Labels und Eingabefelder hinzufügen
tk.Label(root, text="Schub (Thrust in N):").pack()
thrust_entry = tk.Entry(root)
thrust_entry.pack()

tk.Label(root, text="Gewicht (Weight in kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Start-Button mit der neuen Funktion verknüpfen
start_button = tk.Button(root, text="Start", command=start_rocket)
start_button.pack()

# Hauptloop starten
root.mainloop()
