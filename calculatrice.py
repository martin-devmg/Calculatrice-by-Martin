import tkinter as tk
from tkinter import messagebox

# Couleurs pour un design sombre et professionnel
BG_COLOR = "#1e1e2e"  # Couleur de fond principale
BTN_COLOR = "#313244"  # Couleur des boutons
BTN_HOVER = "#45475a"  # Couleur des boutons au survol
TEXT_COLOR = "#cdd6f4" # Couleur du texte
ACCENT_COLOR = "#f8a32d" # Couleur d'accent pour le bouton égal

class Calculatrice:
    def __init__(self, root):
        # Initialisation de la fenêtre principale avec titre et taille fixe
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("360x500")
        self.root.configure(bg=BG_COLOR)
        self.expression = ""  # Expression mathématique entrée par l'utilisateur

        # Champ d'affichage de l'expression et du résultat
        self.entry = tk.Entry(
            root, font=("Consolas", 26), justify="right",
            fg=TEXT_COLOR, bg=BG_COLOR, borderwidth=0, relief="ridge",
            insertbackground=TEXT_COLOR # Curseur visible sur fond sombre
        )
        self.entry.pack(fill="both", ipadx=8, ipady=25, pady=(20, 5), padx=12)

        # Définition de la disposition des boutons de chiffres et opérations
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"]
        ]

        # Création des boutons dynamiquement avec style
        for row_values in buttons:
            row = tk.Frame(root, bg=BG_COLOR)
            row.pack(expand=True, fill="both", padx=12, pady=3)
            for value in row_values:
                button = tk.Button(
                    row, text=value, font=("Consolas", 20), fg=TEXT_COLOR, bg=BTN_COLOR,
                    relief="flat", activebackground=BTN_HOVER, activeforeground=TEXT_COLOR,
                    command=lambda v=value: self.on_button_click(v)
                )
                button.pack(side="left", expand=True, fill="both", padx=4, pady=4)

        # Création du bouton égal avec couleur d'accent
        equal_button = tk.Button(
            root, text="=", font=("Consolas", 20, "bold"), fg=BG_COLOR, bg=ACCENT_COLOR,
            relief="flat", activebackground="#74c7ec", activeforeground=BG_COLOR,
            command=self.calculate
        )
        equal_button.pack(expand=True, fill="both", padx=12, pady=12)

    def on_button_click(self, char):
        # Gestion des actions lors du clic sur un bouton
        if char == "C":
            self.expression = ""  # Réinitialiser l'expression si C est cliqué
        else:
            self.expression += str(char)  # Ajouter le caractère à l'expression en cours
        self.update_display()

    def update_display(self):
        # Met à jour l'affichage de l'expression dans le champ d'entrée
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate(self):
        # Tente de calculer l'expression actuelle
        try:
            result = eval(self.expression)  # Calcul dynamique avec eval
            self.expression = str(result)  # Affiche le résultat
        except Exception:
            # Gestion des erreurs comme division par zéro ou syntaxe incorrecte
            messagebox.showerror("Erreur", "Expression invalide")
            self.expression = ""
        self.update_display()

if __name__ == "__main__":
    # Lancement de l'application
    root = tk.Tk()
    app = Calculatrice(root)
    root.mainloop()