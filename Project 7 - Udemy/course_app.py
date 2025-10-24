import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

class CourseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Data Viewer")
        self.root.geometry("1000x600")

        # Title
        tk.Label(root, text="📊 Course Data Viewer", font=("Arial", 18, "bold")).pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Load CSV", command=self.load_csv, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Show Chart", command=self.show_chart, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Filter Paid Courses", command=self.filter_paid, bg="#FF9800", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Reset", command=self.reset_table, bg="#9C27B0", fg="white").grid(row=0, column=3, padx=5)

        # Table (Treeview)
        self.tree = ttk.Treeview(root, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        vsb = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')

        self.df = None  # to hold the dataset

    def load_csv(self):
        """Open a file dialog to select and load a CSV file."""
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.show_data(self.df)
                messagebox.showinfo("Success", "CSV Loaded Successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file:\n{e}")

    def show_data(self, df):
        """Display dataframe in Treeview table."""
        # Clear previous data
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Insert rows
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def filter_paid(self):
        """Filter to show only paid courses."""
        if self.df is not None:
            paid_df = self.df[self.df["is_paid"] == True]
            self.show_data(paid_df)

    def reset_table(self):
        """Reset table to full dataset."""
        if self.df is not None:
            self.show_data(self.df)

    def show_chart(self):
        """Show bar chart of Subscribers by Subject."""
        if self.df is not None:
            chart_df = self.df.groupby("subject")["num_subscribers"].sum().sort_values(ascending=False)
            chart_df.plot(kind="bar", color="skyblue", figsize=(8, 5))
            plt.title("Total Subscribers by Subject")
            plt.xlabel("Subject")
            plt.ylabel("Number of Subscribers")
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showwarning("Warning", "Please load a CSV first.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CourseApp(root)
    root.mainloop()
