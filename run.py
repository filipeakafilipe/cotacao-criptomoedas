from src.main.composer.get_currencies import get_currencies_composer

if __name__=="__main__":
    response = None
    controller = get_currencies_composer()

    try:
        response = controller.handler()
    except:
        pass

    print(response)