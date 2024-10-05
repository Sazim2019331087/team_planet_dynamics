from datetime import date
import random
from customtkinter import *
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mc
from CTkMessagebox import CTkMessagebox
from pygame import mixer
from tkintermapview import TkinterMapView
import pandas as pd
from matplotlib.animation import FuncAnimation
from tkinterweb import *
import matplotlib.pyplot as plt
import requests
import numpy as np

set_appearance_mode("Light")
set_default_color_theme("green")
app = CTk()
app.geometry("1000x600")
app.resizable(0,0)
app.title("Planet Dynamics")
'''
img = CTkImage(light_image=Image.open("demo_bg_pic.png"), size= (1000,600))
image_place = CTkLabel(master = app,text = "", image = img)
image_place.pack(pady = 0,padx = 0,expand = True)
'''
#==================Establishing Database Connection=========================================
host = "localhost"
user = "root"
password = "password"
db = "planet_dynamics"
port = 4306
con = mc.connect(
    host = host,
    user = user,
    password = password,
    database = db,
    port = port
)

cur = con.cursor()

def dashboard(email):
    # ========all non friend users=============
    sql_for_all_users_non_friend = f"""
    SELECT DISTINCT
        CASE
            WHEN from_ != '{email}' THEN from_
            ELSE to_
        END AS user_email
    FROM friends
    WHERE from_ != '{email}' AND to_ != '{email}';
    """
    cur.execute(sql_for_all_users_non_friend)
    result_all_non_friends_name = cur.fetchall()

    # ========user name=============
    sql_for_user_details = f"SELECT * FROM learner where email='{email}'"
    cur.execute(sql_for_user_details)
    result_user_name = cur.fetchall()
    user_name = result_user_name[0][1]
    # =======total coins=============
    sql_for_user_coin = f"SELECT * from coins where email='{email}'"
    cur.execute(sql_for_user_coin)
    result_user_coin = cur.fetchall()
    user_coin = result_user_coin[0][1]
    # ========friends number===========
    sql_for_user_friend = f"select to_ from friends where from_='{email}'"
    cur.execute(sql_for_user_friend)
    result_user_friend = cur.fetchall()
    user_friend_number = len(result_user_friend)
    # ======own blog fetch=======
    sql_for_user_blog = f"select * from blogs where email='{email}'"
    cur.execute(sql_for_user_blog)
    result_user_blog = cur.fetchall()
    user_blog_number = len(result_user_blog)
    # ======other blog fetch=======
    sql_for_other_blog = f"select * from blogs where email != '{email}'"
    cur.execute(sql_for_other_blog)
    result_other_blog = cur.fetchall()
    # ========follower number===========
    sql_for_user_follower = f"select from_ from friends where to_='{email}'"
    cur.execute(sql_for_user_follower)
    result_user_follower = cur.fetchall()
    user_follower_number = len(result_user_follower)
    mixer.init()

    image_frame.pack_forget()
    welcome_frame.pack_forget()

    def clear_base_content():
        for w in base_content.winfo_children():
            w.pack_forget()

    def activation_signal():
        b0.configure(fg_color="#4CAF50")
        b1.configure(fg_color="#4CAF50")
        b2.configure(fg_color="#4CAF50")
        b3.configure(fg_color="#4CAF50")
        b4.configure(fg_color="#4CAF50")

    def climate_learning_hub():
        clear_base_content()

        def climate_science_lesson():
            clear_base_content()
            def climate_science_lesson_one():
                def raise_course_info_and_contents_frame():
                    less_1_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_1_tab = CTkTabview(base_content)
                less_1_tab.pack(side = LEFT, fill = BOTH, expand = True)
                lesson_one = less_1_tab.add("Lesson 1")
                quiz = less_1_tab.add("Quiz")
                all_lessons = less_1_tab.add("Audio Book")

                def pause_audio():
                    mixer.music.pause()
                    pause_audiobtn.configure(state="disabled")
                    start_audiobtn.configure(state="disabled")
                    unpause_audiobtn.configure(state="normal")
                    stop_audiobtn.configure(state="normal")

                def unpause_audio():
                    mixer.music.unpause()
                    stop_audiobtn.configure(state="normal")
                    pause_audiobtn.configure(state="normal")
                    unpause_audiobtn.configure(state="disabled")
                    start_audiobtn.configure(state="disabled")
                def unpack_audio():
                    mixer.music.stop()
                    stop_audiobtn.configure(state="disabled")
                    start_audiobtn.configure(state="normal")
                    pause_audiobtn.configure(state="disabled")
                    unpause_audiobtn.configure(state="disabled")
                def pack_audio(filepath):
                    mixer.music.load(filepath)
                    mixer.music.play()
                    mixer.music.set_volume(0.8)
                    start_audiobtn.configure(state="disabled")
                    unpause_audiobtn.configure(state="normal")
                    pause_audiobtn.configure(state="normal")
                    stop_audiobtn.configure(state="normal")
                    stop_audio_btn.pack()

                audio_path = "./climate_science/voices/lesson_01.mp3"
                start_audiobtn = CTkButton(all_lessons,text="START",command = lambda : pack_audio(audio_path))
                pause_audiobtn = CTkButton(all_lessons, text="PAUSE", command=pause_audio)
                unpause_audiobtn = CTkButton(all_lessons, text="UNPAUSE", command=unpause_audio)
                stop_audiobtn = CTkButton(all_lessons, text="STOP", command=unpack_audio)
                start_audiobtn.pack(side=TOP,expand=True)
                pause_audiobtn.pack(side=LEFT,expand=True)
                unpause_audiobtn.pack(side=RIGHT,expand=True)
                stop_audiobtn.pack(side=BOTTOM,expand=True)

                Go_to_All_Lesson = CTkButton(all_lessons,text="GO TO ALL LESSONS",command = raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                #print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_1.html"
                lesson_frame_01 = HtmlFrame(lesson_one, messages_enabled=False)
                lesson_frame_01.load_html(html_operation(file_path))
                lesson_frame_01.pack(expand = True, fill = BOTH)

                q1 = CTkLabel(quiz,
                              text="1) What is the primary source of energy that drives Earth’s climate system?\n[a] MOON [b] SUN [c] EARTH'S CORE [d] OCEAN'S CURRENT",
                              font=("Helvetica", 18, "bold"))
                q1.pack(pady=3)

                a1 = CTkComboBox(quiz, values=["Choose one", "MOON", "SUN", "EARTH'S CORE", "OCEAN'S CURRENT"])
                a1.pack(pady=2)

                def evaluate_quiz():
                    coins = 0
                    msg = ""
                    ico = ""
                    if a1.get() == "SUN":
                        coins += 10
                        ico = "check"
                        msg = "Congratulation"
                    else:
                        ico = "warning"
                        msg = "Wrong Answer"
                    quiz_mark = CTkMessagebox(title="Quiz Result", message=msg, icon=ico, option_1="Okay")
                    quiz_submit.configure(state="disabled")
                    present_coin = user_coin
                    present_coin_int = int(present_coin) + int(coins)
                    present_coin_str = str(present_coin_int)
                    sql_coin_update = f"UPDATE coins SET coin = '{present_coin_str}' where email='{email}'"
                    cur.execute(sql_coin_update)
                    con.commit()

                quiz_submit = CTkButton(quiz, text="SUBMIT", command=evaluate_quiz)
                quiz_submit.pack(pady=2)

            def climate_science_lesson_two():
                def raise_course_info_and_contents_frame():
                    less_2_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_2_tab = CTkTabview(base_content)
                less_2_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_two = less_2_tab.add("Lesson 2")
                quiz = less_2_tab.add("Quiz")
                all_lessons = less_2_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_2.html"
                lesson_frame_02 = HtmlFrame(lesson_two, messages_enabled=False)
                lesson_frame_02.load_html(html_operation(file_path))
                lesson_frame_02.pack(expand = True, fill = BOTH)

            def climate_science_lesson_three():
                def raise_course_info_and_contents_frame():
                    less_3_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_3_tab = CTkTabview(base_content)
                less_3_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_three = less_3_tab.add("Lesson 3")
                quiz = less_3_tab.add("Quiz")
                all_lessons = less_3_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_3.html"
                lesson_frame_03 = HtmlFrame(lesson_three, messages_enabled=False)
                lesson_frame_03.load_html(html_operation(file_path))
                lesson_frame_03.pack(expand = True, fill = BOTH)

            def climate_science_lesson_four():
                def raise_course_info_and_contents_frame():
                    less_4_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_4_tab = CTkTabview(base_content)
                less_4_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_four = less_4_tab.add("Lesson 4")
                quiz = less_4_tab.add("Quiz")
                all_lessons = less_4_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_4.html"
                lesson_frame_04 = HtmlFrame(lesson_four, messages_enabled=False)
                lesson_frame_04.load_html(html_operation(file_path))
                lesson_frame_04.pack(expand = True, fill = BOTH)

            def climate_science_lesson_five():
                def raise_course_info_and_contents_frame():
                    less_5_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_5_tab = CTkTabview(base_content)
                less_5_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_five = less_5_tab.add("Lesson 5")
                quiz = less_5_tab.add("Quiz")
                all_lessons = less_5_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_5.html"
                lesson_frame_05 = HtmlFrame(lesson_five, messages_enabled=False)
                lesson_frame_05.load_html(html_operation(file_path))
                lesson_frame_05.pack(expand = True, fill = BOTH)

            def climate_science_lesson_six():
                def raise_course_info_and_contents_frame():
                    less_6_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_6_tab = CTkTabview(base_content)
                less_6_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_six = less_6_tab.add("Lesson 6")
                quiz = less_6_tab.add("Quiz")
                all_lessons = less_6_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_6.html"
                lesson_frame_06 = HtmlFrame(lesson_six, messages_enabled=False)
                lesson_frame_06.load_html(html_operation(file_path))
                lesson_frame_06.pack(expand = True, fill = BOTH)

            def climate_science_lesson_seven():
                def raise_course_info_and_contents_frame():
                    less_7_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_7_tab = CTkTabview(base_content)
                less_7_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_seven = less_7_tab.add("Lesson 7")
                quiz = less_7_tab.add("Quiz")
                all_lessons = less_7_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_7.html"
                lesson_frame_07 = HtmlFrame(lesson_seven, messages_enabled=False)
                lesson_frame_07.load_html(html_operation(file_path))
                lesson_frame_07.pack(expand = True, fill = BOTH)

            def climate_science_lesson_eight():
                def raise_course_info_and_contents_frame():
                    less_8_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_8_tab = CTkTabview(base_content)
                less_8_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_eight = less_8_tab.add("Lesson 8")
                quiz = less_8_tab.add("Quiz")
                all_lessons = less_8_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_8.html"
                lesson_frame_08 = HtmlFrame(lesson_eight, messages_enabled=False)
                lesson_frame_08.load_html(html_operation(file_path))
                lesson_frame_08.pack(expand = True, fill = BOTH)

            def climate_science_lesson_nine():
                def raise_course_info_and_contents_frame():
                    less_9_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_9_tab = CTkTabview(base_content)
                less_9_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_nine = less_9_tab.add("Lesson 9")
                quiz = less_9_tab.add("Quiz")
                all_lessons = less_9_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_9.html"
                lesson_frame_09 = HtmlFrame(lesson_nine, messages_enabled=False)
                lesson_frame_09.load_html(html_operation(file_path))
                lesson_frame_09.pack(expand = True, fill = BOTH)

            def climate_science_lesson_ten():
                def raise_course_info_and_contents_frame():
                    less_10_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_10_tab = CTkTabview(base_content)
                less_10_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_ten = less_10_tab.add("Lesson 10")
                quiz = less_10_tab.add("Quiz")
                all_lessons = less_10_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_10.html"
                lesson_frame_10 = HtmlFrame(lesson_ten, messages_enabled=False)
                lesson_frame_10.load_html(html_operation(file_path))
                lesson_frame_10.pack(expand = True, fill = BOTH)

            def climate_science_lesson_eleven():
                def raise_course_info_and_contents_frame():
                    less_11_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_11_tab = CTkTabview(base_content)
                less_11_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_eleven = less_11_tab.add("Lesson 11")
                quiz = less_11_tab.add("Quiz")
                all_lessons = less_11_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_11.html"
                lesson_frame_11 = HtmlFrame(lesson_eleven, messages_enabled=False)
                lesson_frame_11.load_html(html_operation(file_path))
                lesson_frame_11.pack(expand = True, fill = BOTH)
            def climate_science_lesson_twelve():
                def raise_course_info_and_contents_frame():
                    less_12_tab.pack_forget()
                    contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
                    course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

                def html_operation(file_path):
                    f = open(file_path, "r", encoding='utf-8')
                    h = f.read()
                    return h

                contents_frame.pack_forget()
                course_info_frame.pack_forget()
                less_12_tab = CTkTabview(base_content)
                less_12_tab.pack(side=LEFT, fill=BOTH, expand=True)
                lesson_twelve = less_12_tab.add("Lesson 12")
                quiz = less_12_tab.add("Quiz")
                all_lessons = less_12_tab.add("All Lessons")
                Go_to_All_Lesson = CTkButton(all_lessons, text="GO TO ALL LESSONS",
                                             command=raise_course_info_and_contents_frame)
                Go_to_All_Lesson.pack(side=BOTTOM)
                # print(less_1_tab.get())

                file_path = "./climate_science/lessons/lesson_12.html"
                lesson_frame_12 = HtmlFrame(lesson_twelve, messages_enabled=False)
                lesson_frame_12.load_html(html_operation(file_path))
                lesson_frame_12.pack(expand = True, fill = BOTH)

            base_title.configure(text="Climate Science Course")
            contents_frame = CTkScrollableFrame(base_content, width = 300, corner_radius= 5, border_width=3)
            contents_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
            contents_label = CTkLabel(contents_frame, text = "Contents", font = ("Helvetica", 20), text_color="green")
            contents_label.pack(side = TOP, fill = BOTH, pady =5, padx = 5)
            course_chapter1 = CTkButton(contents_frame, text = "Lesson 01", fg_color="#D3EE98", font = ("Bold", 20,"bold"), text_color="#FFB200", hover_color = "white", command = climate_science_lesson_one)
            course_chapter1.pack(side = TOP, pady = 10, padx = 5)
            course_chapter2 = CTkButton(contents_frame, text="Lesson 02", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                       text_color="#FFB200", hover_color="white", command=climate_science_lesson_two)
            course_chapter2.pack(side=TOP, pady=10, padx=5)
            course_chapter3 = CTkButton(contents_frame, text="Lesson 03", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_three)
            course_chapter3.pack(side=TOP, pady=10, padx=5)
            course_chapter4 = CTkButton(contents_frame, text="Lesson 04", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_four)
            course_chapter4.pack(side=TOP, pady=10, padx=5)
            course_chapter5 = CTkButton(contents_frame, text="Lesson 05", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_five)
            course_chapter5.pack(side=TOP, pady=10, padx=5)
            course_chapter6 = CTkButton(contents_frame, text="Lesson 06", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_six)
            course_chapter6.pack(side=TOP, pady=10, padx=5)
            course_chapter7 = CTkButton(contents_frame, text="Lesson 07", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_seven)
            course_chapter7.pack(side=TOP, pady=10, padx=5)
            course_chapter8 = CTkButton(contents_frame, text="Lesson 08", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_eight)
            course_chapter8.pack(side=TOP, pady=10, padx=5)
            course_chapter9 = CTkButton(contents_frame, text="Lesson 09", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_nine)
            course_chapter9.pack(side=TOP, pady=10, padx=5)
            course_chapter10 = CTkButton(contents_frame, text="Lesson 10", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_ten)
            course_chapter10.pack(side=TOP, pady=10, padx=5)
            course_chapter11 = CTkButton(contents_frame, text="Lesson 11", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_eleven)
            course_chapter11.pack(side=TOP, pady=10, padx=5)
            course_chapter12 = CTkButton(contents_frame, text="Lesson 12", fg_color="#D3EE98", font=("Bold", 20, "bold"),
                                        text_color="#FFB200", hover_color="white", command=climate_science_lesson_twelve)
            course_chapter12.pack(side=TOP, pady=10, padx=5)

            course_info_frame = CTkFrame(base_content, width=300, corner_radius= 5, border_width=3)
            course_info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
            course_info_label = CTkLabel(course_info_frame, text="Course Status", font=("Helvetica", 20), text_color="green")
            course_info_label.pack(side=TOP, fill=BOTH, pady=5, padx=5)
            lesson_percentage = np.array([30,70])
            lesson_label  = ["Completed","Incompleted"]
            explode_label = [0.1,0]
            plt.pie(lesson_percentage,labels=lesson_label,explode = explode_label)
            plt.savefig("course_status.jpg")
            pie_image = CTkImage(light_image= Image.open("course_status.jpg"), size = (300,300))
            pie_image_label = CTkLabel(course_info_frame, text = "", image = pie_image)
            pie_image_label.pack(pady = 10)
        def geology_lesson():
            clear_base_content()
            base_title.configure(text="Geology Course")





        def weather_lesson():
            clear_base_content()
            base_title.configure(text="Weather Course")

        def environment_science_lesson():
            clear_base_content()
            base_title.configure(text="Environment Science Course")

        base_title.configure(text="Climate Learning Hub")
        activation_signal()
        b1.configure(fg_color="red", hover_color="red")

        all_course_lable = CTkLabel(base_content, text="All Courses..", font=("Arial", 30), text_color="#FFB200")
        all_course_lable.pack(side = TOP, pady = 10, padx = 10)

        course_frame = CTkFrame(base_content, fg_color="#D3EE98")
        course_frame.pack(pady = 40)

        climate_science = CTkButton(course_frame, text = "Climate Science", height = 150, width = 120, font = ("Helvetica", 14), border_width=4, fg_color="#FFB200", border_color="#FFDE4D", text_color="white", hover_color= "#EB5B00", command = climate_science_lesson)
        climate_science.pack(side = LEFT, padx = 10)
        geology= CTkButton(course_frame, text = "Geology", height = 150, width = 120, font = ("Helvetica", 14), border_width=4, fg_color="#FFB200", border_color="#FFDE4D", text_color="white",hover_color="#EB5B00", command = geology_lesson)
        geology.pack(side = LEFT, padx = 10)
        weather = CTkButton(course_frame, text="Weather", height=150, width=120, font=("Helvetica", 14), border_width=4, fg_color="#FFB200", border_color="#FFDE4D", text_color="white", hover_color="#EB5B00", command = weather_lesson)
        weather.pack(side=LEFT, padx=10)
        environment_science = CTkButton(course_frame, text="Environment Science", height=150, width=120, font=("Helvetica", 14), border_width=4, fg_color="#FFB200", border_color="#FFDE4D", text_color="white", hover_color="#EB5B00", command = environment_science_lesson)
        environment_science.pack(side=LEFT, padx=10)

        base_content.configure(fg_color="#D3EE98")


    def geo_explorer():
        clear_base_content()
        base_title.configure(text="Geo Explorer")
        activation_signal()
        b2.configure(fg_color="red", hover_color="red")
        base_content.configure(fg_color="#D3EE98")
        map_frame = CTkFrame(base_content, height= 400)
        map_frame.pack(side=TOP, fill=BOTH, expand=True, pady=4, padx=5)
        # Create TkinterMapView instance and pack it
        map_widget = TkinterMapView(map_frame, width=800, height=600)
        map_widget.pack(fill="both", expand=True)

        # Set the initial position (latitude, longitude) and zoom level of the map
        map_widget.set_position(37.7749, -122.4194)  # Initial position: San Francisco
        map_widget.set_zoom(5)

        # Function to handle the location click event
        def on_map_click(event):
            lat, lon = map_widget.get_position()  # Get latitude and longitude
            CTkMessagebox.showinfo("Coordinates", f"Latitude: {lat}, Longitude: {lon}")

        # Bind the left mouse button click event to the function
        map_widget.bind("<ButtonRelease-1>", on_map_click)

        # Start the CustomTkinter main event loop
        data_frame = CTkFrame(base_content)
        data_frame.pack(side=TOP, fill=BOTH, expand=True, pady=3, padx=5)
        co2lable = CTkLabel(data_frame, text = "Carbon- Dioxide\n426 ppm", font = ("Arial", 20,"bold"))
        co2lable.pack(side = LEFT, padx = 10)
        methanelable = CTkLabel(data_frame, text="Methane\n 1929 ppb", font = ("Arial", 20,"bold"))
        methanelable.pack(side=LEFT, padx = 10 )
        warminglable = CTkLabel(data_frame, text="Ocean Warming\n360 zetta joules", font = ("Arial", 20, "bold"))
        warminglable.pack(side=LEFT, padx = 10)

    def adv_research_lib():
        def heatmap_func():
            # Load the datasets
            heat_file = pd.read_csv("D:/planet dynamics/gobal_temp.csv")
            co2_stat_file = pd.read_csv("D:/planet dynamics/stat.csv")
            methane_stat_file = pd.read_csv("D:/planet dynamics/methane_data.csv")

            # Extract data for the first plot (Temperature Anomaly)
            x1 = heat_file["Year"]
            y1 = heat_file["Anomaly"]

            # Extract data for the second plot (CO2 Stats)
            x2 = co2_stat_file["Year"]
            y2 = co2_stat_file["Monthly_Average"]

            # Extract data for the third plot (CH4 Stats)
            x3 = methane_stat_file["year"]
            y3 = methane_stat_file["average"]

            # Define a function to map y-values to colors for both datasets
            def get_color_temp(y_value):
                if -3 <= y_value <= -2:
                    return 'green'
                elif -2 < y_value <= -1:
                    return 'indigo'
                elif -1 < y_value <= 0:
                    return 'black'
                elif 0 < y_value <= 1:
                    return 'orange'
                elif 1 < y_value <= 2:
                    return 'red'
                else:
                    return 'gray'

            def get_color_co2(y_value):
                if 300 <= y_value <= 340:
                    return 'green'
                elif 340 < y_value <= 360:
                    return 'indigo'
                elif 360 < y_value <= 380:
                    return 'black'
                elif 380 < y_value <= 400:
                    return 'orange'
                elif 400 < y_value <= 420:
                    return 'red'
                else:
                    return 'gray'

            def get_color_methane(y_value):
                if 1600 <= y_value <= 1700:
                    return 'green'
                elif 1700 < y_value <= 1750:
                    return 'indigo'
                elif 1750 < y_value <= 1800:
                    return 'black'
                elif 1800 < y_value <= 1850:
                    return 'orange'
                elif 1850 < y_value <= 2000:
                    return 'red'
                else:
                    return 'gray'

            # Create figure and subplots (1 row, 3 columns)
            fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 7))

            # Set properties for the Temperature Anomaly subplot
            ax1.set_xlim(x1.min(), x1.max())
            ax1.set_ylim(y1.min() - 0.2, y1.max() + 0.1)
            ax1.set_xlabel("Year")
            ax1.set_ylabel("Temperature Anomaly (°C)")
            ax1.set_title("Global Temperature Anomaly Over Time")
            ax1.grid(True)

            # Set properties for the CO2 Stats subplot
            ax2.set_xlim(x2.min(), x2.max())
            ax2.set_ylim(y2.min() - 0.2, y2.max() + 0.1)
            ax2.set_xlabel("Year")
            ax2.set_ylabel("CO2 (Parts Per Million)")
            ax2.set_title("Monthly Mean CO2 Values")
            ax2.grid(True)

            # Set properties for the CH4 Stats subplot
            ax3.set_xlim(x3.min(), x3.max())
            ax3.set_ylim(y3.min() - 0.2, y3.max() + 0.1)
            ax3.set_xlabel("Year")
            ax3.set_ylabel("CH4 (Parts Per Billion)")
            ax3.set_title("Monthly Mean CH4 Values")
            ax3.grid(True)

            # Update function for the animation
            def update(frame):
                # Temperature Anomaly Animation (Left Plot)
                ax1.cla()
                colors1 = [get_color_temp(val) for val in y1[:frame]]
                ax1.scatter(x1[:frame], y1[:frame], c=colors1, marker="^")
                ax1.set_xlim(x1.min(), x1.max())
                ax1.set_ylim(y1.min() - 0.2, y1.max() + 0.1)
                ax1.set_xlabel("Year")
                ax1.set_ylabel("Temperature Anomaly (°C)")
                ax1.set_title("Global Temperature Anomaly Over Time")
                ax1.grid(True)

                # CO2 Stats Animation (Middle Plot)
                ax2.cla()
                colors2 = [get_color_co2(val) for val in y2[:frame]]
                ax2.scatter(x2[:frame], y2[:frame], c=colors2, marker="_")
                ax2.set_xlim(x2.min(), x2.max())
                ax2.set_ylim(y2.min() - 0.2, y2.max() + 0.1)
                ax2.set_xlabel("Year")
                ax2.set_ylabel("CO2 (Parts Per Million)")
                ax2.set_title("Monthly Mean CO2 Values")
                ax2.grid(True)

                # CH4 Stats Animation (Right Plot)
                ax3.cla()
                colors3 = [get_color_methane(val) for val in y3[:frame]]
                ax3.scatter(x3[:frame], y3[:frame], c=colors3, marker="+")
                ax3.set_xlim(x3.min(), x3.max())
                ax3.set_ylim(y3.min() - 0.2, y3.max() + 0.1)
                ax3.set_xlabel("Year")
                ax3.set_ylabel("CH4 (Parts Per Billion)")
                ax3.set_title("Monthly Mean CH4 Values")
                ax3.grid(True)

            # Create animation with a proper interval
            ani = FuncAnimation(fig, update, frames=len(x1), interval=0, repeat=False)

            # Display the plots
            plt.tight_layout()
            plt.show()

        def ozone_func():
            for o in ozone.winfo_children():
                o.destroy()

            def generate_image():
                y = year.get()
                m = month.get()
                north_hem_image_url = f"https://ozonewatch.gsfc.nasa.gov/ozone_maps/images/climate/OZONE_D{y}-{m}_G%5E716X716_PA:TIME.IOMPS_PNPP_V21_MGEOS5FP_LNH.PNG"

                south_hem_image_url = f"https://ozonewatch.gsfc.nasa.gov/ozone_maps/images/climate/OZONE_D{y}-{m}_G%5E716X716_PA:TIME.IOMPS_PNPP_V21_MGEOS5FP_LSH.PNG"

                north_hem_save_path = f"./ozone/northern_hemi_sphere_ozone_image_{m}_{y}.png"
                south_hem_save_path = f"./ozone/southern_hemi_sphere_ozone_image_{m}_{y}.png"
                download_image(north_hem_image_url, north_hem_save_path)
                download_image(south_hem_image_url, south_hem_save_path)
                north = CTkFrame(ozone)
                north.pack(side = LEFT, expand = TRUE)
                south = CTkFrame(ozone)
                south.pack(side = LEFT, expand = TRUE)
                image_north = CTkImage(light_image= Image.open(north_hem_save_path), size = (300,300))
                image_north_pic = CTkLabel(north, text = "", image = image_north)
                image_north_pic.pack()
                image_south = CTkImage(light_image= Image.open(south_hem_save_path), size =(300,300))
                image_south_pic = CTkLabel(south, text = "", image = image_south)
                image_south_pic.pack()
                image_north_label = CTkLabel(north, text = "Northern Hemisphere", font = ("Arial", 15))
                image_north_label.pack(side = BOTTOM, padx = 10, pady = 10)
                image_south_label = CTkLabel(south, text="Southern Hemisphere", font=("Arial", 15))
                image_south_label.pack(side=BOTTOM, padx=10, pady=10)
            def download_image(image_url, save_path):
                try:
                    # Send a GET request to the image URL
                    response = requests.get(image_url)

                    # Check if the request was successful
                    if response.status_code == 200:
                        # Write the content of the response (the image) to a file
                        with open(save_path, 'wb') as file:
                            file.write(response.content)
                        print(f"Image successfully downloaded and saved as {save_path}")
                    else:
                        print(f"Failed to retrieve the image. Status code: {response.status_code}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Example usage

            year = CTkEntry(ozone, placeholder_text="Enter Year")
            year.pack(pady = 10, padx = 5, fill = X)
            month = CTkEntry(ozone, placeholder_text = "Enter Month Number (January : 01 , February : 02) ")
            month.pack( pady = 10, padx = 5, fill = X)
            generate = CTkButton(ozone, text = "Generate", command = generate_image)
            generate.pack( pady = 2, padx = 5, fill = X)


        clear_base_content()
        base_title.configure(text="Advance Research Library")
        activation_signal()
        b3.configure(fg_color="red",hover_color="red")
        base_content.configure(fg_color="#D3EE98")
        arl = CTkTabview(base_content, fg_color="#D3EE98")
        arl.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=(5, 10))
        global_ws = arl.add("Global Warming Stats")
        gws_label = CTkLabel(global_ws, text = "Climate Trend Tracker", font = ("Helvetica",35), text_color="#FFAD60")
        gws_label.pack(side = TOP, fill = X, pady = 5, padx = 4)
        gws_image = CTkImage(light_image=Image.open("global_warning_new.png"), size= (400,300))
        co2_image = CTkImage(light_image=Image.open("co2.png"), size=(400, 300))
        methane_image = CTkImage(light_image=Image.open("mathene.png"), size= (400,300))
        image = CTkScrollableFrame(global_ws, width = 450, height = 350)
        image.pack(pady = 10, padx = 10)
        description_label = CTkLabel(image, text="The Climate Trend Tracker visualizes the rise of CO2, global temperatures,\nand methane emissions over time. Powered by NASA’s real-time data,\nit helps users understand the impact of these factors on\nclimate change, encouraging informed action.")
        description_label.pack(padx = 2, pady = 10)
        gws_label_image = CTkLabel(image, text = "", image= gws_image)
        gws_label_image.pack(pady = 10)
        co2_label_image = CTkLabel(image,text = "", image=co2_image)
        co2_label_image.pack(pady=10)
        methane_label_image = CTkLabel(image, text = "", image=methane_image)
        methane_label_image.pack(pady=10)
        gws_button = CTkButton(global_ws, text="Dynamic Graph", fg_color="gold", text_color="white", border_width=2, border_color="orange", command = heatmap_func)
        gws_button.pack(pady = 10)
        ozone = arl.add("Ozone Stats")
        ozone_label = CTkLabel(ozone, text="Ozone Layer Visualization", font=("Helvetica", 35), text_color="#FFAD60")
        ozone_label.pack(side=TOP, fill=X, pady=5, padx=4)
        ozone_button = CTkButton(ozone, text="Ozone Watcher", fg_color="gold", text_color="white", border_width=2, border_color="orange", command = ozone_func)
        ozone_button.pack(pady = 30)

    def climate_community():
        clear_base_content()
        base_title.configure(text="Climate Community")
        activation_signal()
        b4.configure(fg_color="red",hover_color="red")
        base_content.configure(fg_color="#D3EE98")
        community = CTkTabview(base_content)
        community.pack(side=LEFT, fill=BOTH, expand=True, padx = 10, pady = (5,10))
        blogs = community.add("Blogs")
        blogs_scroll = CTkScrollableFrame(blogs, width = 600, height = 800)
        blogs_scroll.pack()
        for other_blog in result_other_blog:
            take_this_blog = other_blog
            blogs_res = CTkFrame(blogs_scroll, fg_color="#e6ffb1", border_color="yellow")
            blogs_res.pack(pady=(5, 0))
            author_label = CTkLabel(blogs_res, text = f"{take_this_blog[1]}", font=("Helvetica", 14), bg_color="yellow")
            author_label.grid(row=0,column=0,sticky="w",padx=2,pady=2)
            published_date = CTkLabel(blogs_res, text = f"{take_this_blog[6]}", font=("Helvetica", 14), bg_color="red")
            published_date.grid(row=0,column=1,sticky="e",padx=(0,2))
            subject_blogs = CTkLabel(blogs_res, text = f"{take_this_blog[4]}", font=("Helvetica", 17), bg_color="lime")
            subject_blogs.grid(row=1,column=0,sticky="w")
            blog_title = CTkLabel(blogs_res, text=f"{take_this_blog[2]}", font=("Helvetica", 19), bg_color="lime")
            blog_title.grid(row=2,column=0,sticky="w")
            blog_content = CTkLabel(blogs_res, text=f"{take_this_blog[3]}", font=("Helvetica", 19), bg_color="lime")
            blog_content.grid(row=3,column=0)


        non_friends = community.add("All Users")

        non_friends_scroll = CTkScrollableFrame(non_friends, width = 300 , height = 400, fg_color="#e6ffb1")
        non_friends_scroll.pack(side = TOP)
        posters = community.add("Poster")
        poster_frame= CTkFrame(posters)
        poster_frame.pack(pady = 10, padx = 10, expand = True, fill = BOTH)
        poster_image = CTkImage(light_image=Image.open("D:/planet dynamics/save me.jpg"), size = (600,700))
        poster_label = CTkLabel(poster_frame, text = "", image = poster_image)
        poster_label.pack()
        def on_email_click(f_email):
            print(f"{email} Clicked Email: {f_email}")

        def create_email_buttons(tab):
            for email in result_all_non_friends_name:
                button = CTkButton(tab, text=email, command=lambda e=email: on_email_click(e))
                button.pack(pady=5, padx=10)

        create_email_buttons(non_friends_scroll)
    def my_dashboard():
        clear_base_content()
        base_title.configure(text="My Dashboard")
        activation_signal()
        b0.configure(fg_color="red",hover_color="red")
        achievment_tab.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=(5, 10))
        user_details.pack(side=LEFT, fill=BOTH, expand=True, padx=(5, 10), pady=(25, 10))
        base_content.configure(fg_color="#C1CFA1")

    #image_frame.pack_forget()
    #welcome_frame.pack_forget()
    frame = CTkFrame(app, corner_radius=10)
    frame.pack(side=LEFT, fill=Y, padx=10)
    control_frame = CTkFrame(frame, corner_radius=10, border_width= 3 ,border_color="#00BCD4")
    control_frame.pack(pady = 2)
    def final_audio_closing():
        mixer.music.stop()
        stop_audio_btn.pack_forget()

    stop_audio_btn = CTkButton(frame,text="STOP AUDIOBOOK",command=final_audio_closing)
    #stop_audio_btn.pack()

    base_frame = CTkFrame(app)
    base_frame.pack(side=LEFT, expand=True, fill=BOTH, padx=10)
    base_title = CTkLabel(base_frame, text=f"{email}", text_color="green", font=("Helvetica", 20), fg_color="yellow",
                          corner_radius=5)
    base_title.pack(side=TOP, fill=X, padx=5, pady=2)

    base_content = CTkFrame(base_frame,corner_radius = 5, border_width= 3)
    base_content.pack(side = LEFT, fill=BOTH,expand=True,padx= 4, pady = 4)
#==============================Dashboard===============================================
    achievment_tab = CTkTabview(base_content, fg_color="#D3EE98", border_width= 3 ,border_color="#00BCD4")
    certificates = achievment_tab.add("Certificates")
    certificates_scroll = CTkScrollableFrame(certificates, fg_color="#D3EE98", height = 400, border_width=3, border_color="#1A237E", scrollbar_button_color="#1A237E")
    certificates_scroll.pack()
    certificate_paper1 = CTkImage(light_image=Image.open("certificate1.png"), size=(200, 150))
    cp1 = CTkLabel(certificates_scroll, text="", image=certificate_paper1)
    cp1.pack(pady = 10)
    certificate_paper2 = CTkImage(light_image=Image.open("certificate1.png"), size=(200, 150))
    cp2 = CTkLabel(certificates_scroll, text="", image=certificate_paper2)
    cp2.pack(pady = 10)
    badges = achievment_tab.add("Badges")
    badges_scroll = CTkScrollableFrame(badges, fg_color="#D3EE98", height = 800, )
    badges_scroll.pack(pady = 10)
    badges_logo1 = CTkImage(light_image=Image.open("badge_1.png"), size=(100, 100))
    bl1 = CTkLabel(badges_scroll, text="", image=badges_logo1)
    bl1.pack()
    badges_logo2 = CTkImage(light_image=Image.open("badge_2.png"), size=(100, 100))
    bl2 = CTkLabel(badges_scroll, text="", image=badges_logo2)
    bl2.pack(pady = 5)
    badges_logo3 = CTkImage(light_image=Image.open("badge3.png"), size=(100, 100))
    bl3 = CTkLabel(badges_scroll, text="", image=badges_logo3)
    bl3.pack(pady=5)
    badges_logo4 = CTkImage(light_image=Image.open("badge4.png"), size=(100, 100))
    bl4 = CTkLabel(badges_scroll, text="", image=badges_logo4)
    bl4.pack(pady=5)
    badges_logo5 = CTkImage(light_image=Image.open("badge5.png"), size=(100, 100))
    bl5 = CTkLabel(badges_scroll, text="", image=badges_logo5)
    bl5.pack(pady=5)
    certificate_paper2 = CTkImage(light_image=Image.open("certificate1.png"), size=(200, 150))
    cp2 = CTkLabel(certificates_scroll, text="", image=certificate_paper2)
    cp2.pack()
    achievment_tab.pack(side = LEFT, fill = BOTH, expand = True, padx = 5,pady=(5,10))

    user_details = CTkFrame(base_content, width=300,corner_radius=5, fg_color="#D3EE98", border_width=3, border_color="#00BCD4")
    user_details.pack(side=LEFT, fill=BOTH, expand = True,padx=(5,10), pady = (25,10))
    user_pic = CTkImage(light_image=Image.open("initial_user_photo.jpg"), size = (150,150))
    user_pic_label = CTkLabel(user_details, text = "",image = user_pic)
    user_pic_label.pack(side = TOP, pady = 20)
    user_name_label = CTkLabel(user_details, text=f"{user_name}", font = ("Bold", 20))
    user_name_label.pack(pady = 3)
    latlang_label = CTkLabel(user_details, text="23.6850 Degree North\n90.3563 Degree East", font = ("Bold", 15))
    latlang_label.pack(pady = 2)

    coins_label = CTkButton(user_details, text = f"Coins: {user_coin}", fg_color="#D3EE98", font = ("Bold", 20,"bold"), text_color="#FFB200", hover_color = "white")
    coins_label.pack(side=TOP, pady = 5)
    def friend_list(l):
        toplevel = CTkToplevel(user_details)
        toplevel.title("Friends List")
        toplevel.geometry("300x400")
        for i in l:
            friend_frame = CTkFrame(toplevel)
            friend_frame.pack(pady=10, padx=20, fill="x")
            name_label = CTkLabel(friend_frame, text=f"{i[0]}", font=("Arial", 16))
            name_label.pack(side="left", padx=10)


    friend_button = CTkButton(user_details, text=f"Friends: {user_friend_number}", fg_color="#D3EE98", font=("Bold", 20, "bold"), text_color="#4F75FF", hover_color="white",command = lambda :friend_list(result_user_friend))
    friend_button.pack(side=TOP, pady=5)

    def follower_list(l):
        toplevel = CTkToplevel(user_details)
        toplevel.title("Follower List")
        toplevel.geometry("300x400")
        for i in l:
            follower_frame = CTkFrame(toplevel)
            follower_frame.pack(pady=10, padx=20, fill="x")
            name_label = CTkLabel(follower_frame, text=f"{i[0]}", font=("Arial", 16))
            name_label.pack(side="left", padx=10)

    follower_button = CTkButton(user_details, text=f"Followers: {user_follower_number}", fg_color="#D3EE98",
                              font=("Bold", 20, "bold"), text_color="#4F75FF", hover_color="white",
                              command=lambda: follower_list(result_user_follower))
    follower_button.pack(side=TOP, pady=5)

    def blog_list(blogs):
        blog_window = CTkToplevel(user_details)
        blog_window.title("My Blog List")
        blog_window.geometry("600x500")

        # Add a header
        header_label = CTkLabel(blog_window, text="My Blog List", font=("Arial", 20))
        header_label.pack(pady=10)
        for blog in blogs:
            frame = CTkFrame(blog_window)
            frame.pack(pady=10, padx=20, fill="x")

            # Subject
            subject_label = CTkLabel(frame, text=f"Subject: {blog[4]}", font=("Arial", 12))
            subject_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            # Title
            title_label = CTkLabel(frame, text=f"Title: {blog[2]}", font=("Arial", 12))
            title_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

            # Content
            content_label = CTkLabel(frame, text=f"Content: {blog[3]}", font=("Arial", 12))
            content_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

            # Rating
            rating_label = CTkLabel(frame, text=f"Rating: {blog[5]}", font=("Arial", 12))
            rating_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

            # Time
            time_label = CTkLabel(frame, text=f"Blog Time: {blog[6]}", font=("Arial", 12))
            time_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    blog_written_button = CTkButton(user_details, text=f"Blogs: {user_blog_number}", fg_color="#D3EE98", font=("Bold", 20, "bold"), text_color="#FFAD60", hover_color="white",command=lambda:blog_list(result_user_blog))
    blog_written_button.pack(side=TOP, pady=5)

    def settings(email):
        update_window = CTkToplevel()  # Create a new Toplevel window
        update_window.geometry("400x500")
        update_window.title("Update Account")

        # Username Entry
        username_label = CTkLabel(update_window, text="Username:")
        username_label.pack(pady=10)
        username_entry = CTkEntry(update_window)
        username_entry.insert(0, user_name)
        username_entry.pack(pady=10)
        username_entry.configure(state="disabled")

        # Password Entry
        password_label = CTkLabel(update_window, text="Password:")
        password_label.pack(pady=10)
        password_entry = CTkEntry(update_window, show="*", placeholder_text="Enter Password")
        password_entry.pack(pady=10)

        def update_account(email):
            sql_for_update_account = f"UPDATE learner SET code = '{password_entry.get()}' where email = '{email}'"
            cur.execute(sql_for_update_account)
            con.commit()
            print(sql_for_update_account)
            update_window.destroy()
            update_message = CTkMessagebox(title="Password Updated",
                                           message=f"{user_name}\nYour Password Has been updated", icon="check",
                                           option_1="OK")

        # Update Account Button
        update_button = CTkButton(update_window, text="Update Account", command=lambda: update_account(email))
        update_button.pack(pady=20)

    settings_button = CTkButton(user_details, text="Settings", fg_color="#D3FF98", font=("Bold", 20, "bold"),
                                text_color="#FFAD60", hover_color="white", command=lambda: settings(email))
    settings_button.pack(side=TOP, pady=5)

    b0 = CTkButton(control_frame, text="My Dashboard", width=150, height=50, border_width=3, corner_radius=7,
                   command=my_dashboard)
    b0.pack(pady=20, padx=5)

    b1 = CTkButton(control_frame, text="Climate Learning Hub", width=150, height=50, border_width=3, corner_radius=7,
                   command=climate_learning_hub)
    b1.pack(pady=20, padx=5)
    b2 = CTkButton(control_frame, text="Geo Explorer", width=150, height=50, border_width=3, corner_radius=7,
                   command=geo_explorer)
    b2.pack(pady=20, padx=5)
    b3 = CTkButton(control_frame, text="Advance Research Library", width=150, height=50, border_width=3,
                   corner_radius=7, command=adv_research_lib)
    b3.pack(pady=20, padx=5)
    b4 = CTkButton(control_frame, text="Climate Community", width=150, height=50, border_width=3, corner_radius=7,
                   command=climate_community)
    b4.pack(pady=20, padx=5)


#==================Login Frame Raise=========================================
def login_frame_raise():
    welcome_btn_frame.pack_forget()
    login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)


#==================go to welcome btn frame=========================================
def cancel_login_account():
    login_frame.pack_forget()
    welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================go to welcome btn frame=========================================
def login_part():
    signup_frame.pack_forget()
    login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)


#==================Signup Frame Raise=========================================
def signup_frame_raise():
    welcome_btn_frame.pack_forget()
    signup_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Welcome new user=========================================
def welcome_new_user():
    registration_message = CTkMessagebox(title = "Registration Successful", message = "You have successfully created an account.\nPress the 'Login' button to enter the login page!!",icon = "check" ,option_1="Login")
    if registration_message.get() == "Login":
        login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User at account creation=========================================
def warn_new_user():
    registration_message = CTkMessagebox(title = "Registration Unsuccessful", message = "Registration Failed.\n 1) Check your Gmail and name\n2)Insert password more than 5 letters",icon = "warning", option_1="Sign Up Again",option_2="Cancel")
    if registration_message.get() == "Sign Up Again":
        signup_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)
    if registration_message.get() == "Cancel":
        signup_frame.pack_forget()
        welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User for existed account=========================================
def warn_existence():
    registration_message = CTkMessagebox(title = "Account Already Existed", message = "You are already a member. Login your account",icon = "info", option_1="Login",option_2="Cancel")
    if registration_message.get() == "Login":
        signup_frame.pack_forget()
        login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)
    if registration_message.get() == "Cancel":
        welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User for creating account=========================================
def warn_for_create_account():
    registration_message = CTkMessagebox(title = "No account found", message = "You have no account.\nPlease Sign Up..",icon = "info", option_1="Sign Up",option_2="Cancel")
    if registration_message.get() == "Sign Up":
        login_frame.pack_forget()
        signup_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)
    if registration_message.get() == "Cancel":
        login_frame.pack_forget()
        welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User for invalid credential=========================================
def warn_for_invalid_credential(name):
    registration_message = CTkMessagebox(title = "Invalid Password", message = f"{name}\nPlease Check Your Password",icon = "warning", option_1="OK")


#==================Warn User for empty credential=========================================
def warn_for_empty_credential():
    registration_message = CTkMessagebox(title = "Empty Credential", message = "Provide accurate credentials",icon = "warning", option_1="OK")


#==================sign up to account=========================================
def signup_account():
    #print(signupemail_entry.get()," and ",signuppass_entry.get(),"and", namesignup_entry.get())
    name = namesignup_entry.get()
    email = signupemail_entry.get()
    pwd = signuppass_entry.get()
    if email.endswith("@gmail.com") and name!="" and len(pwd)>=5:
        sql_for_account_creation = f"INSERT INTO learner (email,name,code) values('{email}','{name}','{pwd}')"
        sql_for_check_existence = f"SELECT email From learner where email = '{email}'"
        sql_for_add_email_to_coin_table = f"INSERT INTO coins (email,coin) values('{email}','0')"
        sql_for_add_friends = f"INSERT INTO friends values ('{email}','Planet_Dynamics')"
        bid = str(random.randint(1,1000))
        blog_time = str(date.today())
        sql_for_add_initial_blog = f"""
        INSERT INTO blogs VALUES('{bid}','{email}','Joined Planet Dynamics','I am happy to join in Planet Dynamics','Planet Dynamics','1','{blog_time}')
        """
        cur.execute(sql_for_check_existence)
        total_accounts = cur.fetchall()
        if len(total_accounts)!=0:
            warn_existence()
        else:
            cur.execute(sql_for_account_creation)
            con.commit()
            cur.execute(sql_for_add_email_to_coin_table)
            con.commit()
            cur.execute(sql_for_add_initial_blog)
            con.commit()
            cur.execute(sql_for_add_friends)
            con.commit()
            welcome_new_user()
            signup_frame.pack_forget()
    else:
        warn_new_user()


#==================Login to account=========================================
def login_account():
    email = email_entry.get()
    pwd = pass_entry.get()
    if len(email)>0 and len(pwd)>0:
        sql = f"SELECT * FROM learner where email = '{email}'"
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) == 0:
            warn_for_create_account()
        else:
            if result[0][2] != pwd:
                warn_for_invalid_credential(result[0][1])
            else:
                dashboard(email)
    else:
        warn_for_empty_credential()



#==================go to welcome btn frame - signup=========================================
def cancel_signup_account():
    signup_frame.pack_forget()
    welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)


#==================image frame=========================================
image_frame = CTkFrame(master = app, width = 650, corner_radius=3)
image_frame.pack(side = LEFT, fill = BOTH, expand = True)
dash_image = CTkImage(light_image=Image.open("dashboard.jpg"), size= (750,600))
image_label = CTkLabel(image_frame, text = "", image = dash_image)
image_label.pack(expand = True, fill = BOTH)
#==================Welcome Frame=========================================
welcome_frame = CTkFrame(master = app, width = 350, corner_radius=5,border_width=3, border_color="#4CAF50", fg_color="#e6ffb1")
welcome_frame.pack(side = RIGHT,padx = 1,fill = BOTH, expand = True)
#========welcome frame label============
welcome_label = CTkLabel(welcome_frame, text="Welcome\nTo\nPlanet Dynamics!!", font = ("Helvetica", 28), text_color="#4CAF50")
welcome_label.pack(pady=10)
#==================Welcome Button Frame=========================================
welcome_btn_frame = CTkFrame(welcome_frame,fg_color="#e6ffb1",width=350)
welcome_btn_frame.pack(side = BOTTOM ,pady = 10, padx = 10,fill = BOTH, expand = True)
#welcome_btn_frame.pack_forget()
#========Login Frame Raise Button=========
login_page = CTkButton(welcome_btn_frame, text="Login", font=("Roboto", 20), corner_radius=15, border_width = 3, command = login_frame_raise, fg_color="#00BCD4", hover_color="#4CAF50")
login_page.pack(expand = True)
#===========OR Label==========
or_label =  CTkLabel(welcome_btn_frame, text="OR", font = ("Helvetica", 25), text_color="#2196F3")
or_label.pack()
#===========SignUp Frame Raise Button========
signup_page = CTkButton(welcome_btn_frame, text="Be a Member Today!", font=("Roboto", 20), corner_radius=15, border_width = 3, command = signup_frame_raise,fg_color="#00BCD4", hover_color="#4CAF50")
signup_page.pack(expand = True)
#==================Login Frame=========================================
login_frame = CTkFrame(welcome_frame,fg_color="#e6ffb1",width=350)
login_frame.pack(side = BOTTOM ,pady = 10, padx = 10,fill = BOTH, expand = True)
login_frame.pack_forget()
#==================positioning frame=========================================
gap_frame = CTkFrame(login_frame,height=100,fg_color="#e6ffb1")
gap_frame.pack()
#==========Login Frame Email==========
email_entry = CTkEntry(login_frame, placeholder_text="Email", width = 300, corner_radius=17, font = ("Arial",15))
email_entry.pack(ipady = 10,pady= 10)
#=======Login Frame Pass=====
pass_entry = CTkEntry(login_frame, placeholder_text="Password", width = 300, corner_radius=17, font = ("Arial",15))
pass_entry.pack(ipady = 10)
#=======Login Button======
login_btn = CTkButton(login_frame, text="Login", font=("Roboto", 15), corner_radius=15, border_width = 3, command = login_account)
login_btn.pack(side = LEFT,expand = True)

cancel_login_btn = CTkButton(login_frame, text="Cancel", font=("Roboto", 15), corner_radius=15, border_width = 3, command = cancel_login_account)
cancel_login_btn.pack(side = LEFT,expand = True)

#=====================Sign Up Frame==================================================
signup_frame = CTkFrame(welcome_frame,fg_color="#e6ffb1",width=350)
signup_frame.pack(side = BOTTOM ,pady = 10, padx = 10,fill = BOTH, expand = True)
signup_frame.pack_forget()
#====positioning frame=======
gap_frame = CTkFrame(signup_frame,height=100,fg_color="#e6ffb1")
gap_frame.pack()
#========Sign up Frame Name (namesignup_entry)========
namesignup_entry = CTkEntry(signup_frame, placeholder_text="Name", width = 300, corner_radius= 17, font = ("Arial",15))
namesignup_entry.pack(ipady = 10,pady= 10)
#======Sign Up Frame Email================
signupemail_entry = CTkEntry(signup_frame, placeholder_text="Email", width = 300, corner_radius=17, font = ("Arial",15))
signupemail_entry.pack(ipady = 10,pady= 10)
#=====Sign Up Frame Pass=========
signuppass_entry = CTkEntry(signup_frame, placeholder_text="Password", width = 300, corner_radius=17, font = ("Arial",15))
signuppass_entry.pack(ipady = 10,pady = 10)
#=====Sign Up Button=========
signup_btn = CTkButton(signup_frame, text="Sign Up", font=("Roboto", 15), corner_radius=15, border_width = 3, command = signup_account)
signup_btn.pack(side = LEFT,expand = True)

cancel_signup_btn = CTkButton(signup_frame, text="Cancel", font=("Roboto", 15), corner_radius=15, border_width = 3, command = cancel_signup_account)
cancel_signup_btn.pack(side = LEFT,expand = True)

#=======Login Button=========
login_btn = CTkButton(signup_frame, text="Login", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = login_part)
login_btn.pack(side = BOTTOM,expand = True)

#login_frame.pack_forget()

app.mainloop()