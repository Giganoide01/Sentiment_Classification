# Sentiment_Classification
Modelos de classificação de sentimentos com base em avaliações da assitente inteligente Alexa (Echo dot 4ª Geração). Trabalho desenvolvido para a avaliação final da matéria de Mineração de Texto e Web da especialização em Ciência de Dados do CIn - UFPE

## Discentes:
- Leonardo Miranda de Brito
- Natália Oliveira

## Conteúdo:
- Dataset: Contém 3 datasets.
  - Datset com texto contendo Stopwords, sem stemming (NoStem_TotalStopwordRemoval_dataset.csv);
  - Datset com texto sem Stopwords, sem stemming (NoStem_StopwordKeep_dataset.csv);
  - Datset com texto sem Stopwords, com stemming (Stem_TotalStopwordRemoval_dataset.csv).

- Scripts: Contém os scripts utilizados durante o projeto.
  - Notebook com o pré-processamento dos dados (pre_processing.ipynb);
  - Notebook com os experimentos com TFIDF e Random Forest com e sem stemming (TFIDF+RF.ipynb);
  - Notebook com os experimentos com classificação por CNN (CNN_classifier.ipynb);
  - Notebook com os experimentos com classificação por LSTM (LSTM_classifier.ipynb);
  - Notebook com os experimentos com classificação por BERT (BERT.ipynb);
  - Notebook com os plots de avaliação extras sobre os classificadores (evaluation_plots.ipynb).

- dataset_with_prediction: Contém datasets de teste salvos com a predição de seu respectivo modelo.
  -  RF_noStem_predict.csv;
  -  RF_Stem_predict.csv;
  -  CNN_predict.csv;
  -  LSTM_predict.csv;
  -  BERT_predict.csv.

- amazon_reviews_scraping: códigos usados durante o web scrapping

## Link para o vídeo
https://www.dropbox.com/s/zfeecqdehywaam9/Mineracao_Texto_TrabFinal_Leonardo_Natalia.mp4?dl=0

## Link para página do streamlit
https://share.streamlit.io/nsilvade/minera-o/main/app.py

## Link para repositório do streamlit
https://github.com/NSILVADE/Minera-o.git
