def extract_features(pdf_file):
  pdf_document = fitz.open(pdf_file)
  num_pages = pdf_document.page_count

  page_wise_features = []
  for page_number in range(num_pages):
    page = pdf_document[page_number]
    text = page.get_text()  # Extract text from current page

    # Tokenization
    tokens = re.findall(r'\b\w+\b', text)
    token_count = len(tokens)

    word_count = len(text.split())
    sentence_count = len(text.split('.'))  # Assuming period-delimited sentences

    # Create a dictionary for features of this page
    page_features = {
        'PDF File': pdf_file,
        'Page Number': page_number + 1,  # Adjust for 1-based indexing
        'Token Count': token_count,
        'Word Count': word_count,
        'Sentence Count': sentence_count,
        'text' : text

    }
    page_wise_features.append(page_features)

  pdf_document.close()
  return page_wise_features

def create_page_wise_table(pdf_files):
  """
  Processes a list of PDF files, extracts page-wise features,
  and returns a pandas DataFrame.
  """
  all_page_features = []
  for pdf_file in pdf_files:
    page_wise_features = extract_features(pdf_file)
    all_page_features.extend(page_wise_features)

  # Create a DataFrame from the features list
  df = pd.DataFrame(all_page_features)
  data['text'] = data['text'].str.strip()
  url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
  data['text'] = data['text'].str.replace(url_pattern, '', regex=True)
  return data


