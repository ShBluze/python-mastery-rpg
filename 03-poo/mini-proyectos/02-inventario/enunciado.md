# 📦 Mini-Proyecto 02 — Sistema de Inventario

**Dificultad**: 🟡 Medio | **XP**: 100 | **Módulo**: 03-poo

---

## 📖 Historia

El gremio de comerciantes necesita un sistema para gestionar su almacén. Diferentes tipos de productos requieren diferentes comportamientos.

## 🎯 Requisitos funcionales

- [ ] ABC `Producto` con atributos comunes: nombre, precio, código
- [ ] Método abstracto `calcular_impuesto()`
- [ ] `ProductoAlimenticio` — impuesto 5%, fecha expiración, requiere refrigeración
- [ ] `ProductoElectronico` — impuesto 15%, meses de garantía
- [ ] `ProductoRopa` — impuesto 10%, talla, material
- [ ] Clase `Inventario` que almacena productos y permite:
  - Agregar/eliminar productos
  - Buscar por nombre o código
  - Listar por tipo
  - Calcular valor total del inventario
  - Aplicar descuento a categoría
- [ ] Propiedades con validación (precio > 0, código único)

## 📋 Criterios de éxito

- Usa ABC y @abstractmethod correctamente
- Herencia bien aplicada (cada subclase añade lo suyo)
- Polimorfismo: `producto.calcular_impuesto()` funciona sin saber el tipo
- Documentación completa

## 🔗 Recursos

- [18-herencia-polimorfismo](../18-herencia-polimorfismo.md)
- [20-clases-abstractas](../20-clases-abstractas.md)
