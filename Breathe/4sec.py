import tkinter as tk
from tkinter import ttk

class BreathingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Breathing Exercise")
        self.root.geometry("500x400")
        self.root.configure(bg="#1a1a2e")
        
        # Center the window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Variables
        self.current_count = 1
        self.countdown = 4
        self.is_running = False
        self.colors = ["#ff6b6b", "#4ecdc4", "#45b7d1", "#f9ca24"]
        self.instructions = [
            "Inhale (Nose)",
            "Hold",
            "Exhale (Mouth)",
            "Hold"
        ]
        
        # Title
        self.title_label = tk.Label(
            root,
            text="Breathing Exercise",
            font=("Helvetica", 24, "bold"),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        self.title_label.pack(pady=20)
        
        # Instruction
        self.instruction_label = tk.Label(
            root,
            text="Inhale (Nose)",
            font=("Helvetica", 16, "bold"),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        self.instruction_label.pack(pady=15)
        
        # Counter display
        self.counter_frame = tk.Frame(root, bg="#1a1a2e")
        self.counter_frame.pack(expand=True)
        
        self.counter_label = tk.Label(
            self.counter_frame,
            text="4",
            font=("Helvetica", 120, "bold"),
            bg="#1a1a2e",
            fg=self.colors[0],
            width=3,
            height=1
        )
        self.counter_label.pack()
        
        # Button frame
        self.button_frame = tk.Frame(root, bg="#1a1a2e")
        self.button_frame.pack(pady=20)
        
        # Start/Stop button
        self.toggle_button = tk.Button(
            self.button_frame,
            text="Start",
            font=("Helvetica", 14, "bold"),
            bg="#4ecdc4",
            fg="#1a1a2e",
            activebackground="#45b7d1",
            activeforeground="#1a1a2e",
            border=0,
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.toggle_exercise
        )
        self.toggle_button.pack(side=tk.LEFT, padx=10)
        
        # Reset button
        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset",
            font=("Helvetica", 14, "bold"),
            bg="#95a5a6",
            fg="#1a1a2e",
            activebackground="#7f8c8d",
            activeforeground="#1a1a2e",
            border=0,
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.reset_counter
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
    
    def toggle_exercise(self):
        if self.is_running:
            self.is_running = False
            self.toggle_button.config(text="Start", bg="#4ecdc4")
        else:
            self.is_running = True
            self.toggle_button.config(text="Stop", bg="#ff6b6b")
            self.count()
    
    def count(self):
        if self.is_running:
            # Update counter and instruction
            self.counter_label.config(
                text=str(self.countdown),
                fg=self.colors[self.current_count - 1]
            )
            self.instruction_label.config(
                text=self.instructions[self.current_count - 1]
            )
            
            # Decrement countdown
            self.countdown -= 1
            
            # If countdown reaches 0, move to next phase
            if self.countdown <= 0:
                self.countdown = 4
                self.current_count += 1
                if self.current_count > 4:
                    self.current_count = 1
            
            # Schedule next update (1 second = 1000ms)
            self.root.after(1000, self.count)
    
    def reset_counter(self):
        self.is_running = False
        self.current_count = 1
        self.countdown = 4
        self.counter_label.config(text="4", fg=self.colors[0])
        self.instruction_label.config(text=self.instructions[0])
        self.toggle_button.config(text="Start", bg="#4ecdc4")

if __name__ == "__main__":
    root = tk.Tk()
    app = BreathingApp(root)
    root.mainloop()
