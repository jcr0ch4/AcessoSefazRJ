#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
#usuario = raw_input("Informe o seu usuario : ")
#senha = raw_input("Informe a sua senha : ")

browser = webdriver.Firefox()
#browser.get("https://www4.fazenda.rj.gov.br/ssa/?msg=")
# Autenticação Via Certificado Digital
browser.get("https://www4.fazenda.rj.gov.br/ssa/certificadoWeb")
time.sleep(1)
username = browser.find_element_by_xpath("//*[@type='text']")
password = browser.find_element_by_xpath("//*[@type='password']")
username.send_keys(usuario)
password.send_keys(senha)
login_attempt = browser.find_element_by_xpath("//button[contains(text(),'ENTRAR')]")
login_attempt.click()
# Entra na Secretaria
secretaria = browser.find_element_by_xpath("//button[@title='[S] SECRETARIA']")
time.sleep(2)
secretaria.send_keys(Keys.BACKSPACE)
secretaria.submit()
secretaria.send_keys(Keys.ENTER)
time.sleep(2)
# Entra no Controle de Reunioes
c1,c2 = pyautogui.locateCenterOnScreen('ccb/controleReuniao.png')
pyautogui.click(c1,c2)
