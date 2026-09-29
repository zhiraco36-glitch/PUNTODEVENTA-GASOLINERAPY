from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox


def btnCalcular_Click():
    try:
        if not tbUsuario.get().strip() or not tbLitros.get().strip() or not tbPuesto.get().strip():
            messagebox.showwarning("Aviso", "Complete todos los campos obligatorios.")
            return

        litros = float(tbLitros.get())
        if litros <= 0:
            raise ValueError()

        combustible = rbCombustible.get()
        precio = 0.0

        if combustible == "MAGNA":
            precio = 23.50
        elif combustible == "PREMIUM":
            precio = 25.40
        elif combustible == "DIESEL":
            precio = 24.80
        else:
            messagebox.showwarning("Aviso", "Seleccione un tipo de combustible.")
            return

        if not rbPago.get():
            messagebox.showwarning("Aviso", "Seleccione un método de pago.")
            return

        subtotal = litros * precio
        iva = subtotal * 0.16
        total = subtotal + iva

        tbIva.delete(0, tk.END)
        tbIva.insert(0, f"{iva:.2f}")
        tbTotal.delete(0, tk.END)
        tbTotal.insert(0, f"{total:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad de litros válida.")
        tbLitros.delete(0, tk.END)
        tbLitros.focus()


def btnLimpiar_Click():
    tbUsuario.delete(0, tk.END)
    tbLitros.delete(0, tk.END)
    tbPuesto.delete(0, tk.END)
    tbTotal.delete(0, tk.END)
    tbIva.delete(0, tk.END)
    tbFecha.delete(0, tk.END)
    tbFecha.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    rbCombustible.set("")
    rbPago.set("")
    tbUsuario.focus()


def btnGuardar_Click():
    if not tbTotal.get().strip():
        messagebox.showwarning("Aviso", "Debe calcular el total antes de guardar.")
        return

    mensaje = (
        f"Folio: N°185\n"
        f"Fecha: {tbFecha.get()}\n"
        f"usuarioo de venta: {tbUsuario.get()}\n"
        f"Puesto: {tbPuesto.get()}\n"
        f"Combustible: {rbCombustible.get()}\n"
        f"Litros: {tbLitros.get()}\n"
        f"Método de Pago: {rbPago.get()}\n"
        f"IVA: ${tbIva.get()}\n"
        f"Total: ${tbTotal.get()}\n"
        + "-" * 30
        + "\n"
    )

    ruta_archivo = r"C:\\Users\\zhira\\Downloads\\PROYECT 04 - copiatxt";

    try:
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

        with open(ruta_archivo, "a", encoding="utf-8") as escritor:
            escritor.write(mensaje + "\n")

        messagebox.showinfo("Confirmación", "Registro guardado con éxito en Descargas.")
        btnLimpiar_Click()
    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al guardar el archivo:\n{ex}")


ventana = tk.Tk()
ventana.title("Punto de Venta - Gasolinera")
ventana.geometry("450x620")
ventana.configure(bg="#d0d0d0")

rbCombustible = tk.StringVar(value="")
rbPago = tk.StringVar(value="")

tk.Label(ventana, text="BIENVENIDOS :D", font=("Arial", 12, "bold"), bg="#d0d0d0").pack(pady=5)
tk.Label(ventana, text="Folio: N°185", font=("Arial", 10, "bold"), bg="#d0d0d0").pack()

tk.Label(ventana, text="usuarioo de venta:", bg="#d0d0d0").pack()
tbUsuario = tk.Entry(ventana, width=25, justify="center")
tbUsuario.pack()

tk.Label(ventana, text="Cantidad de gasolina (Litros):", bg="#d0d0d0").pack()
tbLitros = tk.Entry(ventana, width=25, justify="center")
tbLitros.pack()

tk.Label(ventana, text="Puesto de atención:", bg="#d0d0d0").pack()
tbPuesto = tk.Entry(ventana, width=25, justify="center")
tbPuesto.pack()

gb_comb = tk.LabelFrame(ventana, text="CUAL GUSTARIA CARGAR?", bg="#d0d0d0", padx=10, pady=5)
gb_comb.pack(pady=5)
tk.Radiobutton(gb_comb, text="MAGNA", value="MAGNA", variable=rbCombustible, bg="#d0d0d0").pack(anchor="w")
tk.Radiobutton(gb_comb, text="PREMIUM", value="PREMIUM", variable=rbCombustible, bg="#d0d0d0").pack(anchor="w")
tk.Radiobutton(gb_comb, text="DIESEL", value="DIESEL", variable=rbCombustible, bg="#d0d0d0").pack(anchor="w")

gb_pago = tk.LabelFrame(ventana, text="METODO DE PAGO", bg="#d0d0d0", padx=10, pady=5)
gb_pago.pack(pady=5)
tk.Radiobutton(gb_pago, text="EFECTIVO", value="EFECTIVO", variable=rbPago, bg="#d0d0d0").pack(anchor="w")
tk.Radiobutton(gb_pago, text="TARJETA", value="TARJETA", variable=rbPago, bg="#d0d0d0").pack(anchor="w")
tk.Radiobutton(gb_pago, text="CUPONES", value="CUPONES", variable=rbPago, bg="#d0d0d0").pack(anchor="w")

tk.Label(ventana, text="IVA:", bg="#d0d0d0").pack()
tbIva = tk.Entry(ventana, width=20, justify="center")
tbIva.pack()

tk.Label(ventana, text="Cantidad a pagar:", bg="#d0d0d0").pack()
tbTotal = tk.Entry(ventana, width=20, justify="center")
tbTotal.pack()

tk.Label(ventana, text="Fecha:", bg="#d0d0d0").pack()
tbFecha = tk.Entry(ventana, width=20, justify="center")
tbFecha.pack()
tbFecha.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

btnCalcular = tk.Button(ventana, text="Calcular", width=12, bg="#3B44F7", fg="white", command=btnCalcular_Click, padx=6, pady=3)
btnCalcular.pack(pady=5)

btnLimpiar = tk.Button(ventana, text="Limpiar", width=12, bg="#A3A3A3", fg="white", command=btnLimpiar_Click, padx=6, pady=3)
btnLimpiar.pack(pady=2)

btnGuardar = tk.Button(ventana, text="Guardar", width=12, bg="#28a745", fg="white", command=btnGuardar_Click, padx=6, pady=3)
btnGuardar.pack(pady=2)

ventana.mainloop()