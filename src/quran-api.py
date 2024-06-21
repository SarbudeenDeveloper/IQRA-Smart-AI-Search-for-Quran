import requests
import json
import argparse
import os

# Define the base URLs and translation IDs
base_url = "https://api.quran.com/api/v4/"
chapters_url = base_url + "chapters"
verses_url = base_url + "quran/verses/uthmani"
translations_url = base_url + "quran/translations/"
english_translation_id = 20
tamil_translation_id = 229
json_filename = os.path.join(os.path.dirname(__file__), "../data/quran_data.json")

def fetch_data_and_save_json():
    print("Fetching chapters...")
    chapters_response = requests.get(chapters_url).json()
    chapters = chapters_response['chapters']

    final_data = []

    for chapter in chapters:
        chapter_id = chapter['id']
        name_simple = chapter['name_simple']
        name_arabic = chapter['name_arabic']
        verses_count = chapter['verses_count']
        translated_name = chapter['translated_name']['name']

        # Fetch verses for the chapter
        print(f"Fetching verses for chapter {name_simple}...")
        verses_response = requests.get(verses_url, params={'chapter_number': chapter_id}).json()
        verses = verses_response['verses']

        # Fetch English translations
        print(f"Fetching English translations for chapter {name_simple}...")
        english_translations_response = requests.get(
            translations_url + str(english_translation_id), params={'chapter_number': chapter_id}
        ).json()
        english_translations = english_translations_response['translations']

        # Fetch Tamil translations
        print(f"Fetching Tamil translations for chapter {name_simple}...")
        tamil_translations_response = requests.get(
            translations_url + str(tamil_translation_id), params={'chapter_number': chapter_id}
        ).json()
        tamil_translations = tamil_translations_response['translations']

        verses_data = []
        for i, verse in enumerate(verses):
            verse_key = verse['verse_key']
            text_uthmani = verse['text_uthmani']
            english_translation_text = english_translations[i]['text'] if i < len(english_translations) else ""
            tamil_translation_text = tamil_translations[i]['text'] if i < len(tamil_translations) else ""

            verses_data.append({
                "verseKey": verse_key,
                "textUthmani": text_uthmani,
                "englishTranslationText": english_translation_text,
                "tamilTranslationText": tamil_translation_text
            })

        final_data.append({
            "chapterNameEnglish": name_simple,
            "chapterNameArabic": name_arabic,
            "totalVersesCount": verses_count,
            "chapterTranslatedNameEnglish": translated_name,
            "verses": verses_data
        })

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(json_filename), exist_ok=True)

    # Save data to a JSON file
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(final_data, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to {json_filename}")

    return final_data

def main():
    parser = argparse.ArgumentParser(description="Fetch Quran data and save it to JSON")
    parser.add_argument('--fetch', action='store_true', help="Fetch data from the APIs and save to JSON")
    parser.add_argument('--generate', action='store_true', help="Generate Excel file from JSON data (feature not implemented yet)")

    args = parser.parse_args()

    if args.fetch:
        fetch_data_and_save_json()
    else:
        print("Please specify an action: --fetch to fetch data or --generate to generate Excel from JSON (feature not implemented yet)")

if __name__ == "__main__":
    main()