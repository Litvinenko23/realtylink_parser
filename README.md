# Realtylink parser

RealtyLink Parser is a Python script designed for scraping and collecting information about rental properties from the RealtyLink website. It utilizes web scraping techniques, BeautifulSoup, and Selenium to extract details such as property title, location, description, images, price, rooms quantity, and floor area. The gathered data is then stored in a JSON file for further analysis or use..

## How to Use

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Litvinenko23/realtylink_parser
    ```

2. Navigate to the project directory:

    ```bash
    cd realtylink_parser
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the script:

    ```bash
    python parser.py
    ```

