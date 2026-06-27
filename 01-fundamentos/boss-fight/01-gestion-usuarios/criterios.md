# ✅ Criterios de Aprobación — Boss: Gestión de Usuarios

> Marca cada ítem al verificar. **Todos los obligatorios deben estar marcados** para pasar el Boss.

---

## Obligatorios

- [ ] Menú CLI con opciones numeradas, se repite hasta salir
- [ ] Crear usuario: pide nombre, email, edad, rol. Asigna ID autoincremental
- [ ] Listar usuarios: muestra todos con formato tabla
- [ ] Buscar usuario: por nombre parcial, sin distinguir mayúsculas. Muestra todos los que coinciden
- [ ] Actualizar usuario: pide ID, permite cambiar campos individualmente
- [ ] Eliminar usuario: pide ID, confirma, elimina. Error si no existe
- [ ] Datos persisten entre ejecuciones en `usuarios.json`
- [ ] Validación: email único (no repetir)
- [ ] Validación: edad ≥ 0
- [ ] Validación: nombre no vacío
- [ ] Error controlado si `usuarios.json` está corrupto
- [ ] Error controlado si se busca ID inexistente
- [ ] Error controlado si email duplicado al crear/actualizar
- [ ] Mínimo 5 funciones separadas en al menos 3 archivos
- [ ] Código con docstrings

## Bonus

- [ ] Exportar a CSV con encoding UTF-8
- [ ] Login con contraseña (hash con hashlib.sha256)
- [ ] Paginación al listar (5 usuarios por página)

---

## Resultado

- **Obligatorios**: _/15
- **Bonus**: _/3
- **¿Pasa?**: ❌ No / ✅ Sí

> 💡 Si no pasas: anota qué criterios fallaste, repasa los ejercicios correspondientes y vuelve a intentar. ¡El Boss te espera!
