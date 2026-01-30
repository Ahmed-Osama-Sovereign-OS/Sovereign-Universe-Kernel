import customtkinter as ctk
import threading, time
from kernel_v5 import SovereignKernel
from security_v5 import UniverseSecurity

class SovereignMonsterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.kernel = SovereignKernel()
        self.security = UniverseSecurity()
        
        self.title("SOVEREIGN OS v5.5 - THE FINAL MONSTER")
        self.geometry("1200x900")
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#010101")

        # Header
        self.header = ctk.CTkLabel(self, text="⚡ SOVEREIGN UNIVERSE KERNEL ⚡", 
                                   font=("Orbitron", 40, "bold"), text_color="#00FF41")
        self.header.pack(pady=20)

        # Terminal Box
        self.terminal = ctk.CTkTextbox(self, width=1100, height=550, fg_color="#050505", 
                                       text_color="#00FF41", font=("Consolas", 15), 
                                       border_color="#00FF41", border_width=1)
        self.terminal.pack(pady=10)

        # Buttons Panel
        self.panel = ctk.CTkFrame(self, fg_color="#0a0a0a")
        self.panel.pack(pady=20, fill="x", padx=50)

        ctk.CTkButton(self.panel, text="KERNEL BYPASS", command=self.run_bypass, fg_color="#00FF41", text_color="black").grid(row=0, column=0, padx=20, pady=20)
        ctk.CTkButton(self.panel, text="STEALTH SHIELD", command=self.run_shield, fg_color="#FF4100").grid(row=0, column=1, padx=20, pady=20)
        ctk.CTkButton(self.panel, text="GENERATE UNIVERSE KEY", command=self.run_key, fg_color="#00D4FF", text_color="black").grid(row=0, column=2, padx=20, pady=20)

        threading.Thread(target=self.radar_loop, daemon=True).start()

    def run_bypass(self): self.terminal.insert("end", f"\n>>> [SYSTEM]: {self.kernel.seize_kernel_control()}")
    def run_shield(self): self.terminal.insert("end", f"\n>>> [SECURITY]: {self.security.activate_stealth_mode()}")
    def run_key(self): 
        key = self.security.generate_quantum_key()
        self.terminal.insert("end", f"\n>>> [KEY]: {key[:64]}...")

    def radar_loop(self):
        while True:
            p = self.kernel.get_hardware_pulse()
            self.terminal.delete("1.0", "end")
            log = f"--- SOVEREIGN OS RADAR v5.5 ---\n"
            log += f"STABILITY: {p['stability']}% | RAM: {p['ram']}% | GPU: {p['gpu']}°C\n"
            log += f"SECURITY SHIELD: {self.security.shield_status}\n"
            log += "="*60 + "\n"
            for i, v in enumerate(p['cores']):
                bar = "█" * int(v/4) + "░" * (25 - int(v/4))
                log += f"CORE {i:02} : [{bar}] {v}%\n"
            self.terminal.insert("1.0", log)
            time.sleep(0.6)

if __name__ == "__main__":
    app = SovereignMonsterApp()
    app.mainloop()
