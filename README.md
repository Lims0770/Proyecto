# Proyecto
# Analizador de Puertos Simplificado
## Descripción:

Este programa es un analizador de puertos simple que te permite verificar si un puerto específico está abierto o cerrado en una dirección IP o nombre de host determinado.

## Uso:

```python analizador_puertos.py -d <direccion> -p <puertos> [-t <hilos>]```

### Opciones:

-d (--direccion): La dirección IP o nombre del host a analizar.
-p (--puertos): Los puertos a analizar, separados por comas.
-t (--hilos): Número de hilos a usar (por defecto: 10).

## Ejemplo:

```python analizador_puertos.py -d google.com -p 80,443,22```
#### Salida:

Puerto 80: Abierto

Puerto 443: Abierto

Puerto 22: Cerrado


## Nota:

Este programa solo verifica si un puerto está abierto o cerrado. No realiza ninguna otra prueba.
Se recomienda usar este programa con fines educativos o de investigación.
## Índice
Descripción: #descripcion
Uso: #uso
Opciones: #opciones
Ejemplo: #ejemplo
Salida: #salida
Nota: #nota
