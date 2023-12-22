import flet as ft
from screens.home import HomeView, HomeControls, window_styles_home
from screens.download import DownloadView, DownloadControls, AppBar, window_styles_download


class RouteWindow:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

    def route_change(self, e: ft.RouteChangeEvent):
        if self.page.route == "/":
            self.page.views.clear()
            self.page.views.append(
                HomeView(
                    HomeControls()
                )
            )
            self.page.update()
            window_styles_home(self.page)
        elif self.page.route == "/second_view":
            self.page.views.append(
                DownloadView(
                    AppBar(),
                    DownloadControls()
                )
            )
            self.page.update()
            window_styles_download(self.page)
        self.page.update()

    def view_pop(self, e: ft.ViewPopEvent):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


if __name__ == "__main__":
    def main_app(page: ft.Page):
        t = RouteWindow(page)
        page.on_route_change = t.route_change
        page.on_view_pop = t.view_pop
        page.go(page.route)
        page.update()

    ft.app(target=main_app)
