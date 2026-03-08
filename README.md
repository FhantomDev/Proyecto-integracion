# Ferremax Integration - Sistema ERP & E-commerce

Este proyecto es una solución integral para la gestión de una ferretería, combinando las funcionalidades de un **E-commerce** robusto con un sistema **ERP (Enterprise Resource Planning)** simplificado. Desarrollado con **Django**, integra pasarelas de pago reales y servicios externos para el manejo de divisas.

## 🚀 Características Principales

### 🛒 E-commerce & Ventas
- **Catálogo de Productos:** Gestión dinámica de productos con categorías, marcas y proveedores.
- **Carrito de Compras y Pedidos:** Flujo completo desde la selección del producto hasta la generación del pedido.
- **Pagos Online:** Integración con **Transbank Webpay Plus** mediante su SDK oficial para transacciones seguras.
- **Modos de Compra:** Soporta compras para usuarios registrados y flujos de "pago como invitado".
- **Conversión de Divisas:** Integración con la API del **Banco Central de Chile** para obtener valores actualizados de Dólar y Euro.

### 🏢 Gestión Administrativa (ERP)
El sistema cuenta con un panel de administración y vistas personalizadas según roles de usuario:
- **Administrador:** Control total sobre inventario, cuentas de usuario y configuraciones globales.
- **Vendedor:** Gestión de boletas y atención de pedidos.
- **Bodeguero:** Control de stock y actualización de estados de envío/pedido.
- **Contador:** Supervisión de estados de pago y cierres de caja.

### 🔌 API REST
- Implementación de **Django REST Framework (DRF)** para la exposición de endpoints de productos y categorías.
- Soporte para filtrado avanzado mediante `django-filter`.

## 🛠️ Stack Tecnológico
- **Backend:** Python 3.x, Django 4.2.6
- **API:** Django REST Framework (DRF)
- **Base de Datos:** SQLite (desarrollo)
- **Integraciones:** 
  - Transbank SDK (Pagos)
  - Banco Central de Chile (Servicios REST de divisas)
- **Frontend:** Django Templates (HTML/CSS) con soporte para manejo de imágenes (Pillow).

## 📋 Requisitos
- Python 3.10+
- Pip (gestor de paquetes de Python)

## 🔧 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto-integracion
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

## 📬 Contacto
*Desarrollado como parte de un proyecto de integración para demostrar capacidades en desarrollo Full Stack, integración de APIs y sistemas de gestión empresarial.*
