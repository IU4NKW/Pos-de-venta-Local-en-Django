# Tareas pendientes - Modelos Django POS

## 0. Decisión de arquitectura
- [ ] Definir si se mantiene `User + PerfilUsuario` o se migra a `Usuario(AbstractUser)`.
- [ ] Documentar impacto en `AUTH_USER_MODEL`, migraciones, base de datos y referencias.
- [ ] Alinear nombres de roles: `administrador/jefe_ventas/vendedor` vs `ADMIN/JEFE_VENTAS/VENDEDOR`.

## 1. Usuario
- [ ] Unificar `correo` y `email` en un solo campo único usado como `USERNAME_FIELD`.
- [ ] Revisar `REQUIRED_FIELDS` y el flujo de creación de superusuarios.
- [ ] Agregar `sucursal` si el sistema será multi-sucursal.
- [ ] Agregar `telefono` si se usará en gestión de usuarios.
- [ ] Actualizar `CustomLoginView`, `views.py`, `crear_datos_usuarios.py` y templates.

## 2. Cliente
- [ ] Agregar `telefono`.
- [ ] Agregar `email`.
- [ ] Agregar `comuna`/`ciudad` si aplica.
- [ ] Validar formato y unicidad del RUT.

## 3. Producto e inventario
- [ ] Agregar `categoria`.
- [ ] Agregar `activo`.
- [ ] Agregar `fecha_actualizacion`.
- [ ] Crear `MovimientoStock` para entradas, salidas, ajustes y reposiciones.
- [ ] Definir descuento automático de stock al vender.
- [ ] Revisar `verificar_stock_critico()` y umbrales mínimos.

## 4. Jornada
- [ ] Agregar `sucursal` si aplica.
- [ ] Restringir una sola jornada abierta por sucursal/terminal con `UniqueConstraint` condicional.
- [ ] Cambiar `fecha` a `default=timezone.localdate`.
- [ ] Implementar `abrir_jornada()` y `cerrar_jornada()` con validaciones.
- [ ] Registrar apertura y cierre en `LogAuditoria`.
- [ ] Conectar los botones de admin/jefe a la lógica real, no solo a redirecciones.

## 5. Venta y documentos
- [ ] Agregar `folio` único y numeración por tipo de documento.
- [ ] Agregar `sucursal` si aplica.
- [ ] Agregar `motivo_devolucion` o un modelo `Devolucion`.
- [ ] Definir convención para `NOTA_CREDITO`: montos negativos o movimiento separado.
- [ ] Validar que una nota de crédito tenga `venta_origen` y que la venta original pase a `DEVUELTA`.
- [ ] Calcular `subtotal`, `iva` y `total` en servicio o `save()`.
- [ ] Validar que no se creen ventas sin una jornada abierta.

## 6. DetalleVenta
- [ ] Revisar cálculo de subtotal y redondeo.
- [ ] Validar `cantidad > 0`.
- [ ] Definir si los detalles pueden modificarse después de emitir la venta.

## 7. Auditoría
- [ ] Agregar `ip` y `severidad`.
- [ ] Agregar acciones faltantes: usuario modificado, usuario desactivado, venta anulada, etc.
- [ ] Agregar `sucursal` si aplica.
- [ ] Agregar índices por fecha, usuario y acción.
- [ ] Registrar login, ventas, devoluciones, stock crítico, jornadas y usuarios.

## 8. Migraciones y compatibilidad
- [ ] Crear migraciones con `makemigrations`.
- [ ] Probar `migrate` en una base limpia.
- [ ] Actualizar `admin.py`.
- [ ] Actualizar `views.py`, `urls.py` y templates que usen los campos nuevos.
- [ ] Actualizar `crear_datos_usuarios.py` y datos de prueba.

## 9. Pruebas
- [ ] Tests de roles y permisos.
- [ ] Tests de jornada única y cierre.
- [ ] Tests de venta, IVA, totales y descuento de stock.
- [ ] Tests de devolución y nota de crédito.
- [ ] Tests de auditoría.
- [ ] Ejecutar `python manage.py check` y `python manage.py test`.

## 10. Documentación
- [ ] Actualizar diagrama ER.
- [ ] Documentar decisiones sobre sucursal, folio, notas de crédito y movimientos de stock.
