from collections import defaultdict

anagram_map = defaultdict(list)
print(anagram_map.items())

# def groupAnagrams(self, strs):
#anagram_map = defaultdict(list)
#anagram_map[0].append(1)
#print(anagram_map)
lst = ["eat","tea","tan","ate","nat","bat"]
for word in lst:
    sorted_word = "".join(sorted(word))
    print(list(sorted_word))
# for word in strs:
# sorted_word = ''.join(sorted(word))
# anagram_map[sorted_word].append(word)

# return list(anagram_map.values())
def Group_Anagrams(lst):
    for word in lst:
        sorted_word = "".join(sorted(word))
        print(sorted_word)
        
        anagram_map[sorted_word].append(word)
    print(list(anagram_map.values()))
#Group_Anagrams(["eat","tea","tan","ate","nat","bat"])

