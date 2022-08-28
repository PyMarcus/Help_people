import pyautogui as pyautogui
import pyttsx3 as py
import speech_recognition as sr
from typing import TypeVar, Any
from selenium import webdriver
from selenium.webdriver.common.by import By

T = TypeVar("T")


def recognition() -> None:
    engine = py.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)


def speak(audio: Any, engine: T) -> None:
    engine.say(audio)
    engine.runAndWait()


def get() -> T:
    recognition_ = sr.Recognizer()
    return recognition_


def interation() -> str or None:
    with sr.Microphone() as source:
        print(f"[*]Por favor, diga algo...")
        audio = get().listen(source)
        print(f"[*]Escutei")
        try:
            text = get().recognize_google(audio, language='pt-BR')
            with sr.Microphone() as source2:
                print(f"[*]Voce disse {text}?")
                audio = get().listen(source2)
                confirmation = get().recognize_google(audio, language='pt-BR')
                if confirmation == "sim":
                    return text
                else:
                    print(f"[*]Por favor, repita: ")
                    with sr.Microphone() as source3:
                        audio = get().listen(source3)
                        try:
                            text = get().recognize_google(audio, language='pt-BR')
                            return text
                        except Exception as e:
                            print(f"Não reconheci")
        except Exception as e:
            print(f"[-]ERRO: Não entendi")


def navigation() -> None:
    text: str = interation()
    if text is not None:
        driver = webdriver.Firefox()
        driver.get("https://www.google.com.br")
        driver.find_element(By.TAG_NAME, "input").send_keys(text)
        pyautogui.hotkey('enter')


def main() -> None:
    navigation()


if __name__ == '__main__':
    main()
