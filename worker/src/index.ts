import { Bot, webhookCallback } from "grammy";

export interface Env {
  TELEGRAM_TOKEN: string;
}

// Se crea el bot con los handlers cada vez que llega una peticion.
// Cloudflare Workers es stateless, por lo que este patron es el correcto.
function crearBot(token: string): Bot {
  const bot = new Bot(token);

  bot.command("hola", async (ctx) => {
    const nombre = ctx.from?.first_name ?? "usuario";
    await ctx.reply(
      `Hola, ${nombre}! Soy el bot del Grupo 12 para el curso de Inteligencia Artificial 1.\n` +
        `Usa /ayuda para ver que comandos tengo disponibles.`,
    );
  });

  bot.command("hora", async (ctx) => {
    const ahora = new Date();
    // Guatemala no tiene horario de verano, siempre UTC-6
    const fecha = new Intl.DateTimeFormat("es-GT", {
      timeZone: "America/Guatemala",
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    }).format(ahora);
    const hora = new Intl.DateTimeFormat("es-GT", {
      timeZone: "America/Guatemala",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: false,
    }).format(ahora);
    await ctx.reply(
      `La hora actual en Guatemala es:\n` +
        `Fecha: ${fecha}\n` +
        `Hora:  ${hora} (UTC-6)`,
    );
  });

  bot.command("contacto", async (ctx) => {
    await ctx.reply(
      "Integrantes del Grupo 12:\n\n" +
        "Jose Alberto Pineda Calderon\n" +
        "Carne: 201346084\n\n" +
        "Curso: Inteligencia Artificial 1\n" +
        "Universidad San Carlos de Guatemala\n" +
        "Facultad de Ingenieria",
    );
  });

  bot.command("proyecto", async (ctx) => {
    await ctx.reply(
      "Proyecto 2 - HandTalk AI\n\n" +
        "Sistema de reconocimiento de senas del lenguaje LENSEGUA en tiempo real.\n\n" +
        "Tecnologias utilizadas:\n" +
        "- MediaPipe: extraccion de landmarks de la mano\n" +
        "- scikit-learn: clasificacion con Random Forest / SVM\n" +
        "- Flask: API REST para predicciones\n" +
        "- Vue 3 + Vite: interfaz web\n" +
        "- Docker: contenedores para despliegue\n\n" +
        "Senas reconocidas: hola, gracias, si, no, ayuda, agua, bien, mal, por_favor, casa\n\n" +
        "Repositorio: https://github.com/iamjalberto/IA1_1S2026_G12_Proyecto2",
    );
  });

  bot.command("ayuda", async (ctx) => {
    await ctx.reply(
      "Comandos disponibles:\n\n" +
        "/hola      - Saludo del bot\n" +
        "/hora      - Hora actual en Guatemala\n" +
        "/contacto  - Informacion del grupo\n" +
        "/proyecto  - Descripcion del Proyecto 2\n" +
        "/ayuda     - Muestra este mensaje",
    );
  });

  return bot;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const bot = crearBot(env.TELEGRAM_TOKEN);
    const handleUpdate = webhookCallback(bot, "cloudflare-mod");
    return handleUpdate(request);
  },
};
