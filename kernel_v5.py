import psutil, platform, ctypes, os, GPUtil

class SovereignKernel:
    def __init__(self):
        self.os_type = platform.system()

    def get_hardware_pulse(self):
        """تحليل نبض العتاد الحقيقي"""
        cpu_cores = psutil.cpu_percent(percpu=True)
        mem = psutil.virtual_memory()
        gpus = GPUtil.getGPUs()
        # حساب "معامل الانتروبيا" الفيزيائي
        entropy = sum([abs(x - 50) for x in cpu_cores]) / len(cpu_cores)
        return {
            "cores": cpu_cores,
            "ram": mem.percent,
            "gpu": gpus[0].temperature if gpus else "N/A",
            "stability": round(100 - entropy, 2)
        }

    def seize_kernel_control(self):
        """السيطرة على أولوية النظام (Real-Time Priority)"""
        try:
            p = psutil.Process(os.getpid())
            if self.os_type == "Windows":
                ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00000080)
            else:
                p.nice(-20)
            return "SUCCESS: KERNEL PRIORITY SEIZED"
        except:
            return "ERROR: ADMIN PRIVILEGES REQUIRED"
