import flet as ft
from screens.download import get_url_input


# THIS FUNCTION IS THE RESPONSIBLE FOR WINDOW STYLE
def window_styles_home(page: ft.Page):  # PAGE STYLES
    page.title = "Youtube Download"
    page.window_max_height = 550
    page.window_width = 600
    page.window_height = 550
    page.window_center()
    page.theme_mode = "dark"
    page.update()


class HomeControls(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.url = None
        self.logo_yt = None
        self.bt_continue = None

    def image_logo(self):  # LOGO YOUTUBE
        self.logo_yt = ft.Image(
            src="../assets/youtube.svg",
            fit=ft.ImageFit.CONTAIN,
            height=200
        )
        return self.logo_yt

    def url_input(self):  # INPUT FOR THE VIDEO URL
        self.url = ft.TextField(
            hint_text="Put here the url video",
            focused_border_color="white",
        )
        return self.url

    def button_continue(self):  # BUTTON CONTINUE FOR THE SECOND VIEW

        def on_click_bt(e):
            if "https://www.youtube.com" in self.url.value:
                get_url_input(self.url.value)
                self.page.go("/second_view")
            else:
                self.url.error_text = "Opps! only youtube video"
                self.url.update()

        self.bt_continue = ft.ElevatedButton(
            text="Continue",
            color="white",
            width=190,
            height=40,
            on_click=on_click_bt
        )

        return self.bt_continue

    def build(self):
        return ft.Container(
            content=(
                ft.Column(
                    controls=[
                        self.image_logo(),
                        self.url_input(),
                        self.button_continue()
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ),
            alignment=ft.alignment.center,
            padding=50,
            width=600
        )


# THIS CLASS CONTROLLING HOME VIEW AND ROUTE
class HomeView(ft.View):
    def __init__(self, *args):
        super().__init__()
        self.route = "/"
        self.controls = args
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.scroll = ft.ScrollMode.AUTO
