import tkinter as tk
import random

class PiedraPapelTijera:
    def __init__(self, master):
        self.master = master
        master.title("Piedra, Papel o Tijera")
        
        # Configuración de variables
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        
        # Configuración de la interfaz
        self.setup_interfaz()
    
    def setup_interfaz(self):
        # Marco principal
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack()
        
        # Título
        tk.Label(self.frame, text="Piedra, Papel o Tijera", font=("Arial", 16)).pack(pady=10)
        
        # Botones de selección
        frame_botones = tk.Frame(self.frame)
        frame_botones.pack(pady=10)
        
        opciones = ["Piedra", "Papel", "Tijera"]
        for opcion in opciones:
            boton = tk.Button(frame_botones, text=opcion, 
                               command=lambda o=opcion: self.jugar(o),
                               width=10)
            boton.pack(side=tk.LEFT, padx=5)
        
        # Resultado del juego
        self.label_resultado = tk.Label(self.frame, text="Elige una opción", font=("Arial", 12))
        self.label_resultado.pack(pady=10)
        
        # Selección de la computadora
        self.label_computadora = tk.Label(self.frame, text="Computadora eligió: ", font=("Arial", 10))
        self.label_computadora.pack()
        
        # Marcador de puntuación
        self.label_puntaje = tk.Label(self.frame, 
                                      text=f"Jugador: {self.puntaje_jugador} - Computadora: {self.puntaje_computadora}", 
                                      font=("Arial", 12))
        self.label_puntaje.pack(pady=10)
    
    def jugar(self, eleccion_jugador):
        # Opciones posibles
        opciones = ["Piedra", "Papel", "Tijera"]
        
        # Elección de la computadora
        eleccion_computadora = random.choice(opciones)
        
        # Actualizar label de elección de la computadora
        self.label_computadora.config(text=f"Computadora eligió: {eleccion_computadora}")
        
        # Determinar ganador
        resultado = self.determinar_ganador(eleccion_jugador, eleccion_computadora)
        
        # Mostrar resultado
        if resultado == "Empate":
            self.label_resultado.config(text="¡Empate!", fg="blue")
        elif resultado == "Jugador":
            self.label_resultado.config(text="¡Ganaste!", fg="green")
            self.puntaje_jugador += 1
        else:
            self.label_resultado.config(text="¡Perdiste!", fg="red")
            self.puntaje_computadora += 1
        
        # Actualizar marcador
        self.label_puntaje.config(text=f"Jugador: {self.puntaje_jugador} - Computadora: {self.puntaje_computadora}")
    
    def determinar_ganador(self, jugador, computadora):
        if jugador == computadora:
            return "Empate"
        
        # Reglas del juego
        if (jugador == "Piedra" and computadora == "Tijera") or \
           (jugador == "Tijera" and computadora == "Papel") or \
           (jugador == "Papel" and computadora == "Piedra"):
            return "Jugador"
        
        return "Computadora"

# Crear ventana principal
root = tk.Tk()
root.geometry("350x400")  # Tamaño de la ventana
juego = PiedraPapelTijera(root)
root.mainloop()