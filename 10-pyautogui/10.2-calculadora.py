# Abrir a calculadora do Windows e realizar uma operação simples.
import pyautogui

# Abre o Executar do Windows
pyautogui.hotkey('win','r')
pyautogui.sleep(1)

# Digita 'calc' e pressiona Enter para abrir a calculadora
pyautogui.write('calc',interval=0.5)
pyautogui.press('enter')
pyautogui.sleep(3)

# Realiza a operação 20 + 20
pyautogui.write('20')
pyautogui.press('+')
pyautogui.write('20')
pyautogui.press('enter')

# Alerta informando que a operação foi concluída
pyautogui.alert('Operação concluída! Verifique o resultado na calculadora.')