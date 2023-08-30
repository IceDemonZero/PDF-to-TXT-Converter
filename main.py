import converter as con


extractor = con.Converter("")

def main():
    while True:
        path = str(input("Please provide the path: "))
        extractor.change_document(path)
        extractor.to_txt()


if __name__ == '__main__':
    main
