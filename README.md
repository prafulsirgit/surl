# SURL 🧞‍♂️✨ - Instantly Shorten, Seamlessly Share\!

## Tired of long, clunky URLs? Wish you could brand your links or make them easier to remember?

**URL Genie** is your magical solution\! This simple yet powerful URL shortener allows you to transform lengthy web addresses into concise, shareable links. Whether it's for social media, marketing campaigns, or just tidying up your browser, URL Genie makes your links work smarter, not harder.

-----

## Key Features
 * **Instant Shortening:** Generate short URLs in a flash.
 * **Custom Aliases:** Personalize your shortened links with memorable, branded custom aliases (e.g., `urlgenie.com/your-product-name`).
 * **Auto-Expiring Links:** Links automatically expire after 3 days, ensuring a clean database and promoting good link hygiene.
 * **Secure & Private:** Built with simplicity and privacy in mind.
 * **Lightweight & Efficient:** A fast and responsive experience, powered by Flask and SQLite.

-----

## For the Everyday User

### How to Use URL Genie

    1.  **Visit the homepage:** Simply navigate to the URL Genie web interface.
    2.  **Paste your long URL:** Enter the full web address you want to shorten into the input field.
    3.  **(Optional) Add a Custom Alias:** Want a personalized link? Type in your desired short code (e.g., `my-cool-link`). If left blank, a random one will be generated for you.
    4.  **Click "Shorten"\!** Your new, compact URL will be instantly generated and displayed. Copy it and share away\!

-----

## For Developers

### Getting Started (Local Setup)

URL Genie is built with Python and Flask, using SQLite for its database. It's designed to be straightforward to set up and run.

#### Prerequisites

  * Python 3.6+
  * `pip` (Python package installer)

#### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/prafulsirgit/surl.git
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    python app.py
    ```

    The application will typically run on `http://127.0.0.1:5000/`.

-----

### Project Structure

```
.
├── app.py                  # The main Flask application
├── requirements.txt        # Python dependencies
├── short.db                # SQLite database file (will be created on first run)
├── static/                 # Static assets (CSS, JS, images - if any)
│   └── ...
└── templates/              # HTML templates
    └── index.html          # Main application template
├── LICENSE                 # Project license
└── README.md               # This README file
```

-----

### Code Overview

  * **`app.py`**:
      * **`init_db()`**: Initializes the SQLite database, creating the `urls` table if it doesn't exist.
      * **`generate_code()`**: Generates a random alphanumeric short code for URLs without a custom alias.
      * **`delete_expired()`**: A crucial function that periodically cleans up the database by removing URLs older than 3 days. This helps maintain performance and relevancy.
      * **`index()` route (`/`)**: Handles both displaying the shortening form (GET) and processing URL submission (POST). It manages custom alias conflicts and stores new URLs.
      * **`redirect_to_original()` route (`/<short_code>`)**: This is the core redirection logic. It fetches the original URL based on the `short_code` and redirects the user, or returns a 404 if the link is not found or expired.
  * **`short.db`**: An SQLite database file. This lightweight database is perfect for a simple application like URL Genie, requiring no external setup.
  * **`templates/index.html`**: The front-end HTML template for the URL shortening interface.

-----

### Future Enhancements (Ideas for Contribution\!)

  * **User Accounts:** Allow users to manage their shortened URLs, view statistics, and track clicks.
  * **Click Analytics:** Implement basic click tracking for shortened URLs (e.g., number of clicks, geographical data).
  * **QR Code Generation:** Automatically generate QR codes for each shortened URL.
  * **API Endpoints:** Provide a RESTful API for programmatic URL shortening.
  * **Containerization:** Dockerize the application for easier deployment.
  * **Robust Error Handling:** More sophisticated error handling and user feedback.
  * **Enhanced UI/UX:** Improve the user interface with modern styling and responsiveness.

-----

## Contributing

We welcome contributions\! If you have an idea for a new feature, a bug fix, or an improvement, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature X'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

-----

## License

This project is licensed under the [MIT License](#).

-----

## Connect

Have questions or just want to say hi? Feel free to reach out\!

  * **GitHub:** [prafulsirgit](https://github.com/prafulsirgit)

-----
