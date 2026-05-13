import smtplib
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from playwright.sync_api import sync_playwright

# Disable pyautogui fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.2

# Configuration
MOVIE_NAME = "Dhurandhar The Revenge"
CITY = "Hyderabad"
BUYTICKETS_URL = "https://in.bookmyshow.com/movies/hyderabad/dhurandhar-the-revenge/buytickets/ET00478891/20260322"
THEATRE_NAME = "PVR: Atrium, Gachibowli"
TARGET_TIME = "02:00PM"
NUM_SEATS = 2
SEAT_ROW = "E"
SEAT_NUMBERS = [1, 2]

# Email Configuration (Anaganaga Oka Raju)
# SENDER_EMAIL = "yelurirenu@gmail.com"
# SENDER_PASSWORD = "jiwj qgik sxed lqvr"
# RECEIVER_EMAIL = "vamsichowdarykoppula123@gmail.com"
#RECEIVER_EMAIL = "anandrajpandiri@gmail.com"   #"keerthanayeluri1@gmail.com"

# Email Configuration (Dhurandhar)
SENDER_EMAIL = "bookmyyshows@gmail.com"
SENDER_PASSWORD = "norh grtb nfgh jymb"
RECEIVER_EMAIL ="vennapureddynikhil@gmail.com"
    #("yelurirenu@gmail.com","vamsichowdarykoppula123@gmail.com","manishbadulla8114@gmail.com","vaishnavigannoju@gmail.com","gaddamshivamkumar208@gmail.com")

def send_notification_email(movie_name, details):
    msg = MIMEMultipart("alternative")
    msg["From"] = f"BookMyShow <{SENDER_EMAIL}>"
    msg["To"] = ", ".join(RECEIVER_EMAIL) if isinstance(RECEIVER_EMAIL, tuple) else RECEIVER_EMAIL
    msg["Subject"] = f"Booking Confirmed - {movie_name}"

    html_body = f"""
    <html>
    <body style="margin:0; padding:0; background-color:#f4f4f4; font-family:Arial, sans-serif;">
      <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f4; padding:20px;">
        <tr>
          <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 2px 10px rgba(0,0,0,0.1);">

              <!-- Header -->
              <tr>
                <td style="background: linear-gradient(135deg, #e23744, #c2185b); padding:30px; text-align:center;">
                  <h1 style="color:#ffffff; margin:0; font-size:24px;">Booking Confirmed!</h1>
                  <p style="color:#ffcdd2; margin:5px 0 0; font-size:14px;">Your movie tickets are booked</p>
                </td>
              </tr>

              <!-- Movie Name -->
              <tr>
                <td style="padding:25px 30px 10px; text-align:center;">
                  <h2 style="color:#333; margin:0; font-size:22px;">{details['movie']}</h2>
                  <p style="color:#777; margin:5px 0 0; font-size:13px;">Telugu | UA13+ | Comedy, Romantic, Thriller</p>
                </td>
              </tr>

              <!-- Booking Details -->
              <tr>
                <td style="padding:15px 30px;">
                  <table width="100%" cellpadding="10" cellspacing="0" style="background-color:#fafafa; border-radius:8px; border:1px solid #eee;">
                    <tr>
                      <td style="border-bottom:1px solid #eee; width:40%;">
                        <span style="color:#999; font-size:12px;">THEATRE</span><br>
                        <span style="color:#333; font-size:15px; font-weight:bold;">{details['theatre']}</span>
                      </td>
                      <td style="border-bottom:1px solid #eee;">
                        <span style="color:#999; font-size:12px;">CITY</span><br>
                        <span style="color:#333; font-size:15px; font-weight:bold;">{details['city']}</span>
                      </td>
                    </tr>
                    <tr>
                      <td style="border-bottom:1px solid #eee;">
                        <span style="color:#999; font-size:12px;">DATE</span><br>
                        <span style="color:#333; font-size:15px; font-weight:bold;">{details['date']}</span>
                      </td>
                      <td style="border-bottom:1px solid #eee;">
                        <span style="color:#999; font-size:12px;">SHOWTIME</span><br>
                        <span style="color:#333; font-size:15px; font-weight:bold;">{details['showtime']}</span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <span style="color:#999; font-size:12px;">SEATS</span><br>
                        <span style="color:#e23744; font-size:18px; font-weight:bold;">{details['seats']}</span>
                      </td>
                      <td>
                        <span style="color:#999; font-size:12px;">TICKETS</span><br>
                        <span style="color:#333; font-size:15px; font-weight:bold;">{details['num_tickets']}</span>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>

              <!-- Message -->
              <tr>
                <td style="padding:15px 30px; text-align:center;">
                  <p style="color:#555; font-size:14px; margin:0;">Enjoy the movie! See you there!</p>
                </td>
              </tr>

              <!-- Footer -->
              <tr>
                <td style="background-color:#fafafa; padding:20px 30px; text-align:center; border-top:1px solid #eee;">
                  <p style="color:#aaa; font-size:11px; margin:0;">This is an automated notification email.</p>
                </td>
              </tr>

            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("[OK] Notification email sent to", RECEIVER_EMAIL)
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")


def book_movie():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # STEP 1: Open buytickets page
        print("STEP 1: Opening BookMyShow buytickets page...")
        page.goto(BUYTICKETS_URL, wait_until="domcontentloaded")
        page.wait_for_timeout(10000)
        print(f"[OK] Page loaded: {page.url}")

        # Scroll to load all theatres
        for _ in range(15):
            page.evaluate("window.scrollBy(0, 400)")
            page.wait_for_timeout(500)
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(2000)

        # STEP 2: Find Theatre
        print(f"\nSTEP 2: Finding '{THEATRE_NAME}'...")
        theatre_found = False
        for selector in [f"span:has-text('{THEATRE_NAME}')", f"text='{THEATRE_NAME}'", "span:has-text('PVR')", "span:has-text('Atrium')"]:
            try:
                theatre_el = page.locator(selector).first
                if theatre_el.is_visible(timeout=3000):
                    theatre_el.scroll_into_view_if_needed()
                    page.wait_for_timeout(1000)
                    theatre_found = True
                    print(f"[OK] Found '{THEATRE_NAME}'")
                    break
            except Exception:
                continue
        if not theatre_found:
            print(f"[ERROR] Could not find '{THEATRE_NAME}'")

        # STEP 3: Select Showtime
        print(f"\nSTEP 3: Selecting '{TARGET_TIME}' showtime...")
        # Debug: print all visible showtime links
        page.screenshot(path="debug_showtimes.png")
        all_times = page.locator("a[data-online='Y']").all()
        if not all_times:
            all_times = page.locator("a >> text=/\\d{2}:\\d{2}/").all()
        print(f"  [DEBUG] Found {len(all_times)} showtime elements:")
        for t in all_times[:10]:
            try:
                print(f"    - '{t.text_content().strip()}'")
            except:
                pass
        showtime_found = False
        for selector in [f"text='{TARGET_TIME}'", "text='02:00 PM'", "a:has-text('02:00')", "text='02:00'"]:
            try:
                showtime_el = page.locator(selector).first
                if showtime_el.is_visible(timeout=3000):
                    showtime_el.click()
                    showtime_found = True
                    print(f"[OK] Selected showtime: {TARGET_TIME}")
                    break
            except Exception:
                continue
        if not showtime_found:
            print(f"[ERROR] Could not find showtime '{TARGET_TIME}'")

        page.wait_for_timeout(4000)

        # STEP 4: Select number of seats
        print(f"\nSTEP 4: Selecting {NUM_SEATS} seats...")
        try:
            clicked = page.evaluate(f"""
                () => {{
                    const items = document.querySelectorAll('li');
                    for (const li of items) {{
                        if (li.textContent.trim() === '{NUM_SEATS}') {{
                            li.click();
                            return true;
                        }}
                    }}
                    return false;
                }}
            """)
            if clicked:
                print(f"[OK] Selected {NUM_SEATS} seats")
        except Exception:
            print(f"[ERROR] Could not select {NUM_SEATS} seats")

        page.wait_for_timeout(1000)

        # STEP 5: Click Select Seats
        print("\nSTEP 5: Clicking 'Select Seats'...")
        for selector in ["text='Select Seats'", "button:has-text('Select Seats')"]:
            try:
                el = page.locator(selector).first
                if el.is_visible(timeout=3000):
                    el.click()
                    print("[OK] Clicked 'Select Seats'")
                    break
            except Exception:
                continue

        page.wait_for_timeout(8000)

        # STEP 6: Select actual seats on canvas (Row E, Seats 1 & 2)
        print(f"\nSTEP 6: Selecting Row {SEAT_ROW}, Seats {SEAT_NUMBERS} on canvas...")

        # Find the canvas element (seat layout)
        canvas_elements = page.locator("canvas").all()
        print(f"Found {len(canvas_elements)} canvas elements")

        if canvas_elements:
            main_canvas = max(canvas_elements, key=lambda c: c.bounding_box()['width'] * c.bounding_box()['height'])
            main_canvas.scroll_into_view_if_needed()
            page.wait_for_timeout(2000)

            # Get canvas size
            box = main_canvas.bounding_box()
            canvas_width = box['width']
            canvas_height = box['height']
            print(f"Canvas size: {canvas_width}x{canvas_height}")

            # Take screenshot of seat layout for reference
            page.screenshot(path="debug_seat_layout.png")

            # Use Playwright's click relative to canvas element (no pyautogui needed)
            # Row E, Seats 1 & 2 — percentages relative to canvas
            # Row E, Seats 1 & 2 — calibrated from seat layout screenshot
            click_positions = [
                (0.38, 0.38),  # Seat 1, Row E
                (0.40, 0.38),  # Seat 2, Row E
            ]

            for i, (x_pct, y_pct) in enumerate(click_positions):
                click_x = int(canvas_width * x_pct)
                click_y = int(canvas_height * y_pct)
                print(f"  Clicking Seat {SEAT_NUMBERS[i]} at canvas ({click_x}, {click_y})")
                main_canvas.click(position={"x": click_x, "y": click_y}, force=True)
                page.wait_for_timeout(500)

            print(f"[OK] Clicked Row {SEAT_ROW}, Seats {SEAT_NUMBERS}")
        else:
            print("[ERROR] No canvas found for seat selection")

        page.wait_for_timeout(3000)

        # STEP 7: Click Pay button
        print("\nSTEP 7: Clicking 'Pay' button...")
        pay_clicked = False
        for selector in ["button:has-text('Pay')", "text='Pay'", "div:has-text('Pay') >> nth=0"]:
            try:
                el = page.locator(selector).first
                if el.is_visible(timeout=5000):
                    el.click()
                    pay_clicked = True
                    print("[OK] Clicked Pay")
                    break
            except Exception:
                continue
        if not pay_clicked:
            print("[ERROR] Could not find Pay button")

        page.wait_for_timeout(3000)

        # STEP 8: Click Accept button
        print("\nSTEP 8: Clicking 'Accept' button...")
        accept_clicked = False
        for selector in ["button:has-text('Accept')", "text='Accept'", "div:has-text('Accept') >> nth=0"]:
            try:
                el = page.locator(selector).first
                if el.is_visible(timeout=5000):
                    el.click()
                    accept_clicked = True
                    print("[OK] Clicked Accept")
                    break
            except Exception:
                continue
        if not accept_clicked:
            print("[INFO] No Accept button found (may not be needed)")

        # Wait for page to navigate after Pay/Accept
        page.wait_for_timeout(8000)

        # Gather booking details
        current_url = page.url
        seat_info = ", ".join([f"{SEAT_ROW}{s}" for s in SEAT_NUMBERS])
        details = {
            "movie": MOVIE_NAME,
            "city": CITY,
            "theatre": THEATRE_NAME,
            "date": "Sun, 22 Mar 2026",
            "showtime": TARGET_TIME,
            "seats": seat_info,
            "num_tickets": f"{NUM_SEATS} Tickets",
        }
        print(f"\nCurrent URL: {current_url}")

        # STEP 9: Send notification email
        print("\nSTEP 9: Sending notification email...")
        send_notification_email(MOVIE_NAME, details)

        print("\n=== Browser will close in 30 seconds ===")
        page.wait_for_timeout(30000)
        browser.close()


if __name__ == "__main__":
    book_movie()