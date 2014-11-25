from nltk.tokenize import word_tokenize
import lxml
def main():
	corpus = ', '.join(open('pray-corpus.txt', 'r').readlines())
	tokens = [token.strip(',') for token in corpus.split()]
	bigrams = ngrams(tokens, 2)
	trigrams = ngrams(tokens, 3)

	

	print bigrams_lookup

def ngrams(list, n):
	result = []
	for i in range(len(list)-n+1):
			result.append([token for token in list[i:i+n]])
	return result

if __name__ == '__main__':
	main()