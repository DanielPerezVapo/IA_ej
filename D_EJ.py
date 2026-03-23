import tkinter as tk
from tkinter import messagebox, ttk

ROOT_BG = "#f0f0f0"
CARD_BG = "#ffffff"
ACCENT = "#2d6a9f"
TEXT_MAIN = "#202020"
TEXT_MUTED = "#505050"
PANEL_BG = "#dff3e3"
ALT_CARD_BG = "#fff7e6"
ACCENT_2 = "#e76f51"


root = tk.Tk()
root.title("Menu de ejercicios")
root.geometry("860x580")
root.minsize(760, 520)
root.config(bg=ROOT_BG)


def configurar_estilos():
    style = ttk.Style(root)
    style.theme_use("default")

    style.configure("Root.TFrame", background="#f8f4ec")
    style.configure("Card.TFrame", background=ALT_CARD_BG)
    style.configure("Side.TFrame", background=PANEL_BG)
    style.configure("Title.TLabel", background="#f8f4ec", foreground=ACCENT_2, font=("Segoe UI", 20, "bold"))
    style.configure("Subtitle.TLabel", background=ROOT_BG, foreground=TEXT_MUTED, font=("Segoe UI", 10))
    style.configure("Section.TLabel", background=ALT_CARD_BG, foreground="#264653", font=("Segoe UI", 12, "bold"))
    style.configure("Hint.TLabel", background=ALT_CARD_BG, foreground="#5f6368", font=("Segoe UI", 9))
    style.configure("Field.TLabel", background=ALT_CARD_BG, foreground="#264653", font=("Segoe UI", 10, "bold"))
    style.configure("Panel.TLabelframe", background=ALT_CARD_BG)
    style.configure("Panel.TLabelframe.Label", background=ALT_CARD_BG, foreground=ACCENT_2, font=("Segoe UI", 10, "bold"))
    style.configure("Tab.TNotebook", background=ROOT_BG, borderwidth=0)
    style.configure("Tab.TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=(14, 8))
    style.map("Tab.TNotebook.Tab", background=[("selected", "#ffd6a5")])
    style.configure("SideTitle.TLabel", background=PANEL_BG, foreground="#2a9d8f", font=("Segoe UI", 12, "bold"))
    style.configure("SideText.TLabel", background=PANEL_BG, foreground="#3d405b", font=("Segoe UI", 10))

    style.configure(
        "Modern.TButton",
        font=("Segoe UI", 10),
        padding=(10, 6),
        background="#2a9d8f",
        foreground="#ffffff",
        borderwidth=1,
    )
    style.map(
        "Modern.TButton",
        background=[("active", "#23867a"), ("pressed", "#1d6f65")],
        foreground=[("disabled", "#7b8794")],
    )

    style.configure(
        "Menu.TButton",
        font=("Segoe UI", 10, "bold"),
        padding=(10, 10),
        background="#f4a261",
        foreground="#2b2d42",
        borderwidth=1,
    )
    style.map("Menu.TButton", background=[("active", "#e7904a"), ("pressed", "#d57f39")])

    style.configure("Modern.TEntry", font=("Segoe UI", 10), padding=4)


configurar_estilos()


def crear_ventana_ejercicio(titulo, descripcion):
    w = tk.Toplevel(root)
    w.title(titulo)
    w.geometry("620x520")
    w.minsize(480, 480)
    w.config(bg=ROOT_BG)

    cont = ttk.Frame(w, style="Root.TFrame", padding=16)
    cont.pack(fill="both", expand=True)

    card = ttk.Frame(cont, style="Card.TFrame", padding=12)
    card.pack(fill="both", expand=True)

    cabecera = ttk.Frame(card, style="Card.TFrame")
    cabecera.pack(fill="x", pady=(0, 10))
    ttk.Label(cabecera, text=titulo, style="Section.TLabel").pack(anchor="w")
    ttk.Label(cabecera, text=descripcion, style="Hint.TLabel").pack(anchor="w", pady=(2, 0))

    seccion_salida = ttk.LabelFrame(card, text="Salida", style="Panel.TLabelframe", padding=8)
    seccion_salida.pack(fill="both", expand=True, pady=(0, 10))

    txt = tk.Text(
        seccion_salida,
        height=12,
        wrap="word",
        font=("Consolas", 10),
        bg="#fffdf8",
        fg="#2b2d42",
        relief="solid",
        bd=1,
        insertbackground="#2b2d42",
        highlightthickness=0,
    )
    scroll = ttk.Scrollbar(seccion_salida, orient="vertical", command=txt.yview)
    txt.configure(yscrollcommand=scroll.set)
    txt.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    seccion_form = ttk.LabelFrame(card, text="Datos", style="Panel.TLabelframe", padding=10)
    seccion_form.pack(fill="x")
    form = ttk.Frame(seccion_form, style="Card.TFrame")
    form.pack(fill="x")

    acciones = ttk.Frame(card, style="Card.TFrame")
    acciones.pack(fill="x", pady=(10, 0))

    return w, form, acciones, txt


def crear_campo(form, fila, texto, mostrar=None):
    ttk.Label(form, text=texto, style="Field.TLabel").grid(row=fila, column=0, sticky="w", padx=(0, 8), pady=6)
    entry = ttk.Entry(form, style="Modern.TEntry", show=mostrar)
    entry.grid(row=fila, column=1, sticky="ew", pady=6)
    form.grid_columnconfigure(1, weight=1)
    return entry


def limpiar_y_escribir(txt, contenido):
    txt.delete("1.0", "end")
    txt.insert("end", contenido)


# Ejercicio 1: aumento de sueldos
def ej1():
    _, form, acciones, txt = crear_ventana_ejercicio("Aumento de sueldos", "Calcula incrementos por tramos salariales")
    lista = []

    def aumento(sueldo):
        if sueldo < 4000:
            return sueldo * 0.15
        if sueldo <= 7000:
            return sueldo * 0.10
        return sueldo * 0.08

    def registrar():
        nombre = e1.get().strip()
        try:
            sueldo = float(e2.get())
        except ValueError:
            messagebox.showerror("Error", "Sueldo invalido")
            return

        nuevo = sueldo + aumento(sueldo)
        lista.append((nombre, nuevo))
        limpiar_y_escribir(txt, f"{nombre} nuevo sueldo: {nuevo:.2f}")

    def ver_historial():
        if not lista:
            limpiar_y_escribir(txt, "Sin registros")
            return
        limpiar_y_escribir(txt, "\n".join(str(x) for x in lista))

    e1 = crear_campo(form, 0, "Nombre")
    e2 = crear_campo(form, 1, "Sueldo")

    ttk.Button(acciones, text="Registrar", style="Modern.TButton", command=registrar).pack(side="left", padx=(0, 8))
    ttk.Button(acciones, text="Historial", style="Modern.TButton", command=ver_historial).pack(side="left")


# Ejercicio 2: entradas del parque
def ej2():
    _, form, acciones, txt = crear_ventana_ejercicio("Parque", "Calcula montos por edad y numero de juegos")
    lista = []

    def calcular(edad, juegos):
        total = juegos * 50
        if edad < 10:
            total *= 0.75
        elif edad <= 17:
            total *= 0.90
        return total

    def registrar():
        try:
            edad = int(e_edad.get())
            juegos = int(e_juegos.get())
        except ValueError:
            messagebox.showerror("Error", "Edad y juegos deben ser numeros")
            return

        total = calcular(edad, juegos)
        lista.append(total)
        limpiar_y_escribir(txt, f"Total: {total:.2f}")

    def total_parque():
        limpiar_y_escribir(txt, f"Total parque: {sum(lista):.2f}")

    crear_campo(form, 0, "Nombre")
    e_edad = crear_campo(form, 1, "Edad")
    e_juegos = crear_campo(form, 2, "Juegos")

    ttk.Button(acciones, text="Registrar", style="Modern.TButton", command=registrar).pack(side="left", padx=(0, 8))
    ttk.Button(acciones, text="Total", style="Modern.TButton", command=total_parque).pack(side="left")


# Ejercicio 3: descuentos por mes
def ej3():
    _, form, acciones, txt = crear_ventana_ejercicio("Descuentos", "Aplica descuentos segun el mes de compra")
    lista = []
    meses_validos = {
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    }

    def descuento(mes):
        if mes == "octubre":
            return 0.15
        if mes == "diciembre":
            return 0.20
        if mes == "julio":
            return 0.10
        return 0

    def registrar():
        mes = e_mes.get().strip().lower()

        if mes not in meses_validos:
            messagebox.showerror("Error", "Mes invalido")
            return

        try:
            importe = float(e_importe.get())
        except ValueError:
            messagebox.showerror("Error", "Importe invalido")
            return

        total = importe - (importe * descuento(mes))
        lista.append(total)
        limpiar_y_escribir(txt, f"Total: {total:.2f}")

    def total_vendido():
        limpiar_y_escribir(txt, f"Total vendido: {sum(lista):.2f}")

    crear_campo(form, 0, "Nombre")
    e_mes = crear_campo(form, 1, "Mes")
    e_importe = crear_campo(form, 2, "Importe")

    ttk.Button(acciones, text="Registrar", style="Modern.TButton", command=registrar).pack(side="left", padx=(0, 8))
    ttk.Button(acciones, text="Total", style="Modern.TButton", command=total_vendido).pack(side="left")


# Ejercicio 4: validar menor a 10
def ej4():
    _, form, acciones, txt = crear_ventana_ejercicio("Menor a 10", "Valida numeros y cuenta intentos")
    intentos = 0

    def validar():
        nonlocal intentos
        try:
            numero = int(e_num.get())
        except ValueError:
            messagebox.showerror("Error", "Numero invalido")
            return

        intentos += 1
        if numero < 10:
            txt.insert("end", f"Correcto: {numero} en {intentos} intentos\n")
        else:
            txt.insert("end", "Error, intenta otra vez\n")
        txt.see("end")

    e_num = crear_campo(form, 0, "Numero")
    ttk.Button(acciones, text="Validar", style="Modern.TButton", command=validar).pack(side="left")


# Funcion auxiliar para ejercicios 5 y 6
def en_rango(n):
    return 0 < n < 20


# Ejercicio 5: validar rango entre 1 y 19
def ej5():
    _, form, acciones, txt = crear_ventana_ejercicio("Rango", "Valida si un numero esta entre 1 y 19")

    def validar():
        try:
            numero = int(e_num.get())
        except ValueError:
            messagebox.showerror("Error", "Numero invalido")
            return

        if en_rango(numero):
            txt.insert("end", f"Correcto: {numero}\n")
        else:
            txt.insert("end", "Fuera de rango\n")
        txt.see("end")

    e_num = crear_campo(form, 0, "Numero 1-19")
    ttk.Button(acciones, text="Validar", style="Modern.TButton", command=validar).pack(side="left")


# Ejercicio 6: historial con conteo de incorrectos
def ej6():
    _, form, acciones, txt = crear_ventana_ejercicio("Historial intentos", "Guarda valores e incorrectos")
    lista = []
    malos = 0

    def validar():
        nonlocal malos
        try:
            numero = int(e_num.get())
        except ValueError:
            messagebox.showerror("Error", "Numero invalido")
            return

        lista.append(numero)

        if en_rango(numero):
            txt.insert("end", f"Correcto: {numero}\n")
        else:
            malos += 1
            txt.insert("end", "Incorrecto\n")
        txt.see("end")

    def ver_historial():
        txt.insert("end", f"Historial: {lista}\nIncorrectos: {malos}\n")
        txt.see("end")

    e_num = crear_campo(form, 0, "Numero")
    ttk.Button(acciones, text="Validar", style="Modern.TButton", command=validar).pack(side="left", padx=(0, 8))
    ttk.Button(acciones, text="Ver historial", style="Modern.TButton", command=ver_historial).pack(side="left")


# Ejercicio 7: suma de 1 a N
def ej7():
    _, form, acciones, txt = crear_ventana_ejercicio("Suma N", "Suma desde 1 hasta N")

    def calcular():
        try:
            n = int(e_num.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa un entero positivo")
            return

        numeros = list(range(1, n + 1))
        total = sum(numeros)
        txt.insert("end", f"{numeros} = {total}\n")
        txt.see("end")

    e_num = crear_campo(form, 0, "Numero N")
    ttk.Button(acciones, text="Calcular", style="Modern.TButton", command=calcular).pack(side="left")


# Ejercicio 8: suma acumulativa hasta ingresar 0
def ej8():
    _, form, acciones, txt = crear_ventana_ejercicio("Suma acumulativa", "Ingresa numeros; 0 finaliza")
    lista = []
    suma = 0.0

    def agregar():
        nonlocal suma
        try:
            numero = float(e_num.get())
        except ValueError:
            messagebox.showerror("Error", "Numero invalido")
            return

        if numero == 0:
            txt.insert("end", f"Lista: {lista}\nTotal: {suma:.2f}\n")
        else:
            lista.append(numero)
            suma += numero
            txt.insert("end", f"Suma: {suma:.2f}\n")
        txt.see("end")

    e_num = crear_campo(form, 0, "Numero (0 termina)")
    ttk.Button(acciones, text="Agregar", style="Modern.TButton", command=agregar).pack(side="left")


# Ejercicio 9: acumular hasta superar 100
def ej9():
    _, form, acciones, txt = crear_ventana_ejercicio("Hasta 100", "Acumula valores y detalla al superar 100")
    lista = []
    suma = 0

    def agregar():
        nonlocal suma
        try:
            numero = int(e_num.get())
        except ValueError:
            messagebox.showerror("Error", "Numero invalido")
            return

        lista.append(numero)
        suma += numero
        txt.insert("end", f"Suma: {suma}\n")

        if suma > 100:
            txt.insert("end", f"Final lista: {lista}\nTotal: {suma}\n")
        txt.see("end")

    e_num = crear_campo(form, 0, "Numero")
    ttk.Button(acciones, text="Agregar", style="Modern.TButton", command=agregar).pack(side="left")


# Ejercicio 10: calculo de pagos
def ej10():
    _, form, acciones, txt = crear_ventana_ejercicio("Pago", "Calcula pago total y genera reporte")
    lista = []

    def calcular_pago():
        nombre = e_nombre.get().strip()
        try:
            hn = float(e_hn.get())
            pago_hora = float(e_pago.get())
            he = float(e_he.get())
            hijos = int(e_hijos.get())
        except ValueError:
            messagebox.showerror("Error", "Datos invalidos")
            return

        total = (hn * pago_hora) + (he * pago_hora * 1.5) + (hijos * 0.5 * pago_hora)
        lista.append((nombre, total))
        txt.insert("end", f"{nombre}: {total:.2f}\n")
        txt.see("end")

    def reporte():
        txt.insert("end", "---REPORTE---\n")
        for item in lista:
            txt.insert("end", f"{item}\n")
        txt.see("end")

    e_nombre = crear_campo(form, 0, "Nombre")
    e_hn = crear_campo(form, 1, "Horas normales")
    e_pago = crear_campo(form, 2, "Pago por hora")
    e_he = crear_campo(form, 3, "Horas extra")
    e_hijos = crear_campo(form, 4, "Hijos")

    ttk.Button(acciones, text="Calcular", style="Modern.TButton", command=calcular_pago).pack(side="left", padx=(0, 8))
    ttk.Button(acciones, text="Reporte", style="Modern.TButton", command=reporte).pack(side="left")


# Interfaz principal
main = ttk.Frame(root, style="Root.TFrame", padding=14)
main.pack(fill="both", expand=True)

header = ttk.Frame(main, style="Root.TFrame")
header.pack(fill="x", pady=(2, 10))

contenido = ttk.Frame(main, style="Root.TFrame")
contenido.pack(fill="both", expand=True)

panel_izq = ttk.Frame(contenido, style="Side.TFrame", padding=12)
panel_izq.pack(side="left", fill="y", padx=(0, 10))

card = ttk.Frame(contenido, style="Card.TFrame", padding=14)
card.pack(side="left", fill="both", expand=True)

ttk.Label(header, text="MENU DE EJERCICIOS", style="Title.TLabel").pack(anchor="w")
ttk.Label(
    header,
    text="Selecciona una practica en las pestañas para abrir su interfaz.",
    style="Subtitle.TLabel",
).pack(anchor="w", pady=(4, 0))

ttk.Label(panel_izq, text="Navegacion", style="SideTitle.TLabel").pack(anchor="w")
ttk.Label(
    panel_izq,
    text="Ahora el menu usa colores nuevos y distribucion lateral.",
    style="SideText.TLabel",
    wraplength=170,
    justify="left",
).pack(anchor="w", pady=(6, 12))
ttk.Label(panel_izq, text="Tip", style="SideTitle.TLabel").pack(anchor="w")
ttk.Label(
    panel_izq,
    text="Prueba varias pestañas y cambia entre ejercicios para ver el nuevo orden.",
    style="SideText.TLabel",
    wraplength=170,
    justify="left",
).pack(anchor="w", pady=(6, 0))

botones = [
    ("1. Aumento de sueldos", ej1),
    ("2. Parque", ej2),
    ("3. Descuentos", ej3),
    ("4. Menor a 10", ej4),
    ("5. Rango", ej5),
    ("6. Historial intentos", ej6),
    ("7. Suma N", ej7),
    ("8. Suma acumulativa", ej8),
    ("9. Hasta 100", ej9),
    ("10. Pago", ej10),
]

notebook = ttk.Notebook(card, style="Tab.TNotebook")
notebook.pack(fill="both", expand=True, pady=(4, 0))

tab_1 = ttk.Frame(notebook, style="Card.TFrame", padding=10)
tab_2 = ttk.Frame(notebook, style="Card.TFrame", padding=10)
notebook.add(tab_1, text="Ejercicios 1-5")
notebook.add(tab_2, text="Ejercicios 6-10")

grupo_1 = botones[:5]
grupo_2 = botones[5:]

for indice, (texto, comando) in enumerate(grupo_1):
    btn = ttk.Button(tab_1, text=texto, command=comando, style="Menu.TButton")
    fila = indice // 2
    columna = indice % 2
    btn.grid(row=fila, column=columna, padx=6, pady=6, sticky="nsew")

for indice, (texto, comando) in enumerate(grupo_2):
    btn = ttk.Button(tab_2, text=texto, command=comando, style="Menu.TButton")
    fila = indice // 2
    columna = indice % 2
    btn.grid(row=fila, column=columna, padx=6, pady=6, sticky="nsew")

tab_1.grid_columnconfigure(0, weight=1)
tab_1.grid_columnconfigure(1, weight=1)
tab_2.grid_columnconfigure(0, weight=1)
tab_2.grid_columnconfigure(1, weight=1)

root.mainloop()
