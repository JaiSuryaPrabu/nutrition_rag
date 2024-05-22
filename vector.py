def vector(filtered_df):
    filtered_df = data[data['Token Count'] > 30]
    

    model_name = 'sentence-transformers/all-mpnet-base-v2'

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    embeddings = []
    for text in filtered_df['text']:
            encoded_input = tokenizer(text, return_tensors='pt', padding='max_length', truncation=True)
  
            output = model(**encoded_input)
  
            sentence_embedding = output.last_hidden_state[:, 0].detach().numpy()[0]
            embeddings.append(sentence_embedding)

    embeddings_tensor = tf.convert_to_tensor(embeddings)
    return embeddings_tensor
