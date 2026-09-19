def mostrar_menu():
    print("\n--- MÓDULO DE SOPORTE ACADÉMICO ---")
    print("1. Registrar nueva solicitud")
    print("2. Salir")


def validar_texto_obligatorio(campo, longitud_minima=3):
    while True:
        valor = input(f"Ingrese {campo}: ").strip()
        if len(valor) >= longitud_minima:
            return valor
        print(
            f"Error: El campo '{campo}' no puede estar vacío y debe tener al menos {longitud_minima} caracteres."
        )


def validar_tipo_consulta():
    tipos_validos = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    while True:
        tipo = (
            input(
                "Ingrese tipo de consulta (Matrícula, Pagos, Constancia, Plataforma, Otro): "
            )
            .strip()
            .lower()
        )
        if tipo in tipos_validos:
            return tipo
        print("Error: Tipo de consulta no válido. Intente nuevamente.")

        
def asignar_prioridad(tipo_consulta):
    if tipo_consulta in ["matrícula", "plataforma"]:
        return "Alta"
    else:
        return "Baja"


def mostrar_resumen_solicitud(codigo, nombre, tipo, descripcion, prioridad):
    print("\n-------------------------------------------")
    print("      RESUMEN DE SOLICITUD REGISTRADA      ")
    print("-------------------------------------------")
    print(f"Código Estudiante : {codigo}")
    print(f"Nombre            : {nombre}")
    print(f"Tipo de Consulta  : {tipo.capitalize()}")
    print(f"Descripción       : {descripcion}")
    print(f"Prioridad Asignada: {prioridad}")
    print("-------------------------------------------\n")


def main():
    solicitudes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- NUEVO REGISTRO DE ATENCIÓN ---")
            codigo = validar_texto_obligatorio(
                "código de estudiante", longitud_minima=5
            )
            nombre = validar_texto_obligatorio(
                "nombre del estudiante", longitud_minima=3
            )
            tipo = validar_tipo_consulta()
            descripcion = validar_texto_obligatorio(
                "descripción breve del caso", longitud_minima=5
            )

            prioridad = asignar_prioridad(tipo)
            mostrar_resumen_solicitud(
                codigo, nombre, tipo, descripcion, prioridad
            )

            solicitudes.append({
                "codigo": codigo,
                "nombre": nombre,
                "tipo": tipo,
                "descripcion": descripcion,
                "prioridad": prioridad,
            })
            print(
                f"Total de solicitudes registradas en esta sesión: {len(solicitudes)}"
            )

        elif opcion == "2":
            print("Saliendo del sistema de soporte académico...")
            break
        else:
            print("Opción inválida. Seleccione 1 o 2.")


if __name__ == "__main__":
    main()