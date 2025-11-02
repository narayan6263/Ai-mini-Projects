# # # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # # from collections import Counter

# # # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # # # 🔥 Allow connections from React (port 3000)
# # # # # # # # # # # # # CORS(app, resources={r"/*": {"origins": "*"}})

# # # # # # # # # # # # # @app.route('/analyze', methods=['POST'])
# # # # # # # # # # # # # def analyze():
# # # # # # # # # # # # #     data = request.get_json()
# # # # # # # # # # # # #     text = data.get('text', '')
# # # # # # # # # # # # #     words = text.split()

# # # # # # # # # # # # #     result = {
# # # # # # # # # # # # #         "characters": len(text),
# # # # # # # # # # # # #         "words": len(words),
# # # # # # # # # # # # #         "unique_words": len(set(words)),
# # # # # # # # # # # # #         "top_words": Counter(words).most_common(5)
# # # # # # # # # # # # #     }

# # # # # # # # # # # # #     return jsonify(result)

# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app.run(host="0.0.0.0", port=5000)
# # # # # # # # # # # # # backend/app.py
# # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # from collections import Counter
# # # # # # # # # # # # from textblob import TextBlob
# # # # # # # # # # # # import nltk
# # # # # # # # # # # # nltk.download('punkt')

# # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # # # # # # # def analyze():
# # # # # # # # # # # #     data = request.get_json()
# # # # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # # # #     words = nltk.word_tokenize(text)
# # # # # # # # # # # #     words_clean = [w.lower() for w in words if w.isalpha()]
# # # # # # # # # # # #     word_count = Counter(words_clean)
# # # # # # # # # # # #     top_words = word_count.most_common(5)
# # # # # # # # # # # #     return jsonify({
# # # # # # # # # # # #         "characters": len(text),
# # # # # # # # # # # #         "words": len(words_clean),
# # # # # # # # # # # #         "unique_words": len(set(words_clean)),
# # # # # # # # # # # #         "top_words": top_words
# # # # # # # # # # # #     })

# # # # # # # # # # # # @app.route("/ai-free", methods=["POST"])
# # # # # # # # # # # # def ai_free():
# # # # # # # # # # # #     data = request.get_json()
# # # # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # # # #     # Simple summarization (first 3 sentences)
# # # # # # # # # # # #     sentences = nltk.sent_tokenize(text)
# # # # # # # # # # # #     summary = " ".join(sentences[:3])
# # # # # # # # # # # #     return jsonify({"summary": summary})

# # # # # # # # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # # # # # # # def keywords():
# # # # # # # # # # # #     data = request.get_json()
# # # # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # # # #     words = nltk.word_tokenize(text)
# # # # # # # # # # # #     words_clean = [w.lower() for w in words if w.isalpha()]
# # # # # # # # # # # #     word_count = Counter(words_clean)
# # # # # # # # # # # #     keywords = [w for w, c in word_count.most_common(10)]
# # # # # # # # # # # #     return jsonify({"keywords": keywords})

# # # # # # # # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # # # # # # # def sentiment():
# # # # # # # # # # # #     data = request.get_json()
# # # # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # # # #     blob = TextBlob(text)
# # # # # # # # # # # #     polarity = blob.sentiment.polarity
# # # # # # # # # # # #     if polarity > 0:
# # # # # # # # # # # #         sentiment = "Positive"
# # # # # # # # # # # #     elif polarity < 0:
# # # # # # # # # # # #         sentiment = "Negative"
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         sentiment = "Neutral"
# # # # # # # # # # # #     return jsonify({"sentiment": sentiment, "polarity": polarity})

# # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # from collections import Counter
# # # # # # # # # # # import re

# # # # # # # # # # # # For AI summary
# # # # # # # # # # # from sumy.parsers.plaintext import PlaintextParser
# # # # # # # # # # # from sumy.nlp.tokenizers import Tokenizer
# # # # # # # # # # # from sumy.summarizers.lsa import LsaSummarizer

# # # # # # # # # # # # For sentiment analysis
# # # # # # # # # # # from textblob import TextBlob

# # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # CORS(app)

# # # # # # # # # # # # ----------------------
# # # # # # # # # # # # Text Analysis Endpoint
# # # # # # # # # # # # ----------------------
# # # # # # # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # # # # # # def analyze_text():
# # # # # # # # # # #     data = request.json
# # # # # # # # # # #     text = data.get("text", "")

# # # # # # # # # # #     if not text.strip():
# # # # # # # # # # #         return jsonify({"error": "No text provided"}), 400

# # # # # # # # # # #     # Clean text and split
# # # # # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # # # # #     word_counts = Counter(words)
# # # # # # # # # # #     top_words = word_counts.most_common(5)

# # # # # # # # # # #     result = {
# # # # # # # # # # #         "characters": len(text),
# # # # # # # # # # #         "words": len(words),
# # # # # # # # # # #         "unique_words": len(word_counts),
# # # # # # # # # # #         "top_words": top_words
# # # # # # # # # # #     }
# # # # # # # # # # #     return jsonify(result)

# # # # # # # # # # # # ----------------------
# # # # # # # # # # # # AI Summary Endpoint
# # # # # # # # # # # # ----------------------
# # # # # # # # # # # @app.route("/ai-free", methods=["POST"])
# # # # # # # # # # # def ai_summary():
# # # # # # # # # # #     data = request.json
# # # # # # # # # # #     text = data.get("text", "")

# # # # # # # # # # #     if not text.strip():
# # # # # # # # # # #         return jsonify({"summary": "No text provided"})

# # # # # # # # # # #     parser = PlaintextParser.from_string(text, Tokenizer("english"))
# # # # # # # # # # #     summarizer = LsaSummarizer()
# # # # # # # # # # #     summary_sentences = summarizer(parser.document, sentences_count=5)
# # # # # # # # # # #     summary = " ".join([str(s) for s in summary_sentences])

# # # # # # # # # # #     if not summary:
# # # # # # # # # # #         summary = "Text too short to summarize"

# # # # # # # # # # #     return jsonify({"summary": summary})

# # # # # # # # # # # # ----------------------
# # # # # # # # # # # # Keywords Extraction
# # # # # # # # # # # # ----------------------
# # # # # # # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # # # # # # def keywords():
# # # # # # # # # # #     data = request.json
# # # # # # # # # # #     text = data.get("text", "")

# # # # # # # # # # #     if not text.strip():
# # # # # # # # # # #         return jsonify({"keywords": []})

# # # # # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # # # # #     word_counts = Counter(words)
# # # # # # # # # # #     top_words = [w for w, c in word_counts.most_common(5)]

# # # # # # # # # # #     return jsonify({"keywords": top_words})

# # # # # # # # # # # # ----------------------
# # # # # # # # # # # # Sentiment Analysis
# # # # # # # # # # # # ----------------------
# # # # # # # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # # # # # # def sentiment():
# # # # # # # # # # #     data = request.json
# # # # # # # # # # #     text = data.get("text", "")

# # # # # # # # # # #     if not text.strip():
# # # # # # # # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})

# # # # # # # # # # #     blob = TextBlob(text)
# # # # # # # # # # #     polarity = blob.sentiment.polarity

# # # # # # # # # # #     if polarity > 0:
# # # # # # # # # # #         sentiment_result = "positive"
# # # # # # # # # # #     elif polarity < 0:
# # # # # # # # # # #         sentiment_result = "negative"
# # # # # # # # # # #     else:
# # # # # # # # # # #         sentiment_result = "neutral"

# # # # # # # # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # # # # # # # ----------------------
# # # # # # # # # # # # Run Server
# # # # # # # # # # # # ----------------------
# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # from collections import Counter
# # # # # # # # # # import re
# # # # # # # # # # import requests

# # # # # # # # # # # For fallback local AI generation
# # # # # # # # # # from transformers import pipeline

# # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # CORS(app)

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Gemini AI Config
# # # # # # # # # # # ----------------------
# # # # # # # # # # API_KEY = "AIzaSyDPDjDu1_aArU35YdtVLGCBcc6KlHa9VIQ"
# # # # # # # # # # MODEL_NAME = "gemini-2.0-flash"

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Load fallback local AI model
# # # # # # # # # # # ----------------------
# # # # # # # # # # print("⏳ Loading local fallback AI model (distilgpt2)...")
# # # # # # # # # # local_generator = pipeline("text-generation", model="distilgpt2")
# # # # # # # # # # print("✅ Local AI model loaded!")

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Home
# # # # # # # # # # # ----------------------
# # # # # # # # # # @app.route("/")
# # # # # # # # # # def home():
# # # # # # # # # #     return jsonify({"message": "AI Article Generator API running!"})

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Text Analysis
# # # # # # # # # # # ----------------------
# # # # # # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # # # # # def analyze_text():
# # # # # # # # # #     data = request.get_json()
# # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # #     if not text.strip():
# # # # # # # # # #         return jsonify({"error": "No text provided"}), 400

# # # # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # # # #     word_counts = Counter(words)
# # # # # # # # # #     top_words = word_counts.most_common(5)

# # # # # # # # # #     result = {
# # # # # # # # # #         "characters": len(text),
# # # # # # # # # #         "words": len(words),
# # # # # # # # # #         "unique_words": len(word_counts),
# # # # # # # # # #         "top_words": top_words
# # # # # # # # # #     }
# # # # # # # # # #     return jsonify(result)

# # # # # # # # # # # ----------------------
# # # # # # # # # # # AI Summary
# # # # # # # # # # # ----------------------
# # # # # # # # # # from sumy.parsers.plaintext import PlaintextParser
# # # # # # # # # # from sumy.nlp.tokenizers import Tokenizer
# # # # # # # # # # from sumy.summarizers.lsa import LsaSummarizer

# # # # # # # # # # @app.route("/ai-summary", methods=["POST"])
# # # # # # # # # # def ai_summary():
# # # # # # # # # #     data = request.get_json()
# # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # #     if not text.strip():
# # # # # # # # # #         return jsonify({"summary": "No text provided"})

# # # # # # # # # #     parser = PlaintextParser.from_string(text, Tokenizer("english"))
# # # # # # # # # #     summarizer = LsaSummarizer()
# # # # # # # # # #     summary_sentences = summarizer(parser.document, sentences_count=5)
# # # # # # # # # #     summary = " ".join([str(s) for s in summary_sentences])
# # # # # # # # # #     if not summary:
# # # # # # # # # #         summary = "Text too short to summarize"
# # # # # # # # # #     return jsonify({"summary": summary})

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Keywords
# # # # # # # # # # # ----------------------
# # # # # # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # # # # # def keywords():
# # # # # # # # # #     data = request.get_json()
# # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # #     if not text.strip():
# # # # # # # # # #         return jsonify({"keywords": []})
# # # # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # # # #     word_counts = Counter(words)
# # # # # # # # # #     top_words = [w for w, c in word_counts.most_common(10)]
# # # # # # # # # #     return jsonify({"keywords": top_words})

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Sentiment Analysis
# # # # # # # # # # # ----------------------
# # # # # # # # # # from textblob import TextBlob

# # # # # # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # # # # # def sentiment():
# # # # # # # # # #     data = request.get_json()
# # # # # # # # # #     text = data.get("text", "")
# # # # # # # # # #     if not text.strip():
# # # # # # # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})
# # # # # # # # # #     blob = TextBlob(text)
# # # # # # # # # #     polarity = blob.sentiment.polarity
# # # # # # # # # #     if polarity > 0:
# # # # # # # # # #         sentiment_result = "positive"
# # # # # # # # # #     elif polarity < 0:
# # # # # # # # # #         sentiment_result = "negative"
# # # # # # # # # #     else:
# # # # # # # # # #         sentiment_result = "neutral"
# # # # # # # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # # # # # # ----------------------
# # # # # # # # # # # AI Article Generator
# # # # # # # # # # # ----------------------
# # # # # # # # # # @app.route("/generate-article", methods=["POST"])
# # # # # # # # # # def generate_article():
# # # # # # # # # #     data = request.get_json()
# # # # # # # # # #     topic = data.get("topic", "technology")
# # # # # # # # # #     url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"
# # # # # # # # # #     headers = {
# # # # # # # # # #         "Content-Type": "application/json",
# # # # # # # # # #         "X-goog-api-key": API_KEY
# # # # # # # # # #     }
# # # # # # # # # #     payload = {
# # # # # # # # # #         "contents": [{"parts": [{"text": f"Write a detailed informative article about {topic}. Include introduction, important points, and conclusion."}]}]
# # # # # # # # # #     }

# # # # # # # # # #     try:
# # # # # # # # # #         response = requests.post(url, headers=headers, json=payload)
# # # # # # # # # #         if response.status_code == 429:
# # # # # # # # # #             # Quota exhausted → fallback to local model
# # # # # # # # # #             fallback_text = local_generator(f"Write a detailed article about {topic}.", max_length=500)[0]["generated_text"]
# # # # # # # # # #             return jsonify({"article": fallback_text})
# # # # # # # # # #         elif response.status_code != 200:
# # # # # # # # # #             return jsonify({"error": "AI request failed, using fallback", "details": response.text}), 500

# # # # # # # # # #         data = response.json()
# # # # # # # # # #         article_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

# # # # # # # # # #         if not article_text:
# # # # # # # # # #             # Fallback if Gemini returns empty
# # # # # # # # # #             article_text = local_generator(f"Write a detailed article about {topic}.", max_length=500)[0]["generated_text"]

# # # # # # # # # #         return jsonify({"article": article_text})
# # # # # # # # # #     except Exception as e:
# # # # # # # # # #         # Fallback in case of any error
# # # # # # # # # #         article_text = local_generator(f"Write a detailed article about {topic}.", max_length=500)[0]["generated_text"]
# # # # # # # # # #         return jsonify({"article": article_text})

# # # # # # # # # # # ----------------------
# # # # # # # # # # # Run server
# # # # # # # # # # # ----------------------
# # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # # # # # # # backend/app.py
# # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # from flask_cors import CORS
# # # # # # # # # from collections import Counter
# # # # # # # # # import re
# # # # # # # # # import requests
# # # # # # # # # import nltk
# # # # # # # # # from textblob import TextBlob
# # # # # # # # # from sumy.parsers.plaintext import PlaintextParser
# # # # # # # # # from sumy.nlp.tokenizers import Tokenizer
# # # # # # # # # from sumy.summarizers.lsa import LsaSummarizer
# # # # # # # # # from transformers import pipeline

# # # # # # # # # # ----------------------
# # # # # # # # # # Setup
# # # # # # # # # # ----------------------
# # # # # # # # # app = Flask(__name__)
# # # # # # # # # CORS(app)

# # # # # # # # # # Download NLTK data
# # # # # # # # # nltk.download('punkt')

# # # # # # # # # # ----------------------
# # # # # # # # # # Gemini AI Config
# # # # # # # # # # ----------------------
# # # # # # # # # API_KEY = "AIzaSyDPDjDu1_aArU35YdtVLGCBcc6KlHa9VIQ"
# # # # # # # # # MODEL_NAME = "gemini-2.0-flash"

# # # # # # # # # # ----------------------
# # # # # # # # # # Fallback local AI model
# # # # # # # # # # ----------------------
# # # # # # # # # print("⏳ Loading local fallback AI model...")
# # # # # # # # # local_generator = pipeline("text-generation", model="distilgpt2")
# # # # # # # # # local_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# # # # # # # # # print("✅ Local AI models loaded!")

# # # # # # # # # # ----------------------
# # # # # # # # # # Home
# # # # # # # # # # ----------------------
# # # # # # # # # @app.route("/")
# # # # # # # # # def home():
# # # # # # # # #     return jsonify({"message": "AI Article Generator API running!"})

# # # # # # # # # # ----------------------
# # # # # # # # # # Text Analysis
# # # # # # # # # # ----------------------
# # # # # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # # # # def analyze_text():
# # # # # # # # #     data = request.get_json()
# # # # # # # # #     text = data.get("text", "")
# # # # # # # # #     if not text.strip():
# # # # # # # # #         return jsonify({"error": "No text provided"}), 400

# # # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # # #     word_counts = Counter(words)
# # # # # # # # #     top_words = word_counts.most_common(5)

# # # # # # # # #     result = {
# # # # # # # # #         "characters": len(text),
# # # # # # # # #         "words": len(words),
# # # # # # # # #         "unique_words": len(word_counts),
# # # # # # # # #         "top_words": top_words
# # # # # # # # #     }
# # # # # # # # #     return jsonify(result)

# # # # # # # # # # ----------------------
# # # # # # # # # # AI Summary
# # # # # # # # # # ----------------------
# # # # # # # # # @app.route("/ai-summary", methods=["POST"])
# # # # # # # # # def ai_summary():
# # # # # # # # #     data = request.get_json()
# # # # # # # # #     text = data.get("text", "")
# # # # # # # # #     if not text.strip():
# # # # # # # # #         return jsonify({"summary": "No text provided"})
    
# # # # # # # # #     try:
# # # # # # # # #         parser = PlaintextParser.from_string(text, Tokenizer("english"))
# # # # # # # # #         summarizer = LsaSummarizer()
# # # # # # # # #         sentences_count = min(5, len(parser.document.sentences))
# # # # # # # # #         if sentences_count == 0:
# # # # # # # # #             raise ValueError("Text too short")
# # # # # # # # #         summary_sentences = summarizer(parser.document, sentences_count)
# # # # # # # # #         summary = " ".join([str(s) for s in summary_sentences])
# # # # # # # # #         if not summary.strip():
# # # # # # # # #             raise ValueError("Empty summary")
# # # # # # # # #         return jsonify({"summary": summary})
# # # # # # # # #     except:
# # # # # # # # #         # fallback summarization
# # # # # # # # #         summary = local_summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
# # # # # # # # #         return jsonify({"summary": summary})

# # # # # # # # # # ----------------------
# # # # # # # # # # Keywords Extraction
# # # # # # # # # # ----------------------
# # # # # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # # # # def keywords():
# # # # # # # # #     data = request.get_json()
# # # # # # # # #     text = data.get("text", "")
# # # # # # # # #     if not text.strip():
# # # # # # # # #         return jsonify({"keywords": []})
    
# # # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # # #     word_counts = Counter(words)
# # # # # # # # #     top_words = [w for w, _ in word_counts.most_common(10)]
# # # # # # # # #     return jsonify({"keywords": top_words})

# # # # # # # # # # ----------------------
# # # # # # # # # # Sentiment Analysis
# # # # # # # # # # ----------------------
# # # # # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # # # # def sentiment():
# # # # # # # # #     data = request.get_json()
# # # # # # # # #     text = data.get("text", "")
# # # # # # # # #     if not text.strip():
# # # # # # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})
    
# # # # # # # # #     blob = TextBlob(text)
# # # # # # # # #     polarity = blob.sentiment.polarity
# # # # # # # # #     if polarity > 0:
# # # # # # # # #         sentiment_result = "positive"
# # # # # # # # #     elif polarity < 0:
# # # # # # # # #         sentiment_result = "negative"
# # # # # # # # #     else:
# # # # # # # # #         sentiment_result = "neutral"
# # # # # # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # # # # # ----------------------
# # # # # # # # # # AI Article Generator
# # # # # # # # # # ----------------------
# # # # # # # # # @app.route("/generate-article", methods=["POST"])
# # # # # # # # # def generate_article():
# # # # # # # # #     data = request.get_json()
# # # # # # # # #     topic = data.get("topic", "technology")
    
# # # # # # # # #     url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"
# # # # # # # # #     headers = {
# # # # # # # # #         "Content-Type": "application/json",
# # # # # # # # #         "X-goog-api-key": API_KEY
# # # # # # # # #     }
# # # # # # # # #     payload = {
# # # # # # # # #         "contents": [
# # # # # # # # #             {"parts": [{"text": f"Write a detailed informative article about {topic}. Include introduction, key points, and conclusion."}]}
# # # # # # # # #         ]
# # # # # # # # #     }

# # # # # # # # #     try:
# # # # # # # # #         response = requests.post(url, headers=headers, json=payload)
# # # # # # # # #         if response.status_code == 429 or response.status_code != 200:
# # # # # # # # #             # fallback local generation
# # # # # # # # #             fallback_text = local_generator(f"Write a detailed article about {topic}.", max_length=500)[0]["generated_text"]
# # # # # # # # #             return jsonify({"article": fallback_text})

# # # # # # # # #         data = response.json()
# # # # # # # # #         article_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
# # # # # # # # #         if not article_text.strip():
# # # # # # # # #             article_text = local_generator(f"Write a detailed article about {topic}.", max_length=500)[0]["generated_text"]
# # # # # # # # #         return jsonify({"article": article_text})
# # # # # # # # #     except Exception as e:
# # # # # # # # #         # fallback in case of any error
# # # # # # # # #         article_text = local_generator(f"Write a detailed article about {topic}.", max_length=500)[0]["generated_text"]
# # # # # # # # #         return jsonify({"article": article_text})

# # # # # # # # # # ----------------------
# # # # # # # # # # Run Server
# # # # # # # # # # ----------------------
# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # # # # # # backend/app.py
# # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # from flask_cors import CORS
# # # # # # # # from collections import Counter
# # # # # # # # import re
# # # # # # # # import nltk
# # # # # # # # from textblob import TextBlob
# # # # # # # # from transformers import pipeline

# # # # # # # # # Download punkt for sentence tokenization
# # # # # # # # nltk.download('punkt')

# # # # # # # # app = Flask(__name__)
# # # # # # # # CORS(app)

# # # # # # # # # ----------------------
# # # # # # # # # Load local AI models
# # # # # # # # # ----------------------
# # # # # # # # print("⏳ Loading local AI models...")
# # # # # # # # # Summarization (BART)
# # # # # # # # try:
# # # # # # # #     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# # # # # # # # except Exception:
# # # # # # # #     summarizer = None

# # # # # # # # # Article generation (GPT-2)
# # # # # # # # try:
# # # # # # # #     article_generator = pipeline("text-generation", model="distilgpt2")
# # # # # # # # except Exception:
# # # # # # # #     article_generator = None
# # # # # # # # print("✅ Local AI models loaded!")

# # # # # # # # # ----------------------
# # # # # # # # # Text Analysis Endpoint
# # # # # # # # # ----------------------
# # # # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # # # def analyze_text():
# # # # # # # #     data = request.json
# # # # # # # #     text = data.get("text", "")
# # # # # # # #     if not text.strip():
# # # # # # # #         return jsonify({"error": "No text provided"}), 400

# # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # #     word_counts = Counter(words)
# # # # # # # #     top_words = word_counts.most_common(5)

# # # # # # # #     result = {
# # # # # # # #         "characters": len(text),
# # # # # # # #         "words": len(words),
# # # # # # # #         "unique_words": len(word_counts),
# # # # # # # #         "top_words": top_words
# # # # # # # #     }
# # # # # # # #     return jsonify(result)

# # # # # # # # # ----------------------
# # # # # # # # # AI Summary Endpoint
# # # # # # # # # ----------------------
# # # # # # # # @app.route("/ai-summary", methods=["POST"])
# # # # # # # # def ai_summary():
# # # # # # # #     data = request.json
# # # # # # # #     text = data.get("text", "")
# # # # # # # #     if not text.strip():
# # # # # # # #         return jsonify({"summary": "No text provided"})

# # # # # # # #     try:
# # # # # # # #         if summarizer and len(text.split()) >= 20:
# # # # # # # #             # Use model for longer text
# # # # # # # #             summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
# # # # # # # #         else:
# # # # # # # #             # Fallback: first 2 sentences
# # # # # # # #             sentences = nltk.sent_tokenize(text)
# # # # # # # #             summary = " ".join(sentences[:2])
# # # # # # # #     except Exception:
# # # # # # # #         sentences = nltk.sent_tokenize(text)
# # # # # # # #         summary = " ".join(sentences[:2]) if sentences else text

# # # # # # # #     return jsonify({"summary": summary})

# # # # # # # # # ----------------------
# # # # # # # # # Keywords Extraction
# # # # # # # # # ----------------------
# # # # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # # # def keywords():
# # # # # # # #     data = request.json
# # # # # # # #     text = data.get("text", "")
# # # # # # # #     if not text.strip():
# # # # # # # #         return jsonify({"keywords": []})
# # # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # # #     word_counts = Counter(words)
# # # # # # # #     top_words = [w for w, c in word_counts.most_common(10)]
# # # # # # # #     return jsonify({"keywords": top_words})

# # # # # # # # # ----------------------
# # # # # # # # # Sentiment Analysis
# # # # # # # # # ----------------------
# # # # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # # # def sentiment():
# # # # # # # #     data = request.json
# # # # # # # #     text = data.get("text", "")
# # # # # # # #     if not text.strip():
# # # # # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})
# # # # # # # #     blob = TextBlob(text)
# # # # # # # #     polarity = blob.sentiment.polarity
# # # # # # # #     if polarity > 0:
# # # # # # # #         sentiment_result = "positive"
# # # # # # # #     elif polarity < 0:
# # # # # # # #         sentiment_result = "negative"
# # # # # # # #     else:
# # # # # # # #         sentiment_result = "neutral"
# # # # # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # # # # ----------------------
# # # # # # # # # AI Article Generation (local)
# # # # # # # # # ----------------------
# # # # # # # # @app.route("/generate-article", methods=["POST"])
# # # # # # # # def generate_article():
# # # # # # # #     data = request.json
# # # # # # # #     topic = data.get("topic", "technology")
# # # # # # # #     prompt = f"Write a detailed informative article about {topic}. Include introduction, main points, and conclusion."

# # # # # # # #     try:
# # # # # # # #         if article_generator:
# # # # # # # #             article_text = article_generator(prompt, max_length=500, do_sample=True)[0]["generated_text"]
# # # # # # # #         else:
# # # # # # # #             article_text = "AI generator not available. Please install transformers model."
# # # # # # # #     except Exception:
# # # # # # # #         article_text = "Failed to generate article."

# # # # # # # #     return jsonify({"article": article_text})

# # # # # # # # # ----------------------
# # # # # # # # # Run server
# # # # # # # # # ----------------------
# # # # # # # # if __name__ == "__main__":
# # # # # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # # # # # backend/app.py
# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS
# # # # # # # from collections import Counter
# # # # # # # import re
# # # # # # # import nltk
# # # # # # # from textblob import TextBlob

# # # # # # # # Download punkt for sentence tokenization
# # # # # # # nltk.download('punkt')

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)

# # # # # # # # ----------------------
# # # # # # # # Text Analysis
# # # # # # # # ----------------------
# # # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # # def analyze_text():
# # # # # # #     data = request.json
# # # # # # #     text = data.get("text", "")
# # # # # # #     if not text.strip():
# # # # # # #         return jsonify({"error": "No text provided"}), 400

# # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # #     word_counts = Counter(words)
# # # # # # #     top_words = word_counts.most_common(5)

# # # # # # #     result = {
# # # # # # #         "characters": len(text),
# # # # # # #         "words": len(words),
# # # # # # #         "unique_words": len(word_counts),
# # # # # # #         "top_words": top_words
# # # # # # #     }
# # # # # # #     return jsonify(result)

# # # # # # # # ----------------------
# # # # # # # # AI Summary (Simple, reliable)
# # # # # # # # ----------------------
# # # # # # # @app.route("/ai-summary", methods=["POST"])
# # # # # # # def ai_summary():
# # # # # # #     data = request.json
# # # # # # #     text = data.get("text", "")
# # # # # # #     if not text.strip():
# # # # # # #         return jsonify({"summary": "No text provided"})

# # # # # # #     sentences = nltk.sent_tokenize(text)
# # # # # # #     # Use first 3 sentences as summary
# # # # # # #     summary = " ".join(sentences[:3]) if sentences else text
# # # # # # #     return jsonify({"summary": summary})

# # # # # # # # ----------------------
# # # # # # # # Keywords Extraction
# # # # # # # # ----------------------
# # # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # # def keywords():
# # # # # # #     data = request.json
# # # # # # #     text = data.get("text", "")
# # # # # # #     if not text.strip():
# # # # # # #         return jsonify({"keywords": []})
# # # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # # #     word_counts = Counter(words)
# # # # # # #     top_words = [w for w, c in word_counts.most_common(10)]
# # # # # # #     return jsonify({"keywords": top_words})

# # # # # # # # ----------------------
# # # # # # # # Sentiment Analysis
# # # # # # # # ----------------------
# # # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # # def sentiment():
# # # # # # #     data = request.json
# # # # # # #     text = data.get("text", "")
# # # # # # #     if not text.strip():
# # # # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})
# # # # # # #     blob = TextBlob(text)
# # # # # # #     polarity = blob.sentiment.polarity
# # # # # # #     if polarity > 0:
# # # # # # #         sentiment_result = "positive"
# # # # # # #     elif polarity < 0:
# # # # # # #         sentiment_result = "negative"
# # # # # # #     else:
# # # # # # #         sentiment_result = "neutral"
# # # # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # # # ----------------------
# # # # # # # # AI Article Generation (Simple)
# # # # # # # # ----------------------
# # # # # # # @app.route("/generate-article", methods=["POST"])
# # # # # # # def generate_article():
# # # # # # #     data = request.json
# # # # # # #     topic = data.get("topic", "technology")
# # # # # # #     # Simple placeholder article using topic
# # # # # # #     article_text = (
# # # # # # #         f"Introduction:\nThis article discusses {topic}.\n\n"
# # # # # # #         f"Main Points:\n- Point 1 about {topic}\n- Point 2 about {topic}\n- Point 3 about {topic}\n\n"
# # # # # # #         f"Conclusion:\nIn conclusion, {topic} is important and has many applications."
# # # # # # #     )
# # # # # # #     return jsonify({"article": article_text})

# # # # # # # # ----------------------
# # # # # # # # Run server
# # # # # # # # ----------------------
# # # # # # # if __name__ == "__main__":
# # # # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # # # from flask import Flask, request, jsonify
# # # # # # from flask_cors import CORS
# # # # # # from collections import Counter
# # # # # # import re
# # # # # # import nltk
# # # # # # from textblob import TextBlob
# # # # # # from transformers import pipeline

# # # # # # nltk.download('punkt')

# # # # # # app = Flask(__name__)
# # # # # # CORS(app)

# # # # # # # Load local AI models
# # # # # # print("⏳ Loading local AI models...")
# # # # # # try:
# # # # # #     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# # # # # # except Exception:
# # # # # #     summarizer = None

# # # # # # try:
# # # # # #     article_generator = pipeline("text-generation", model="distilgpt2")
# # # # # # except Exception:
# # # # # #     article_generator = None
# # # # # # print("✅ Local AI models loaded!")

# # # # # # # Text Analysis
# # # # # # @app.route("/analyze", methods=["POST"])
# # # # # # def analyze_text():
# # # # # #     data = request.json
# # # # # #     text = data.get("text", "")
# # # # # #     if not text.strip():
# # # # # #         return jsonify({"error": "No text provided"}), 400
# # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # #     word_counts = Counter(words)
# # # # # #     top_words = word_counts.most_common(5)
# # # # # #     return jsonify({
# # # # # #         "characters": len(text),
# # # # # #         "words": len(words),
# # # # # #         "unique_words": len(word_counts),
# # # # # #         "top_words": top_words
# # # # # #     })

# # # # # # # AI Summary
# # # # # # @app.route("/ai-summary", methods=["POST"])
# # # # # # def ai_summary():
# # # # # #     data = request.json
# # # # # #     text = data.get("text", "")
# # # # # #     if not text.strip():
# # # # # #         return jsonify({"summary": "No text provided"})
# # # # # #     try:
# # # # # #         if summarizer and len(text.split()) >= 20:
# # # # # #             summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
# # # # # #         else:
# # # # # #             sentences = nltk.sent_tokenize(text)
# # # # # #             summary = " ".join(sentences[:2])
# # # # # #     except Exception:
# # # # # #         sentences = nltk.sent_tokenize(text)
# # # # # #         summary = " ".join(sentences[:2]) if sentences else text
# # # # # #     return jsonify({"summary": summary})

# # # # # # # Keywords
# # # # # # @app.route("/keywords", methods=["POST"])
# # # # # # def keywords():
# # # # # #     data = request.json
# # # # # #     text = data.get("text", "")
# # # # # #     if not text.strip():
# # # # # #         return jsonify({"keywords": []})
# # # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # # #     word_counts = Counter(words)
# # # # # #     top_words = [w for w, c in word_counts.most_common(10)]
# # # # # #     return jsonify({"keywords": top_words})

# # # # # # # Sentiment
# # # # # # @app.route("/sentiment", methods=["POST"])
# # # # # # def sentiment():
# # # # # #     data = request.json
# # # # # #     text = data.get("text", "")
# # # # # #     if not text.strip():
# # # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})
# # # # # #     blob = TextBlob(text)
# # # # # #     polarity = blob.sentiment.polarity
# # # # # #     if polarity > 0:
# # # # # #         sentiment_result = "positive"
# # # # # #     elif polarity < 0:
# # # # # #         sentiment_result = "negative"
# # # # # #     else:
# # # # # #         sentiment_result = "neutral"
# # # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # # Article generation
# # # # # # @app.route("/generate-article", methods=["POST"])
# # # # # # def generate_article():
# # # # # #     data = request.json
# # # # # #     topic = data.get("topic", "technology")
# # # # # #     prompt = f"Write a detailed informative article about {topic}. Include introduction, main points, and conclusion."
# # # # # #     try:
# # # # # #         if article_generator:
# # # # # #             article_text = article_generator(prompt, max_length=500, do_sample=True)[0]["generated_text"]
# # # # # #         else:
# # # # # #             article_text = "AI generator not available. Please install transformers model."
# # # # # #     except Exception:
# # # # # #         article_text = "Failed to generate article."
# # # # # #     return jsonify({"article": article_text})

# # # # # # if __name__ == "__main__":
# # # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # # from flask import Flask, request, jsonify
# # # # # from flask_cors import CORS
# # # # # from collections import Counter
# # # # # import re
# # # # # import nltk
# # # # # from textblob import TextBlob

# # # # # # ----------------------
# # # # # # Setup
# # # # # # ----------------------
# # # # # app = Flask(__name__)
# # # # # CORS(app)

# # # # # # Download punkt for sentence tokenization
# # # # # nltk.download('punkt')

# # # # # # ----------------------
# # # # # # Text Analysis Endpoint
# # # # # # ----------------------
# # # # # @app.route("/analyze", methods=["POST"])
# # # # # def analyze_text():
# # # # #     data = request.json
# # # # #     text = data.get("text", "")
# # # # #     if not text.strip():
# # # # #         return jsonify({"error": "No text provided"}), 400

# # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # #     word_counts = Counter(words)
# # # # #     top_words = word_counts.most_common(5)

# # # # #     result = {
# # # # #         "characters": len(text),
# # # # #         "words": len(words),
# # # # #         "unique_words": len(word_counts),
# # # # #         "top_words": top_words
# # # # #     }
# # # # #     return jsonify(result)

# # # # # # ----------------------
# # # # # # AI Summary Endpoint (simple)
# # # # # # ----------------------
# # # # # @app.route("/ai-summary", methods=["POST"])
# # # # # def ai_summary():
# # # # #     data = request.json
# # # # #     text = data.get("text", "")
# # # # #     if not text.strip():
# # # # #         return jsonify({"summary": "No text provided"})

# # # # #     # Simple summarization: first 3 sentences
# # # # #     sentences = nltk.sent_tokenize(text)
# # # # #     summary = " ".join(sentences[:3]) if sentences else text

# # # # #     return jsonify({"summary": summary})

# # # # # # ----------------------
# # # # # # Keywords Extraction
# # # # # # ----------------------
# # # # # @app.route("/keywords", methods=["POST"])
# # # # # def keywords():
# # # # #     data = request.json
# # # # #     text = data.get("text", "")
# # # # #     if not text.strip():
# # # # #         return jsonify({"keywords": []})

# # # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # # #     word_counts = Counter(words)
# # # # #     top_words = [w for w, _ in word_counts.most_common(10)]
# # # # #     return jsonify({"keywords": top_words})

# # # # # # ----------------------
# # # # # # Sentiment Analysis
# # # # # # ----------------------
# # # # # @app.route("/sentiment", methods=["POST"])
# # # # # def sentiment():
# # # # #     data = request.json
# # # # #     text = data.get("text", "")
# # # # #     if not text.strip():
# # # # #         return jsonify({"sentiment": "neutral", "polarity": 0})

# # # # #     blob = TextBlob(text)
# # # # #     polarity = blob.sentiment.polarity
# # # # #     if polarity > 0:
# # # # #         sentiment_result = "positive"
# # # # #     elif polarity < 0:
# # # # #         sentiment_result = "negative"
# # # # #     else:
# # # # #         sentiment_result = "neutral"

# # # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # # ----------------------
# # # # # # AI Article Generation (simple placeholder)
# # # # # # ----------------------
# # # # # @app.route("/generate-article", methods=["POST"])
# # # # # def generate_article():
# # # # #     data = request.json
# # # # #     topic = data.get("topic", "technology")
# # # # #     # Simple placeholder: repeat topic intro
# # # # #     article_text = f"Here is a simple article about {topic}. " \
# # # # #                    f"This article is generated locally. " \
# # # # #                    f"You can expand this article as needed."

# # # # #     return jsonify({"article": article_text})

# # # # # # ----------------------
# # # # # # Run server
# # # # # # ----------------------
# # # # # if __name__ == "__main__":
# # # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # # from flask import Flask, request, jsonify
# # # # from flask_cors import CORS
# # # # from collections import Counter
# # # # import re
# # # # import nltk
# # # # from textblob import TextBlob
# # # # from sumy.parsers.plaintext import PlaintextParser
# # # # from sumy.nlp.tokenizers import Tokenizer
# # # # from sumy.summarizers.lsa import LsaSummarizer

# # # # # ----------------------
# # # # # Setup
# # # # # ----------------------
# # # # app = Flask(__name__)
# # # # CORS(app)

# # # # # Download required NLTK data
# # # # nltk.download('punkt')

# # # # # ----------------------
# # # # # Text Analysis
# # # # # ----------------------
# # # # @app.route("/analyze", methods=["POST"])
# # # # def analyze_text():
# # # #     data = request.json
# # # #     text = data.get("text", "")
# # # #     if not text.strip():
# # # #         return jsonify({"error": "No text provided"}), 400

# # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # #     word_counts = Counter(words)
# # # #     top_words = word_counts.most_common(5)

# # # #     return jsonify({
# # # #         "characters": len(text),
# # # #         "words": len(words),
# # # #         "unique_words": len(word_counts),
# # # #         "top_words": top_words
# # # #     })

# # # # # ----------------------
# # # # # AI Summary
# # # # # ----------------------
# # # # @app.route("/ai-summary", methods=["POST"])
# # # # def ai_summary():
# # # #     data = request.json
# # # #     text = data.get("text", "")
# # # #     if not text.strip():
# # # #         return jsonify({"summary": "No text provided"})

# # # #     try:
# # # #         parser = PlaintextParser.from_string(text, Tokenizer("english"))
# # # #         summarizer = LsaSummarizer()
# # # #         sentence_count = min(5, len(parser.document.sentences))
# # # #         if sentence_count == 0:
# # # #             raise ValueError("Text too short to summarize")
# # # #         summary_sentences = summarizer(parser.document, sentence_count)
# # # #         summary = " ".join(str(s) for s in summary_sentences)
# # # #         if not summary.strip():
# # # #             raise ValueError("Empty summary")
# # # #     except Exception:
# # # #         # fallback: first 3 sentences
# # # #         sentences = nltk.sent_tokenize(text)
# # # #         summary = " ".join(sentences[:3])

# # # #     return jsonify({"summary": summary})

# # # # # ----------------------
# # # # # Keywords
# # # # # ----------------------
# # # # @app.route("/keywords", methods=["POST"])
# # # # def keywords():
# # # #     data = request.json
# # # #     text = data.get("text", "")
# # # #     if not text.strip():
# # # #         return jsonify({"keywords": []})

# # # #     words = re.findall(r"\b\w+\b", text.lower())
# # # #     word_counts = Counter(words)
# # # #     top_words = [w for w, _ in word_counts.most_common(10)]

# # # #     return jsonify({"keywords": top_words})

# # # # # ----------------------
# # # # # Sentiment Analysis
# # # # # ----------------------
# # # # @app.route("/sentiment", methods=["POST"])
# # # # def sentiment():
# # # #     data = request.json
# # # #     text = data.get("text", "")
# # # #     if not text.strip():
# # # #         return jsonify({"sentiment": "neutral", "polarity": 0})

# # # #     try:
# # # #         blob = TextBlob(text)
# # # #         polarity = blob.sentiment.polarity
# # # #         if polarity > 0:
# # # #             sentiment_result = "positive"
# # # #         elif polarity < 0:
# # # #             sentiment_result = "negative"
# # # #         else:
# # # #             sentiment_result = "neutral"
# # # #     except Exception:
# # # #         sentiment_result = "neutral"
# # # #         polarity = 0

# # # #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # # # ----------------------
# # # # # Run Server
# # # # # ----------------------
# # # # if __name__ == "__main__":
# # # #     app.run(host="127.0.0.1", port=5000, debug=True)
# # # from flask import Flask, request, jsonify
# # # import pickle

# # # app = Flask(__name__)

# # # model = pickle.load(open("expense_model.pkl", "rb"))
# # # vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # # @app.route("/expense-chat", methods=["POST"])
# # # def expense_chat():
# # #     data = request.json
# # #     message = data.get("message", "")
# # #     if not message.strip():
# # #         return jsonify({"response": "Please type something!"})

# # #     X = vectorizer.transform([message])
# # #     intent = model.predict(X)[0]

# # #     # Simple responses (later integrate DB)
# # #     responses = {
# # #         "add_expense": "Okay, expense added!",
# # #         "show_total": "You spent $1500 this month.",
# # #         "show_category": "You spent $200 on food.",
# # #         "delete_expense": "Last expense deleted."
# # #     }

# # #     return jsonify({"response": responses.get(intent, "I don't understand.")})

# # # if __name__ == "__main__":
# # #     app.run(debug=True)
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # from collections import Counter
# # import re

# # # For AI summary
# # from sumy.parsers.plaintext import PlaintextParser
# # from sumy.nlp.tokenizers import Tokenizer
# # from sumy.summarizers.lsa import LsaSummarizer

# # # For sentiment analysis
# # from textblob import TextBlob

# # app = Flask(__name__)
# # CORS(app)

# # # ----------------------
# # # Text Analysis Endpoint
# # # ----------------------
# # @app.route("/analyze", methods=["POST"])
# # def analyze_text():
# #     data = request.json
# #     text = data.get("text", "")

# #     if not text.strip():
# #         return jsonify({"error": "No text provided"}), 400

# #     # Clean text and split
# #     words = re.findall(r"\b\w+\b", text.lower())
# #     word_counts = Counter(words)
# #     top_words = word_counts.most_common(5)

# #     result = {
# #         "characters": len(text),
# #         "words": len(words),
# #         "unique_words": len(word_counts),
# #         "top_words": top_words
# #     }
# #     return jsonify(result)

# # # ----------------------
# # # AI Summary Endpoint
# # # ----------------------
# # @app.route("/ai-free", methods=["POST"])
# # def ai_summary():
# #     data = request.json
# #     text = data.get("text", "")

# #     if not text.strip():
# #         return jsonify({"summary": "No text provided"})

# #     parser = PlaintextParser.from_string(text, Tokenizer("english"))
# #     summarizer = LsaSummarizer()
# #     summary_sentences = summarizer(parser.document, sentences_count=5)
# #     summary = " ".join([str(s) for s in summary_sentences])

# #     if not summary:
# #         summary = "Text too short to summarize"

# #     return jsonify({"summary": summary})

# # # ----------------------
# # # Keywords Extraction
# # # ----------------------
# # @app.route("/keywords", methods=["POST"])
# # def keywords():
# #     data = request.json
# #     text = data.get("text", "")

# #     if not text.strip():
# #         return jsonify({"keywords": []})

# #     words = re.findall(r"\b\w+\b", text.lower())
# #     word_counts = Counter(words)
# #     top_words = [w for w, c in word_counts.most_common(5)]

# #     return jsonify({"keywords": top_words})

# # # ----------------------
# # # Sentiment Analysis
# # # ----------------------
# # @app.route("/sentiment", methods=["POST"])
# # def sentiment():
# #     data = request.json
# #     text = data.get("text", "")

# #     if not text.strip():
# #         return jsonify({"sentiment": "neutral", "polarity": 0})

# #     blob = TextBlob(text)
# #     polarity = blob.sentiment.polarity

# #     if polarity > 0:
# #         sentiment_result = "positive"
# #     elif polarity < 0:
# #         sentiment_result = "negative"
# #     else:
# #         sentiment_result = "neutral"

# #     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # # ----------------------
# # # Run Server
# # # ----------------------
# # if __name__ == "__main__":
# #     app.run(host="127.0.0.1", port=5000, debug=True)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from collections import Counter
# import re
# import nltk
# from textblob import TextBlob
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from transformers import pipeline

# # ----------------------
# # Setup
# # ----------------------
# app = Flask(__name__)
# CORS(app)

# # Download required NLTK data
# nltk.download('punkt')

# # ----------------------
# # Load local AI models
# # ----------------------
# print("⏳ Loading local AI models...")
# # Summarization (BART)
# try:
#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# except Exception:
#     summarizer = None

# # Article generation (GPT-2)
# try:
#     article_generator = pipeline("text-generation", model="distilgpt2")
# except Exception:
#     article_generator = None
# print("✅ Local AI models loaded!")

# # ----------------------
# # Text Analysis Endpoint
# # ----------------------
# @app.route("/analyze", methods=["POST"])
# def analyze_text():
#     data = request.json
#     text = data.get("text", "")
#     if not text.strip():
#         return jsonify({"error": "No text provided"}), 400

#     words = re.findall(r"\b\w+\b", text.lower())
#     word_counts = Counter(words)
#     top_words = word_counts.most_common(5)

#     result = {
#         "characters": len(text),
#         "words": len(words),
#         "unique_words": len(word_counts),
#         "top_words": top_words
#     }
#     return jsonify(result)

# # ----------------------
# # AI Summary Endpoint
# # ----------------------
# @app.route("/ai-summary", methods=["POST"])
# def ai_summary():
#     data = request.json
#     text = data.get("text", "")
#     if not text.strip():
#         return jsonify({"summary": "No text provided"})
    
#     try:
#         if summarizer and len(text.split()) >= 20:
#             # Use model for longer text
#             summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
#         else:
#             # Fallback: first 2 sentences
#             sentences = nltk.sent_tokenize(text)
#             summary = " ".join(sentences[:2])
#     except Exception:
#         sentences = nltk.sent_tokenize(text)
#         summary = " ".join(sentences[:2]) if sentences else text

#     return jsonify({"summary": summary})

# # ----------------------
# # Keywords Extraction
# # ----------------------
# @app.route("/keywords", methods=["POST"])
# def keywords():
#     data = request.json
#     text = data.get("text", "")
#     if not text.strip():
#         return jsonify({"keywords": []})
#     words = re.findall(r"\b\w+\b", text.lower())
#     word_counts = Counter(words)
#     top_words = [w for w, c in word_counts.most_common(10)]
#     return jsonify({"keywords": top_words})

# # ----------------------
# # Sentiment Analysis
# # ----------------------
# @app.route("/sentiment", methods=["POST"])
# def sentiment():
#     data = request.json
#     text = data.get("text", "")
#     if not text.strip():
#         return jsonify({"sentiment": "neutral", "polarity": 0})
    
#     try:
#         blob = TextBlob(text)
#         polarity = blob.sentiment.polarity
#         if polarity > 0:
#             sentiment_result = "positive"
#         elif polarity < 0:
#             sentiment_result = "negative"
#         else:
#             sentiment_result = "neutral"
#     except Exception:
#         sentiment_result = "neutral"
#         polarity = 0

#     return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# # ----------------------
# # AI Article Generation (local)
# # ----------------------
# @app.route("/generate-article", methods=["POST"])
# def generate_article():
#     data = request.json
#     topic = data.get("topic", "technology")
#     prompt = f"Write a detailed informative article about {topic}. Include introduction, main points, and conclusion."

#     try:
#         if article_generator:
#             article_text = article_generator(prompt, max_length=500, do_sample=True)[0]["generated_text"]
#         else:
#             article_text = "AI generator not available. Please install transformers model."
#     except Exception:
#         article_text = "Failed to generate article."

#     return jsonify({"article": article_text})

# # ----------------------
# # Run server
# # ----------------------
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import Counter
import re
import nltk
from textblob import TextBlob
from transformers import pipeline

# ----------------------
# Setup
# ----------------------
app = Flask(__name__)
CORS(app)

# Download NLTK data
nltk.download('punkt')

# ----------------------
# Load AI models
# ----------------------
print("⏳ Loading local AI models...")
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception:
    summarizer = None

try:
    article_generator = pipeline("text-generation", model="distilgpt2")
except Exception:
    article_generator = None
print("✅ Local AI models loaded!")

# ----------------------
# Text Analysis
# ----------------------
@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.json
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    words = re.findall(r"\b\w+\b", text.lower())
    word_counts = Counter(words)
    top_words = word_counts.most_common(5)

    result = {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(word_counts),
        "top_words": top_words
    }
    return jsonify(result)

# ----------------------
# AI Summary
# ----------------------
@app.route("/ai-summary", methods=["POST"])
def ai_summary():
    data = request.json
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"summary": "No text provided"})
    
    try:
        if summarizer and len(text.split()) >= 20:
            summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
        else:
            # fallback: first 2 sentences
            from nltk.tokenize import sent_tokenize
            sentences = sent_tokenize(text)
            summary = " ".join(sentences[:2])
    except Exception:
        from nltk.tokenize import sent_tokenize
        sentences = sent_tokenize(text)
        summary = " ".join(sentences[:2]) if sentences else text

    return jsonify({"summary": summary})

# ----------------------
# Keywords Extraction
# ----------------------
@app.route("/keywords", methods=["POST"])
def keywords():
    data = request.json
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"keywords": []})
    
    words = re.findall(r"\b\w+\b", text.lower())
    word_counts = Counter(words)
    top_words = [w for w, c in word_counts.most_common(10)]
    return jsonify({"keywords": top_words})

# ----------------------
# Sentiment Analysis
# ----------------------
@app.route("/sentiment", methods=["POST"])
def sentiment():
    data = request.json
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"sentiment": "neutral", "polarity": 0})
    
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment_result = "positive"
        elif polarity < 0:
            sentiment_result = "negative"
        else:
            sentiment_result = "neutral"
    except Exception:
        sentiment_result = "neutral"
        polarity = 0

    return jsonify({"sentiment": sentiment_result, "polarity": polarity})

# ----------------------
# Run server
# ----------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
