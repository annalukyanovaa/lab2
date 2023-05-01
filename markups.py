from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain=KeyboardButton('👈ГЛАВНОЕ МЕНЮ')

btnAbit=KeyboardButton('АБИТУРИЕНТ')
btnStud=KeyboardButton('ПЕРВОКУРСНИК')
mainMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(btnAbit,btnStud)

otherMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1 = ["📌МИН БАЛЛЫ ЕГЭ 2023"]
buttons2 = ["📌ИНФОРМАЦИЯ О ВУЗЕ"]
buttons3= ["📌НАПРАВЛЕНИЯ ПОДГОТОВКИ И СПЕЦИАЛЬНОСТЕЙ"]
buttons4 = ["📌ПРИЕМНАЯ КОМИССИЯ"]
buttons5 = ["📌ИНФОРМАЦИЯ О ХОДЕ ПРИЕМА"]
otherMenu.add(*buttons1)
otherMenu.add(*buttons2)
otherMenu.add(*buttons3)
otherMenu.add(*buttons4)
otherMenu.add(*buttons5)
otherMenu.add(btnMain)

otherMenu2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons6=["📌СХЕМА РАСПОЛОЖЕНИЯ КОРПУСОВ"]
buttons7=["📌АДРЕСА КОРПУСОВ"]
buttons8=["📌РАСПИСАНИЕ ЗАНЯТИЙ"]
otherMenu2.add(*buttons6)
otherMenu2.add(*buttons7)
otherMenu2.add(*buttons8)
otherMenu2.add(btnMain)