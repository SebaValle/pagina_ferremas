from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pedido, DetalleVenta
from .serializer import PedidoSerializer
from .utils import obtener_valor_dolar
from productos.models import InventarioSucursal
from django.db import transaction
from rest_framework import serializers as drf_serializers

# IMPORTS REQUERIDOS PARA EL PDF (REPORTLAB)
from django.http import HttpResponse
from rest_framework.decorators import action
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
<<<<<<< HEAD
        # 1. API Externa: Obtener el valor del dólar del día
        try:
            valor_dolar = obtener_valor_dolar()
            valor_dolar = float(valor_dolar) if valor_dolar else 950.0
        except Exception:
            valor_dolar = 950.0 
        
        # 2. Separar los items de la petición para que el serializer base no falle
        data_pedido = request.data.copy()
        items_data = data_pedido.pop('items', [])

        # 3. Validar y guardar Pedido base (Nace temporalmente en 0)
        serializer = self.get_serializer(data=data_pedido)
=======
        # 1. API Externa: Obtener dólar
        valor_dolar = obtener_valor_dolar() or 950.0 
        
        # 2. Validar Pedido (Vendedor, Sucursal, Cliente)
        serializer = self.get_serializer(data=request.data)
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
        serializer.is_valid(raise_exception=True)
        pedido = serializer.save(valor_dolar_dia=valor_dolar)

        total_acumulado = 0
<<<<<<< HEAD

        # 4. Procesar y registrar cada ítem en el DetalleVenta
        for item in items_data:
            try:
                inv = InventarioSucursal.objects.select_related('producto').get(
                    producto_id=item['producto'], 
                    sucursal=pedido.sucursal
                )
            except InventarioSucursal.DoesNotExist:
                raise drf_serializers.ValidationError({
                    "error": f"El producto {item['producto']} no está registrado en la sucursal {pedido.sucursal.id}"
                })
=======
        # 3. EL FOR: Procesa cada producto del pedido
        items_data = request.data.get('items', [])

        for item in items_data:
            inv = InventarioSucursal.objects.get(
                producto_id=item['producto'], 
                sucursal=pedido.sucursal
            )
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
            
            # Control de Stock
            if inv.stock >= item['cantidad']:
                inv.stock -= item['cantidad']
                inv.save()
                
<<<<<<< HEAD
                precio_actual = inv.producto.precio
                sub = precio_actual * item['cantidad']
                
=======
                # Obtenemos el precio del producto
                precio_actual = inv.producto.precio
                sub = precio_actual * item['cantidad']
                
                # CORRECCIÓN AQUÍ: Usamos precio_actual en el print
                print(f"DEBUG: Precio encontrado: {precio_actual}") 
                
                # USAR EL NOMBRE EXACTO DEL MODELO
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
                DetalleVenta.objects.create(
                    pedido=pedido,
                    producto_id=item['producto'],
                    cantidad=item['cantidad'],
<<<<<<< HEAD
                    precio_unitario_historico=precio_actual,
=======
                    precio_unitario_historico=precio_actual, 
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
                    subtotal=sub
                )
                total_acumulado += sub
            else:
                raise drf_serializers.ValidationError({
                    "error": f"No hay stock suficiente para {inv.producto.nombre}. Disponible: {inv.stock}"
                })

<<<<<<< HEAD
        # 5. Guardar totales convirtiendo explícitamente a float para compatibilidad con DecimalField
        pedido.total = float(total_acumulado)
=======
        # 4. Guardar totales finales en el pedido
        pedido.total_clp = total_acumulado
        pedido.total_usd = float(total_acumulado) / valor_dolar
        pedido.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 4. Guardar totales finales en el pedido
        pedido.total_clp = total_acumulado
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
        pedido.total_usd = float(total_acumulado) / valor_dolar
        pedido.save()

        # Retornamos los datos frescos del objeto guardado
        serializer_final = self.get_serializer(pedido)
        return Response(serializer_final.data, status=status.HTTP_201_CREATED)


    # ACCIÓN PARA GENERAR LA FACTURA PDF EN TIEMPO REAL
    @action(detail=True, methods=['get'], url_path='generar_factura')
    def generar_factura(self, request, pk=None):
        try:
            pedido = self.get_object()
            # Forzamos la lectura limpia de los detalles guardados
            detalles = DetalleVenta.objects.filter(pedido=pedido).select_related('producto')
        except Pedido.DoesNotExist:
            return Response({"error": "Pedido no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Configuración de respuesta tipo PDF binario
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="factura_pedido_{pedido.id}.pdf"'

        # Configuración del documento PDF (márgenes y tamaño)
        doc = SimpleDocTemplate(response, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
        story = []
        styles = getSampleStyleSheet()

        # Estilos visuales
        style_title = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor("#1A365D"), spaceAfter=12)
        style_normal = ParagraphStyle('Normal', parent=styles['Normal'], fontSize=10, leading=14)
        style_bold = ParagraphStyle('Bold', parent=styles['Normal'], fontSize=10, leading=14, fontName="Helvetica-Bold")

        # --- Encabezado de la Empresa ---
        story.append(Paragraph("<b>FERREMAS S.A.</b>", style_title))
        story.append(Paragraph("Rut: 76.123.456-K<br/>Casa Central: Av. Vitacura 1234, Santiago<br/>Contacto: contacto@ferremas.cl", style_normal))
        story.append(Spacer(1, 15))
        story.append(Paragraph("<hr/>", style_normal))
        story.append(Spacer(1, 15))

        # --- Datos de la Factura y Cliente (CORREGIDO: pedido.fecha) ---
        fecha_formateada = pedido.fecha.strftime('%d/%m/%Y %H:%M') if pedido.fecha else 'Hoy'
        info_data = [
            [Paragraph(f"<b>N° FACTURA:</b> {pedido.id}", style_normal), Paragraph(f"<b>FECHA:</b> {fecha_formateada}", style_normal)],
            [Paragraph(f"<b>CLIENTE ID:</b> {pedido.cliente.id if pedido.cliente else 'N/A'}", style_normal), Paragraph(f"<b>VENDEDOR ID:</b> {pedido.vendedor.id if pedido.vendedor else 'N/A'}", style_normal)],
            [Paragraph(f"<b>TIPO ENTREGA:</b> {pedido.tipo_entrega.upper()}", style_normal), Paragraph(f"<b>ESTADO:</b> {pedido.estado.upper()}", style_normal)]
        ]
        t_info = Table(info_data, colWidths=[270, 270])
        t_info.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
        story.append(t_info)
        story.append(Spacer(1, 20))

        # --- Tabla de Productos / Items ---
        table_data = [[
            Paragraph("<b>Producto</b>", style_bold), 
            Paragraph("<b>Cant.</b>", style_bold), 
            Paragraph("<b>Precio Unit.</b>", style_bold), 
            Paragraph("<b>Subtotal</b>", style_bold)
        ]]

        # TRUCO MAESTRO: Sumamos los subtotales directamente aquí para pintar el total real en la tabla
        total_clp_calculado = 0

        for d in detalles:
            subtotal_item = int(float(d.subtotal)) if d.subtotal else 0
            total_clp_calculado += subtotal_item

            table_data.append([
                Paragraph(d.producto.nombre, style_normal),
                Paragraph(str(d.cantidad), style_normal),
                Paragraph(f"${int(float(d.precio_unitario_historico)):,}", style_normal),
                Paragraph(f"${subtotal_item:,}", style_normal)
            ])

        # Recalcular el total en USD basado en la suma de las filas impresas
        valor_dolar = float(pedido.valor_dolar_dia) if pedido.valor_dolar_dia else 950.0
        total_usd_calculado = float(total_clp_calculado) / valor_dolar

        # Agregar filas de totales dinámicos al final de la tabla
        table_data.append(["", "", Paragraph("<b>TOTAL CLP:</b>", style_bold), Paragraph(f"<b>${total_clp_calculado:,}</b>", style_bold)])
        table_data.append(["", "", Paragraph("<b>TOTAL USD:</b>", style_bold), Paragraph(f"<b>${total_usd_calculado:.2f}</b>", style_bold)])

        # Estilo de la tabla de productos
        t_productos = Table(table_data, colWidths=[240, 60, 120, 120])
        t_productos.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1A365D")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('BACKGROUND', (0,1), (-1,-3), colors.HexColor("#F7FAFC")),
            ('GRID', (0,0), (-1,-3), 0.5, colors.lightgrey),
            ('LINEABOVE', (2,-2), (3,-1), 1, colors.HexColor("#1A365D")),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        
        for i in range(4):
            table_data[0][i].style.textColor = colors.whitesmoke

        story.append(t_productos)
        
        # Construcción del PDF final
        doc.build(story)
        return response