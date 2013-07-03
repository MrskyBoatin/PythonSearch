# -*- coding: utf-8 -*-

import re
import unidecode
import io

class PythonSearch(object):
    def __init__(self, stopwords, stopwords_prepare, rules, rules_prepare):
        self.rules = self.__load_rules(rules)
        self.rules_prepare = self.__load_rules(rules_prepare)
        self.stopwords = self.__load_stopwords(self.rules_prepare,stopwords)
        self.stopwords_prepare = self.__load_stopwords(self.rules_prepare,stopwords_prepare)
        
    def __load_stopwords(self, rules_prepare, file_stopwords):
        stopwords = self.__apply_first_matching_rule(rules_prepare, io.open(file_stopwords, encoding='utf-8'))
        #print("Loaded %s stopwords from %s" % (len(stopwords), file_stopwords))
        return stopwords
        
    def __load_rules(self, file_rules):
        rules = {}
        for rule in io.open(file_rules, encoding='utf-8'):
            groups = re.search('"([^"]*)" "([^"]*)"',rule)
            lookFor = groups.group(1)
            replaceWith = groups.group(2)
            rules[lookFor] = replaceWith
        #print("Loaded %s rules from %s" % (len(rules), file_rules))
        return rules

    def __apply_all_mathing_rules(self, rules, string):
        for rule in rules:
            string = re.sub(rule,rules[rule],string)
        return string

    def __apply_first_matching_rule(self, rules, strings):
        output = []
        for string in strings:
            to_append = string.strip()
            rules_candidates = []
            rules_max = -1
            for rule in rules:
                if re.search(rule,to_append) is not None:
                    rules_candidates.append(rule)
                    if len(rule) > rules_max:
                        rules_max = len(rule)
            for rule in rules_candidates:
                if len(rule) == rules_max:
                    to_append = re.sub(rule,rules[rule],to_append)
                    break
            output.append(to_append)
        return output
    
    def __not_word_in_list(self, word, stopwords):
        for stopword in stopwords:
            if stopword.lower() == word.lower():
                return False
        return True
    
    def __filter_stopwords(self, word): 
        return self.__not_word_in_list(word, self.stopwords)
    
    def __filter_stopwords_prepare(self, word):
        return self.__not_word_in_list(word, self.stopwords_prepare)

    def get_keys(self,string):
        string = unidecode.unidecode(string)
        string = string.lower()
        string = self.__apply_all_mathing_rules(self.rules_prepare, string)
        keys = string.split()
        keys = filter(self.__filter_stopwords_prepare, keys)
        keys = self.__apply_first_matching_rule(self.rules, keys)
        keys = filter(self.__filter_stopwords, keys)
        keys = list(set(keys))
        keys = sorted(keys)
        return keys

if __name__ == "__main__":
    ps = PythonSearch('../../resources/stopwords.txt', '../../resources/stopwords_prepare.txt', '../../resources/rules.txt', '../../resources/rules_prepare.txt')
    for key in ps.get_keys("använda"):
        print(key)
