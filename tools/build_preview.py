from tools import build_fonts


def main() -> None:
    build_fonts.main(
        cleanup=True,
        font_formats={'otf.woff2'},
    )


if __name__ == '__main__':
    main()
