import flet as ft

def main(page: ft.Page):
    page.title = "عداد الإقلاع عن الإباحية"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def update_count(e):
        days = (page.controls[1].controls[1].text)
        try:
            days = int(days)
        except ValueError:
            page.controls[1].controls[1].text = "0"
            days = 0
        page.controls[1].controls[1].text = str(days + 1)
        page.update()

    def reset_count(e):
        page.controls[1].controls[1].text = "0"
        page.update()

    page.controls = [
        ft.Text(value="عداد الإقلاع عن الإباحية", text_align="center", width=300),
        ft.Container(
            width=300,
            padding=10,
            border_radius=10,
            border=ft.border.all(1, "blue"),
            content=ft.Column(
                controls=[
                    ft.Text(value="عدد الأيام"),
                    ft.TextField(
                        value="0",
                        text_align="center",
                        width=200,
                        border_radius=5,
                        border=ft.border.all(1, "blue"),
                    ),
                ]
            ),
        ),
        ft.ElevatedButton("أضف يوم", on_click=update_count),
        ft.ElevatedButton("إعادة التعيين", on_click=reset_count),
    ]
    page.update()

ft.app(target=main)