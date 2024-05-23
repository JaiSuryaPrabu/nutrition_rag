from sentence_transformers import SentenceTransformer
#assigning the df to data 
data = create_page_wise_table(pdf_files)#create_page_wise_table is a function in text extraction.py
#removing rows with token count less than 30
filtered_df = data[data['Token Count'] > 30]

#hugging face model
model_name = "all-mpnet-base-v2"
device = 'cpu'  



def embed_text(model_name, data, device):
 

  embedding_model = SentenceTransformer(model_name_or_path=model_name, device=device)

  for item in data:
    item["embeddings"] = embedding_model.encode(item["sentence_chunk"], convert_to_tensor=True)

  


  text_data = []
  for text in filtered_df['text']:
    text_data.append({"sentence_chunk": text})

  embeddings_data = embed_text(model_name, text_data, device)

  filtered_df["embeds"] = [item["embeddings"] for item in embeddings_data]

  return filtered_df

#convert df into csv 
def df_to_csv(dataframe, filename):
  dataframe.to_csv(filename, index=False)  

print(df_to_csv(filtered_df, "output.csv"))  
