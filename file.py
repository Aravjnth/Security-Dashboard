import tkinter as tk
from tkinter import ttk
import random

class SecurityDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Dashboard")
        self.root.geometry("800x600")

        # Create tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)

        # Create frames for each tab
        self.overview_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.overview_frame, text="Overview")

        self.alerts_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.alerts_frame, text="Alerts")

        self.systems_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.systems_frame, text="Systems")

        # Overview tab
        self.overview_label = ttk.Label(self.overview_frame, text="Overview")
        self.overview_label.pack(pady=20)

        self.system_status_label = ttk.Label(self.overview_frame, text="System Status:")
        self.system_status_label.pack()

        self.system_status_value = ttk.Label(self.overview_frame, text="Online")
        self.system_status_value.pack()

        self.security_score_label = ttk.Label(self.overview_frame, text="Security Score:")
        self.security_score_label.pack()

        self.security_score_value = ttk.Label(self.overview_frame, text="80%")
        self.security_score_value.pack()

        # Alerts tab
        self.alerts_label = ttk.Label(self.alerts_frame, text="Alerts")
        self.alerts_label.pack(pady=20)

        self.alerts_treeview = ttk.Treeview(self.alerts_frame, columns=("Time", "Type", "Description"))
        self.alerts_treeview.pack()

        self.alerts_treeview.heading("#0", text="ID")
        self.alerts_treeview.heading("Time", text="Time")
        self.alerts_treeview.heading("Type", text="Type")
        self.alerts_treeview.heading("Description", text="Description")

        self.alerts_treeview.insert("", "end", values=("1", "2023-02-20 14:30", "Suspicious Login", "User 'john' logged in from unknown location"))
        self.alerts_treeview.insert("", "end", values=("2", "2023-02-20 14:35", "Malware Detection", "Malware detected on system 'erver1'"))

        # Systems tab
        self.systems_label = ttk.Label(self.systems_frame, text="Systems")
        self.systems_label.pack(pady=20)

        self.systems_treeview = ttk.Treeview(self.systems_frame, columns=("Name", "Status", "Last Update"))
        self.systems_treeview.pack()

        self.systems_treeview.heading("#0", text="ID")
        self.systems_treeview.heading("Name", text="Name")
        self.systems_treeview.heading("Status", text="Status")
        self.systems_treeview.heading("Last Update", text="Last Update")

        self.systems_treeview.insert("", "end", values=("1", "server1", "Online", "2023-02-20 14:30"))
        self.systems_treeview.insert("", "end", values=("2", "server2", "Offline", "2023-02-20 14:35"))

    def update_system_status(self):
        status = random.choice(["Online", "Offline"])
        self.system_status_value.config(text=status)
        self.root.after(10000, self.update_system_status)

    def update_security_score(self):
        score = random.randint(0, 100)
        self.security_score_value.config(text=f"{score}%")
        self.root.after(10000, self.update_security_score)

    def update_alerts(self):
        self.alerts_treeview.insert("", "end", values=("3", "2023-02-20 14:40", "Suspicious Activity", "User 'jane' accessed sensitive data"))
        self.root.after(10000, self.update_alerts)

    def update_systems(self):
        self.systems_treeview.insert("", "end", values=("3", "server3", "Online", "2023-02-20 14:45"))
        self.root.after(10000, self.update_systems)

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = SecurityDashboard(root)

    # Update dashboard initially
    dashboard.update_system_status()
    dashboard.update_security_score()
    dashboard.update_alerts()
    dashboard.update_systems()

    root.mainloop()