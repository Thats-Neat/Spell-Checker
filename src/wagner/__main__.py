from algo import wagner_fischer


if __name__ == "__main__":
    instance = wagner_fischer()
    word, possible = instance.manual_input()
    print("Distance:", instance.wagner(word, possible))
