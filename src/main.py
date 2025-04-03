from src import create_app


def main():
    app = create_app()
    app.run(port=6543)


if __name__ == "__main__":
    main()
