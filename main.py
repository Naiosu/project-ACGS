from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.lang import Builder
from time import sleep
from kivy.clock import Clock
from random import randint
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

class SoundManager:
    bg_sound = None

    @classmethod
    def play_bg_sound(cls, sound_file_path):
        if cls.bg_sound:
            cls.bg_sound.stop()

        cls.bg_sound = SoundLoader.load(sound_file_path)
        if cls.bg_sound:
            cls.bg_sound.loop = True
            cls.bg_sound.play()

    @classmethod
    def stop_bg_sound(cls):
        if cls.bg_sound:
            cls.bg_sound.stop()
            
class StartupScreen(Screen):
    def on_enter(self):

        self.video = Video(source='Intro2.mp4', state='play', options={'allow_stretch': True})
        self.add_widget(self.video)

        # self.label = Label(text ="Touch to start...", pos_hint={'center_x': 0.5, 'center_y': 0.2})
        # self.label.font_size = '30dp'
        # self.add_widget(self.label)

        # anim = Animation(opacity=0, duration=3) + Animation(opacity=1, duration=3)
        # anim.repeat = True
        # anim.start(self.label)

        #SoundManager.play_bg_sound('main_sound.mp3')

        self.event1 = Clock.schedule_once(self.on_stop, 11)

    def on_touch_up(self, touch):

        if self.video and self.video.state == 'play':
            self.video.state = 'stop'

        self.event1.cancel()

        self.manager.switch_to(MenuScreen())
        SoundManager.play_bg_sound('main_sound.mp3')
    
    def on_stop(self, dt):
        if self.video and self.video.state == 'play':
            self.video.state = 'stop'

        self.manager.switch_to(MenuScreen())
        SoundManager.play_bg_sound('main_sound.mp3')

class MenuScreen(Screen):
    def on_enter(self):

        layout = RelativeLayout()

        logo = Image(source='game_logo.png', pos_hint={'center_x': 0.5, 'center_y': 0.6} )
        layout.add_widget(logo)
 
        background = Image(source='scielab.png', fit_mode = 'contain')
        self.add_widget(background)

        start_button = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.2, 'center_y': 0.2})
        start_button.background_normal = 'START.png'
        start_button.bind(on_release=lambda x: self.manager.switch_to(GameScreen()))
        layout.add_widget(start_button)

        exit_button = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        exit_button.background_normal = 'EXIT.png'
        exit_button.bind(on_release=lambda x: App.get_running_app().stop())
        layout.add_widget(exit_button)

        credits = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.8, 'center_y': 0.2})
        credits.background_normal = 'CREDITS.PNG'
        credits.bind(on_release=lambda x: self.manager.switch_to(Credits()))
        layout.add_widget(credits)

        self.add_widget(layout)


        anim = Animation(opacity = 0, duration = 0) + Animation(opacity=1, duration=1)
        anim.repeat = False
        anim.start(layout)
        anim.start(background)

class Credits(Screen):
    def on_enter(self, *args):
        layout = RelativeLayout()

        group = Label(text ='Created by BSCpE 1-2\nGROUP 7 - ACGS', pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(group)

        authors = Label(text ='Jayson C. Albos \nZeruel Kody C. \nJed Micko A. Gonzales \nChristian P. Samudio', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(authors)

        back_button = Button(text="Back", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        back_button.bind(on_release=lambda x: self.manager.switch_to(MenuScreen()))
        layout.add_widget(back_button)

        self.add_widget(layout)

class GameScreen(Screen):
    def on_enter(self):

        layout = RelativeLayout()

        background = Image(source='Game_Menu.png', fit_mode='contain')
        self.add_widget(background)

        addition_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        addition_button.background_normal = 'addition.png'
        addition_button.bind(on_release=lambda x: SoundManager.stop_bg_sound())
        addition_button.bind(on_release=lambda x: self.manager.switch_to(Add_screen()))
        layout.add_widget(addition_button)

        Subtraction = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        Subtraction.background_normal = 'subtraction.png'
        Subtraction.bind(on_release=lambda x: SoundManager.stop_bg_sound())
        Subtraction.bind(on_release=lambda x: self.manager.switch_to(Sub_screen()))
        layout.add_widget(Subtraction)

        Multiplication = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        Multiplication.background_normal = 'multiplication.png'
        Multiplication.bind(on_release=lambda x: SoundManager.stop_bg_sound())
        Multiplication.bind(on_release=lambda x: self.manager.switch_to(Mul_screen()))
        layout.add_widget(Multiplication)

        Division = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        Division.background_normal = 'division.png'
        Division.bind(on_release=lambda x: SoundManager.stop_bg_sound())
        Division.bind(on_release=lambda x: self.manager.switch_to(Div_screen()))
        layout.add_widget(Division)

        back_button = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.9, 'center_y': 0.9})
        back_button.background_normal = 'BACK.png'
        back_button.bind(on_release=lambda x: self.manager.switch_to(MenuScreen()))
        layout.add_widget(back_button)

        self.add_widget(layout)

        anim = Animation(opacity = 0, duration = 0) + Animation(opacity=1, duration=1)
        anim.repeat = False
        anim.start(layout)
        anim.start(background)

class Add_screen(Screen):
    def on_enter(self, *args):
        self.layout = RelativeLayout()

        background = Image(source='quiz_bg.png', fit_mode='contain')
        self.add_widget(background)

        self.score = 0
        self.counter = 0

        self.back_button = Button(size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.back_button.background_normal = 'BACK.png'
        self.back_button.bind(on_release=self.custom_back)
        self.layout.add_widget(self.back_button)
        

        self.counter_tab = Label(text = '', font_size='30dp',color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.7})

        self.score_tab = Label(text = '', font_size='28dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.6})
        # self.layout.add_widget(self.score_tab)

        self.Text = Label(text = 'Press Start to Begin',font_size='48dp',color='black', bold = 'True', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.Text)

        self.Input = TextInput(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.layout.add_widget(Input)

        self.Start_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Start_button.background_normal = 'start_quiz.png'
        self.Start_button.bind(on_release=self.start)
        self.layout.add_widget(self.Start_button)

        self.add_widget(self.layout)
        SoundManager.play_bg_sound('quiz.mp3')

    
    def start(self, *args):
        
        self.counter += 1
        if self.counter == 11:
            self.layout.remove_widget(self.score_tab)
            self.layout.remove_widget(self.Input)
            self.layout.remove_widget(self.counter_tab)
            self.Text.text = f'Your score is {self.score}'
            self.layout.remove_widget(self.Submit_button)
            self.layout.remove_widget(self.back_button)

            self.back_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
            self.back_button.background_normal = 'longback.png'
            self.back_button.bind(on_release=self.custom_back)
            self.layout.add_widget(self.back_button)


            return False

        random1 = randint(1,10)
        random2 = randint(1,10)

        self.correct = random1 + random2

        self.layout.remove_widget(self.Start_button)        
        self.Text.text = f'{random1} + {random2} = ?'

        self.score_tab.text = f'{self.score} / 10'
        self.counter_tab.text = f'No. {self.counter}'
    
        # self.Input = TextInput(multiline=False, size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.Input.bind(text=self.on_text)

        self.Submit_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Submit_button.background_normal = 'submit.png'
        self.Submit_button.bind(on_release=self.correction)

        if self.counter == 1:
            self.layout.add_widget(self.score_tab)
            self.layout.add_widget(self.counter_tab)
            self.layout.add_widget(self.Input)
            self.layout.add_widget(self.Submit_button)

    def update(self, text):
        print(self.Input.text, text)


    def correction(self, *args):
        
        update = Clock.schedule_once(self.update, 0)
        
        
        if str(self.correct) == self.Input.text:
            self.score += 1
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.Text.text = 'CORRECT!'
            self.quick_interval = Clock.schedule_once(self.start,2)
        else:
            self.Text.text = 'WRONG!'
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.quick_interval = Clock.schedule_once(self.start,2)
    
    def custom_back(self, *args):
        self.manager.switch_to(GameScreen())
        SoundManager.play_bg_sound('main_sound.mp3')
        

class Sub_screen(Screen):
    def on_enter(self, *args):
        self.layout = RelativeLayout()

        background = Image(source='quiz_bg.png', fit_mode='contain')
        self.add_widget(background)

        self.score = 0
        self.counter = 0

        self.back_button = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.back_button.background_normal = 'BACK.png'
        self.back_button.bind(on_release=self.custom_back)
        self.layout.add_widget(self.back_button)
            

        self.counter_tab = Label(text = '',font_size='30dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.7})

        self.score_tab = Label(text = '',font_size='28dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.6})
        # self.layout.add_widget(self.score_tab)

        self.Text = Label(text = 'Press Start to Begin',font_size='48dp', color='black', bold = 'True', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.Text)

        self.Input = TextInput(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.layout.add_widget(Input)

        self.Start_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Start_button.background_normal = 'start_quiz.png'
        self.Start_button.bind(on_release=self.start)
        self.layout.add_widget(self.Start_button)

        self.add_widget(self.layout)
        SoundManager.play_bg_sound('quiz.mp3')

    
    def start(self, *args):
        
        self.counter += 1
        if self.counter == 11:
            self.layout.remove_widget(self.score_tab)
            self.layout.remove_widget(self.Input)
            self.layout.remove_widget(self.counter_tab)
            self.layout.remove_widget(self.Submit_button)
            self.layout.remove_widget(self.back_button)

            self.Text.text = f'Your score is {self.score}'

            self.back_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
            self.back_button.background_normal = 'longback.png'
            self.back_button.bind(on_release=self.custom_back)
            self.layout.add_widget(self.back_button)


            return False

        random1 = randint(1,10)
        random2 = randint(1,10)

        if random1 > random2:
            self.correct = random1 - random2
            self.Text.text = f'{random1} - {random2} = ?'
        else:
            self.correct = random2 - random1
            self.Text.text = f'{random2} - {random1} = ?'

        self.layout.remove_widget(self.Start_button)        

        self.score_tab.text = f'{self.score} / 10'
        self.counter_tab.text = f'No. {self.counter}'
    
        # self.Input = TextInput(multiline=False, size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.Input.bind(text=self.on_text)

        self.Submit_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Submit_button.background_normal = 'submit.png'
        self.Submit_button.bind(on_release=self.correction)

        if self.counter == 1:
            self.layout.add_widget(self.score_tab)
            self.layout.add_widget(self.counter_tab)
            self.layout.add_widget(self.Input)
            self.layout.add_widget(self.Submit_button)

    def update(self, text):
        print(self.Input.text, text)


    def correction(self, *args):
        
        update = Clock.schedule_once(self.update, 0)
        
        if str(self.correct) == self.Input.text:
            self.score += 1
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.Text.text = 'CORRECT!'
            self.quick_interval = Clock.schedule_once(self.start,2)
        else:
            self.Text.text = 'WRONG!'
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.quick_interval = Clock.schedule_once(self.start,2)
    
    def custom_back(self, *args):
        self.manager.switch_to(GameScreen())
        SoundManager.play_bg_sound('main_sound.mp3')


class Mul_screen(Screen):
    def on_enter(self, *args):
        self.layout = RelativeLayout()

        background = Image(source='quiz_bg.png', fit_mode='contain')
        self.add_widget(background)

        self.score = 0
        self.counter = 0

        self.back_button = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.back_button.background_normal = 'BACK.png'
        self.back_button.bind(on_release=self.custom_back)
        self.layout.add_widget(self.back_button)
        

        self.counter_tab = Label(text = '',font_size='30dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.7})

        self.score_tab = Label(text = '',font_size='28dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.6})
        # self.layout.add_widget(self.score_tab)

        self.Text = Label(text = 'Press Start to Begin',font_size='48dp', color='black', bold = 'True', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.Text)

        self.Input = TextInput(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.layout.add_widget(Input)

        self.Start_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Start_button.background_normal = 'start_quiz.png'
        self.Start_button.bind(on_release=self.start)
        self.layout.add_widget(self.Start_button)

        self.add_widget(self.layout)
        SoundManager.play_bg_sound('quiz.mp3')

    
    def start(self, *args):
        
        self.counter += 1
        if self.counter == 11:
            self.layout.remove_widget(self.score_tab)
            self.layout.remove_widget(self.Input)
            self.layout.remove_widget(self.counter_tab)
            self.Text.text = f'Your score is {self.score}'
            self.layout.remove_widget(self.Submit_button)
            self.layout.remove_widget(self.back_button)

            self.back_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
            self.back_button.background_normal = 'longback.png'
            self.back_button.bind(on_release=self.custom_back)
            self.layout.add_widget(self.back_button)


            return False

        random1 = randint(1,10)
        random2 = randint(1,10)

        self.correct = random1 * random2

        self.layout.remove_widget(self.Start_button)        
        self.Text.text = f'{random1} x {random2} = ?'

        self.score_tab.text = f'{self.score} / 10'
        self.counter_tab.text = f'No. {self.counter}'
    
        # self.Input = TextInput(multiline=False, size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.Input.bind(text=self.on_text)

        self.Submit_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Submit_button.background_normal = 'submit.png'
        self.Submit_button.bind(on_release=self.correction)

        if self.counter == 1:
            self.layout.add_widget(self.score_tab)
            self.layout.add_widget(self.counter_tab)
            self.layout.add_widget(self.Input)
            self.layout.add_widget(self.Submit_button)

    def update(self, text):
        print(self.Input.text, text)


    def correction(self, *args):
        
        update = Clock.schedule_once(self.update, 0)
        
        if str(self.correct) == self.Input.text:
            self.score += 1
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.Text.text = 'CORRECT!'
            self.quick_interval = Clock.schedule_once(self.start,2)
        else:
            self.Text.text = 'WRONG!'
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.quick_interval = Clock.schedule_once(self.start,2)
    
    def custom_back(self, *args):
        self.manager.switch_to(GameScreen())
        SoundManager.play_bg_sound('main_sound.mp3')


class Div_screen(Screen):
    def on_enter(self, *args):
        self.layout = RelativeLayout()

        background = Image(source='quiz_bg.png', fit_mode='contain')
        self.add_widget(background)

        self.score = 0
        self.counter = 0

        self.back_button = Button(size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.back_button.background_normal = 'BACK.png'
        self.back_button.bind(on_release=self.custom_back)
        self.layout.add_widget(self.back_button)
        

        self.counter_tab = Label(text = '',font_size='30dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.7})

        self.score_tab = Label(text = '',font_size='28dp', color='black', bold = 'True', pos_hint={'center_x': 0.3, 'center_y': 0.6})
        # self.layout.add_widget(self.score_tab)

        self.Text = Label(text = 'Press Start to Begin',font_size='48dp', color='black', bold = 'True', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.Text)

        self.Input = TextInput(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.layout.add_widget(Input)

        self.Start_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Start_button.background_normal = 'start_quiz.png'
        self.Start_button.bind(on_release=self.start)
        self.layout.add_widget(self.Start_button)

        self.add_widget(self.layout)
        SoundManager.play_bg_sound('quiz.mp3')

    
    def start(self, *args):
        
        self.counter += 1
        if self.counter == 11:
            self.layout.remove_widget(self.score_tab)
            self.layout.remove_widget(self.Input)
            self.layout.remove_widget(self.counter_tab)
            self.Text.text = f'Your score is {self.score}'
            self.layout.remove_widget(self.Submit_button)
            self.layout.remove_widget(self.back_button)

            self.back_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
            self.back_button.background_normal = 'longback.png'
            self.back_button.bind(on_release=self.custom_back)
            self.layout.add_widget(self.back_button)


            return False

        random1 = randint(1,24) * 2

        if random1 % 3 == 0:
            self.Text.text = f'{random1} / 3 = ?'
            self.correct = random1 / 3
        elif random1 % 2 == 0:
            self.Text.text = f'{random1} / 2 = ?'
            self.correct = random1 / 2

        self.layout.remove_widget(self.Start_button)        

        self.score_tab.text = f'{self.score} / 10'
        self.counter_tab.text = f'No. {self.counter}'
    
        # self.Input = TextInput(multiline=False, size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        # self.Input.bind(text=self.on_text)

        self.Submit_button = Button(size_hint=(None, None), size=(500, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.Submit_button.background_normal = 'submit.png'
        self.Submit_button.bind(on_release=self.correction)

        if self.counter == 1:
            self.layout.add_widget(self.score_tab)
            self.layout.add_widget(self.counter_tab)
            self.layout.add_widget(self.Input)
            self.layout.add_widget(self.Submit_button)

    def update(self, text):
        print(self.Input.text, text)


    def correction(self, *args):
        
        update = Clock.schedule_once(self.update, 0)
        
        try:
            if self.correct == float(self.Input.text):
                self.score += 1
                self.score_tab.text = f'{self.score} / 10'
                self.Input.text = ''
                self.Text.text = 'CORRECT!'
                self.quick_interval = Clock.schedule_once(self.start,2)
            else:
                self.Text.text = 'WRONG!'
                self.score_tab.text = f'{self.score} / 10'
                self.Input.text = ''
                self.quick_interval = Clock.schedule_once(self.start,2)
        except(ValueError):
            self.Text.text = 'WRONG!'
            self.score_tab.text = f'{self.score} / 10'
            self.Input.text = ''
            self.quick_interval = Clock.schedule_once(self.start,2)
    
    def custom_back(self, *args):
        self.manager.switch_to(GameScreen())
        SoundManager.play_bg_sound('main_sound.mp3')


class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())

        startup_screen = StartupScreen(name='startup')
        menu_screen = MenuScreen(name='menu')
        cred_screen = Credits(name='cred')
        game_screen = GameScreen(name='game')
        add_screen = Add_screen(name='add')
        sub_screen = Sub_screen(name='sub')
        mul_screen = Mul_screen(name='mul')
        div_screen = Div_screen(name='mul')

        sm.add_widget(startup_screen)
        sm.add_widget(menu_screen)
        sm.add_widget(game_screen)
        sm.add_widget(add_screen)
        sm.add_widget(sub_screen)
        sm.add_widget(mul_screen)
        sm.add_widget(div_screen)
        sm.add_widget(cred_screen)

        return sm


if __name__ == '__main__':
    MyApp().run()