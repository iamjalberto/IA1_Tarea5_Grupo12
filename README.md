# Tarea 5 - Bot de Telegram IA1

**Curso:** Inteligencia Artificial 1  
**Universidad San Carlos de Guatemala**  
**Grupo 12**

## Integrantes

| Nombre | Carne |
|--------|-------|
| Jose Alberto Pineda Calderon | 201346084 |

## Descripcion

Bot de Telegram que funciona como mini asistente del proyecto para el curso de Inteligencia Artificial 1. Responde a comandos informativos sobre el grupo y el proyecto principal.

## Comandos disponibles

| Comando | Descripcion |
|---------|-------------|
| `/hola` | Saluda al usuario por su nombre |
| `/hora` | Muestra la hora actual en Guatemala (UTC-6) |
| `/contacto` | Muestra el nombre y carne del integrante del grupo |
| `/proyecto` | Describe el Proyecto 2 (HandTalk AI) con enlace al repositorio |
| `/ayuda` | Lista todos los comandos disponibles |

## Bot

Busca el bot en Telegram: [@IA1_G12_bot](https://t.me/IA1_G12_bot)

## Instalacion y ejecucion

```bash
# Clonar el repositorio
git clone https://github.com/iamjalberto/IA1_Tarea5_Grupo12
cd IA1_Tarea5_Grupo12

# Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar token
cp .env.example .env
# Editar .env y colocar el token real de BotFather

# Ejecutar el bot
python bot.py
```

## Tecnologias utilizadas

- Python 3.10+
- [python-telegram-bot](https://python-telegram-bot.org/) v20+
- python-dotenv

## Licencia

MIT
