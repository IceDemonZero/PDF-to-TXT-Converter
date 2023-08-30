import converter as con


def main():
    converter = con.Converter("")
    while True:
        path = str(input("Please provide the path: "))

        # converts document to txt
        converter.change_document(path)

        # outputs raw text of the pdf
        converter.to_txt()


if __name__ == '__main__':
    main()
