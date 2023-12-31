{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e71c7331",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       English        Arabic\n",
      "0         part           جزء\n",
      "1      history         تاريخ\n",
      "2       search          يبحث\n",
      "3         only           فقط\n",
      "4       police          شرطة\n",
      "..         ...           ...\n",
      "96      rather         بدلاً\n",
      "97   will have  سوف نحصل على\n",
      "98       girls         فتيات\n",
      "99     to play          للعب\n",
      "100     office          مكتب\n",
      "\n",
      "[101 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "from tkinter import *\n",
    "import pandas as pd\n",
    "import random\n",
    "BACKGROUND_COLOR = \"#B1DDC6\"\n",
    "current_card = {}\n",
    "to_learn = {}\n",
    "\n",
    "\n",
    "try:\n",
    "    data = pd.read_csv(\"data/words_to_learn.csv\")\n",
    "except FileNotFoundError:\n",
    "    original_data = pd.read_csv(\"data/ar-en-data.csv\")\n",
    "    print(original_data)\n",
    "    to_learn = original_data.to_dict(orient=\"records\")\n",
    "else:\n",
    "    to_learn = data.to_dict(orient=\"records\")\n",
    "\n",
    "##\n",
    "def next_card():\n",
    "    global current_card , flip_timer\n",
    "    window.after_cancel(flip_timer)\n",
    "    current_card = random.choice(to_learn)\n",
    "    canvas.itemconfig(card_tiitle , text=\"English\" , fill=\"black\")\n",
    "    canvas.itemconfig(card_word , text=current_card[\"English\"],fill=\"black\")\n",
    "    canvas.itemconfig(card_background , image=front_img)\n",
    "    flip_timer = window.after(3000 , func=flip_card)\n",
    "\n",
    "    \n",
    "def flip_card():\n",
    "    canvas.itemconfig(card_tiitle , text=\"Arabic\",  fill=\"white\")\n",
    "    canvas.itemconfig(card_word , text=current_card[\"Arabic\"] , fill=\"white\")\n",
    "    canvas.itemconfig(card_background , image=back_img)\n",
    "\n",
    "    \n",
    "def is_known():\n",
    "    to_learn.remove(current_card)\n",
    "    print(len(to_learn))\n",
    "    data = pd.DataFrame(to_learn)\n",
    "    data.to_csv(\"data/words_to_learn.csv\", index=False)\n",
    "    next_card()\n",
    "    \n",
    "\n",
    "window = Tk()\n",
    "window.title(\"translate\")\n",
    "window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)\n",
    "\n",
    "flip_timer = window.after(3000 , func=flip_card)\n",
    "\n",
    "##\n",
    "canvas = Canvas(width=800,height=526)\n",
    "front_img = PhotoImage(file=\"images/card_front.png\")\n",
    "back_img = PhotoImage(file=\"images/card_back.png\")\n",
    "\n",
    "card_background = canvas.create_image(400,263,image=front_img)\n",
    "card_tiitle = canvas.create_text(400,150,text=\"\",font=(\"Arial\",40,\"italic\"))\n",
    "card_word = canvas.create_text(400,263,text=\"\",font=(\"Arial\",60,\"bold\"))\n",
    "\n",
    "canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)\n",
    "canvas.grid(row=0,column=0,columnspan=2)\n",
    "\n",
    "##\n",
    "wrong_img = PhotoImage(file=\"images/wrong.png\")\n",
    "wrong_btn = Button(image=wrong_img, command=next_card)\n",
    "wrong_btn.config(bg=BACKGROUND_COLOR,highlightthickness=0)\n",
    "\n",
    "##\n",
    "right_img = PhotoImage(file=\"images/right.png\")\n",
    "right_btn = Button(image=right_img , command=is_known)\n",
    "right_btn.config(bg=BACKGROUND_COLOR,highlightthickness=0)\n",
    "\n",
    "wrong_btn.grid(row=1,column=0)\n",
    "right_btn.grid(row=1,column=1)\n",
    "\n",
    "next_card()\n",
    "window.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b35bd209",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58173b7c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
