import flet as ft
from pytube import YouTube
from pathlib import Path
URL = ""


def get_url_input(url):
    global URL
    URL = url


def window_styles_download(page: ft.Page):  # PAGE STYLES
    page.title = "Youtube Download"
    page.window_max_width = 900
    page.window_max_height = 600
    page.window_width = 900
    page.window_height = 600
    page.window_center()
    page.theme_mode = "dark"


class DownloadView(ft.View):
    def __init__(self, *args):
        super().__init__()
        self.route = "/"
        self.controls = args
        self.scroll = ft.ScrollMode.AUTO


class AppBar(ft.AppBar):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Go back")
        self.leading = self.icon_back()
        self.elevation = 1

    def icon_back(self):
        return ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            on_click=lambda e: self.page.go("/")
        )


class DownloadControls(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.url = URL
        self.youtube = None
        self.dropdow = None
        self.set_data_video()

    def set_data_video(self):
        youtube = YouTube(f"{self.url}")
        self.youtube = youtube

    def title_vide(self):
        return ft.Text(
            value=self.youtube.title,
            color="white",
            weight=ft.FontWeight.W_600,
            size=32
        )

    def image_video(self):
        return ft.Image(
            src=f"{self.youtube.thumbnail_url}",
            fit=ft.ImageFit.CONTAIN,
            col={"md": 6}
        )

    def dropdown_options(self):
        self.dropdow = ft.Dropdown(
            options=[
                ft.dropdown.Option("Hight Quality"),
                ft.dropdown.Option("Low Quality"),
                ft.dropdown.Option("Audio"),
            ],
            color="white",
            hint_text="Select Quality",
            hint_style=ft.TextStyle(color="white"),
            focused_border_color="white"
        )
        return self.dropdow

    def button_download(self):
        path_download = Path.home() / "Descargas"
        if self.dropdow.value == None:
            self.dropdow.error_text = "Selec a quality"
            self.dropdow.update()

        elif self.dropdow.value == "Hight Quality":
            self.dropdow.error_text = ""
            self.dropdow.update()
            self.youtube.streams.get_highest_resolution().download(path_download)

        elif self.dropdow.value == "Low Quality":
            self.dropdow.error_text = ""
            self.dropdow.update()
            self.youtube.streams.get_lowest_resolution().download(path_download)

        elif self.dropdow.value == "Audio":
            self.dropdow.error_text = ""
            self.dropdow.update()
            self.youtube.streams.get_audio_only().download(path_download)

    def build(self):

        return ft.ResponsiveRow(
            controls=[
                # CONTAINER IMAGE AND TITLE
                ft.Container(
                    content=(
                        ft.Column(
                            controls=[
                                self.image_video(),
                                self.title_vide()
                            ]
                        )
                    ),
                    col={"md": 7}
                ),
                # CONTAINER OPTIONS DOWNLOAD
                ft.Container(
                    content=(
                        ft.Column(
                            controls=[
                                self.dropdown_options(),
                                ft.ElevatedButton(
                                    text="Download",
                                    color="white",
                                    width=200,
                                    height=40,
                                    on_click=lambda e: self.button_download(),

                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ),
                    col={"md": 5}
                )
            ]
        )
