import tkinter as tk


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x650")
        self.root.config(padx=30, pady=30, bg="#f4f4f4")

        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. Programming in Python "
            "is both rewarding and fun. Building desktop applications with Tkinter "
            "helps sharpen your logic and user interface design skills."
        )

        self.time_left = 60
        self.timer_running = False
        self.timer_id = None

        # Title Label
        self.title_label = tk.Label(
            root, text="Python Typing Speed Test",
            font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333333"
        )
        self.title_label.pack(pady=10)

        # Timer Label
        self.timer_label = tk.Label(
            root, text="Time Left: 60s",
            font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#E91E63"
        )
        self.timer_label.pack(pady=5)

        # Sample Text Display Box
        self.text_display = tk.Text(
            root, height=5, width=70, font=("Arial", 13),
            wrap=tk.WORD, bd=1, relief=tk.SOLID
        )
        self.text_display.insert(tk.END, self.sample_text)
        self.text_display.config(state=tk.DISABLED)  # Make it read-only
        self.text_display.pack(pady=10)

        # User Input Box
        self.user_input = tk.Text(
            root, height=5, width=70, font=("Arial", 13),
            wrap=tk.WORD, bd=1, relief=tk.SOLID
        )
        self.user_input.pack(pady=10)
        self.user_input.config(state=tk.DISABLED)  # Disabled until start is clicked

        # Controls Frame
        self.control_frame = tk.Frame(root, bg="#f4f4f4")
        self.control_frame.pack(pady=10)

        # Start Button
        self.start_btn = tk.Button(
            self.control_frame, text="▶ Start Test",
            font=("Arial", 12, "bold"), command=self.start_test
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        # Reset Button
        self.reset_btn = tk.Button(
            self.control_frame, text="🔄 Reset",
            font=("Arial", 12, "bold"), command=self.reset_test
        )
        self.reset_btn.grid(row=0, column=1, padx=10)

        # Result Label
        self.result_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"),
            bg="#f4f4f4", fg="#2196F3"
        )
        self.result_label.pack(pady=10)

    def start_test(self):
        if not self.timer_running:
            self.time_left = 60
            self.timer_running = True
            self.user_input.config(state=tk.NORMAL)
            self.user_input.delete("1.0", tk.END)
            self.user_input.focus()
            self.result_label.config(text="")
            self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            self.timer_running = False
            self.timer_label.config(text="Time's up!")
            self.user_input.config(state=tk.DISABLED)
            self.calculate_wpm()

    def calculate_wpm(self):
        typed_text = self.user_input.get("1.0", tk.END).strip()
        words = typed_text.split()
        word_count = len(words)

        # Words Per Minute calculation (60 seconds = 1 minute)
        wpm = word_count

        # Accuracy calculation compared against the sample text
        sample_words = self.sample_text.split()
        correct_words = sum(1 for a, b in zip(words, sample_words) if a == b)
        accuracy = (correct_words / len(sample_words)) * 100 if sample_words else 0

        self.result_label.config(
            text=f"Test Finished!\nSpeed: {wpm} WPM | Accuracy: {accuracy:.1f}%"
        )

    def reset_test(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_running = False
        self.time_left = 60
        self.timer_label.config(text="Time Left: 60s")
        self.user_input.delete("1.0", tk.END)
        self.user_input.config(state=tk.DISABLED)
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()