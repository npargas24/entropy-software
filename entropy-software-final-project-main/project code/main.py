from kivy.app import App
# from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem

# Here I'm setting the text segments. I'm doin it here, because in the future
# I could add a function to randomize text if I abstract it out to this.
regularText = "And as I sat there brooding on the old, unknown world, I thought of Gatsby’s wonder when he first picked out the green light at the end of Daisy’s dock. He had come a long way to this blue lawn and his dream must have seemed so close that he could hardly fail to grasp it. He did not know that it was already behind him, somewhere back in that vast obscurity beyond the city, where the dark fields of the republic rolled on under the night. Gatsby believed in the green light, the orgastic future that year by year recedes before us. It eluded us then, but that’s no matter—tomorrow we will run faster, stretch out our arms farther.... And one fine morning we’ll... So we beat on, boats against the current, borne back ceaselessly into the past."
codeText = "while true: Please help me."

# these pass the elements created in the Kivy file to the functions in main.
class TabWrapper(BoxLayout):
    pass

class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class TypingScreen(Screen):
    pass

class StatisticsScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class LeaderboardScreen(Screen):
    pass

class SettingScreen(Screen):
    def on_state(self):
        print(self.ids.textMode.state, self.ids.codeMode.state)


class TypingTestApp(MDApp):
    # savedTestText = None

    #def typingTest(self, savedTestText):


    def build(self):
        # The screenmanager should allow us to manage switching betwen screens.
        # here I create the scren manager:
        sm = ScreenManager(transition=SlideTransition())

        # here I create our screens, with their respective names:
        sm.add_widget(SettingScreen(name = 'login'))
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(TypingScreen(name = 'typingtest'))
        sm.add_widget(StatisticsScreen(name = 'statistics'))
        # sm.add_widget(AccountScreen(name = 'account'))
        sm.add_widget(LeaderboardScreen(name = 'leaderboard'))
        sm.add_widget(SettingScreen(name = 'settings'))

        # Still trying to figure out how to reference the specific variable of typingTestExampleText
        # sm.get_screen('typingtest').ids.typingTestExampleText.text = codeText
        # returns the screen manager to the app
        return TabWrapper()

    # while True:
    # i = 0
    # while i < 100:
    #     print()
    #     i+1

        # if TabWrapper.BoxLayout.ScreenManager.get_screen(SettingScreen).ids["codeMode"].state == 'down':
        #     savedTestText = codeText
        # else:
        #     savedTestText = regularText


# this runs what we want to run, namely our main app. This will run our main.
if __name__ == '__main__':
    TypingTestApp().run()
