import re
def isValidURL(url):
    """
    Write a function Boolean isValidURL(String url).
    Input : str = “https://www.bigohtech.com/”
    Output : Yes
    Explanation : The above URL is a valid URL.
    Input : str = “https:// www.bigohtech.com/”
    Output : No
    Explanation : Note that there is a space after https://, hence the URL is invalid.
    """
    pattern = r"^https://www\.[a-zA-Z0-9]+\.com/$"
    if re.match(pattern, url):
        return True
    else:
        return False
str = input("Enter URL : ")
print(isValidURL(str))
