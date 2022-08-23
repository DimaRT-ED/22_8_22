from pom.pages.home_page import HomePage


def test_login(dr):

    data = ['standard_user', 'secret_sauce']
    """
    usrName = 'standard_user'
    password = 'secret_sauce'
"""
    homepage = HomePage(dr)
    homepage.load_page()
    #homepage.login(usrName, password)
    homepage.login(data[0], data[1])