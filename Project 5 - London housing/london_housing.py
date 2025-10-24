import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Load CSV Once ----------------
CSV_FILE = "london.csv"  # Replace with your CSV path
df = pd.read_csv(CSV_FILE)

# ---------------- Tkinter App ----------------
class RealEstateApp:
    def __init__(self, root, df):
        self.root = root
        self.df = df
        self.root.title("Real Estate Data Operations")
        self.root.geometry("900x600")

        tk.Label(root, text="🏘️ Real Estate Data Operations", font=("Arial", 18, "bold")).pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Show Summary", command=self.show_summary,
                  bg="#2196F3", fg="white", width=20).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Top 5 Areas by Houses Sold", command=self.top5_areas,
                  bg="#FF9800", fg="white", width=20).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Crime vs Price Scatter", command=self.crime_vs_price,
                  bg="#9C27B0", fg="white", width=20).grid(row=0, column=2, padx=5)

        # Table (Treeview)
        self.tree = ttk.Treeview(root, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        vsb = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')

        self.show_data(df)

    def show_data(self, df):
        """Display DataFrame in Treeview table"""
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

    # ---------------- Operations ----------------
    def show_summary(self):
        """Show summary statistics of numeric columns"""
        summary = self.df.describe()
        messagebox.showinfo("Summary Statistics", str(summary))

    def top5_areas(self):
        """Plot Top 5 Areas by Houses Sold"""
        top5 = self.df.groupby("area")["houses_sold"].sum().sort_values(ascending=False).head(5)
        top5.plot(kind="bar", color="skyblue", figsize=(7,5))
        plt.title("Top 5 Areas by Houses Sold")
        plt.xlabel("Area")
        plt.ylabel("Houses Sold")
        plt.tight_layout()
        plt.show()

    def crime_vs_price(self):
        """Scatter plot: no_of_crimes vs average_price"""
        plt.figure(figsize=(8,5))
        plt.scatter(self.df["no_of_crimes"], self.df["average_price"], color="orange")
        plt.title("Crime vs Average Price")
        plt.xlabel("Number of Crimes")
        plt.ylabel("Average Price")
        plt.tight_layout()
        plt.show()


# ---------------- Run App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RealEstateApp(root, df)
    root.mainloop()
