from app_ui.interface import build_interface


def main():
    app = build_interface()
    app.launch(inbrowser=True, share=False)


if __name__ == "__main__":
    main()