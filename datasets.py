

class Corpus:
  """
  Generic class to dowload and preprocess corpora.
  Save it in jsonl format.
  """

  def __init__(self):
    pass

class StackExchange(Corpus):
  """
  Mine from StackExchange structured data in the format:
  - Title
  - Question Body
  - Question number of up/downvotes
  - Question tags
  - Answers
       - Answer text
       - Answer number of up/downvotes

  We might need to limit the number of questions from StackOverflow.
  See source for where to download archives for the different stack exchanges.
  """

class Reddit(Corpus):
  """
  For scripts and explanation, have a look at the linked github repository.
  From Google Cloud Big Query, we mine (comment, response) pairs from Reddit.
  In the PolyAI repo, they limit comments and responses to 128 characters.
  It might be good to use also longer pairs, e.g. up to 2048 characters for comment or response.
  """

class AmazonQA(Corpus):
  """
  (Question, Answer) Pairs from Amazon
  """

class OpenSubtitles(Corpus):
  """
  (Text, Response) Pairs from OpenSubtitles
  """

class NFCorpus(Corpus):
  """
  Biomedical QA-dataset. Data format: (Question, Answer-passage)
  """

class HotpotQA(Corpus):
  """
  Multi-Hop QA-Dataset. Data format: (Question, Answer-passage)
  """

class NewsQA(Corpus):
  """
  News article QA dataset. Format (Question, Answer-passage)
  """

class SearchQA(Corpus):
  """
  QA dataset created from Jeopardy! questions. Format (Question, Answer-passage)
  """

class Gdelt(Corpus):
  """
  Pairs of original and modified news article titles. Format (original_title, modified_title)
  """

class Paws(Corpus):
  """
  Pairs of paraphrases sentences, and
  pairs that have high lexical overlap without being paraphrases.
  Format (text, paraphrased_text) or (text, paraphrased_text, hard-negative text)
  """
