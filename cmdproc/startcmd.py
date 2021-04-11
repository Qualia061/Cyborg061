#!/usr/bin/env python3

"""
支持 /start 和 /help
"""

import config
from telegram import Update,BotCommand
from telegram.ext import Dispatcher,CommandHandler,CallbackContext

def help():
    return """

    /weather - 查询天气
    /help - 查看帮助

    开发者用命令：
    /info 将任意信息的json内容发给你
    /ainfo 用这个命令回复一个信息，它会把里面的特殊内容的Python对象声明返回给你

    管理员用命令：
    /admin 管理机器人
    """

def help_city():
    return """
    /weather - 查询天气 
    /help - 查看帮助
    """

def start(update : Update, context : CallbackContext):
    msg = help()
    update.message.reply_text(msg)

def start_city(update : Update, context : CallbackContext):
    update.message.reply_text(help_city())

def add_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler(["start","help"], start))
    return [BotCommand('help','获取帮助')]

def add_dispather_city(dp: Dispatcher):
    dp.add_handler(CommandHandler(["start","help"], start_city))
    return [BotCommand('help','获取帮助')]
