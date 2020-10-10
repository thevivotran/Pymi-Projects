import requests
import bs4
import sys

def get_full_results():
    """
    Function to get lottery results
    """
    result = []

    f = requests.get("https://ketqua.net")
    tree = bs4.BeautifulSoup(f.text, features="lxml")

    for element in tree.find_all('td'):
        if 'data-pattern' in str(element): #'data-pattern' is on every line that have the result numbers
            result.append(element.text)
    result.pop(0)
    return result


def get_2digits_results():
    """
    Function to get lottery results with 2 last numbers
    """
    result = []
    for number in get_full_results():
        result.append(number[-2:])
    return result


def check_results(numbers):
    result = []
    lottery_results = get_2digits_results()
    for number in numbers:
        if number in lottery_results:
            result.append(number)

    if len(result) == 0:
        return get_full_results()[1:]
    elif len(result) == 1:
        return 'You have won a price with the number: {}'.format(result)
    else:
        return ('You have won {} prices'.format(len(result))
                + 'with the numbers: {}'.format(result))


def main():
    print(check_results(sys.argv[1:]))


if __name__ == "__main__":
    main()
