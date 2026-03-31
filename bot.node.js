const { Telegraf } = require('telegraf');
const fetch = require('node-fetch');
require('dotenv').config();

const TOKEN = process.env.TELEGRAM_TOKEN;
const API_QUOTE_URL = process.env.API_QUOTE_URL || 'https://api.quotable.io/random';

if (!TOKEN) {
  throw new Error('TELEGRAM_TOKEN não encontrado. Crie .env com TELEGRAM_TOKEN=xxx');
}

const bot = new Telegraf(TOKEN);

bot.start((ctx) => ctx.reply('Olá! Sou o BotMarcela (Node). Use /help para ver comandos.'));

bot.help((ctx) => {
  ctx.reply('/start - iniciar\n/help - ajuda\n/echo <texto> - repete texto\n/hora - hora atual\n/quote - frase de API');
});

bot.command('echo', (ctx) => {
  const text = ctx.message.text.split(' ').slice(1).join(' ');
  if (!text) {
    ctx.reply('Use: /echo texto');
    return;
  }
  ctx.reply(text);
});

bot.command('hora', (ctx) => {
  const now = new Date().toISOString().replace('T', ' ').substring(0, 19);
  ctx.reply(`Agora são: ${now}`);
});

bot.command('quote', async (ctx) => {
  try {
    ctx.reply('Buscando frase da API...');
    const res = await fetch(API_QUOTE_URL);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    const text = data.content || data.quote || data.text;
    const author = data.author || data.from || 'desconhecido';
    if (!text) throw new Error('Resposta de API mal formada');
    ctx.reply(`"${text}"\n- ${author}`);
  } catch (err) {
    console.error('Erro quote:', err);
    ctx.reply('Desculpe, não consegui obter a frase da API. Tente mais tarde.');
  }
});

bot.on('text', (ctx) => {
  if (ctx.message.text.startsWith('/')) return; // ignora comandos já tratados
  ctx.reply('Desculpe, não entendi. Use /help.');
});

bot.launch();
console.log('Bot Marcela (Node) iniciado');

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
