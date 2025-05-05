## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![Cloudscraper](https://img.shields.io/badge/Cloudscraper-v1.2.71-orange)](https://github.com/codemanki/cloudscraper)
[![Google Sheets API](https://img.shields.io/badge/Google%20Sheets%20API-v4-yellowgreen)](https://developers.google.com/sheets/api)

# Geoex-Scraping

A data scraping from the Geoex system


## Installation

Clone the project

```bash
  git clone https://github.com/Max-GF/Geoex-Scraping.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. Check the [.env.example](.env.example) file for reference.

`COOKIES`
`GXSESSION`
`GXBOT`

## Usage

```bash
  python main.py
```

## Optimizations

- Types for some return, like `consult_project_in_geoex`;
- Use `concurrent.futures` or some threading features to make the code more efficient;
- Change the way of getting variables, like projects from `load_project_list`;

## Feedback

If you have any feedback, please reach out to me at maxdultra@gmail.com

## Authors

- [@Max-GF](https://github.com/Max-GF)

