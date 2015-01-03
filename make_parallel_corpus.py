import re, pickle, codecs, os
from zhon import hanzi, pinyin


if __name__ == '__main__':

	data = pickle.load(open('data_u.pkl', 'r'))

	punct = hanzi.punctuation + pinyin.punctuation
	
	for i, k in enumerate(data.keys()):
		sents = filter(lambda x: len(x) > 0, re.split('[%s]' % punct, data[k][0]))
		with codecs.open(os.path.join('parellel',str(i)+'.anc-mod.anc'), 'w', encoding='utf-8') as f:
			f.write('\n'.join(sents))
		sents = filter(lambda x: len(x) > 0, re.split('[%s]' % punct, data[k][1]))
		with codecs.open(os.path.join('parellel',str(i)+'.anc-mod.mod'), 'w', encoding='utf-8') as f:
			f.write('\n'.join(sents))
		
