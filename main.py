import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import re
import pyperclip


def replace_delimiters(text):
    # Replace \[ \] with $$
    text = re.sub(r'\\\[', r'$$', text)
    text = re.sub(r'\\\]', r'$$', text)

    # Replace \( \) with $
    text = re.sub(r'\\\(', r'$', text)
    text = re.sub(r'\\\)', r'$', text)

    return text


def on_convert():
    original_text = input_text.get("1.0", tk.END)
    converted_text = replace_delimiters(original_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, converted_text)


def on_copy():
    converted_text = output_text.get("1.0", tk.END)
    pyperclip.copy(converted_text)
    messagebox.showinfo("信息", "转换后的文本已复制到剪贴板。")


# 创建主窗口
root = tk.Tk()
root.title("定界符替换器")

# 创建输入文本框
input_label = tk.Label(root, text="输入文本:")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_text.pack(padx=10, pady=5)

# 创建转换按钮
convert_button = tk.Button(root, text="转换", command=on_convert)
convert_button.pack(pady=5)

# 创建输出文本框
output_label = tk.Label(root, text="输出文本:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_text.pack(padx=10, pady=5)

# 创建复制按钮
copy_button = tk.Button(root, text="复制", command=on_copy)
copy_button.pack(pady=5)

# 运行主循环
root.mainloop()
