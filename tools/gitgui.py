#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import os

class GitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("fsociety Git Manager")
        self.root.geometry("700x600")
        self.root.configure(bg="#0d1117")
        
        # Stil
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Fira Code', 10), padding=5)
        style.configure('TLabel', font=('Fira Code', 10), background='#0d1117', foreground='#c9d1d9')
        style.configure('TFrame', background='#0d1117')
        
        # Ana çerçeve
        main_frame = ttk.Frame(root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Başlık
        title = tk.Label(main_frame, text="⚡ fsociety Git Manager", 
                        font=('Fira Code', 16, 'bold'), fg="#58a6ff", bg="#0d1117")
        title.pack(pady=(0,15))
        
        # Buton çerçevesi
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(0,10))
        
        # Butonlar
        self.add_btn = tk.Button(btn_frame, text="📦 git add .", 
                                 font=('Fira Code', 11, 'bold'),
                                 bg="#238636", fg="white", activebackground="#2ea043",
                                 command=self.git_add, cursor="hand2")
        self.add_btn.pack(side=tk.LEFT, padx=(0,5))
        
        self.status_btn = tk.Button(btn_frame, text="📋 git status", 
                                    font=('Fira Code', 11, 'bold'),
                                    bg="#1f6feb", fg="white", activebackground="#388bfd",
                                    command=self.git_status, cursor="hand2")
        self.status_btn.pack(side=tk.LEFT, padx=5)
        
        self.push_btn = tk.Button(btn_frame, text="🚀 git push", 
                                  font=('Fira Code', 11, 'bold'),
                                  bg="#da3633", fg="white", activebackground="#f85149",
                                  command=self.git_push, cursor="hand2")
        self.push_btn.pack(side=tk.LEFT, padx=5)
        
        # Çıktı alanı
        output_label = tk.Label(main_frame, text="📤 Çıktı:", 
                               font=('Fira Code', 10, 'bold'), fg="#8b949e", bg="#0d1117")
        output_label.pack(anchor="w", pady=(10,5))
        
        self.output = scrolledtext.ScrolledText(main_frame, height=12, 
                                                bg="#161b22", fg="#c9d1d9",
                                                font=('Fira Code', 9),
                                                insertbackground='white')
        self.output.pack(fill=tk.BOTH, expand=True, pady=(0,10))
        
        # Commit mesajı çerçevesi
        commit_frame = ttk.Frame(main_frame)
        commit_frame.pack(fill=tk.X, pady=(5,10))
        
        commit_label = tk.Label(commit_frame, text="💬 Commit Mesajı:", 
                               font=('Fira Code', 10, 'bold'), fg="#8b949e", bg="#0d1117")
        commit_label.pack(anchor="w")
        
        self.commit_msg = tk.Entry(commit_frame, 
                                   font=('Fira Code', 10),
                                   bg="#161b22", fg="#c9d1d9", insertbackground='white',
                                   relief=tk.FLAT)
        self.commit_msg.pack(fill=tk.X, pady=(5,0))
        self.commit_msg.insert(0, "Güncelleme yapıldı")
        
        # Commit butonu
        self.commit_btn = tk.Button(commit_frame, text="✅ git commit", 
                                    font=('Fira Code', 11, 'bold'),
                                    bg="#1b6e2e", fg="white", activebackground="#238636",
                                    command=self.git_commit, cursor="hand2")
        self.commit_btn.pack(pady=(10,0))
        
        # Durum çubuğu
        self.status_bar = tk.Label(main_frame, text="🟢 Hazır", 
                                   font=('Fira Code', 9), fg="#3fb950", bg="#0d1117")
        self.status_bar.pack(anchor="w")
        
    def run_command(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, 
                                   cwd=os.path.expanduser("~/Desktop/fsociety"))
            return result.stdout + result.stderr
        except Exception as e:
            return str(e)
    
    def update_output(self, text):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
    
    def set_status(self, text, color="#3fb950"):
        self.status_bar.config(text=text, fg=color)
    
    def git_add(self):
        self.set_status("🟡 git add . çalışıyor...", "#d2991d")
        output = self.run_command("git add .")
        self.update_output(output if output else "✅ Tüm dosyalar eklendi.")
        self.set_status("🟢 Dosyalar eklendi")
    
    def git_status(self):
        self.set_status("🟡 git status çalışıyor...", "#d2991d")
        output = self.run_command("git status")
        self.update_output(output)
        self.set_status("🟢 Durum görüntülendi")
    
    def git_commit(self):
        msg = self.commit_msg.get().strip()
        if not msg:
            messagebox.showwarning("Uyarı", "Commit mesajı boş olamaz!")
            return
        self.set_status("🟡 Commit yapılıyor...", "#d2991d")
        output = self.run_command(f'git commit -m "{msg}"')
        self.update_output(output)
        self.set_status("🟢 Commit tamamlandı", "#3fb950")
    
    def git_push(self):
        self.set_status("🟡 Push yapılıyor...", "#d2991d")
        output = self.run_command("git push")
        self.update_output(output if output else "✅ Başarıyla gönderildi.")
        if "error" in output.lower() or "fatal" in output.lower():
            self.set_status("🔴 Push başarısız!", "#f85149")
        else:
            self.set_status("🟢 Push tamamlandı", "#3fb950")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitGUI(root)
    root.mainloop()
