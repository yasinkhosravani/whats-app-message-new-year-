
import webbrowser
import keyboard
import time
import os
from urllib.parse import quote

x = ['989375853913']#Phone number
for i in range(0,len(x)):
    phone_number = x[i] # replace with your recipient's phone number
    mess = """با احترام و آرزوی بهترین‌ها برای شما، در این روزهای پایانی سال، آرزو می‌کنم که سال جدید با شادی، سلامتی و موفقیت برای شما آغاز شود. به امید فرا رسیدن نوروز باستانی، که نشانه تجدید حیات، آرامش و توفیق برای همه ماست. عیدتان پیشاپیش مبارک

    یاسین خسروانی"""
    base_url = "https://web.whatsapp.com/"# Define the base URL and the message URL
    message_url = f"https://web.whatsapp.com/send?phone={phone_number}&text="+ quote(mess)
    webbrowser.open(message_url)#open web


    # Wait for the user to focus on the input field
    time.sleep(20)

    # Simulate the press of the "Enter" key
    keyboard.press_and_release('enter')

    time.sleep(15)

    # Send a keyboard shortcut to close the current tab in Google Chrome
    os.system("echo 'tell application \"Google Chrome\" to tell the active tab of its first window to close' | osascript")
else :
     os.system("pkill -f 'Google Chrome'") #close all tab chrome

