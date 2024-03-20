import tkinter as tk

#function
def check_winner():
    winner = ""
    if btn1["text"] == btn2["text"] == btn3["text"] != "":
        winner = btn1["text"]
    elif btn4["text"] == btn5["text"] == btn6["text"] != "":
        winner = btn4["text"]
    elif btn7["text"] == btn3["text"] == btn9["text"] != "":
        winner = btn7["text"]
    elif btn1["text"] == btn4["text"] == btn7["text"] != "":
        winner = btn1["text"]
    elif btn2["text"] == btn5["text"] == btn8["text"] != "":
        winner = btn2["text"]
    elif btn3["text"] == btn6["text"] == btn9["text"] != "":
        winner = btn3["text"]
    elif btn1["text"] == btn5["text"] == btn9["text"] != "":
        winner = btn1["text"]
    elif btn3["text"] == btn5["text"] == btn7["text"] != "":
        winner = btn3["text"]
    if winner != "":
        lbl_winner["text"] == f"winner:{winner}"
        btn1["state"] = btn2["state"] = btn3["state"] = btn4["state"] = btn5["state"] = btn6["state"] = btn7["state"] = btn8["state"] = btn9["state"] = tk.DISABLED
        
def click_btn1():
    if btn1['text'] == "":
        btn1['text'] = turn
        check_winner()
        change_turn()
        
def click_btn2():
    if btn2['text'] == "":
        btn2['text'] = turn
        check_winner()
        change_turn()
        
def click_btn3():
    if btn3['text'] == "":
        btn3['text'] = turn
        check_winner()
        change_turn()
        
def click_btn4():
    if btn4['text'] == "":
        btn4['text'] = turn
        check_winner()
        change_turn()
        
def click_btn5():
    if btn5['text'] == "":
        btn5['text'] = turn
        check_winner()
        change_turn()
        
def click_btn6():
    if btn6['text'] == "":
        btn6['text'] = turn
        check_winner()
        change_turn()
        
def click_btn7():
    if btn7['text'] == "":
        btn7['text'] = turn
        check_winner()
        change_turn()
        
def click_btn8():
    if btn8['text'] == "":
        btn8['text'] = turn
        check_winner()
        change_turn()
        
def click_btn9():
    if btn9['text'] == "":
        btn9['text'] = turn
        check_winner()
        change_turn()
        
def change_turn():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    lbl_turn["text"] = f"Turn: {turn}"
    
def reset():
    global turn
    turn = "X"
    lbl_turn["text"] = f"Turn: {turn}"
    btn1["text"] = btn2["text"] = btn3["text"] = btn4["text"] = btn5["text"] = btn6["text"] = btn7["text"] = btn8["text"] = btn9["text"] = ""
    btn1["state"] = btn2["state"] = btn3["state"] = btn4["state"] = btn5["state"] = btn6["state"] = btn7["state"] = btn8["state"] = btn9["state"] = tk.NORMAL
    lbl_winner["text"] = ""


root =tk.Tk()
root.geometry("300x300")
root.title("tiktaktu")

# widgets declarations
center_window = tk.Frame(root, width=300, height=300)
lbl_turn = tk.Label(center_window, text="Turn: X")
btn1 = tk.Button(center_window, text="", command=click_btn1)
btn2 = tk.Button(center_window, text="", command=click_btn2)
btn3 = tk.Button(center_window, text="", command=click_btn3)
btn4 = tk.Button(center_window, text="", command=click_btn4)
btn5 = tk.Button(center_window, text="", command=click_btn5)
btn6 = tk.Button(center_window, text="", command=click_btn6)
btn7 = tk.Button(center_window, text="", command=click_btn7)
btn8 = tk.Button(center_window, text="", command=click_btn8)
btn9 = tk.Button(center_window, text="", command=click_btn9)
lbl_winner = tk.Button(center_window, text="")
turn = "X"
resetbtn = tk.Button(center_window, text="Reset", command=reset)

#widget placement
lbl_turn.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0, sticky="ew", ipadx=20, ipady=20)
btn2.grid(row=1, column=1, sticky="ew", ipadx=20, ipady=20)
btn3.grid(row=1, column=2, sticky="ew", ipadx=20, ipady=20)
btn4.grid(row=2, column=0, sticky="ew", ipadx=20, ipady=20)
btn5.grid(row=2, column=1, sticky="ew", ipadx=20, ipady=20)
btn6.grid(row=2, column=2, sticky="ew", ipadx=20, ipady=20)
btn7.grid(row=3, column=0, sticky="ew", ipadx=20, ipady=20)
btn8.grid(row=3, column=1, sticky="ew", ipadx=20, ipady=20)
btn9.grid(row=3, column=2, sticky="ew", ipadx=20, ipady=20)

lbl_winner.grid(row=40, column=0, columnspan=3)
resetbtn.grid(row=5, column=0, columnspan=3)
center_window.pack()

root.mainloop()

            
    
        
        