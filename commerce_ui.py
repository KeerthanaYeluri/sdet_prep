

from playwright.sync_api import Page, expect

from Python_basics.counting_no_of_characters import count


#locators:
# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()

def test_verify_plocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    # 1) page.get_by_alt_text
    logo=page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible(timeout=15000)
    # 2nd locator is get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible(timeout=15000)

   # 3)  get_by_role()
    page.get_by_role("link", name="Register").click()
    expect(page.get_by_role("heading",name="Register")).to_be_visible(timeout=15000)

    # 4) get_by_label()
    page.get_by_label("Female").check()
    page.get_by_label("First name:").fill("abc")
    page.wait_for_timeout(2)
    page.get_by_label("Last name:").fill("xyz")
    page.get_by_label("Email:").fill("keerthuyeluri@gmail.com")
    page.get_by_label("Company name:").fill("abc")
    page.locator("#Password").fill("Password@123")
    page.locator("#ConfirmPassword").fill("Password@123")

    # 5) get_by_placeholder
    page.get_by_placeholder("Search store").fill("abc")

    # 6) get_by_title
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    #7) page.get_by_test_id
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    page.wait_for_timeout(5000)

 # Practicing OrangeHRM application.

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


''''''
# CSS locators
# 1) tag Id                tag#Id
# 2) tag class             tag.class
# 3) tag attribute         tag[attribute=value]
# 4) tag class attribute   tag.class[attribute=value]
''''''

def test_verify_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    # page.locator("input#small-searchterms").fill("dresses")
    # page.locator("#small-searchterms").fill("dresses")

    #tag class
    # page.locator("input.search-box-text").fill("dresses")
    # #page.locator(".search-box-t
    #
    ##Xpath locators:
    # ext").fill("dresses")
    # page.wait_for_timeout(5000)

    #tag attribute
    page.locator("[name=q]").fill("dresses")
    page.wait_for_timeout(5000)

    #tag class attribute
    #page.locator("input.search-box-text[value='Search store']")
    page.locator(".search-box-text[value='Search store']").click()
    page.wait_for_timeout(5000)


#Xpath locators:

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #1. Absolute xpath(full xpath)
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    expect(logo).to_be_visible(timeout=5000)

    #2. Relative xpath :      //tagname[@attribute='value']
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

    #3. xpath with contains()
    products=page.locator("//h2//a[contains(@href,'computer')]")
    products_count=products.count()           #counts starts from 1
    print("products count:",products_count)
    expect(products).to_have_count(products_count)

    print("first product:",products.first.text_content())
    print("last product:",products.last.text_content())
    print("N-th product:",products.nth(2).text_content())        #nth starts from index 0

    product_title=products.all_text_contents()      #all_text_contains() this function returns all items.
    print("product_title:",product_title)    # printing all product titles by using list.

    print("printing product titles using looping statement.....")
    for i in product_title:
        print(i)

    #xpath with starts-with()
    building_products=page.locator("//h2//a[starts-with(@href./'build')]")
    print("count of building products:",building_products.count())
    expect(building_products).to_have_count(building_products.count())

    #xpath with text()  is representing


def test_dynamic_locators_using_xpaths(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    for i in range(5):
        # page.locator("//button[text()='START' or text()='STOP']").click()
        # page.locator("//button[@name='start' or @name='stop']").click()
        #page.locator("//button[contains(@name,'st')]").click()
        page.locator("//button[starts-with(@name,'st')]").click()
        page.wait_for_timeout(2000)

    # dynamic locators by using css selectors
    #//button[name='start'],button[name='stop']
    # // button[name^='st']   # equals to starts=with() in xpath
    # // button[name*='st']   # equals to contains() in xpath

