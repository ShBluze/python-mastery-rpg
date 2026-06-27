# 🏦 Mini-Proyecto 01 — Sistema Bancario

**Dificultad**: 🟡 Medio | **XP**: 100 | **Módulo**: 03-poo

---

## 📖 Historia

El banco real del reino necesita un sistema para gestionar cuentas, transacciones y clientes. Construye el núcleo del sistema con POO.

## 🎯 Requisitos funcionales

- [ ] Clase `Cliente` con nombre, id, email, teléfono
- [ ] Clase `Cuenta` con número, saldo, titular, tipo (ahorro/corriente)
- [ ] Clase `Transaccion` con fecha, tipo (depósito/retiro/transferencia), monto, cuenta origen, cuenta destino
- [ ] Clase `Banco` que gestiona clientes, cuentas y transacciones
- [ ] Métodos: abrir cuenta, cerrar cuenta, depositar, retirar, transferir
- [ ] Validaciones: saldo insuficiente, cuenta no encontrada, límite diario
- [ ] Historial de transacciones por cuenta
- [ ] Properties para validar datos (email válido, saldo no negativo)

## 📋 Criterios de éxito

- Encapsulamiento correcto (atributos privados con _)
- Properties con validación
- Excepción personalizada `SaldoInsuficienteError`
- Tipado completo
- Docstrings en todas las clases y métodos

## 🔗 Recursos

- [15-clases-objetos](../15-clases-objetos.md)
- [16-tipos-metodos](../16-tipos-metodos.md)
- [19-encapsulamiento](../19-encapsulamiento.md)
- [21-dataclasses-pydantic](../21-dataclasses-pydantic.md)
