# IQRA Smart AI Search for Quran

IQRA Smart AI Search for Quran is an advanced search tool powered by ChatGPT, designed to make searching Quranic verses easy and efficient. Currently, Quran translations are available in Arabic, English, and Tamil.

## About

This project aims to assist users in searching Quranic verses effortlessly using AI. It leverages the power of ChatGPT and the Quran.com API to provide accurate and relevant search results. One of our primary goals is to provide access to the Quran to everyone easily.

## Features

- Search Quranic verses easily
- Available translations:
  - English by Saheeh International
  - Tamil by Sheikh Omar Sharif bin Abdul Salam
  - Arabic Uthmani Script
- Open for developer contributions
- Issue tracking and feature requests supported

## How It Works

1. The Python script `quran-api.py` fetches data from the Quran.com API.
2. It generates a `quran_data.json` file containing the necessary Quranic data.
3. The generated JSON file is used to train the IQRA Smart AI Search for Quran GPT.

## Getting Started

### Prerequisites

- Python 3.12.0
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SarbudeenDeveloper/IQRA-Smart-AI-Search-for-Quran.git
    cd IQRA-Smart-AI-Search-for-Quran
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Python script to generate the JSON file:
    ```sh
    python src/quran-api.py
    ```

## Contributing

We welcome contributions from the developer community. If you're interested in contributing, please fork the repository and create a pull request with your changes.

## Issues and Feature Requests

Feel free to file issues and raise feature requests. We value your feedback and strive to improve the project continuously.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Folder Structure
```
IQRA-Smart-AI-Search-for-Quran/
├── data/
│ └── quran_data.json
├── src/
│ └── quran-api.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Contact

For any inquiries or further information, please contact us at [email@example.com](mailto:email@example.com).