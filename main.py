#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# 2026/04/01
# シンプルなミニチャット
# --------------------------------------------------

from langchain_ollama.llms import OllamaLLM
import readline

LLM_MODEL  = 'gemma3:12b'
OLLAMA_URL = 'http://192.168.1.64:11434'

def main():
    ollama = OllamaLLM(model=LLM_MODEL, base_url=OLLAMA_URL)

    print("minichat: 質問を入力してください。終了するには'exit'を入力。")

    while True:
        try:
            query = input("\n質問> ").strip()

            if query.lower() in ("exit", "quit", 'q', 'ｑ'):
                print("終了します")
                break

            if not query:
                continue

            answer = ollama.invoke(query)
            print(f"回答> {answer}")

        except EOFError:
            break
        except Exception as e:
            print(f"\nエラー: {e}")

if __name__ == "__main__":
    main()
