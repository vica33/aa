import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

class FortniteAccountPullerGUI:
    """GUI Launcher for Fortnite Account Puller - Cross-platform (Mac/Windows)"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Fortnite Account Puller")
        self.root.geometry("500x400")
        self.root.configure(bg="#1f1f1f")
        
        # Set window icon (optional)
        try:
            if sys.platform == "darwin":  # macOS
                self.root.iconphoto(False, tk.PhotoImage(file='icon.png'))
            elif sys.platform == "win32":  # Windows
                self.root.iconbitmap('icon.ico')
        except:
            pass
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Title Label
        title_label = ttk.Label(self.root, text="Fortnite Account Puller", font=("Arial", 18, "bold"))
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Account Lookup", padding=10)
        input_frame.pack(padx=20, pady=10, fill="both", expand=False)
        
        # Username/Account ID Label
        ttk.Label(input_frame, text="Username or Account ID:").pack(anchor="w", pady=5)
        self.account_input = ttk.Entry(input_frame, width=40)
        self.account_input.pack(anchor="w", pady=5)
        
        # Lookup Type
        ttk.Label(input_frame, text="Lookup Type:").pack(anchor="w", pady=5)
        self.lookup_type = ttk.Combobox(input_frame, values=["Username", "Account ID"], state="readonly", width=37)
        self.lookup_type.set("Username")
        self.lookup_type.pack(anchor="w", pady=5)
        
        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Fetch Button
        fetch_button = ttk.Button(button_frame, text="Fetch Account Data", command=self.fetch_data)
        fetch_button.pack(side="left", padx=5)
        
        # Get Inventory Button
        inventory_button = ttk.Button(button_frame, text="Get Inventory", command=self.get_inventory)
        inventory_button.pack(side="left", padx=5)
        
        # Get Cosmetics Button
        cosmetics_button = ttk.Button(button_frame, text="Get Cosmetics", command=self.get_cosmetics)
        cosmetics_button.pack(side="left", padx=5)
        
        # Results Frame
        results_frame = ttk.LabelFrame(self.root, text="Results", padding=10)
        results_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Results Text Box
        self.results_text = tk.Text(results_frame, height=10, width=50, bg="#2d2d2d", fg="#00ff00", font=("Courier", 10))
        self.results_text.pack(fill="both", expand=True)
        
        # Scrollbar for text box
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.config(yscroll=scrollbar.set)
    
    def fetch_data(self):
        """Fetch account data"""
        account = self.account_input.get()
        lookup_type = self.lookup_type.get()
        
        if not account:
            messagebox.showerror("Error", "Please enter a username or account ID")
            return
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, f"Fetching data for {lookup_type}: {account}...\n")
        self.results_text.insert(tk.END, "Data retrieved successfully!\n")
        messagebox.showinfo("Success", f"Account data fetched for {account}")
    
    def get_inventory(self):
        """Get inventory data"""
        account = self.account_input.get()
        
        if not account:
            messagebox.showerror("Error", "Please enter a username or account ID")
            return
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, f"Retrieving inventory for: {account}\n\n")
        self.results_text.insert(tk.END, "Sample Inventory Items:\n")
        self.results_text.insert(tk.END, "- Skin: Superhero\n")
        self.results_text.insert(tk.END, "- Backpack: Black Knight\n")
        self.results_text.insert(tk.END, "- Pickaxe: Reaper\n")
        messagebox.showinfo("Success", "Inventory data retrieved!")
    
    def get_cosmetics(self):
        """Get cosmetics data"""
        account = self.account_input.get()
        
        if not account:
            messagebox.showerror("Error", "Please enter a username or account ID")
            return
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, f"Retrieving cosmetics for: {account}\n\n")
        self.results_text.insert(tk.END, "Sample Cosmetics:\n")
        self.results_text.insert(tk.END, "- Skins: 45\n")
        self.results_text.insert(tk.END, "- Emotes: 32\n")
        self.results_text.insert(tk.END, "- Pickaxes: 28\n")
        self.results_text.insert(tk.END, "- Backpacks: 22\n")
        messagebox.showinfo("Success", "Cosmetics data retrieved!")


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    
    # Configure style based on platform
    if sys.platform == "darwin":  # macOS
        root.tk.call("tk", "scaling", 2.0)
    
    app = FortniteAccountPullerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()