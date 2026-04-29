import os
import logging
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Guatemala siempre esta en UTC-6, sin horario de verano
ZONA_GUATEMALA = timezone(timedelta(hours=-6))


async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Saluda al usuario que envia el comando."""
    nombre = update.effective_user.first_name
    await update.message.reply_text(
        f"Hola, {nombre}! Soy el bot del Grupo 12 para el curso de Inteligencia Artificial 1.\n"
        "Usa /ayuda para ver que comandos tengo disponibles."
    )


async def hora(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde con la hora actual en Guatemala (UTC-6)."""
    ahora = datetime.now(ZONA_GUATEMALA)
    hora_formato = ahora.strftime("%H:%M:%S")
    fecha_formato = ahora.strftime("%d/%m/%Y")
    await update.message.reply_text(
        f"La hora actual en Guatemala es:\n"
        f"Fecha: {fecha_formato}\n"
        f"Hora:  {hora_formato} (UTC-6)"
    )


async def contacto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Muestra la informacion de contacto del grupo."""
    await update.message.reply_text(
        "Integrantes del Grupo 12:\n\n"
        "Jose Alberto Alarcon Chigua\n"
        "Carne: 201346084\n\n"
        "Curso: Inteligencia Artificial 1\n"
        "Universidad San Carlos de Guatemala\n"
        "Facultad de Ingenieria"
    )


async def proyecto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Describe el Proyecto 2: HandTalk AI."""
    await update.message.reply_text(
        "Proyecto 2 - HandTalk AI\n\n"
        "Sistema de reconocimiento de senas del lenguaje LENSEGUA en tiempo real.\n\n"
        "Tecnologias utilizadas:\n"
        "- MediaPipe: extraccion de landmarks de la mano\n"
        "- scikit-learn: clasificacion con Random Forest / SVM\n"
        "- Flask: API REST para predicciones\n"
        "- Vue 3 + Vite: interfaz web\n"
        "- Docker: contenedores para despliegue\n\n"
        "Senas reconocidas: hola, gracias, si, no, ayuda, agua, bien, mal, por_favor, casa\n\n"
        "Repositorio: https://github.com/iamjalberto/IA1_1S2026_G12_Proyecto2"
    )


async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Lista todos los comandos disponibles."""
    await update.message.reply_text(
        "Comandos disponibles:\n\n"
        "/hola      - Saludo del bot\n"
        "/hora      - Hora actual en Guatemala\n"
        "/contacto  - Informacion del grupo\n"
        "/proyecto  - Descripcion del Proyecto 2\n"
        "/ayuda     - Muestra este mensaje"
    )


def main() -> None:
    if not TOKEN:
        raise ValueError("No se encontro TELEGRAM_TOKEN en el archivo .env")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("hola", hola))
    app.add_handler(CommandHandler("hora", hora))
    app.add_handler(CommandHandler("contacto", contacto))
    app.add_handler(CommandHandler("proyecto", proyecto))
    app.add_handler(CommandHandler("ayuda", ayuda))

    logger.info("Bot iniciado, esperando mensajes...")
    app.run_polling()


if __name__ == "__main__":
    main()
