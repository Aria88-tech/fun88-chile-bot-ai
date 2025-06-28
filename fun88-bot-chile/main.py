import os, asyncio, nest_asyncio, openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

nest_asyncio.apply()

openai.api_key = os.getenv("OPENAI_API_KEY")
TOKEN = "TU_TELEGRAM_TOKEN_AQUI"

async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"🙌 ¡Bienvenido {user.first_name}! Este es el grupo de Fun88 Chile 🇨🇱"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="¿Qué te interesa? Deportes, Tragamonedas, Casino o Juegos de mesa"
        )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "deposit" in msg or "depositar" in msg:
        await update.message.reply_text(
            "💰 Para depositar entra en https://www.fun88chile.com y sigue los pasos."
        )
    elif "retiro" in msg:
        await update.message.reply_text(
            "🏧 Puedes retirar hasta CLP 9.000.000 siguiendo los pasos en Fun88."
        )
    elif "bono" in msg:
        await update.message.reply_text(
            "🎁 Revisa los bonos aquí: https://www.fun88chile.com/promotions"
        )
    else:
        # fallback IA
        prompt = f"Usuario pregunta: {update.message.text}"
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": prompt}],
            max_tokens=150, temperature=0.7
        )
        respuesta = resp.choices[0].message.content.strip()
        await update.message.reply_text(respuesta)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
